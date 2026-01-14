"""
Example Python module for demonstrating AI-powered documentation updates.

This is a sample file to trigger Demo 4 when modified.
"""

def hello_world():
    """
    Print a hello world message.
    
    Returns:
        str: A greeting message
    """
    return "Hello, World!"


def add_numbers(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Sum of a and b
    """
    return a + b


class Calculator:
    """A simple calculator class."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.result = 0
    
    def multiply(self, x, y):
        """
        Multiply two numbers.
        
        Args:
            x (float): First number
            y (float): Second number
        
        Returns:
            float: Product of x and y
        """
        self.result = x * y
        return self.result
    
    def get_result(self):
        """
        Get the last calculation result.
        
        Returns:
            float: Last calculated result
        """
        return self.result


if __name__ == "__main__":
    print(hello_world())
    print(f"2 + 3 = {add_numbers(2, 3)}")
    
    calc = Calculator()
    print(f"4 * 5 = {calc.multiply(4, 5)}")
