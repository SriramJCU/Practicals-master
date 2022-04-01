
# 1
file = open("name.txt", "w")
name = input("Please enter your name: ")
file.write(name)
file.close()

# 2
file = open("name.txt", "r")
name = file.read()
print(f"Your name is {name}.")
file.close()

# 3
file = open("numbers.txt", "r")
number_1 = int(file.readline())
number_2 = int(file.readline())
result = number_1 + number_2
print("The result is: ", result)
file.close()

# 4
file = open("numbers.txt", "r")
result = 0
for line in file:
    result += int(line)

print(result)
file.close()