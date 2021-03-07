test = {
  'name': 'Problem 6',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> check_passphrase(passphrase) # Ensuring you completed design doc & changed passphrase
          '814716d640bad70cbb9c76c72f2810e06f588a1bc1039d2510acab2d'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> score_function("speling", "spelling")
          1
          >>> score_function("used", "use")
          1
          >>> score_function("misspelled", "spelling")
          6
          >>> score_function("spelling", "spelling")
          0
          >>> score_function("wird", "bird")
          1
          >>> score_function("wird", "wire")
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> score_function("hello", "goodbye")
          7
          >>> score_function("ate", "apple")
          3
          >>> score_function("from", "form")
          2
          >>> score_function("first", "flashy")
          4
          >>> score_function("hash", "ash")
          1
          >>> score_function("ash", "hash")
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "peeling", "gestate", "west",
          ...                     "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, score_function)
          'spelling'
          >>> autocorrect("abstrction", small_words_list, score_function)
          'abstraction'
          >>> autocorrect("wird", small_words_list, score_function)
          'bird'
          >>> autocorrect("gest", small_words_list, score_function)
          'nest'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> try:
      ...    from typing_test import score_function, autocorrect
      ...    from utils import *
      ... except ImportError:
      ...    raise ImportError("You probably didn't define score_function in typing_test.py yet!")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
