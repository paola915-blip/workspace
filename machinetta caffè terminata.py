 scegli metodo di pagamento non funziona ancora , aggiungo progress bar



import sys	# per progress bar
import time



def updt(total, progress):		#progress bar
    """
    Displays or updates a console progress bar.
    Original source: https://stackoverflow.com/a/15860757/1391441
    """
    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()



runs = 30	# il numero regola la durata della progress bar



chiavetta=input
ricarica=0

chiavetta=0.00


diecicent=0.10
venticent=0.20
cinquantacent=0.50
bicchieri=10


maximport=float(input("dimmi max importo "))
#def inserisci_monete():
	#inseriscimonete=float(input("inseriscimonete ")

	
	
		





#def switch_demo(argument):
#	switcher = {
			#1: "chiavetta",
			
			#2: contanti()
			
			
	#}
	#print (switcher.get(argument, "only 2 payment methods"))
	
#selezionametodopagamento=int(input("selezionametodopagamento"))
#print(switch_demo(selezionametodopagamento))
	

while chiavetta<maximport:
	
		
		ricarica=round(float(input("inserisci moneta ")),2)
		while ricarica>2:
			print("max moneta da 2 euro, 5cent non accettati, dammi un'altra moneta")
			ricarica=round(float(input("inserisci moneta ")),2)
	
		if (ricarica==0.10 or ricarica==0.20 or ricarica%0.5==0 or ricarica%1==0):
			chiavetta=chiavetta+ricarica
	
	
			print("importo tot chiavetta" ,round(chiavetta,2))
	
		elif (ricarica==0.30):
			print("non esiste moneta da 30cent")
		
		elif (ricarica==0.40):
	
		
			print("non esiste moneta da 40cent")
	
	
		elif (ricarica==0.60):
			print("non esiste moneta da 60cent")
	
		elif (ricarica==0.70):
			print("non esiste moneta da 70cent")
	
		elif (ricarica==0.80):
			print("non esiste moneta da 80cent")
	
		elif (ricarica==0.90):
			print("non esiste moneta da 90cent")
	
	
	
	
	
		else:
			print("deve essere diecicent, venticent ,50cent, 1 euro o 2 euro")
		
	
	
	
		if chiavetta >maximport:
			print("ritirare seguente importo")
			print(maximport-chiavetta)
	
		if chiavetta>maximport:
			chiavetta=maximport
		
	
print("saldochiavetta ", chiavetta)			
		










nome="cappuccino"
nome1="caffè espresso"
nome2="caffè-macchiato"
nome3="latte-macchiato"
nome4="caffè-ginsen"	
nome5="caffè-corretto "
nome6="caffe-americano"
nome7="the"
nome8="cioccolata fondente"
nome9="cioccolata latte"

prezzo= {"prezzo ":0.50}
prezzo1= {"prezzo ": 0.20}
prezzo2={"prezzo ":0.30}
prezzo3={"prezzo ":0.40}
prezzo4={"prezzo ":0.60}
prezzo5={"prezzo ":0.25}
prezzo6={"prezzo ":0.40}
prezzo7={"prezzo ":0.30}
prezzo8=("prezzo";0.35)
prezzo9=("prezzo";0.25)

prezzoarray=0.50
prezzoarray1=0.20
prezzoarray2=0.30
prezzoarray3=0.40
prezzoarray4=0.60
prezzoarray5=0.25
prezzoarray6=0.40
prezzoarray7=0.30
prezzoarray8=0.35
prezzoarray9=0.25



quantitälatte = "latte:""20ml"
quantitälatte1 = "latte:""0.00 ml"
quantitälatte2 = "latte:""10ml"
quantitälatte3 = "latte:""40ml"
quantitälatte4 = "latte:""0.00"
quantitälatte5 = "latte:""0.00 ml"
quantitälatte6 = "latte:""0.00 ml"
quantitäginsen= "ginsen:""3ml"
quantitäciccolata="cioccolata20ml"
quantitàthe = "the15cl"    
uantitäacqua= 	"acqua:""20ml"



