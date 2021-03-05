""" Optional questions for Lab 05 """

from lab05 import *


# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = "."
    for word in tokens:
        if prev not in table:
            "*** YOUR CODE HERE ***"
            table[prev] = [word]
        else:
            table[prev] += [word]
        "*** YOUR CODE HERE ***"
        prev = word
    return table


def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random

    result = ""
    while word not in [".", "!", "?"]:
        "*** YOUR CODE HERE ***"
        if len(result) != 0:
            result += " "
        result += word
        word = table[word][0]
    return result.strip() + word


def shakespeare_tokens(path="shakespeare.txt",
                       url="http://composingprograms.com/shakespeare.txt"):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen

    if os.path.exists(path):
        return open("shakespeare.txt", encoding="ascii").read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding="ascii").split()


# Uncomment the following two lines
tokens = shakespeare_tokens()
table = build_successors_table(tokens)


def random_sent():
    import random

    return construct_sent(random.choice(table["."]), table)


def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t), [tree(v) for v in vals])
    return tree(label(t), [sprout_leaves(b, vals) for b in branches(t)])


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if not t1 or not t2:
        return t1 or t2
    return tree(
        label(t1) + label(t2),
        [
            add_trees(b1, b2)
            for b1, b2 in pair_lists(branches(t1), branches(t2))
        ],
    )


def pair_lists(l1, l2):
    return [(i < len(l1) and l1[i] or None, i < len(l2) and l2[i] or None)
            for i in range(max(len(l1), len(l2)))]
