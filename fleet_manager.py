n = ["Kirk", "Riker", "Picard", "Data", "Worf"]
r = ["Captain", "Commander", "Captain", "Lt. Commander", "Lieutenant" ]
d = ["Command", "Command", "Command", "Operations", "Security"]
i = ["0010", "1001", "0111", "1111", "1011"]
def main():
    init_database()

def init_database():
    for b in range(len(n)):
        print(n[b] + " - " + r[b] + " - " + d[b] + " - " + i[b])




main()