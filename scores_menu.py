
"""
module-level docstring
CP1404 - Practical no 02
Mason McKenzie
"""

score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("not valid")
elif score >= 90:
    print("excellent")
elif score >= 50:
    print("passable")
else:
    print("bad")
#docstring for function
def main():

    for i in range(score):
        print('*', end=' ')
    print()


main()