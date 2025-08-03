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

repr
str
print

import math
math.floor
math.trunc

high number precisiion

0o20
oct('64')

int(3.14)

int('64',8)  # 64 in octal
int('64',2) # 64 in binary

import random
random.random()
random.randint(1,10)


l1=['lemon','masala','ginger','mint']
random.choice(l1)
random.shuffle(l1)

from decimal import Decimal
Decimal('0.1') +Decimal('0.1')+Decimal('0.1')=Decimal('0.3')

from fractions i port Fraction
myFra=Fraction(2,7)

setone={1,2,3,4}
setone & {1,3} ={1,3}
setone | {1,7} ={1,2,3,4,7}
setone -{1,2,3,4} =set()  # empty parenthesis ka type dict hota h

true==1
false==0

true is 1

true +4

#string
chai="       masala chai    "

chai.strip()
chai.replace()
chai ="lemon,ginger,masala,mint"
chai.split(',')
chai.count('chai')

order="I ordered {} cups of {} chai "
print(order.format(quantity,chai_type))


print("".join (chai_vareity)) # list -> string

chai="he said, \" chai is good\" "  # to include double quotes


chai =r"Masala\nChai"

print("masala" in chai)
