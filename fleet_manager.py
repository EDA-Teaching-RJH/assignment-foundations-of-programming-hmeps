print("---STAR TREK CHARACTER LIST---")
n = ["Kirk", "Riker", "Picard", "Data", "Worf"]
r = ["Captain", "Commander", "Captain", "Lt. Commander", "Lieutenant" ]
d = ["Command", "Command", "Command", "Operations", "Security"]
i = ["0010", "1001", "0111", "1111", "1011"]
def main():
    init_database()
    display_menu()

def init_database():
    for b in range(len(n)):
        print(n[b] + " - " + r[b] + " - " + d[b] + " - " + i[b])

def display_menu():
    name = str(input("What is your full name? "))
    fav_character = str(input("Who is your favourite character from the list provided above? "))
    print(f"Student logged in is: {name} \nYour favourite character is {fav_character}!")





main()