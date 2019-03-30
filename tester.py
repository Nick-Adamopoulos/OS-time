from time import perf_counter as time
from time import sleep

def main():
	time_start = time()
	x=0
  
	for i in range(1,500000):
		x+=i**2
		x*i

	time_finish = time()
	total = time_finish - time_start
	return total
  
x=input("""Press Enter to start the procedure
>>>""")

if x=='':
	for i in range(0,20):
		print(main())
		sleep(2)
	
