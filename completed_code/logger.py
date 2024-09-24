DEBUG = False 

def log_msg(type, msg, file_name="log.txt"):
  with open(file_name, "a") as log_file:
    match type: 
      case "LOG":
        log_file.write(msg + "\n")

      case "DEBUG":
        if DEBUG:
          print("DEBUG: " + msg + "\n")

def debugOff():
  global DEBUG
  DEBUG = False

def debugOn():
  global DEBUG
  DEBUG = True