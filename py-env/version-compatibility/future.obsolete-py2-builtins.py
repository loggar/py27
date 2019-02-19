"""
Another thing to keep in mind is that there are 12 Python 2 builtins which have been removed from Python 3.
Make sure that you don’t use them in Python 2 in order to make your code compatible with Python 3.
Here is a way to enforce that you abandon these 12 builtins in Python 2 as well:
"""

from future.builtins.disabled import *

apply()
# Output: NameError: obsolete Python 2 builtin apply is disabled
