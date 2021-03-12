test = {
  'name': 'has-cycle?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (has-cycle? s)
          #f
          scm> (has-cycle? cycle)
          #t
          scm> (has-cycle? cycle-within)
          #t
          scm> (has-cycle? long)
          #t
          scm> (has-cycle? cycle-free)
          #f
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab14)
      scm> (define s (cons-stream 1 (cons-stream 2 nil)))
      scm> (define cycle (cons-stream 1 (cons-stream 1 cycle)))
      scm> (define cycle-within (cons-stream 1 (cons-stream 2 cycle)))
      scm> (define long (cons-stream 1 long))
      scm> (define (stream-add s n) (if (= n 0) s (cons-stream n (stream-add s (- n 1)))))
      scm> (define long (stream-add long 10))
      scm> (define cycle-free (stream-add nil 10))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
