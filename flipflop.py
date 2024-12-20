def palindrome(r):
    s=0
    e=len(r)-1
    while (s>e):
        if(r[s]!=r[e]):
            return False
        else:
            s=s+1
            e=e-1
    return True
if(palindrome(("o",2,"m","a","d","a","m",2,"o"))):
    print("The Tuple is a palindrome")
else:
    print("The Tuple is not a palindrome")        