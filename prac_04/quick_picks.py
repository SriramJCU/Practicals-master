import random


NUMBER_OF_PICKS = int(input("How many picks? "))
SIZE_OF_EACH_PICK = 6

for i in range(NUMBER_OF_PICKS):
    pick = []
    for j in range(SIZE_OF_EACH_PICK):
        while True:
            number = random.randint(1, 45)
            if number not in pick:
                pick.append(number)
                break


    pick.sort()
    for num in pick:
        print("{:3}".format(num), end=" ")
    print()




