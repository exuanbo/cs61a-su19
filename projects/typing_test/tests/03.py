test = {
  'name': 'Problem 3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pig_latin("banana")
          'ananabay'
          >>> pig_latin("explain")
          'explainway'
          >>> pig_latin("ubiquitous")
          'ubiquitousway'
          >>> pig_latin("string")
          'ingstray'
          >>> pig_latin("aardvark")
          'aardvarkway'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pig_latin("yak")
          'akyay'
          >>> pig_latin("obvious")
          'obviousway'
          >>> pig_latin("beautiful")
          'eautifulbay'
          >>> pig_latin("full-time")
          'ull-timefay'
          >>> pig_latin("i/o")
          'i/oway'
          >>> pig_latin("8-way")
          'ay8-way'
          >>> pig_latin("schtschurowskia")
          'urowskiaschtschay'
          >>> pig_latin("rhythm")
          'rhythmay'
          >>> pig_latin("2019")
          '2019ay'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> try:
      ...    from typing_test import pig_latin
      ... except ImportError:
      ...    raise ImportError("You probably didn't define pig_latin in typing_test.py yet!")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
