import os
import sys

"""
@args:
1. Path for prefix settings.
2. Desired prefix. (optional).
"""

PREFIX = "b"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Please add the path for this program")
    elif len(sys.argv) > 2:
        PREFIX = sys.argv[2]

    path = sys.argv[1]
    for s in os.listdir(path):
        os.rename(path + os.sep + s, path + os.sep + PREFIX + s)
