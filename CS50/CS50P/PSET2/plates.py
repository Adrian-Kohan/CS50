def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha and not s[-1].isalpha
        return True






main()