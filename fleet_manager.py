print("---STAR TREK CHARACTER LIST---")
n = ["Kirk", "Riker", "Picard", "Data", "Worf"]
r = ["Captain", "Commander", "Captain", "Lt. Commander", "Lieutenant" ]
d = ["Command", "Command", "Command", "Operations", "Security"]
i = ["1010", "1001", "0001", "1111", "1011"]
def main():
    init_database()
    display_menu()
    add_member()
    remove_member()

def init_database():
    for b in range(len(n)):
        print(n[b] + " - " + r[b] + " - " + d[b] + " - " + i[b])

def display_menu():
    name = str(input("What is your full name? "))
    fav_character = str(input("Who is your favourite character from the list provided above? "))
    print(f"Student logged in is: {name} \nYour favourite character is {fav_character}!")

def add_member():
    add_name = str(input("Enter full name of new member: "))
    add_rank = str(input("Enter the rank of the new member: "))
    while add_rank not in r:
        print("Not a valid TNG rank, Try Again!")
        add_rank = str(input("Enter the rank of the new member: "))
    add_division = str(input("Enter the division of the new member: "))
    while add_division not in d:
        print("Not a valid division, Try Again!")
        add_division = str(input("Enter the division of the new member: "))
    add_id =  str(input("Enter the ID of the new member: "))
    while add_id in i:
        print("Not a unique ID number entered, Try Again!")
        add_id = str(input("Enter the ID of the new member: "))

    n.append(add_name)
    r.append(add_rank)
    d.append(add_division)
    i.append(add_id)

def remove_member():
    find_id = str(input("Enter the value of the ID you want to remove: "))
    while True:
        if find_id in i:
            idx = i.index(find_id)

            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            i.pop(idx)

            print("Member successfully removed!")
            break
        else:
            print("ID not found in database, Try Again!")
            find_id = str(input("Enter the name of the ID you want to remove: "))




main()