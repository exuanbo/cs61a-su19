test = {
  'name': 'cadr-caddr',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cddr '(1 2 3 4))
          f69d877c9d1cc2439829045a806713f3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cadr '(1 2 3 4))
          86902deeeb9755c15c199c7130a618ba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (caddr '(1 2 3 4))
          0f84c8951dcc7525fd37e710a2405e91
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw06)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
