#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
module docstring - short summary
If the description is long, the first line should be a short summary that makes sense on its own,
separated from the rest by a newline
"""

__version__ = "1.0.0"
__author__ = "Author 1, Author 2, Author 3"             # only code writers
__email__ = "author@bogusproject.com"
__maintainer__ = "Maintainer 1"                         # should be the person who will fix bugs and make improvements
__copyright__ = "Copyright 2019, The Bogus Project"
__license__ = "GPL"
__status__ = "Production"                               # Prototype, Development or Production
__credits__ = ["name 1", "name 2"]                      # also include contributors that wrote no code

# --------------------------------------------------------------------------------

# Import built-in modules first
# followed by third-party modules
# followed by any changes to the path
# your own modules.


def main(args=None):
    pass



if '__main__' == __name__:
    import sys
    main(sys.argv)