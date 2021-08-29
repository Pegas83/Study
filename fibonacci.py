#0,1,1,2,3,5,8,13,21
fibonacci_seq = [0, 1]
for i in range(2, 20):
    num = fibonacci_seq[i-2] + fibonacci_seq[i-1]
    fibonacci_seq.append(num)
print(fibonacci_seq)
