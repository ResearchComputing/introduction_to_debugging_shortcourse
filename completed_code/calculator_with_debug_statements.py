def calculate(operation, valueA, valueB):
  if DEBUG:
    print("calculate(operation=",operation,",valueA=",valueA,",valueB=",valueB,")")

  result = 0 

  if operation == "multiply":
    if DEBUG:
      print("Selected multiply operation")
    result = valueA * valueB
    
  elif operation == "divide": 
    if DEBUG:
      print("Selected divide operation")
    result = valueA / valueB
      
  elif operation == "add":
    if DEBUG:
      print("Selected add operation")
    result = valueA + valueB   
    
  elif operation == "subtract":
    if DEBUG:
      print("Selected subtract operation") 
    result = valueB - valueA  
    
  if DEBUG:
      print("Result of operation:", result)
  return result

DEBUG = True

print(calculate("multiply", 3, 2))
