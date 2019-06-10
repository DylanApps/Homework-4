MyUniqueList = []
MyLeftOvers = []
while True:
    Var = input(">   ")
    if Var not in MyUniqueList:
        MyUniqueList.append(Var)
    else:
        MyLeftOvers.append(Var)
    print(MyUniqueList)
    print(MyLeftOvers)