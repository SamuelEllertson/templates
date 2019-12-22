#!/usr/bin/env python

def main():
    pass

def foo(a,b):
    """The function to foo two numbers
  
    Parameters: 
        a (number): The first number to be foo'ed. 
        b (number): The second number to be foo'ed. 
      
    Returns: 
        number: the foo'ed result of a and b.

    Examples:
        >>> foo(5,10)
        50

        >>> foo(0,4)
        Traceback (most recent call last):
        ...
        ValueError
    """


if __name__ == '__main__':
    should_test = True
    
    if should_test:
        import doctest
        print(doctest.testmod())
    
    main()