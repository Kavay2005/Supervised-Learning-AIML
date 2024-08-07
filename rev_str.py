def rev_string(s):
    n=len(s)
    for ele in range(n-1,-1,-1):
        print(s[ele],end='\t')
string=input("Enter a string:")
print("Original string: ",string)
rev_string(string)
        
