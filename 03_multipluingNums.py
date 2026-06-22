import math

input_num = int(input("Enter your number: "))

while input_num > 9:
    numbers = [int(numbers) for numbers in str(input_num)]
    input_num = math.prod(numbers)

print(input_num)
 