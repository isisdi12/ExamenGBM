
def total(x): 
	return int((x * (x + 1)) / 2) 

def cuentasalto(n): 
	n = abs(n) #El numero del cual se inicie va a ser positivo no importando que
	ans = 0
	while (total(ans) < n or
		(total(ans) - n) & 1): # se necesita que el numero sea menor a n
		ans += 1
	return ans 
if __name__ == '__main__': 
	n = 100

	print(cuentasalto(n)) 
