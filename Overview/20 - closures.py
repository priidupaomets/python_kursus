"""
closures.py

Sisemiste peidetud funktsioonide deklareerimine ja kasutamine
"""

def f(x):
    def g(y):
        return x + y
    return g  # Return a closure.

def h(x):
    return lambda y: x + y  # Return a closure.

# Omistame nüüd funktsioonide poolt tagastatu muutujatele
a = f(1)
b = h(1)

# Kutsume funktsioonid a ja b läbi muutujate välja
print(a(5))  # 6
print(b(5))  # 6


#
# Me võime taolist asja kasutada ka funktsiooni kaasa andmiseks teisele funktsioonile (dekoraator)
#

def f1(f):
    def f2():
        print("Enne")
        f()
        print("Pärast")
    return f2

# Anname teada, et funktsiooni f3 välja kutsel, antakse see tegelikult kaasa f1 funktsioonile
@f1
def f3():
    print("f3")

# Kutsume välja
f3()
# Enne
# f3
# Pärast

#
# Veidi kasulikum näide
#
import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f"Elapsed: {(t2-t1) * 1000}ms")
    return wrapper

@elapsed_time
def big_sum():
    pass

big_sum()
