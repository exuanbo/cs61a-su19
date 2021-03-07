test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> path = "data/words.txt"
          >>> len(lines_from_file(path)) # Number of lines in the file
          20000
          >>> 'a\n' not in lines_from_file(path) # Newlines should not be present
          True
          >>> lines_from_file(path)[0] 
          'a'
          >>> 'aa' in lines_from_file(path)
          True
          >>> 'aa\n' not in lines_from_file(path)
          True
          >>> 'seemingly' in lines_from_file(path)
          True
          >>> 'heterogeneous ' in lines_from_file(path)
          False
          >>> 'heterogeneous' in lines_from_file(path)
          True
          >>> '61A' in lines_from_file(path)
          False
          >>> lines_from_file(path)[900:905]
          ['applicable', 'applicant', 'applicants', 'application', 'applications']
          >>> lines_from_file(path)[1940:1945]
          ['biz', 'bizarre', 'bizjournals', 'bizjournalshire', 'bizkit']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> path = "data/test.txt"
          >>> len(lines_from_file(path)) # Number of lines in the file
          9
          >>> 'a ' in lines_from_file(path)
          False
          >>> 'a' in lines_from_file(path)
          True
          >>> lines_from_file(path)
          ['This', 'is', 'a', 'test', '', '', '', '', "I'm later in the file!"]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> path = "data/sample_paragraphs.txt"
          >>> new_sample(path, 0)[:15] # Get first 15 characters 
          '"Before I died,'
          >>> new_sample(path, 1685)[:32] # Get first 32 characters 
          'I etched your name in the clouds'
          >>> new_sample("data/words.txt", 12388) # Should be able to read from any file
          'oldham'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> try:
      ...    from typing_test import new_sample, lines_from_file
      ... except ImportError:
      ...    raise ImportError("You probably didn't define new_sample in typing_test.py yet!")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
