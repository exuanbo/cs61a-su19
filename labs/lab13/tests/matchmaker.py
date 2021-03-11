test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          dog|Old Town Road|green|blue
          cheetah|Clair De Lune|magenta|blue
          cat|Old Town Road|blue|purple
          dog|All I want for Christmas|white|light blue
          cat|Bohemian Rhapsody|dark white|red
          cat|Bohemian Rhapsody|dark white|red
          dog|Bohemian Rhapsody|blue|light gray
          dog|Bohemian Rhapsody|blue|lavender
          dog|Bohemian Rhapsody|blue|royal blue
          dog|Bohemian Rhapsody|blue|orange
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
