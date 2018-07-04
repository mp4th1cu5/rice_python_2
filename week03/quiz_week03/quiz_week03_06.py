fib = [0,1]
for i in range (20):
    sum_of_fib = fib[-1]+fib[-2]
    fib.append(sum_of_fib)
print (fib)
