import random

#makes list of birthdays (1-365, for each day in a year)
def make_babies(number_of_babies) -> list :
    list_of_birthdays = [ random.randint(1,365) for number in range(number_of_babies)]
    # for number in range(number_of_babies):
    #     birthday = random.randint(1,365)
    #     list_of_birthdays.append(birthday)
    #list_of_birthdays.sort()
    #print(list_of_birthdays)
    return list_of_birthdays

def check_list_for_dup(list_to_check) -> bool :
    if len(list_to_check) == len( set(list_to_check)):
        return False #no match
    else:
        return True #is a match

def welcome_message():
    print(f"Hello! This program will make babies and tell you if they share any birthdays.")

if __name__ == '__main__':
    welcome_message()

    ask_to_make = input('Would you like to see if some babies have the same Birthdays? (y/n):')

    if ask_to_make == 'y':

        number_to_make = int(input('How many would you like to make?(23 for 50%, 50 for 97%):'))
        bool = check_list_for_dup( make_babies(number_to_make)) 

        if bool == True:
            print('There is a match!')
        else:
            print('No match in this bunch.')
            
    elif ask_to_make == 'n':
        pass
    else:
        print('Invalid Input')
