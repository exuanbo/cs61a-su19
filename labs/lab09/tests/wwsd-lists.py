test = {
  'name': 'What Would Scheme Print?',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'setup': """
      """,
      'cases': [
        {
          'code':"""
          scm> (cons 1 (cons 2 nil))
          (1 2)
          """,
          'hidden':False
        },
        {
          'code':"""
          scm> (car (cons 1 (cons 2 nil)))
          1
          """,
          'hidden':False
        },
        {
          'code':"""
          scm> (cdr (cons 1 (cons 2 nil)))
          (2)
          """,
          'hidden':False
        },
        {
          'code':"""
          scm> (list 1 2 3)
          (1 2 3)
          """,
          'hidden':False
        },
        {
          'code':"""
          scm> '(1 2 3)
          (1 2 3)
          """,
          'hidden':False
        },
        {
          'code':"""
          scm> (cons 1 '(list 2 3))  ; Recall quoting
          (1 list 2 3)
          """,
          'hidden': False
        }
      ]
    },
    {
      'type': 'scheme',
      'scored': True,
      'setup': """
      """,
      'cases': [
        {
          'code': """
          scm> '(cons 4 (cons (cons 6 8) ()))
          (cons 4 (cons (cons 6 8) ()))
          """,
          'hidden': False
        }
      ]
    }
  ]
}
