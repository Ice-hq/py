while True:
  KORN = input("Voltage: ")
  R = input("Resistance: ")
  try:
    KORN = int(KORN)
    R = int(R)
    I = KORN/R
    print(I)
    break
  except(ValueError, ZeroDivisionError):
    print("Error")
    pass
  
