while True:
  U = input("Voltage: ")
  R = input("Resistance: ")
  try:
    U = int(U)
    R = int(R)
    I = U/R
    print(I)
    break
  except(ValueError, ZeroDivisionError):
    print("Error")
    pass
  
