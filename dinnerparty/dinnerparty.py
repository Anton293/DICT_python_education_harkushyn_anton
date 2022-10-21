import random

list_members = {}
list_members_arr = []


def distribution_of_funds():
    print("Enter the number of friends joining (including you):")
    input_number_person: int = int(input("> "))
    if input_number_person < 1:
        print("No one is joining for the party")
        return
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(input_number_person):
        input_member = input("> ")
        list_members.update({f"{input_member}": 0})
    print("Enter the total amount.")
    input_amount = int(input("> "))
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_person = input("> ")
    choice_lucky_person = random.choice([key for key in list_members.keys()])
    if lucky_person.lower() == 'yes':
        input_number_person -= 1
        print(f"{choice_lucky_person} is the lucky one!")
    else:
        print("No one is going to be lucky")
    amount_person = round((input_amount / input_number_person), 2)
    for key in list_members.keys():
        if key == choice_lucky_person and lucky_person.lower() == 'yes':
            list_members[key] = 'free'
        else:
            list_members[key] = amount_person
    print(list_members)


distribution_of_funds()
