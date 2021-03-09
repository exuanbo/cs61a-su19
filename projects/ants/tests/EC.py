test = {
  'name': 'Problem EC',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing status parameters
          >>> slow = SlowThrower()
          >>> scary = ScaryThrower()
          >>> SlowThrower.food_cost
          4
          >>> ScaryThrower.food_cost
          6
          >>> slow.armor
          1
          >>> scary.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Slow
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> colony.places["tunnel_0_0"].add_insect(slow)
          >>> colony.places["tunnel_0_4"].add_insect(bee)
          >>> slow.action(colony)
          >>> colony.time = 1
          >>> bee.action(colony)
          >>> bee.place.name # SlowThrower should cause slowness on odd turns
          'tunnel_0_4'
          >>> colony.time += 1
          >>> bee.action(colony)
          >>> bee.place.name # SlowThrower should cause slowness on odd turns
          'tunnel_0_3'
          >>> for _ in range(3):
          ...    colony.time += 1
          ...    bee.action(colony)
          >>> bee.place.name
          'tunnel_0_1'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Scare
          >>> error_msg = "ScaryThrower doesn't scare for exactly two turns."
          >>> scary = ScaryThrower()
          >>> bee = Bee(3)
          >>> colony.places["tunnel_0_0"].add_insect(scary)
          >>> colony.places["tunnel_0_4"].add_insect(bee)
          >>> scary.action(colony)
          >>> bee.action(colony)
          >>> bee.place.name # ScaryThrower should scare for two turns
          'tunnel_0_5'
          >>> bee.action(colony)
          >>> bee.place.name # ScaryThrower should scare for two turns
          'tunnel_0_6'
          >>> bee.action(colony)
          >>> bee.place.name
          'tunnel_0_5'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if effects stack
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> slow_place = colony.places["tunnel_0_0"]
          >>> bee_place = colony.places["tunnel_0_4"]
          >>> slow_place.add_insect(slow)
          >>> bee_place.add_insect(bee)
          >>> for _ in range(2):    # slow bee two times
          ...    slow.action(colony)
          
          >>> colony.time = 1
          >>> for _ in range(5):        # bee should only move on odd times
          ...    bee.action(colony)
          ...    colony.time += 1
          
          >>> bee.place.name
          'tunnel_0_2'
          
          >>> colony.time += 1      # slow effects have worn off
          >>> bee.action(colony)
          >>> bee.place.name
          'tunnel_0_1'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing multiple scared bees
          >>> scare1 = ScaryThrower()
          >>> scare2 = ScaryThrower()
          >>> bee1 = Bee(3)
          >>> bee2 = Bee(3)
          
          >>> colony.places["tunnel_0_0"].add_insect(scare1)
          >>> colony.places["tunnel_0_1"].add_insect(bee1)
          >>> colony.places["tunnel_0_4"].add_insect(scare2)
          >>> colony.places["tunnel_0_5"].add_insect(bee2)
          
          >>> scare1.action(colony)
          >>> scare2.action(colony)
          >>> bee1.action(colony)
          >>> bee2.action(colony)
          
          >>> bee1.place.name
          'tunnel_0_2'
          >>> bee2.place.name
          'tunnel_0_6'
          
          >>> bee1.action(colony)
          >>> bee2.action(colony)
          
          >>> bee1.place.name
          'tunnel_0_3'
          >>> bee2.place.name
          'tunnel_0_7'
          
          >>> bee1.action(colony)
          >>> bee2.action(colony)
          
          >>> bee1.place.name
          'tunnel_0_2'
          >>> bee2.place.name
          'tunnel_0_6'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> scare = ScaryThrower()
          >>> bee = Bee(3)
          >>> colony.places["tunnel_0_0"].add_insect(scare)
          >>> colony.places["tunnel_0_1"].add_insect(bee)
          
          >>> scare.action(colony)
          >>> bee.action(colony)
          
          >>> bee.place.name
          'tunnel_0_2'
          
          >>> bee.action(colony)
          
          >>> bee.place.name
          'tunnel_0_3'
          
          >>> #
          >>> # Same bee should not be scared more than once
          >>> scare.action(colony)
          >>> bee.action(colony)
          
          >>> bee.place.name
          'tunnel_0_2'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing long effect stack
          >>> scary = ScaryThrower()
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> colony.places["tunnel_0_0"].add_insect(scary)
          >>> colony.places["tunnel_0_1"].add_insect(slow)
          >>> colony.places["tunnel_0_3"].add_insect(bee)
          
          >>> scary.action(colony) # scare bee once
          
          >>> colony.time = 0
          >>> bee.action(colony) # scared
          >>> bee.place.name
          'tunnel_0_4'
          
          >>> for _ in range(3): # slow bee three times
          ...    slow.action(colony)
          
          >>> colony.time = 1
          >>> bee.action(colony) # scared, but also slowed thrice
          >>> bee.place.name
          'tunnel_0_4'
          
          >>> colony.time = 2
          >>> bee.action(colony) # scared and slowed thrice
          >>> bee.place.name
          'tunnel_0_5'
          
          >>> colony.time = 3
          >>> bee.action(colony) # slowed thrice
          >>> bee.place.name
          'tunnel_0_5'
          
          >>> colony.time = 4
          >>> bee.action(colony) # slowed twice
          >>> bee.place.name
          'tunnel_0_4'
          
          >>> colony.time = 5
          >>> bee.action(colony) # slowed twice
          >>> bee.place.name
          'tunnel_0_4'
          
          >>> colony.time = 6
          >>> bee.action(colony) # slowed once
          >>> bee.place.name
          'tunnel_0_3'
          
          >>> colony.time = 7
          >>> bee.action(colony) # status effects have worn off
          >>> bee.place.name
          'tunnel_0_2'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
