import random
import string

def character_number(department_choice):
    number = random.randint(0, 9)

    if department_choice == "marketing":
        letter = "M"
    elif department_choice == "accounting":
        letter = "A"
    elif department_choice == "finops":
        letter = "F"
    else:
        letter = random.choice(string.ascii_uppercase)

    return f"{letter}{number}"

def main():
    instance_count = int(input('How many instances do you need names for?\n'))
    department_choice = input('What department will these instances be used for?\n').lower()

    print(f'Generating {instance_count} names for department: {department_choice}')
    for i in range(instance_count):
        print(f"Instance {i + 1}: {character_number(department_choice)}")

main()