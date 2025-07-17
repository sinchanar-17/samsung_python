def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i+1:]
        permute(left + right, answer + ch)


permute("ABC")
