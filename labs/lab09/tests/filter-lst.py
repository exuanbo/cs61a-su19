test = {
  'name': 'filter-lst',
  'points': 1,
  'suites': [
    {
      'scored': True,
      'setup': """
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'type': 'scheme',
      'cases': [
        {
          'code': """
          scm> (filter-lst even? '(1 2 3 4))
          (2 4)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (filter-lst odd? '(1 3 5))
          (1 3 5)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (filter-lst odd? '(2 4 6 1))
          (1)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (filter-lst even? '(3))
          ()
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (filter-lst odd? nil)
          ()
          """,
          'hidden': False
        }
      ]
    }
  ]
}
