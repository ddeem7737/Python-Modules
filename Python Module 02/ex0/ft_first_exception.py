def input_temperature(temp_str):
	try:
		x = int(temp_str)
		return x
	except:
		print("OOPS!!!, You inputted an invalid temperature. Please try again with a valid one")

print("=== Garden Temperature ===\n")


print("Input data is '25'")
print(f"Temperature is {input_temperature(25)}C\n")
print("Input data is 'abc'")
print(input_temperature("abc"))
