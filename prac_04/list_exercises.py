numbers = []
total_numbers = 5
for i in range(total_numbers):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is: {numbers[-1]}")
print(f"The smallest number is: {min(numbers)}")
print(f"The largest number is: {max(numbers)}")
print(f"The average of the numbers is: {(min(numbers) + max(numbers) / 2)}")