import random
from re import T

#makes list of birthday (1-365, for each day in a year)
def make_babies(number_of_babies):
    list_of_birthdays = [ random.randint(1,365) for number in range(number_of_babies)]
    # for number in range(number_of_babies):
    #     birthday = random.randint(1,365)
    #     list_of_birthdays.append(birthday)
    #list_of_birthdays.sort()
    #print(list_of_birthdays)
    return list_of_birthdays

def check_list_for_dup(list_to_check):
    if len(list_to_check) == len( set(list_to_check)):
        return False #no match
    else:
        return True #is a match
    


if __name__ == '__main__':
    bool = check_list_for_dup( make_babies(23)) 
    if bool == True:
        print('match')
    else:
        print('nope')