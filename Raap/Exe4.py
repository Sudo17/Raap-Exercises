#Define player scores
if __name__ == "__main__":
	input_arr = [1, 2, 0, 0, 4, 1, 6, 2, 1, 3]
	batsmen = [0, 0]
	curr_batsman = 0
	for i in range(len(input_arr)):
		batsmen[curr_batsman] += input_arr[i]
		if i % 5 == 0 and input_arr[i] % 2 == 0:
			curr_batsman = (curr_batsman + 1) % 2
		elif input_arr[i] % 2 and (i == 0 or i % 5):
			curr_batsman = (curr_batsman + 1) % 2

#Print individual scores
	print("Total score:", sum(input_arr))
	print("Batsman 1:", batsmen[0])
	print("Batsman 2:", batsmen[1])