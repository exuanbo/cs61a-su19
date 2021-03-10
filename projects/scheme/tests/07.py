test = {
  'name': 'Problem 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'fd4dd892ccea3adcf9446dc4a9738d47',
          'choices': [
            r"""
            Pair('quote', Pair(A, nil)), where:
                A is the quoted expression
            """,
            r"""
            [A], where:
                A is the quoted expression
            """,
            r"""
            Pair(A, nil), where:
                A is the quoted expression
            """,
            r"""
            A, where:
                A is the quoted expression
            """
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is the structure of the expressions argument to do_quote_form?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> ''hello
          f675ad62f5f67e5229145843fd6bbcaa
          # locked
          # choice: (quote hello)
          # choice: hello
          # choice: (hello)
          # choice: (quote (quote (hello)))
          scm> (quote (1 2))
          484e4b42665b2864d685ef07fe666107
          # locked
          scm> (car '(1 2 3))
          eb892a26497f936d1f6cae54aacc5f51
          # locked
          scm> (cdr '(1 2))
          750540b47bda75ff036b4a9aa741b087
          # locked
          scm> (eval (cons 'car '('(4 2))))
          46beb7deeeb5e9af1c8d785b12558317
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> read_line(" 'x ")
          d88f877a51ba10d1c3a834a690bb43e0
          # locked
          # choice: Pair('x', nil)
          # choice: 'x'
          # choice: Pair('quote', 'x')
          # choice: Pair('quote', Pair('x', nil))
          >>> read_line(" '(a b) ")
          e16dd0e729d41b52ddd5d4d38cbfc7e6
          # locked
          # choice: Pair('a', Pair('b', nil))
          # choice: Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
          # choice: Pair('quote', Pair('a', 'b'))
          # choice: Pair('quote', Pair('a', Pair('b', nil)))
          >>> read_line(" `(,b) ")
          c315b61bf342c663357b4788117c3f33
          # locked
          # choice: Pair('quasiquote', Pair(Pair(Pair('unquote', Pair('b', nil)), nil), nil))
          # choice: Pair('unquote', Pair('b', nil))
          # choice: Pair('quasiquote', Pair(Pair('unquote', Pair('b', nil)), nil))
          # choice: Pair('quasiquote', Pair('unquote', Pair('b', nil)))
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a (b 'c))")
          Pair('a', Pair(Pair('b', Pair(Pair('quote', Pair('c', nil)), nil)), nil))
          >>> read_line("(a (b '(c d)))")
          Pair('a', Pair(Pair('b', Pair(Pair('quote', Pair(Pair('c', Pair('d', nil)), nil)), nil)), nil))
          >>> read_line("')")
          SyntaxError
          >>> read_line("'()")
          Pair('quote', Pair(nil, nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("'('a)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), nil), nil))
          >>> read_line("''a")
          Pair('quote', Pair(Pair('quote', Pair('a', nil)), nil))
          >>> read_line("'('('a 'b 'c))")
          Pair('quote', Pair(Pair(Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), Pair(Pair('quote', Pair('b', nil)), Pair(Pair('quote', Pair('c', nil)), nil))), nil)), nil), nil))
          >>> read_line("(+ '(1 2) 3)")
          Pair('+', Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(3, nil)))
          >>> read_line("'('+ '(1 2) '3)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('+', nil)), Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(Pair('quote', Pair(3, nil)), nil))), nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(["'hello"])))
          Pair('quote', Pair('hello', nil))
          >>> read_line("(car '(1 2))")
          Pair('car', Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), nil))
          >>> print(read_line("(car '(1 2))"))
          (car (quote (1 2)))
          >>> read_line("'('a)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), nil), nil))
          >>> read_line("''a")
          Pair('quote', Pair(Pair('quote', Pair('a', nil)), nil))
          >>> read_line("'('('a 'b 'c))")
          Pair('quote', Pair(Pair(Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), Pair(Pair('quote', Pair('b', nil)), Pair(Pair('quote', Pair('c', nil)), nil))), nil)), nil), nil))
          >>> read_line("(+ '(1 2) 3)")
          Pair('+', Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(3, nil)))
          >>> read_line("'('+ '(1 2) '3)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('+', nil)), Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(Pair('quote', Pair(3, nil)), nil))), nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(["`hello"])))
          Pair('quasiquote', Pair('hello', nil))
          >>> read_line("(car `(1 2))")
          Pair('car', Pair(Pair('quasiquote', Pair(Pair(1, Pair(2, nil)), nil)), nil))
          >>> print(read_line("(car `(1 2))"))
          (car (quasiquote (1 2)))
          >>> read_line(" `(,b) ")
          Pair('quasiquote', Pair(Pair(Pair('unquote', Pair('b', nil)), nil), nil))
          >>> read_line("'(`(,a ,b ,c))")
          Pair('quote', Pair(Pair(Pair('quasiquote', Pair(Pair(Pair('unquote', Pair('a', nil)), Pair(Pair('unquote', Pair('b', nil)), Pair(Pair('unquote', Pair('c', nil)), nil))), nil)), nil), nil))
          >>> read_line(" `(a ,b) ")
          Pair('quasiquote', Pair(Pair('a', Pair(Pair('unquote', Pair('b', nil)), nil)), nil))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (quote hello)
          hello
          scm> 'hello
          hello
          scm> (quote (1 2))
          (1 2)
          scm> '(1 2)
          (1 2)
          scm> (car (car '((1))))
          1
          scm> (quote 3)
          3
          scm> (quasiquote a)
          a
          scm> `a
          a
          scm> `(a b c)
          (a b c)
          scm> (define b 2)
          b
          scm> `(a ,b c)
          (a 2 c)
          scm> ,b
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
