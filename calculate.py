'''импорт библиотек'''
import circle
import square

'''определение дотсупных фигур и функций '''
figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}
'''calc принимает три аргумента: fig (фигура), func (функция) и size (размеры).'''
'''Проверка корректности ввода: Используются утверждения (assert), чтобы убедиться, что вводимые фигуры есть в списках'''
'''вычесление результата'''
'''Вывод результата'''
def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')
'''устанавливаются пустые значения, в будущим которые будут заполнены пользователем'''
if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
'''запрашивается у пользователя ввести название фигуры. Цикл будет повторяться, пока не будет введено корректное название из списка figs.'''    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n
'''ввод размеров'''
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
'''вызов функии'''
	calc(fig, func, size)



