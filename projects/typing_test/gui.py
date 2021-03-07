import json
import socketserver
import string
import urllib.parse
import webbrowser
from http import server, HTTPStatus
from http.server import HTTPServer
from random import randrange

import typing_test

PORT = 31415
PARAGRAPH_PATH = "./data/sample_paragraphs.txt"
NUM_PARAGRAPHS = 5474  # seriously??? fixme
WORDS_LIST = sorted(typing_test.lines_from_file('data/words.txt'))

class Handler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        path = "gui/" + urllib.parse.unquote(self.path)[1:]

        if "scripts" in path and not path.endswith(".js"):
            path += ".js"

        if path.endswith(".css"):
            self.send_header("Content-type", "text/css")
        elif path.endswith(".js"):
            self.send_header("Content-type", "application/javascript")
        self.end_headers()
        if path == "gui/":
            path = "gui/index.html"
        try:
            with open(path, "rb") as f:  # lol better make sure that port is closed
                self.wfile.write(f.read())
        except Exception as e:
            print(e)
            # raise

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        raw_data = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(raw_data.decode("ascii"))
        path = urllib.parse.unquote(self.path)

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "application/JSON")
        self.end_headers()

        try:
            self.wfile.write(bytes(PATH_LOOKUP[path](data), "utf-8"))
        except Exception as e:
            print(e)
            raise

    def log_message(self, *args, **kwargs):
        pass


PATH_LOOKUP = {}


def route(path):
    def wrap(f):
        PATH_LOOKUP[path] = f
        return f

    return wrap


@route("/request_paragraph")
def request_paragraph(data):
    paragraph_index = randrange(NUM_PARAGRAPHS)
    return typing_test.new_sample(PARAGRAPH_PATH, paragraph_index)


@route("/analyze")
def compute_accuracy(data):
    prompted_text = data["promptedText"][0]
    typed_text = data.get("typedText", [""])[0]
    start_time = float(data["startTime"][0])
    end_time = float(data["endTime"][0])
    return json.dumps(
        typing_test.analyze(prompted_text, typed_text, start_time, end_time)
    )


@route("/translate_to_pig_latin")
def translate_to_pig_latin(data):
    text = data["text"][0]
    starting = text.split()
    translator = str.maketrans("", "", string.punctuation)
    stripped = [word.translate(translator) for word in starting]
    revised = []
    for index in range(len(stripped)):
        # this try-except is meant to handle numbers, 'F' or other things that have cannot be handled by pig_latin
        word = stripped[index]
        try:
            # this if-else is because only punctuation need to be added such as -, ?!
            if word != "":
                revised.append(typing_test.pig_latin(word.lower()))
            else:
                revised.append(starting[index])
        except:
            revised.append(word)

    # handles capitalization
    for i in range(len(stripped)):
        word = stripped[i]
        if word != "" and word[0].isupper():
            revised[i] = revised[i].capitalize()

    # for words with punctuation such as "Before, or end", defines first and last as first and last appearance of a letter
    for i in range(len(starting)):
        word = starting[i]
        for j in range(len(word)):
            if word[j] not in string.punctuation:
                first = j
                break
        for j in reversed(range(len(word))):
            if word[j] not in string.punctuation:
                last = j
                break

        # Adding punctuation from the original word using first/last
        if word != revised:
            if first != 0:
                revised[i] = word[:first] + revised[i]
            if last != len(word) - 1:
                revised[i] = revised[i] + word[last + 1 :]

    return " ".join(revised)


@route("/autocorrect")
def autocorrect(data):
    word = data.get("word", [""])[0]

    if word in WORDS_LIST:
        return word

    translator = str.maketrans("", "", string.punctuation)
    stripped = word.translate(translator)
    revised = stripped

    # Autocorrects current words on display after removing punctuation
    try:
        if stripped != "":
            revised = (
                typing_test.autocorrect(
                    stripped.lower(),
                    WORDS_LIST,
                    typing_test.score_function_final,
                )
            )
    except Exception as e:
        print(e)

    # handles capitalization
    if stripped != "" and stripped[0].isupper():
        revised = revised.capitalize()

    # finds the index of the first and last word in the original so wrapping punctuation can be added
    for j in range(len(word)):
        if word[j] not in string.punctuation:
            first = j
            break
    for j in reversed(range(len(word))):
        if word[j] not in string.punctuation:
            last = j
            break
    # adds wrapping punctuation
    if word != revised:
        if first != 0:
            revised = word[:first] + revised
        if last != len(word) - 1:
            revised = revised + word[last + 1 :]

    return revised


def start():
    socketserver.TCPServer.allow_reuse_address = True
    httpd = HTTPServer(("localhost", PORT), Handler)
    webbrowser.open("http://localhost:" + str(PORT), new=0, autoraise=True)
    httpd.serve_forever()


start()