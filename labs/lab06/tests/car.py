test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> from car import *
          >>> garcias_car = Car('Tesla', 'Model S')
          >>> garcias_car.model
          'Model S'
          >>> garcias_car.gas = 10
          >>> garcias_car.drive()
          'Tesla Model S goes vroom!'
          >>> garcias_car.drive()
          'Cannot drive!'
          >>> garcias_car.fill_gas()
          'Gas level: 20'
          >>> garcias_car.gas
          20
          >>> Car.gas
          30
          """,
        },
        {
          'code': """
          >>> from car import *
          >>> garcias_car = Car('Tesla', 'Model S')
          >>> garcias_car.wheels = 2
          >>> garcias_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> garcias_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          'Cannot drive!'
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          >>> Car.drive(garcias_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Cannot drive!'
          """,
        },
        {
          'code': """
          >>> from car import *
          >>> garcias_car = MonsterTruck('Monster', 'Batmobile')
          >>> garcias_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.drive(garcias_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Monster Batmobile goes vroom!'
          >>> MonsterTruck.drive(garcias_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.rev(garcias_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          """,
        }
      ]
    }
  ]
}
