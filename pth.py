def calculate_bmi(weight, height):
  """Calculates the Body Mass Index (BMI) for a given weight and height.

  Args:
      weight (float): Weight in kilograms.
      height (float): Height in meters.

  Returns:
      float: The calculated BMI value.
  """
  if height <= 0:
    raise ValueError("Height cannot be zero or negative")
  bmi = weight / (height * height)
  return bmi

def interpret_bmi(bmi):
  """Interprets the calculated BMI value based on standard BMI categories.

  Args:
      bmi (float): The calculated BMI value.

  Returns:
      str: A string interpretation of the BMI category.
  """
  if bmi < 18.5:
    return "Underweight"
  elif bmi < 25:
    return "Normal weight"
  elif bmi < 30:
    return "Overweight"
  else:
    return "Obese"

# Example usage
weight = 70.0
height = 1.75

bmi = calculate_bmi(weight, height)
bmi_interpretation = interpret_bmi(bmi)

print(f"BMI for weight {weight} kg and height {height} m: {bmi:.2f}")
print(f"BMI Interpretation: {bmi_interpretation}")
