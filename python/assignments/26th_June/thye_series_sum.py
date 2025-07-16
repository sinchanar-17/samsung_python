#find the sum of series n - n^2/3 - n^4/5 -n^8/7 ....m terms [1<=n<=4 and 2=<m<=10]
def series_sum():
    n = int(input("enter n(term) value: "))
    m = int(input("enter number of terms: "))
    if not (1 <= n <= 4 and 2 <= m <= 10):
        return 'invalid input'
    sum = 0
    for i in range(m):
        numerator = n ** 2 ** i
        denominator = 2 * i + 1
        sign = -(1) ** i
        term = (numerator / denominator) * sign 
        sum += term 
    print('sum of series: ', sum)
series_sum()
