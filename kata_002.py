import math

def is_square(n): 
    if n < 0:
        return False
    float_root = math.sqrt(n)
    int_root = int(float_root)
    return int_root == float_root
