def print_string_utils(string):
  return string


def extract_lengthy_capitals_utils(list_capitals: list) -> list:
  '''
  Skims thorough a list of capitals and extracts
  all capitals that have more than 5 letters by 
  returning a new list.

  Arguments:
  - list_capitals(list): List of capitals to skim
  through.
  
  Returns:
  - lenghty_capitals(list): List of capitals with
  more than 5 letters.
  '''
  lengthy_capitals = []

  for capital in list_capitals:
    if len(capital) > 5:
      lengthy_capitals.append(capital)
  
  return lengthy_capitals