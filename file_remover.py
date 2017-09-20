import os
import sys

"""
Remove all file names with desired string in them. 
@args:
1. Path for prefix settings.
2. desired string to remove
"""

BAD_STR = "-"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Please add the path for this program")
    elif len(sys.argv) > 2:
        BAD_STR = sys.argv[2]

    path = sys.argv[1]
    for s in os.listdir(path):
        if BAD_STR in s:
            os.remove(path + os.sep + s)
