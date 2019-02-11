def check(user):
    import csv
    # print("1")
    f = 'details.txt'
    # f = str(findFile(userName))
    # print(f)
    # h = "'"
    # j = h + f + h
    # print(j)
    with open(f, mode='r') as data:
        # print("2")
        csv_read = csv.DictReader(data)
        linec = 1
        res = 0
        for row in csv_read:
            # print("3")
            # print(f'{row["userName"]}')
            if(f'{row["userName"]}'==userName):
                # print("user access granted")
                # usern = f'{row["userName"]}'
                res = 1 
                linec+=1
            else:
                linec+=1
                # print("4")
    return res

def findFile(userName):
    year = userName[0:2]
    dept = userName[2:4].upper()
    roll = userName[4:6]
    print("year: ",year," dept: ",dept," roll: ",roll)
    new = "".join((year,dept))
    t = '.txt'
    print(new)
    file = new + t
    print(file)
    return file


while(1):       
    userName = str(input("enter the username"))
    test = check(userName)
    if(test == 1):
        # print("5")
        print("access granted")
    else:
        # print("6")
        print("try again")

