"""
CP1404- Practical
https://github.com/WaiYarAung28/CP1404
"""
password = (input("Enter passwords: "))
def main():
    get_password(password)
def get_password(password):
    if password != "1234":
        print("Wrong")
    else:
        print("Correct")
main()



