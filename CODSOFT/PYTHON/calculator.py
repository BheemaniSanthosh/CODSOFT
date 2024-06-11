def calculate(A, B,C):
  """
  Performs basic arithmetic operations based on the provided operator.

  Args:
      A: The first number.
      B: The second number.
      C: The arithmetic operation (+, -, *, /).

  Returns:
      The result of the calculation.
  """
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
  # Get user input
  try:
    A = float(input("Enter the first number: "))
    B = float(input("Enter the second number: "))
    C = input("Choose operation (+, -, *, /): ")
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    continue

  # Perform calculation
  result = calculate(A, B,C)

  # Display result (if no errors)
  if result is not None:
    print(f"{A} {C} {B} = {result}")

  # Ask user to continue
  choice = input("Do you want to continue? (y/n): ")
  if choice.lower() != "y":
    break

print("Calculator closed.")