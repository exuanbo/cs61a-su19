test = {
  'name': 'smallest-int',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int;
          2019/08/06 11:55:41 PM MDT|3
          2019/08/06 7:39:13 PM MDT|3
          2019/08/06 10:23:42 PM MDT|4
          2019/08/06 10:55:38 PM MDT|4
          2019/08/06 4:22:56 PM MDT|4
          2019/08/06 4:54:35 PM MDT|4
          2019/08/06 8:17:11 PM MDT|5
          2019/08/06 10:53:09 PM MDT|6
          2019/08/06 5:24:43 PM MDT|6
          2019/08/06 7:25:22 PM MDT|6
          2019/08/06 10:26:56 PM MDT|7
          2019/08/06 4:30:17 PM MDT|7
          2019/08/06 5:43:06 PM MDT|7
          2019/08/06 6:23:10 PM MDT|7
          2019/08/06 7:31:21 PM MDT|7
          2019/08/06 4:25:54 PM MDT|8
          2019/08/06 5:13:55 PM MDT|8
          2019/08/06 5:32:52 PM MDT|8
          2019/08/06 4:37:07 PM MDT|9
          2019/08/06 6:35:56 PM MDT|10
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
