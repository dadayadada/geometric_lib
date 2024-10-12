
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# L-03
- Circle and square added  8ba9aeb
- Docs added  d078c8d
- Docs added  6adb962

# L-04
- Triangle added  d080c78
- Doc updated for triangle 51c40eb
- Add calculate.py  d76db2a
- Update docs for calculate  b5b0fae
- Add rectangle.py  3049431

# L-05
- Add user agreement  438b89a
- Update Docs.Add user agreement info  86edb1c


* Examples of function call
- Circle
```

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r
print(area(5),perimeter(6)

```
- Output: 78.4 37.7

- Square
```

def area(a):
    return a * a


def perimeter(a):
    return 4 * a
print(area(6),perimeter(3))

```
- Output: 36 12 

- Triangle
```
def area(a, b, c):
    return (a + b + c) / 2


def perimeter(a, b, c):
    return a + b + c
print(area(1,2,3),perimeter(4,5,6))

```
- Output: 3.0 15 	

- Calculate 
```

import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)

```
- Input:
- square
- perimeter
- 3
- Output:
- 12
