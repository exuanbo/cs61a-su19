test = {
  'name': 'Higher Order Functions, Part 2',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def cloning(x):
          ...     def machine(y):
          ...          y += 3
          ...          return x(y)
          ...     return machine
          >>> def increment(x):
          ...     return x + 1
          >>> dolly = cloning(increment)
          >>> a = 3
          >>> dolly(a)
          7
          >>> a
          3
          >>> x23 = cloning(increment)
          >>> x23(2) == dolly(2)
          True
          >>> x23 == dolly
          False
          >>> x23(dolly)
          Error
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
