def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(list(path))
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result


print(combination_sum([2,3,6,7], 7))
