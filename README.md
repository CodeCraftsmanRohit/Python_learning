# Python_learning
it is a repo for learning python from scratch

'''

from importlib import reload

import sys
sys.platform()

import os
os.cwd()
'''

mutable vs immutable

[] ,() ,{}



In Python, tuples and lists are both used to store collections of items, but they have several key differences. Here's a clear comparison:

🔑 Key Differences Between Tuple and List
Feature	List	Tuple
Syntax	[1, 2, 3]	(1, 2, 3)
Mutable	✅ Yes — can be changed	❌ No — immutable
Performance	Slower (more flexible)	Faster (less overhead)
Use Case	When you need to modify data	When data should not change
Methods Available	Many (e.g., append, remove)	Few (count, index)
Hashable (can be dict keys)	❌ No	✅ Yes (if all elements are hashable)
Memory Usage	Typically more memory	Less memory than l


import copy
copy.copy
copy.deepcopy

m==n

m is n
