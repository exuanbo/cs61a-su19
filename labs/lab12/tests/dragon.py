test = {
  'name': 'dragon',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (flatmap (lambda (x) (list (+ x 10) x)) nil)
          ()
          scm> (flatmap list '(1 2 3))
          (1 2 3)
          scm> (flatmap (lambda (x) (list (+ x 10) x)) '(1 2 3))
          (11 1 12 2 13 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (expand '(f))
          (f)
          scm> (expand '(x))
          (x r y f r)
          scm> (expand '(y))
          (l f x l y)
          scm> (expand '(f x y))
          (f x r y f r l f x l y)
          scm> (expand '(f r l f r l x x))
          (f r l f r l x r y f r x r y f r)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab12_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
