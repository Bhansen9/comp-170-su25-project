
from Birthday import Birthday
from Friend import Friend



def List_Friends():
    #create list to store data from friends_database.csv
    friends = []
    #open file using the read mode
    with open("comp-170-su25-project/friends_database.csv", 'r') as file:
        for line in file:
            #split up line do the data by getting rid of spaces and by removing the ',' inbetween data
            csv_info_counter = line.strip().split(',')
            #makes sure all data that is load are full profiles, meaning that they have every (first name, last name, mailing address, birth month, birth date)
            if len(csv_info_counter) == 5:
                #strips the values of extra spaces and ','
                first, last, mailing, month, day = [x.strip() for x in csv_info_counter]
                #sets the data to the paraperteirs requiered for each invidual person in the data set
                friend = Friend(first, last, mailing)
                friend.birthday = Birthday(int(month), int(day))
                #addes the friends to the list
                friends.append(friend)
    return friends


def start_menu():
    #prints the options for the main menu and takes an input that changes where the user goes
    #added space
    print()
    print("1 - Create new friend record")
    print("2 - Search for a friend")
    print("3 - Run reports")
    print("4 - Exit")
    return input("Enter an option above: ")


def Run_Report_menu(friends,):
    #prints all the reports that the user can use, relaying on the user_input option to lead the user what tests they run
    print("3.1 - List of friends alphabetically")
    print("3.2 - List of friends by upcoming birthdays")
    print("3.3 - Mailing labels for friends")
    print("3.9 - Return to the previous menu")
    user_input = input("Select an option above: ")
    #added space to make it look nice
    print()
    
    if user_input == "3.1":
        #sets varable to f.full_name() which acesses friend.py and the function full name. This adds all friends in the data set
        #making it a sting which can be sort() by alphabeticaly, then prints out each name alphabetically
        friend_alphabetically = [(f.full_name(), f) for f in friends]
        friend_alphabetically.sort()
        for name, f in friend_alphabetically:
            print(name)
            print()
    elif user_input == "3.2":
        #sets varable to f.birthday.days_until which access friends.py then birthday.py to the function days_until()
        #This function creates the days until each persons birthday from the data set
        upcoming_birthday_list = [(f.birthday.days_until(),f) for f in friends]
        #Then this varable is sorted with .sort() 
        upcoming_birthday_list.sort()
        for days, f in upcoming_birthday_list:
            #then prints out each persons full name and the days until there next birthday
            print(f"{f.full_name()} - Birthday is in {days} days")
            print()

    elif user_input == "3.3":
        for f in friends:
            #prints out each persons full name and the mailining address
            print(f"{f.full_name()} \n {f.mailing_address()}")
            print()

    elif user_input == "3.9":
        #returns user to start menu
        start_menu()

       
    

def create_friend():
    #collects all data needed, first_name, last_name,mailing_address, month,day
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    mailing_address = input("Mailing Address: ")
    month = int(input("Birth month: "))
    day = int(input("Birth date: "))
    #then sets each value collected to the right class paramerters
    person = Friend(first_name, last_name, mailing_address)
    person.birthday = Birthday(month, day)
    #then lets the user know that to save this new data they must exit the application
    print("You must exit the application to save friend details")
    return person

def search_friend(friends, name):
    #this search allows if you search it in lower case it will stil return the name your looking for
    return [f for f in friends if name.lower() in f.full_name().lower()]

def save_friends(friends):
    #opens the database in write mode so the create_friend() data saves in it
    with open("comp-170-su25-project/friends_database.csv", mode='w', encoding='utf-8') as file:
        
        for friend in friends:
       #strips uneed spaces form all the data that was write in but fills in blanks if data was not entered
            first = friend.first_name.strip()
            last = friend.last_name.strip()
            mailing = friend.mailing.strip() if friend.mailing else ""
          
            if friend.birthday:
                #sets month and day to str to store it easier but when return and load_friend() run it sets them to int
                month = str(friend.birthday.get_month())
                day = str(friend.birthday.get_day())
            else:
                month = ""
                day = ""

#sets rows in the database to be orginized in order
            row = [first, last, mailing, month, day]
            #includes a ',' inbetween each parameter 
            file.write(",".join(row) + "\n")

def main():
    friends = List_Friends()

    while True:
        choice = start_menu()

        if choice == "1":
            #if choice is run it runs the create_friend() funtion
            friend = create_friend()
            # also make sure it is added to the list just incase it is not in the create_friend() program
            friends.append(friend)

        elif choice == "2":
            name = input("Enter name to search: ")
            #runs search_friend function using the name inputed
            results = search_friend(friends, name)
            if results:
                i = 1  
                for f in results:
                    #prints the option and the full name
                    print(f"{i}. {f.full_name()}")
                    #then add more to the counter incase it is looped again with more options
                    i += 1
                    #choice is seleced with the number that shows up with the name in question
                    idx = int(input("Select a friend to edit/delete (0 to cancel): ")) - 1
                    #if user pick a person 
                if 0 <= idx < len(results):
                    #options are to edit or delete
                    sub_choice = input("Edit (e) or Delete (d)? ")
                    if sub_choice == "e":
                        #if 'e' then the data entered will be set to the create_friend()
                        updated = create_friend()
                        friends[friends.index(results[idx])] = updated
                    elif sub_choice == "d":
                        #if delete it will remove the data from the database file
                        confirm = input("Are you sure? Type 'DELETE' to confirm: ")
                        if confirm == "DELETE":
                            friends.remove(results[idx])
            else:
                print("No match found.")

        elif choice == "3":
            #opens report menu
            Run_Report_menu(friends)
        
        elif choice == "4":
            #run the save friend function
            save_friends(friends)
            print("See you later")
            exit()
        else:
            print(f"The option selected does not exist, pick another")
            start_menu()




if __name__ == "__main__":
    main()




