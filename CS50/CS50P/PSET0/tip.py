def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d.replace("$", "")
    d 
    float("{:.1f}".format(d))
    return d


def percent_to_float(p):
    p.replace("%", "")
    float("{:.2f}".format(p))
    p  = p / 100
    return p


main()