test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> tiffanys_car = Car('Tesla', 'Model S')
          >>> tiffanys_car.model
          'Model S'
          >>> tiffanys_car.gas = 10
          >>> tiffanys_car.drive()
          'Tesla Model S goes vroom!'
          >>> tiffanys_car.drive()
          'Cannot drive!'
          >>> tiffanys_car.fill_gas()
          'Gas level: 20'
          >>> tiffanys_car.gas
          20
          >>> Car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> christophers_car = Car('Tesla', 'Model S')
          >>> christophers_car.wheels = 2
          >>> christophers_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> christophers_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          'Cannot drive!'
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          >>> Car.drive(christophers_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Cannot drive!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> alexs_car = MonsterTruck('Monster', 'Batmobile')
          >>> alexs_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.drive(alexs_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Monster Batmobile goes vroom!'
          >>> MonsterTruck.drive(alexs_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.rev(alexs_car) # Type Error if an error occurs and Nothing if nothing is displayed
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
