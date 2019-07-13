Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> numbers = []
def numeric_range(numbers):
    if not numbers:
       print(0)
    else:
      for number in numbers:
        num1 = max(numbers)
        num2 = min(numbers)
        number = num1 - num2
      print(number)
  
numeric_range([2,5,7,8])
numeric_range([])
SyntaxError: multiple statements found while compiling a single statement
>>> numbers = []
    def numeric_range(numbers):
    if not numbers:
       print(0)
    else:
      for number in numbers:
        num1 = max(numbers)
        num2 = min(numbers)
        number = num1 - num2
      print(number)
  
   numeric_range([2,5,7,8])
   numeric_range([])
   
SyntaxError: multiple statements found while compiling a single statement
>>> numbers = []
def numeric_range(numbers):
    if not numbers:
       print(0)
    else:
      for number in numbers:
        num1 = max(numbers)
        num2 = min(numbers)
        number = num1 - num2
      print(number)
  
numeric_range([2,5,7,8])
numeric_range([])
