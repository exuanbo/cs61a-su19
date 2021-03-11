test = {
  'name': 'smallest-int-having',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_having LIMIT 50;
          2019/08/06 8:17:11 PM MDT|5
          2019/08/06 4:37:07 PM MDT|9
          2019/08/06 6:35:56 PM MDT|10
          2019/08/06 9:33:47 PM MDT|13
          2019/08/06 9:49:44 PM MDT|16
          2019/08/06 7:11:54 PM MDT|18
          2019/08/06 4:42:48 PM MDT|20
          2019/08/06 4:33:47 PM MDT|21
          2019/08/06 10:37:02 PM MDT|23
          2019/08/06 5:39:08 PM MDT|24
          2019/08/06 6:59:14 PM MDT|25
          2019/08/06 4:33:12 PM MDT|29
          2019/08/06 4:22:54 PM MDT|32
          2019/08/06 10:04:43 PM MDT|35
          2019/08/06 4:59:50 PM MDT|36
          2019/08/06 4:32:49 PM MDT|42
          2019/08/06 4:49:56 PM MDT|43
          2019/08/06 6:43:56 PM MDT|52
          2019/08/06 4:47:30 PM MDT|53
          2019/08/06 11:57:12 PM MDT|57
          2019/08/06 5:05:40 PM MDT|69
          2019/08/06 9:12:18 PM MDT|73
          2019/08/06 10:17:14 PM MDT|107
          2019/08/06 4:19:18 PM MDT|123
          2019/08/06 5:54:36 PM MDT|124
          2019/08/06 4:30:02 PM MDT|999999999999999999
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
