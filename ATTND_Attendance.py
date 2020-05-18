for _ in range(int(input())):
    fname= []
    lname = []
    for _ in range(int(input())):
        first_name,last_name = map(str,input().split())
        fname.append(first_name)
        lname.append(last_name)

    # create a dict--> dict(key,value) --> dict(name,count)
    dict_name = {}
    for item in fname:
        if item in dict_name:
            dict_name[item] += 1
        else:
            dict_name[item] = 1
            
    # if count = 1 then firstname else print full name   
    for i in range(len(fname)):
        for key,value in dict_name.items():
            if fname[i] == key:
                if value == 1:
                    print(fname[i])
                else:
                    print(fname[i]    ,'',lname[i])
