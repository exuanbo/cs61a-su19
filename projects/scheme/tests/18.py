test = {
  'name': 'Problem 18',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (zip '())
          (() ())
          scm> (zip '((1 4) (2 5) (3 6)))
          ((1 2 3) (4 5 6))
          scm> (zip '((a b) (c d) (e f)))
          ((a c e) (b d f))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (zip '((() ()) (() ())))
          ((() ()) (() ()))
          scm> (zip '(((1) (2 3)) ((4) (5 6))))
          (((1) (4)) ((2 3) (5 6)))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
