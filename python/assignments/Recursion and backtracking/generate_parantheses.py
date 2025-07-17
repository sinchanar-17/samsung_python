def generate_parentheses(n):
    result = []

    def backtrack(open_n, close_n, current=""):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_n < n:
            backtrack(open_n + 1, close_n, current + "(")
        if close_n < open_n:
            backtrack(open_n, close_n + 1, current + ")")

    backtrack(0, 0)
    return result


print(generate_parentheses(3))
