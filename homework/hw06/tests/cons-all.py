test = {
  'name': 'cons-all',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cons-all 1 '())
          ()
          scm> (cons-all 0 '((1 2)))
          ((0 1 2))
          scm> (cons-all 0 '((1 2) (3 4) (5 6)))
          ((0 1 2) (0 3 4) (0 5 6))
          scm> (cons-all 1 '(()))
          ((1))
          scm> (cons-all 'a '((b c) ((d e) f)))
          ((a b c) (a (d e) f))
          """,
          'hidden': False,
          'locked': False
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
