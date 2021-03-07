test = {
  'name': 'Problem 5',
  'points': 2,
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
          >>> swap_score("car", "cad")
          1
          >>> swap_score("pront", "print")
          1
          >>> swap_score("misspollid", "misspelled")
          2
          >>> swap_score("this", "that")
          2
          >>> swap_score("one", "two")
          3
          >>> swap_score("from", "form")
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_score("goodbye", "good")
          0
          >>> swap_score("worry", "word")
          1
          >>> swap_score("first", "flashy")
          3
          >>> swap_score("hash", "ash")
          3
          >>> swap_score("ash", "hash")
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "peeling", "gestate", "west",
          ...                     "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, swap_score)
          'spell'
          >>> autocorrect("abstrction", small_words_list, swap_score)
          'nest'
          >>> autocorrect("wird", small_words_list, swap_score)
          'bird'
          >>> autocorrect("gest", small_words_list, swap_score)
          'gestate'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> try:
      ...    from typing_test import swap_score, autocorrect
      ...    from utils import *
      ... except ImportError:
      ...    raise ImportError("You probably didn't define swap_score in typing_test.py yet!")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