drink_array= [nome,	prezzo , quantitälatte]
drink_array1=[nome1, prezzo1, quantitälatte1]

drink_array2=[nome2, prezzo2, quantitälatte2]
drink_array3=[nome3, prezzo3, quantitälatte3 ]

drink_array4=[nome4, prezzo4, quantitälatte4, quantitäginsen]

drink_array5=[nome5, prezzo5,   quantitälatte5, quantitägrappa ]

drink_array6=[nome6, prezzo6, quantitälatte6, quantitäacqua]

drink_arrey7=[nome7, prezzo7,quuantitàacqua7]

drink_array8[nome8,prezzo8]	

def switch_demo(argument):
	switcher = {
			1: drink_array,
			
			2: drink_array1,
			
			3: drink_array2,
 
			4: drink_array3,
            
			5: drink_array4,
			         
			6: drink_array5,
			 
			7: drink_array6
			
			8:drink_array7

			9:drink_array8
			
			10:drink_array9
	}
	print (switcher.get(argument, "invalid drink: buttons that can be pressed are 1,2,3,4,5,6,7"))
	
import tkinter as tk
    
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


def press1():
	print(switch_demo(1))
def press2():
	print(switch_demo(2))

def press3():
	print(switch_demo(3))

def press4():
	print(switch_demo(4))
	
def press5():
	print(switch_demo(5))	
	
def press6():
	print(switch_demo(6))

def press7():
	print(switch_demo(7))


def press8():
	print(switch_demo(8))
	print("pulsante 8 non funzionante")
	
def press9():
	print(switch_demo(9))
	print("pulsante 9 non funzionante")	
button = tk.Button(frame, 
                   text="button 1", 
                   fg="red",
                   command=press1)
button.pack(side=tk.LEFT)
button1 = tk.Button(frame, 
                   text="button 2", 
                   fg="blue",
                   command=press2)
button1.pack(side=tk.LEFT)

button2 = tk.Button(frame, 
                   text="button 3", 
                   fg="red",
                   command=press3)
button2.pack(side=tk.LEFT)


button3 = tk.Button(frame, 
                   text="button 4", 
                   fg="blue",
                   command=press4)
button3.pack(side=tk.LEFT)


button4 = tk.Button(frame, 
                   text="button 5", 
                   fg="red",
                   command=press5)
button4.pack(side=tk.LEFT)


button5 = tk.Button(frame, 
                   text="button 6", 
                   fg="blue",
                   command=press6)
button5.pack(side=tk.LEFT)

button6 = tk.Button(frame, 
                   text="button 7", 
                   fg="red",
                   command=press7)
button6.pack(side=tk.LEFT)


button7 = tk.Button(frame, 
                   text="button 8", 
                   fg="blue",
                   command=press8)
button7.pack(side=tk.LEFT)

button8 = tk.Button(frame, 
                   text="button 9", 
                   fg="red",
                   command=press9)
button8.pack(side=tk.LEFT)

button9.pack(side=tk.RIGHT)


root.mainloop()



#correggere logica bicchieri--> si riducono di uno; se sono esauriti non si puö selezionare bevanda



