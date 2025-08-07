
from Birthday import Birthday
from Friend import Person



def List_Friends():
    friends = []
    with open("comp-170-su25-project/friends_database.csv", 'r') as file:
        for line in file:
            csv_info_counter = line.strip().split(',')
            if len(csv_info_counter) == 5:
                first, last, mailing, month, day = [x.strip() for x in csv_info_counter]
                person = Person(first, last, mailing)
                person.birthday = Birthday(int(month), int(day))
                friends.append(person)
    return friends


def start_menu():
    print("1 - Create new friend record")
    print("2 - Search for a freind")
    print("3 - Run reports")
    print("4 - Exit")
    return input("Enter an option above: ")



def Run_Report_menu():
    print("3.1 - List of friends alphabetically")
    print("3.2 - List of friends by upcoming birthdays")
    print("3.3 - Mailing labels for friends")
    print("3.9 - Return to the previous menu")
    user_input = input("Select an option above: ")




def main():
    friends = List_Friends()

    while True:
        choice = start_menu()




if __name__ == "__main__":
    main()




