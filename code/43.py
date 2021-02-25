def multiply(self, num1: str, num2: str) -> str:
    """
    Note: You must not use any built-in BigInteger 
    library or convert the inputs to integer directly.
    """
    ascii_0=ord('0')
    num1=num1[::-1]
    num2=num2[::-1]
    total=0
    for idx1,char1 in enumerate(num1):
        digit1=ord(char1)-ascii_0            
        
        for idx2,char2 in enumerate(num2):
            digit2=ord(char2)-ascii_0
            total+=digit1*digit2*10**(idx1+idx2)
    
    return str(total)
