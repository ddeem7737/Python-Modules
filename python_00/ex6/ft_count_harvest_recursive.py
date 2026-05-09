def recursive(n):
	if n == 0:
		return 1
	else:
		a = recursive(n - 1)
		print("Day:", a)
		return a + 1

def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	recursive(days)

ft_count_harvest_recursive()