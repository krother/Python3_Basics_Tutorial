
import math

def fibonacci(k):
    """Slow recursive implementation"""
    if k == 0: 
        return 0
    if k == 1: 
        return 1
    return fibonacci(k-1) + fibonacci(k-2)


def fibonacci(k):
    """Non-recursive implementation."""
    if k == 0: 
        return k
    a = 0
    b = 1
    for i in range(k):
        a, b = b, a+b
    return b
    
    
def fibonacci(k):
    """implementation without loop"""
    phi = 0.5 * (1.0 + math.sqrt(5.0))
    return int( math.pow(phi, k)/math.sqrt(5.0) + 0.5 )


if __name__ == '__main__':
    print(fibonacci(30))

