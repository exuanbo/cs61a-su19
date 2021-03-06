test = {
  'name': 'Call Expressions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from operator import add
          >>> def double(x):
          ...     return x + x
          >>> def square(y):
          ...     return y * y
          >>> def f(z):
          ...     add(square(double(z)), 1)
          >>> f(4)
          fd8df12894b49bf2c3a4705c3d3193f4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def foo(x, y):
          ...     print("x or y")
          ...     return x or y
          >>> a = foo
          fd8df12894b49bf2c3a4705c3d3193f4
          # locked
          >>> b = foo()
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          >>> c = a(print("x"), print("y"))
          e8bccfd485df815928620ee859d22623
          516263f4e0556448f570fb3883d3465c
          2ce17417571aeea1ce138ca763246bdc
          # locked
          >>> print(c)
          ecd4117e3519db3e91577e0c66d69602
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def welcome():
          ...     print('welcome to')
          ...     return 'hello'
          >>> def cs61a():
          ...     print('cs61a')
          ...     return 'world'
          >>> print(welcome(), cs61a())
          6a4cdd9c4efe5db367cb8b27c4fdf874
          b679c4c818610ab50d64b9e0fff90e1c
          526acdb3cc4db84038ffa720e75aedfa
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
