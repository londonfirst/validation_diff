#Just some random Py code for playing with Git

data = {"100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64,
        "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25,
        "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15,
        "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11,
        "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40}




def logic(inp_age: int):
    # adding +5 to money if age is less tr age and +20 if not
    money_total = 0
    for i in data.values():
        if i < inp_age:
            money_total = money_total + 5
        else:
            money_total = money_total + 20
    return money_total


def main():
    age = int(input())
    default_age = 18 # The default age for comparing is 18 years
    default_price = logic(default_age)
    changed_price = logic(age)
    percent_change = int(((changed_price - default_price)/default_price) * 100)
    return print(f'{percent_change}')


if __name__ == "__main__":
    main()
else:
    print("it's not the main")


#ver 4  will be with regex checking
