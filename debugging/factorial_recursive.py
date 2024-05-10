#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Function Description:
    ---------------------
    This function calculates the factorial of a non-negative integer using recursion.
    The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n.
    For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
    
    Parameters:
    -----------
    n : int
        The non-negative integer for which the factorial is to be calculated.
        
    Returns:
    --------
    int
        The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))  # Calculate factorial of the input integer provided as command-line argument
print(f)  # Print the result
