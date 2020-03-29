# for j, m in enumerate(dir()):
#     print(f"\n{j+1} module name: {m}\n")
#     for i, v in enumerate(dir(m)):
#         print(i + 1, v)

import sys
import builtins
import os
from random import random

rand = random()*100
print(rand)

# for i, v in enumerate(dir(os)):
#     print(i+1, v)

# for i, v in enumerate(dir(builtins)):
#     print(i+1, v)

# for i, v in enumerate(dir(sys)):
#     print(i+1, v)

