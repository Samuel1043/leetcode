def addStrings(num1: str, num2: str) -> str:
    N = len(num1)
    M = len(num2)
    digits = max(N, M)

    i = 1
    remain = 0
    ans = ''
    while i < digits+1 or remain:
        cur = remain
        if i < N+1:
            cur += ord(num1[-i])-48
        if i < M+1:
            cur += ord(num2[-i])-48

        ans = str(cur % 10)+ans
        if cur >= 10:
            remain = 1
        else:
            remain = 0
        i += 1

    return str(ans)
