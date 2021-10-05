
"""
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
import os

def find_files(suffix, path):
    # check if path is directory or not
    if not os.path.isdir(path):
        return "invalid path"
    # collect all subdirectories and files in list for looping
    list_of_paths = os.listdir(path)
    output = []
    for element in list_of_paths:
        item = os.path.join(path, element)
        # check if the item is a directory
        if os.path.isdir(item):
            # recursion method
            output += find_files(suffix, item)
        # check if the file extension equals the suffix
        if os.path.isfile(item) and item.endswith(suffix):
            output.append(item)
    
    return output
    

testString = "/Users/rafaellevy/Downloads/testdir"
print(find_files("", testString ))
# expect empty list
print(find_files(".c", testString ))
# expect a list with all the files ending in .c
print(find_files(".pdf", testString ))
# expect empty list

   