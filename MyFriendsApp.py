
from Birthday import Birthday
from Friend import Friend



def List_Friends():
    friends = []
    with open("comp-170-su25-project/friends_database.csv", 'r') as file:
        for line in file:
            csv_info_counter = line.strip().split(',')
            if len(csv_info_counter) == 5:
                first, last, mailing, month, day = [x.strip() for x in csv_info_counter]
                person = Friend(first, last, mailing)
                person.birthday = Birthday(int(month), int(day))
                friends.append(person)
    return friends


def start_menu():
    print("1 - Create new friend record")
    print("2 - Search for a freind")
    print("3 - Run reports")
    print("4 - Exit")
    return input("Enter an option above: ")


def Run_Report_menu(friends):
    print("3.1 - List of friends alphabetically")
    print("3.2 - List of friends by upcoming birthdays")
    print("3.3 - Mailing labels for friends")
    print("3.9 - Return to the previous menu")
    user_input = input("Select an option above: ")
    print()
    
    if user_input == "3.1":
        friend_alphabetically = [(f.full_name(), f) for f in friends]
        friend_alphabetically.sort()
        for name, f in friend_alphabetically:
            print(name)
            print()
    elif user_input == "3.2":
        upcoming_birthday_list = [(f.birthday.days_until(),f) for f in friends]
        upcoming_birthday_list.sort()
        for days, f in upcoming_birthday_list:
            print(f"{f.full_name()} - Birthday is in {days} days")
            print()

    elif user_input == "3.3":
        for f in friends:
            print(f"{f.full_name()} \n {f.mailing_address}")
            print()

    elif user_input == "3.9":
        start_menu()

       
    


def create_friend():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    Mailing_address = input("Mailing Address: ")
    month = int(input("Birth month: "))
    day = int(input("Birth date: "))
    Birthday(month,day)
    return Friend(first_name, last_name, Mailing_address) and print("You must exit the application to save freind details")




def main():
    friends = List_Friends()

    while True:
        choice = start_menu()

        if choice == "1":
            friend = create_friend()
            friends.append(friend)

        elif choice == "3":
            Run_Report_menu(friends)




if __name__ == "__main__":
    main()




