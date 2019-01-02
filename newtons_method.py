import math 
def f(x):
    return .5 + math.sin(x) - math.cos(x)

def div_f(x):
    return math.cos(x) + math.sin(x)
x0 = 1
converges = False

count = 1
while count <= 4:
    x1 = x0 - f(x0)/div_f(x0)

    print(f'Iternation {count}:')
    print(f'x0 = {x0}')
    print(f'x1 = {x1}')
    print(f'f(x0) = {f(x0)}')
    print(f'f\'(x0) = {div_f(x0)}')
    print(f'|(x1-x0)/x1| = {abs((x1 - x0)/x1)}')

    x0 = x1
    count += 1

if(converges):
     print("Soultion found!")

else:
    print("Did not converge!")