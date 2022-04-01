"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    valid = is_valid(score)
    if valid:
        print(score_result(score))
    else:
        print('Invalid Score')


def is_valid(score):
    if score < 0 or score > 100:
        return False
    return True


def score_result(score):
    result = None
    if score < 50:
        result = "Bad"
    elif 50 <= score <= 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result

main()