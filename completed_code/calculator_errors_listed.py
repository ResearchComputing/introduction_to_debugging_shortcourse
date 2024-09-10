def calculate(operation, valueA, valueB):
  result = 0 

  if operation == "multiply":
    result = valueA * valueB
    
  elif operation == "divide"   #Error 1 - Syntax Error, missing colon ':'
    result = valueA / valueB   #Error 3 - Runtime Error, doesn't prevent divide-by-zero
      
  elif operation == "add":
    result = valueA + valueA   #Error 2 - Typo error, adds valueA to itself (doubles) instead of expected behavior A + B
    
  elif operation == "subtract": 
    result = valueA - valueB   
  return result

print(calculate("multiply", 3, 2))   #Test 1
print(calculate("divide", 4, 0))     #Test 2
print(calculate("add", 7, 11))       #Test 3