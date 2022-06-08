from linear import LinearRegression

l = LinearRegression()
Input = [[1], [2], [3], [4], [5]]
Output = [[10], [20], [30], [40], [50]]
l.train(Input, Output)
enter = [[6], [7], [8]]
result = l.regression(enter)
print(f'{enter}: {result}')

# training improve with more values
