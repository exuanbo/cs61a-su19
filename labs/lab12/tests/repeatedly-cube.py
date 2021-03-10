test = {
  'name': 'repeatedly-cube',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (repeatedly-cube 100 1)
          1
          scm> (repeatedly-cube 2 2)
          512
          scm> (repeatedly-cube 3 2)
          134217728
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab12)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
