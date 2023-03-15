def main(s,n,k):
    """
    The s string variable is given. return from index n to index k.
    Args:
        s(str): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        str: answer
    """
    a=0
    if str(s)==s:
        a+=1
        if int(n)==n:
            a+=1
            if int(k)==k: 
                a+=1
                return s[n:-k:]

print(main("codeschool",2,5))