from linear import LinearRegression

l = LinearRegression()
Input = [[3], [1], [5], [2], [4]]
Output = [[27], [9], [45], [18], [36]]
l.train(Input, Output)
enter = [[8], [6], [9], [7]]
result = l.regression(enter)
print(f'{enter}: {result}')
