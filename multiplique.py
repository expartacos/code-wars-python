# Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:

# multiply(3)==15 # 3 * 5¹
# multiply(10)==250 # 10 * 5²
# multiply(200)==25000 # 200 * 5³
# multiply(0)==0 # 0 * 5¹
# multiply(-3)==-15 # -3 * 5¹



def multiply(n):
    a = 1
    b = str(abs(n))
    for i in range(len(b)):
        a += i
        return print(n * 5 ** a)


(multiply(-3))