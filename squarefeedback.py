

def square_loop(n, iterations):
	result = n
	for i in range(iterations):
		result *= n
		print(result)
def main():
	re = int(input('real: '))
	im = int(input('imaginary: '))
	iterations = int(input('iterations: '))
	square_loop(complex(re,im), iterations) #for complex feedback
	#square_loop(re, iterations) #for real feedback
main()