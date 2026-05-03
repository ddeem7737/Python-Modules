class GardenError(Exception):
	def __init__(self, message = "Unkown Gaden Error"):
		super().__init__(message)

class PlantError(GardenError):
	def __init__(self, message = "Unkown Plant Error"):
		super().__init__(message)
class WaterError(GardenError):
	def __init__(self, message = "Unkown Water Error"):
		super().__init__(message)

def check_plant():
	raise PlantError("The tomato plant is wilting!")

def check_water():
	raise WaterError("Not enough water in the tank")

def test_custom_errors():
	print("=== Custom Garden Errors Demo ===")

	print("Testing PlantError...")
	try:
		check_plant()
	except PlantError as error:
		print(f"Caught PlantError: {error}")
	
	print("Testing WaterError...")
	try:
		check_water()
	except WaterError as error:
		print(f"Caught WaterError: {error}")
	
	print("Testing catching all garden errors...")
	try:
		check_plant()
	except GardenError as error:
		print(f"Caught Garden Error: {error}")
	try:
		check_water()
	except WaterError as error:
		print(f"Caught WaterError: {error}")
	print("All custom errors types work correctly")

if __name__ == "__main__":
	test_custom_errors()