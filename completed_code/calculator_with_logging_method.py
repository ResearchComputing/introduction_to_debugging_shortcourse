from logger import * 

def calculate(operation, valueA, valueB):
  log_msg("LOG", "calculate(operation=" + str(operation) + ",valueA=" + str(valueA) + ",valueB=" + str(valueB) + ")")

  result = 0 

  if operation == "multiply":
    log_msg("DEBUG", "Selected multiply operation")
    result = valueA * valueB
    
  elif operation == "divide": 
    log_msg("DEBUG", "Selected divide operation")
    result = valueA / valueB
      
  elif operation == "add":
    log_msg("DEBUG","Selected add operation")
    result = valueA + valueB   
    
  elif operation == "subtract":
    log_msg("DEBUG","Selected subtract operation") 
    result = valueB - valueA  
    
  log_msg("LOG","Result of operation:", result)
  return result

print(calculate("multiply", 3, 2))