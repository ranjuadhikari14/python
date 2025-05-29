def fib_series(num):
    fibo=[]
    a=0
    b=1
    for i in range(num):
        fibo.append(a)
        a, b = b, a + b
    return fibo

num_series=int(input("enter the number of terms:"))
if(num_series<=0):
    print("please,enter the positive integer value")
else:
    print(f"fibonacii series of the given number are:",fib_series(num_series))