while((chiavetta-prezzoarray)>0):
	
	
	#if bicchieri>0:
	selezionabibita=float(input("seleziona bevanda "))
	
	
	#	bicchieri=bicchieri-1
	
	#elif bicchieri==0: 
	#	print (switch_demo())
	#	print("i bicchieri sono esauriti, la preghiamo di rivolgersi al personale")
				
				
		
	if selezionabibita==1:
		if bicchieri>0:
			quantitàzuccheroingrammi=int(input("quanto zucchero desidera (grammi) ? "))
		
		print("bicchieri rimanenti",bicchieri)	
		if bicchieri<5 and bicchieri>=1:
			print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")

		chiavetta=chiavetta-prezzoarray
		print("hai selezionato bevanda1")
		print (switch_demo(selezionabibita))
		print("quantità zucchero", quantitàzuccheroingrammi ," g")
		print("prezzo ", prezzoarray)
		print("importo rimanente chiavetta", chiavetta)
		print("attendi 10 secondi")
		for run_num in range(runs):
			time.sleep(.1)
			updt(runs, run_num + 1)
		print("your drink is ready")

		
		
		
		
	if selezionabibita==2:
		if bicchieri>0:
			quantitàzuccheroingrammi1=int(input("quanto zucchero desidera (grammi)? " ))
		print("bicchieri rimanenti",bicchieri)
		if bicchieri<5 and bicchieri>=1:
			print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")
		
		
		
		chiavetta=chiavetta-prezzoarray1
		print("hai selezionato bevanda2")
		print (switch_demo(selezionabibita))
		print("quantità zucchero selezionto", quantitàzuccheroingrammi1, " g")
		print("prezzo ", prezzoarray1)
		print("importo rimanente chiavetta", (chiavetta))
		print("attendi 10 secondi")
		for run_num in range(runs):
			time.sleep(.1)
			updt(runs, run_num + 1)
		print("your drink is ready, drink it and enjoy it")

		
		
	if selezionabibita==3:
		chiavetta=chiavetta-prezzoarray2
		print("hai selezionato bevanda3")
		print (switch_demo(selezionabibita))
		print("prezzo ", prezzoarray2)
		print("importo rimanente chiavetta", chiavetta)
		print("bicchieri rimanenti",bicchieri)
		if bicchieri<5 and bicchieri>=1:
			print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")
	
		
		
		
		print("attendi 10 secondi")
		
		for run_num in range(runs):
			time.sleep(.1)
			updt(runs, run_num + 1)
		print("your drink is ready, drink it and enjoy it")

		
		
		
	if selezionabibita==4:
		chiavetta=chiavetta-prezzoarray3
		print("hai selezionato bevanda4")
		print (switch_demo(selezionabibita))
		print("prezzo ", prezzoarray3)
		print("bicchieri rimanenti",bicchieri)
		if bicchieri<5 and bicchieri>=1:
			print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")
	
		
		
		
		print("importo rimanente chiavetta", (chiavetta))
		print("attendi 10 secondi")
		for run_num in range(runs):
			time.sleep(.1)
			updt(runs, run_num + 1)
		print("your drink is ready, drink it and enjoy it")

		
	if selezionabibita==5:
		chiavetta=chiavetta-prezzoarray4
		print("hai selezionato bevanda5")
		print (switch_demo(selezionabibita))
		print("prezzo ", prezzoarray4)
		print("bicchieri rimanenti",bicchieri)
		if bicchieri<5 and bicchieri>=1:
			print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")
		
		print("importo rimanente chiavetta", chiavetta )
		print("attendi 10 secondi")
		for run_num in range(runs):
			time.sleep(.1)
			updt(runs, run_num + 1)
		print("your drink is ready, drink it and enjoy it")
	
	if selezionabibita==6:
		chiavetta=chiavetta-prezzoarray5
		print("hai selezionato bevanda6")
		print (switch_demo(selezionabibita))
		print("bicchieri rimanenti",bicchieri)
		if bicchieri<5 and bicchieri>=1:
			print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")
	
	
	
		print("prezzo ", prezzoarray5)
		print("importo rimanente chiavetta", (chiavetta))
		print("attendi 10 secondi")
		for run_num in range(runs):
			time.sleep(.1)
			updt(runs, run_num + 1)
		print("your drink is ready, drink it and enjoy it")

			
	if selezionabibita==7:
		chiavetta=chiavetta-prezzoarray6
		print("hai selezionato bevanda7")
		print (switch_demo(selezionabibita))
		print("bicchieri rimanenti",bicchieri)
		if bicchieri<5 and bicchieri>=1:
			print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")
		
	
	
		print("prezzo ", prezzoarray6)
		print("importo rimanente chiavetta", chiavetta )
		print("attendi 10 secondi")
		for run_num in range(runs):
			time.sleep(.1)
			updt(runs, run_num + 1)
		print("your drink is ready, drink it and enjoy it")
	
	
	
	
	
		
	
	
	
	
	
	
	
	while (chiavetta<0.60):
		print("ricarica chiavetta")
