test = {
  'name': 'obedience',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          7|5
          Choose this option instead|2
          7|6
          the number 7 below.|6
          7|6
          the number 7 below.|5
          7|2
          7|2
          You're not the boss of me!|6
          Choose this option instead|4
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
