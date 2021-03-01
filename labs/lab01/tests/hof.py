test = {
  'name': 'Higher Order Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          beets
          >>> chocolate
          Function
          >>> chocolate()
          sweets
          'cake'
          >>> more_chocolate, more_cake = chocolate(), cake
          sweets
          >>> more_chocolate
          'cake'
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return chocolate
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          Function
          >>> snake(10, 20)()
          sweets
          'cake'
          >>> cake = 'cake'
          >>> snake(10, 20)
          30
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
