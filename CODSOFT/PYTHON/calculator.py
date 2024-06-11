def calculate(A, B,C):
 
  if C == "+":
    return A + B
  elif C == "-":
    return A - B
  elif C == "*":
    return A * B
  elif C == "/":
    if B == 0:
      print("Error: Division by zero")
      return None
    else:
      return A/ B
  else:
    print("Invalid operator")
    return None

while True:

  try:
    A = float(input("Enter the first number: "))
    B = float(input("Enter the second number: "))
    C = input("Choose operation (+, -, *, /): ")
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    continue


  result = calculate(A, B,C)

 
  if result is not None:
    print(f"{A} {C} {B} = {result}")

 
  choice = input("Do you want to continue? (y/n): ")
  if choice.lower() != "y":
    break

print("Calculator closed.")
