test = {
  'name': 'Problem 7',
  'points': 1,
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
          >>> score1 = score_function_accurate("wird", "wiry")
          >>> score2 = score_function_accurate("wird", "bird")
          >>> score3 = score_function_accurate("wird", "wire")
          >>> score3 < score1 and score3 < score2
          True
          >>> score2 > score1
          True
          >>> int(score_function_accurate("speling", "spelling"))
          1
          >>> int(score_function_accurate("used", "use"))
          1
          >>> int(score_function_accurate("hash", "ash"))
          1
          >>> int(score_function_accurate("ash", "hash"))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "wire", "peeling", "gestate", 
          ...                     "west", "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, score_function_accurate)
          'spelling'
          >>> autocorrect("abstrction", small_words_list, score_function_accurate)
          'abstraction'
          >>> autocorrect("wird", small_words_list, score_function_accurate)
          'wire'
          >>> autocorrect("gest", small_words_list, score_function_accurate)
          'test'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> try:
      ...    from typing_test import score_function_accurate, autocorrect
      ...    from utils import *
      ... except ImportError:
      ...    raise ImportError("You probably didn't define score_function_accurate in typing_test.py yet!")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
