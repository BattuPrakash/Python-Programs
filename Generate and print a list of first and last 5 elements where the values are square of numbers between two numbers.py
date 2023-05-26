def printvalues():
    l=list()
    for i in range(start,end+1):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
start=int(input())
end=int(input())
printvalues()
