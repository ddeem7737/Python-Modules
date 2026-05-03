import sys

def analyse_data():
	print("== Player Score Analytics ===")
	lst = []
	i = 1
	while i < len(sys.argv):
		try:
			lst += [int(sys.argv[i])]
		except:
			print(f"Invalid parameter: '{sys.argv[i]}'")
		i += 1
	if len(lst) == 0:
		print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
		return
	else:
		print(f"Scores processed: {lst}")
		print(f"Total Players: {len(lst)}")
		print(f"Total Score: {sum(lst)}")
		print(f"Avarage Score: {sum(lst)/(len(lst))}")
		print(f"Max Score: {max(lst)}")
		print(f"Min Score: {min(lst)}")
		print(f"Score range: {max(lst) - min(lst)}")

if __name__ == "__main__":
	analyse_data()	