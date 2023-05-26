def append_middle(s1,s2):
    print("Original Strings are",s1,s2)

    mi=int(len(s1)/2)
    
    x=s1[:mi:]
    x=x+s2
    x=x+s1[mi:]
    print(x)
s1=input()
s2=input()
append_middle(s1,s2)

