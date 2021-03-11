test = {
  'name': 'lets-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from su19favpets;
          dog|15
          cat|9
          lion|4
          cheetah|3
          golden retriever|3
          pig|3
          corgi|2
          horse|2
          human|2
          koala|2
          sqlite> SELECT * from su19dog;
          dog|15
          sqlite> SELECT * from obedienceimages;
          7|1|6
          7|2|7
          7|4|3
          7|5|7
          7|6|11
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
