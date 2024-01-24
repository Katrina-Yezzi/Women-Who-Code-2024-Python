# Women Who Code (Python) Challenge No. 14
# Write a program to print the first n numbers of a Fibonacci sequence.


def fib_seq(n):
    fib = [1,1] 

    if n == 0:
        result=[0]

    else:
        for i in range(2,n):           
            next_num = fib[i-1] + fib[i-2]
            fib.append(next_num)
        result = fib[:n]
            
    print(f'F({n}) = {result}')
        
    return result

n = int(input('Enter the value of n: '))
fib_seq(n)
