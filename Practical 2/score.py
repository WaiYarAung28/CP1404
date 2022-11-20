"""
CP1404/CP5632 - Practical
determine score status
"""
score = float(input("Enter score: "))
def main():
    get_score(score)
def get_score(score):
    if score > 100 :
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score >= 0:
        print ("Bad")
    else:
        print("Invalid score")
main()