test = {
  'name': 'Problem 2',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> analyze("12345", "12345", 0, 3)
          [20.0, 100.0]
          >>> analyze("a b c", "a b c", 10, 30) # Spaces count as characters!
          [3.0, 100.0]
          >>> analyze("a  b  c  d", "b  a  c  d", 12, 17)
          [24.0, 50.0]
          >>> analyze("a b", "c d e", 70, 190)
          [0.5, 0.0]
          >>> analyze("a b c", " a d ", 70, 190)
          [0.5, 50.0]
          >>> analyze("abc", " ", 10, 11)
          [12.0, 0.0]
          >>> analyze("abc", "", 10, 20)
          [0.0, 0.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> reference_text = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string1 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string2 = "Abstraction, in general, is a fundamentl concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction usd in other fields such as art."
          >>> typed_string3 = "Abstraction,"
          >>> typed_string4 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. extra"
          >>> typed_string5 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. art"
          >>> typed_string6 = "abstraction"
          >>> def check_wpm(pair, speed, accuracy):
          ...   if round(pair[0], 1) != speed:
          ...      print("WPM Incorrect: Expected {0} but got {1}".format(speed, round(pair[0], 1)))
          ...   elif round(pair[1], 1) != accuracy:
          ...      print("Accuracy Incorrect: Expected {0} but got {1}".format(accuracy, round(pair[1], 1)))
          >>> check_wpm(analyze(reference_text, typed_string1, 0, 67), 99.2, 100.0)
          >>> check_wpm(analyze(reference_text, typed_string2, 0, 67), 98.9, 97.7)
          >>> check_wpm(analyze(reference_text, typed_string3, 0, 67), 2.1, 100.0)
          >>> check_wpm(analyze(reference_text, typed_string4, 0, 67), 100.3, 100.0)
          >>> check_wpm(analyze(reference_text, typed_string5, 0, 67), 199.3, 100.0)
          >>> check_wpm(analyze(reference_text, typed_string6, 0, 1), 132.0, 0.0)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> try:
      ...    from typing_test import analyze
      ... except ImportError:
      ...    raise ImportError("You probably didn't define analyze in typing_test.py yet!")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
