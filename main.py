from instagram_data import data
from random import randint
from os import system

# Clears console before next level


def clear(): return system('cls')

# main game


def higher_or_lower_game(first_person: dict, points: int):
    '''
    Takes FIRST PERSON from a list and a POINTS variable.
    Returns SECOND PERSON from last question and modified points.
    '''

    # showing needed data
    print("Which one have more followers?")

    print(
        f"{first_person['name']} from {first_person['country']} and is {first_person['description']}")

    print(
        f"{first_person['name']} has {first_person['follower_count']} milion follower count")

    print('Or')
    second_person = data[randint(0, 49)]
    print(
        f"{second_person['name']} from {second_person['country']} and is {second_person['description']}")

    # getting answear from player
    answer = input("Your guess (A or B): ").lower()

    # checking answear of player
    if answer == 'a' and first_person['follower_count'] > second_person['follower_count']:
        print('Correct!')
        points += 1
        input('enter any key to continue ')
        clear()
        return second_person, points
    elif answer == 'b' and first_person['follower_count'] < second_person['follower_count']:
        print('Correct!')
        points += 1
        input('enter any key to continue ')
        clear()
        return second_person, points
    elif first_person['follower_count'] == second_person['follower_count']:
        print('Draw!')
        input('enter any key to continue ')
        clear()
        return second_person, points
    else:
        print("Not correct :/")
        print(
            f"{second_person['name']} has {second_person['follower_count']} milion follower count")
        print(f"You scored {points} points")
        input('enter any key to continue ')
        clear()
        # asking for a reset
        restart_game = input("Do you want to restart? y/n ").lower()
        if restart_game == 'y':
            return higher_or_lower_game(data[randint(0, 49)], points=0)
        else:
            return None


print("Welcome to higher or lower game")
points = 0
first_person = data[randint(0, 49)]
while True:
    try:
        first_person, points = higher_or_lower_game(first_person, points)
    except TypeError:
        break
