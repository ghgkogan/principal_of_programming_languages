# ------------------------------------------------
#                       Q1
# ------------------------------------------------
x=5
def func(y):
    print(y)
    print(x)
    x=x+1
#func(3)

# ------------------------------------------------
#                       Q2
# ------------------------------------------------
x=5
def func(y):
    print(y)
    x=10
    x=x+1
    print(x)
#func(3)

# ------------------------------------------------
#                       Q3
# ------------------------------------------------
x=5
def func(x):
    x+=1
    print(x)
#func(3)
    
# ------------------------------------------------
#                       Q4
# ------------------------------------------------
def g(u):
    def f(i):
            return u+i
    return f(10)
#g(20)

# ------------------------------------------------
#                       Q5
# ------------------------------------------------
def g(u):
    return f(u,10)
def f(i,j):
    return i+j
#g(20)

# ------------------------------------------------
#                       Q6
# ------------------------------------------------
x=3
def boring(x):
        def why(y):
            x=y
        why(5)
        return x
print(boring(4))

# ------------------------------------------------
#                       Q7
# ------------------------------------------------
x=3
def interesting(x):
        def because(y):
                nonlocal x
                x=y
        because(5)
        return x
#print(interesting(4))
#print(x)

# ------------------------------------------------
#                       Q8
# ------------------------------------------------
x=3
def boring(x):
    def why(y):
        global x
        x=y
    why(5)
    return x
#boring(4)
#x

# ------------------------------------------------
#                       Q9
# ------------------------------------------------
def outer():
    x=1
    def inner(z):
        x+=1
        print(x)
    return inner(3)
#outer()

# ------------------------------------------------
#                       Q10
# ------------------------------------------------
def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)

# ------------------------------------------------
#                       Q11
# ------------------------------------------------
x=5
def f():
    y=10
    global x
    x+=y
    return y
#f()
#x
#a=f()
#a
# ------------------------------------------------
#                       Q12
# ------------------------------------------------
def func1(x):
    def funcA(y):
        if abs(y**2-x)<0.001:
            return True
        else:
            return False
    def funcB(y):
        while funcA(y):
            y=funcC(y)
        return y
    def funcC(y):
        return (y+x/y)/2.0
    return funcB(1.0)
#func1(4)
# ------------------------------------------------
#                       Q13
# ------------------------------------------------
a = 0
def f1(x):
    def f2(y):
        nonlocal x
        x = x * 2
        return x > y
    def f3(y):
        global a
        a = a + 1
        return a + y
    def f4(y):
        nonlocal x
        x = x + 1
        return y + x

    y = 'a'
    if f2(x):
        y = f3(x)
    print('a={0}, x={1}, y={2}'.format(a, x, y))
    return f4

#f1(5)(10)
#f1(10)
#f1 = f1(5)
#print(f1(10))
#print(f1(10))
# ------------------------------------------------
#                       Q14
# ------------------------------------------------
def f(x):
    return 2*x+3
def g(f,x,y):
    x=f(x)+f(y)
    return x
#x=10
#g(f,x,x*2)


