import sys

def show_data():
	print("=== Command Quest ===")
	print(f"Program Name: {sys.argv[0]}")
	if len(sys.argv) == 1:
		print("No Arguments Provided!")
	else:
		i = 1
		print (f"Arguments Recieved: {len(sys.argv) - 1}")
		while i < len(sys.argv):
			print(f"Argument {i}: {sys.argv[i]}")
			i += 1
	print(f"Total Arguments: {len(sys.argv)}")

if __name__ == "__main__":
	show_data()