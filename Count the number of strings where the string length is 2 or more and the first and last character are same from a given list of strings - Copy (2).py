def match_words(list1):
    count=0
    for word in list1:
        if len(word)>1 and word[0]==word[-1]:
            count+=1
    return count
list1=list(map(str,input().split()))
print(match_words(list1))
