"""
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

def main():
    """Function docstring"""
    # statements...
    do_stuff()


def do_stuff():
    """Function docstring"""
    # statements...


main()
