test = {
  'name': 'size',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM low_variance;
          curly|63
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw07.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
