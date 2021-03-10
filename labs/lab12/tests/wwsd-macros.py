test = {
  'name': 'wwsd-macros',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> +
          51bfa5984c87ff1d71bfa9ca621f85f4
          # locked
          scm> list
          a23083f783ea763b6585652e0816edca
          # locked
          scm> (define-macro (f x) (car x))
          83d9b1603da85dd6d278078a1f8afda8
          # locked
          scm> (f (2 3 4)) ; type SchemeError for error, or Nothing for nothing
          b764c5386326cd8ae89e4efe0c923e84
          # locked
          scm> (f (+ 2 3))
          51bfa5984c87ff1d71bfa9ca621f85f4
          # locked
          scm> (define x 2000)
          ecf2b304041c91c68610920edf6214eb
          # locked
          scm> (f (x y z))
          60d2afc8beea4d0f7c24bae779a93328
          # locked
          scm> (f (list 2 3 4))
          a23083f783ea763b6585652e0816edca
          # locked
          scm> (f (quote (2 3 4)))
          443b7d7e1f6dc28b66183d0823fa4384
          # locked
          scm> (define quote 7000)
          48c8ad7efab74c1eb5133f264834f79d
          # locked
          scm> (f (quote (2 3 4)))
          1754aaef39d25285edb514499728e228
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define-macro (g x) (+ x 2))
          d6310604e0434df326dccb3c5a00fb29
          # locked
          scm> (g 2)
          ffb5aaa34514b07fff5f97d4e2bbc604
          # locked
          scm> (g (+ 2 3))
          443b7d7e1f6dc28b66183d0823fa4384
          # locked
          scm> (define-macro (h x) (list '+ x 2))
          e475e9d246f84693fe142abd743cb118
          # locked
          scm> (h (+ 2 3))
          aea886c5344dce93fdfe92cd56235cbb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define-macro (if-else-5 condition consequent) `(if ,condition ,consequent 5))
          d649bbef3d885c89ced48f4ac0cfa02d
          # locked
          scm> (if-else-5 #t 2)
          b764c5386326cd8ae89e4efe0c923e84
          # locked
          scm> (if-else-5 #f 3)
          3b2d9316bebaa3b3f233e455d255a9e1
          # locked
          scm> (if-else-5 #t (/ 1 0))
          443b7d7e1f6dc28b66183d0823fa4384
          # locked
          scm> (if-else-5 #f (/ 1 0))
          3b2d9316bebaa3b3f233e455d255a9e1
          # locked
          scm> (if-else-5 (= 1 1) 2)
          b764c5386326cd8ae89e4efe0c923e84
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
