# In-Built Functions
int()
str()
bool()


# Module Function
import math

print(dir(math))

# Importing Specific Function
from math import sqrt

print(sqrt(16))

# Importing All Function
from math import *

# User-Defined Function

# def function_name(parameters):
#   // do something


def print_sum(first, second):
    print(first + second)


print_sum(5, 2)
