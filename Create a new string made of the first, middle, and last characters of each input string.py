def append_string(s1,s2):
    s3=s1[0]+s2[0]
    m1=int(len(s1)/2)
    m2=int(len(s2)/2)
    s3=s3+s1[m1]+s2[m2]
    s3=s3+s1[-1]+s2[-1]
    print(s3)








s1=input()
s2=input()
append_string(s1,s2)
