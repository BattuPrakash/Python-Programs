#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
def mixed_string(s1,s2):
    s3=s1[0]+s2[-1]
    s3=s3+s1[1]+s2[-2]
s1=input()
s2=input()
mixed_string(s1,s2)
