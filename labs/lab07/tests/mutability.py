test = {
  'name': 'Mutability',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lst = [5, 6, 7, 8]
          >>> lst.append(6)
          fd8df12894b49bf2c3a4705c3d3193f4
          # locked
          >>> lst
          7b34159ae847900d406f35a5788ae045
          # locked
          >>> lst.insert(0, 9)
          >>> lst
          f888c6c8c2837981bb4e2f63d443cc8c
          # locked
          >>> x = lst.pop(2)
          >>> lst
          c9e941e225fba84174e5e1a0c7962c0b
          # locked
          >>> lst.remove(x)
          >>> lst
          02f6805e635355480bec2170a06846b8
          # locked
          >>> a, b = lst, lst[:]
          >>> a is lst
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> b == lst
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> b is lst
          1a1d55c577c8de00da2b32e78f9335d1
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          a193134aaca4f55ba817f224d1d07e25
          # locked
          >>> len(pokemon)
          9a023de211dac9bf8558350f5fa3bdca
          # locked
          >>> pokemon['jolteon'] = 135
          >>> pokemon['mew'] = 25
          >>> len(pokemon)
          f2991d685f624ad59b79213e20800653
          # locked
          >>> 'mewtwo' in pokemon
          1a1d55c577c8de00da2b32e78f9335d1
          # locked
          >>> 'pikachu' in pokemon
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> 25 in pokemon
          1a1d55c577c8de00da2b32e78f9335d1
          # locked
          >>> 151 in pokemon
          1a1d55c577c8de00da2b32e78f9335d1
          # locked
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> pokemon['ditto']
          a4466723f36eb7913cfd24496b74c24f
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
