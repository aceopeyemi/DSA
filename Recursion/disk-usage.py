import os

def disk_usage(path):
  """
  Return the total disk space used by a file/folder and it's descendants
  
  Inupt --  A string designating a path to a file-system entry
  Output -- Cumulative disk space used by that entry and any nested entries
  """
  total = os.path.getsize(path)                # account for direct usage

  if os.path.isdir(path):                      # confirm string path as directory
    for filename in os.listdir(path):
      child_path = os.path.join(path, filename) # compose path for each child in directory
      total += disk_usage(child_path)

  print('{0: <7}'.format(total), path)
  return total


disk_usage("/home/xviix/Desktop/Learning/python")