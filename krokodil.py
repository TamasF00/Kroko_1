import random

maxn = 10

def main():
	run_game = True

	print("Szia, ez egy rovid jatek! :-)")
	print(f"Talald ki, hogy menny krokodil van a toban 1 tol {maxn} ig.")
	
	while run_game == True:
		questions()
		print()
		answer = input("Akarsz meg jatszani? Ha igen akkor irj egy Y ont :") 
		if answer.upper() != "Y":
			print()
			print("Kileptel a jatekbol.")
			run_game = False
		
def questions():
	guess = None
	tryz = 1
	n = random.randint(1, maxn)
	while guess != n:
	    while True:
	    	try:
	    		print()
	    		guess = int(input("Szerinted mennyi? :"))
	    		break
 	   	except ValueError:
	   	 	print("Oops!  Ez nem szam..")
	    if guess > n:
	        print("kevesebb")
	        tryz += 1
	    if guess < n:
	        print("tobb")
	        tryz += 1
        
	print(f"Igen, {tryz}. alkalomra eltalaltad!")
	if tryz == 1:
		print("Te egy gondolatolvaso vagy!")
	else:
		print("Gratulalok, nyertel!")
	
if __name__ == "__main__":
	main()