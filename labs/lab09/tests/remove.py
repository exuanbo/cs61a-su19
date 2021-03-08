test = {
  'name': 'remove',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'setup': """
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'cases': [
        {
          'code': """
          scm> (remove 3 nil)
          ()
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (remove 2 '(1 3 2))
          (1 3)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (remove 1 '(1 3 2))
          (3 2)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (remove 42 '(1 3 2))
          (1 3 2)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (remove 3 '(1 3 3 7))
          (1 7)
          """,
          'hidden': False
        }
      ]
    }
  ]
}
