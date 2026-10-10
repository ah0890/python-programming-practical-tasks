# Task 2: NumPy Array Data Type Conversion
# This program creates a NumPy array of integers and converts it
# into an array of floating-point numbers.

import numpy as np

# Create a NumPy array from a list of integers
marks = np.array([78, 85, 92, 67, 88])

print("=" * 40)
print("   NUMPY ARRAY DATA TYPE CONVERSION")
print("=" * 40)

# Display the original integer array and its data type
print("\nOriginal Array :", marks)
print("Data Type      :", marks.dtype)

# Convert the array to float using astype()
# astype() returns a NEW array; the original array is not changed
float_marks = marks.astype(float)

# Display the converted float array and its data type
print("\nConverted Array:", float_marks)
print("Data Type      :", float_marks.dtype)
print("=" * 40)
