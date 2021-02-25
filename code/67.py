def addBinary(a: str, b: str) -> str:
    total=int(a)+int(b)
    ans=''
    while total>0:
        cur=total%10
        ans=str(cur%2)+ans

        total//=10
        
        if cur>=2:
            total+=1
    return '0' if ans=='' else ans