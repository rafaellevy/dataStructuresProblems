
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
    # if os.path.endswith(suffix):
        # listOfPaths.append(os.path)
    # if os.path.isdir(path):
        # filesAndDirectories = os.listdir(path)
        # for name in FilesAndDirectories:
            # if os.path.endswith(suffix):
                # listOfPaths.append(os.path)    
            # newPath = os.path.join(name)
            # find_files(suffix, newPath)



    #return listOfPaths 

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python


# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))