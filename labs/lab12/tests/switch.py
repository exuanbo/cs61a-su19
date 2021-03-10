test = {
  'name': 'switch',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (switch 1 ((1 (print 'a))
          ....            (2 (print 'b))
          ....            (3 (print 'c))))
          a
          scm> (switch (+ 1 1) ((1 (print 'a))
          ....                  (2 (print 'b))
          ....                  (3 (print 'c))))
          b
          scm> (define x 'b)
          x
          scm> (switch x ((a (print 1))
          ....            (b (print 2))
          ....            (c (print 3))))
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab12_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
