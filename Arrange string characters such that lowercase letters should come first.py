def strings_lower_upper(s1):
    lower=[]
    upper=[]
    for i in s:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)

    sorted_string=''.join(lower+upper)

    print(sorted_string)





s=input()
strings_lower_upper(s)
