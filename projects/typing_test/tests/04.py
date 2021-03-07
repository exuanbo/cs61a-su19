test = {
  'name': 'Problem 4',
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
          >>> score_fn_1 = lambda w1, w2: abs(len(w2) - len(w1))
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], score_fn_1)
          'cult'
          >>> autocorrect("wor", ["worry", "car", "part"], score_fn_1)
          'car'
          >>> score_fn_2 = lambda w1, w2: w1[0] != w2[0] # 0 if first chars equal, 1 otherwise
          >>> autocorrect("wrod", ["word", "rod"], score_fn_2)
          'word'
          >>> autocorrect("inside", ["inside", "idea"], score_fn_2) # Contained inside the words list
          'inside'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> score_fn_3 = lambda w1, w2: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) #Num matching chars
          >>> autocorrect("tosting", ["testing", "asking", "fasting"], score_fn_3)
          'testing'
          >>> autocorrect("tsting", ["testing", "rowing"], score_fn_3)
          'rowing'
          >>> autocorrect("bwe", ["awe", "bye"], score_fn_3)
          'awe'
          >>> autocorrect("bwe", ["bye", "awe"], score_fn_3)
          'bye'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect("testng", words_list, lambda w1, w2: 1)
          'a'
          >>> autocorrect("testing", words_list, lambda w1, w2: 1)
          'testing'
          >>> autocorrect("gesting", words_list, lambda w1, w2: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) + abs(len(w1) - len(w2)))
          'getting'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> try:
      ...    from typing_test import autocorrect, lines_from_file
      ...    from utils import *
      ...    words_list = sorted(lines_from_file('data/words.txt'))
      ... except ImportError:
      ...    raise ImportError("You probably didn't define autocorrect in typing_test.py yet!")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
