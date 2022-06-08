from linear import LinearRegression

l = LinearRegression()
Input = [[1], [2], [3], [4], [5]]
Output = [[10], [20], [30], [40], [50]]
l.train(Input, Output)
enter = [[6]]
result = l.regression(enter)
print(f'{enter}: {result}')

# training to convert input in *10 and float - Ex. 6 = 60.0
