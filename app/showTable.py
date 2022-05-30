def show(data):
    print("{:<30} | {:}".format(data[0][0], data[0][1]))
    data = data[1:]
    print("__________________________________________________________________________________")
    for row in data:
        name, repo = row[0], row[1]
        print("{:<30} | {:}".format(name, repo))