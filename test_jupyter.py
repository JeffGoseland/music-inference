#!/usr/bin/env python3
"""
Simple test script to verify Jupyter is working
Copy and paste these code blocks into your Jupyter notebook cells
"""

# Test 1: Basic Python functionality
print("🎉 Jupyter is running!")
print(f"Python version: {__import__('sys').version}")
print(f"Current working directory: {__import__('os').getcwd()}")

# Test 2: Simple calculations
import math

x = 42
y = 3.14
result = x * y

print(f"Math test: {x} × {y} = {result}")
print(f"Square root of {x}: {math.sqrt(x):.2f}")
print(f"Pi: {math.pi}")

# Test 3: List and dictionary operations
test_list = [1, 2, 3, 4, 5]
test_dict = {"name": "Jupyter", "status": "Running", "version": "4.0"}

print("List operations:")
print(f"Original list: {test_list}")
print(f"Sum: {sum(test_list)}")
print(f"Length: {len(test_list)}")
print(f"Doubled: {[x*2 for x in test_list]}")

print("\nDictionary operations:")
for key, value in test_dict.items():
    print(f"{key}: {value}")

# Test 4: Date and time
from datetime import datetime

current_time = datetime.now()
print(f"🕐 Current time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"📅 Today's date: {current_time.strftime('%A, %B %d, %Y')}")

# Test 5: File system access
import os

print("📁 Current directory contents:")
for item in os.listdir('.'):
    if os.path.isdir(item):
        print(f"📂 {item}/")
    else:
        print(f"📄 {item}")

# Test 6: Random number generation
import random

print("🎲 Random number tests:")
print(f"Random integer (1-100): {random.randint(1, 100)}")
print(f"Random float (0-1): {random.random():.3f}")
print(f"Random choice from list: {random.choice(['apple', 'banana', 'cherry'])}")

# Generate a list of random numbers
random_numbers = [random.randint(1, 50) for _ in range(5)]
print(f"Random list: {random_numbers}")

# Test 7: Success message
print("✅ All tests completed successfully!")
print("🎵 Your Jupyter environment is ready for music data analysis!")
print("\nNext steps:")
print("1. Import your music data")
print("2. Start analyzing with pandas and numpy")
print("3. Create visualizations with matplotlib/seaborn")
print("4. Build your music analysis pipeline!")
