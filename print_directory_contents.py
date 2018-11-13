path='/Users/zhibwang/tmp'
def print_directory_content(path):
  import os
  for item in os.listdir(path): 
    item_full_path = os.path.join(path, item)
    if os.path.isdir(item_full_path):
      print_directory_content(item_full_path)
    print item_full_path

print_directory_content(path)
