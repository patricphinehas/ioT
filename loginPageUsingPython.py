def check(user):
    import csv
    # print("1")
    with open('details.txt', mode='r') as data:
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
while(1):       
    userName = str(input("enter the username"))
    test = check(userName)
    if(test == 1):
        # print("5")
        print("access granted")
    else:
        # print("6")
        print("try again")

