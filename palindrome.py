def is_palindrome(s):
    i= 0
    j=len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

s = input("Enter a string: ")
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
