def badge():
	nome="Stefano"
	cognome="P."
	codicef="PRTSFN96E17F388I"

a=3
b=5
personeammesse=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len(personeammesse))
print(personeammesse)

def aggiungonuovapersona():
	aggiungonuovapersona=input("nuovocliente ")
	personeammesse.append(aggiungonuovapersona)
#aggiungonuovapersona()


def badge():
	nome="Stefano"
	cognome="P."
	codicef="PRTSFN96E17F388I"




def badge():
    	nome="Carlo"
	cognome="G."
	codicef="CRLBTT37C33I653G"

personeammesse=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len(personeammesse))
print(personeammesse)

def badge():
    	nome="Stefano"
	cognome="C."
	codicef="PPTSNF91A17G388N"

personeammesse=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len(personeammesse))
print(personeammesse)


def badge():
    	nome="Marco"
	cognome="S."
	codicef="CRNMCO73B75E367T"

ersoneammesse=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len(personeammesse))
print(personeammesse)

def badge():
    	nome="Manlio"
	cognome="t."
	codicef="MNTMLO94C91E600F"

personeammesse=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len(personeammesse))
print(personeammesse)

def badge():
    	nom="Donatello"
	cognome="C."
	codicef="PSODNO61B64E600M"

personeammesse=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len(personeammesse))
print(personeammesse)

def badge():
    	nom="Paolo"
	cognome="C."
	codicef="CO73B75E367T"

nomipossessori=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len(possessoricorretti))
print(possessoricorretti)

def beg ():
    nome="Carlo"
    cognome="P."
    codicefe"CO73B75E367T"

nomipossessori=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len (codiceferrato))
print(codiceferrato)

def badge():
    	nome="Stefano"
	cognome="C."
	codicef"PRTSFN96E17F388I"

nomi possessori=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len (codiceferrato))
print(codiceferrato)





def badge():
    	nome="Carlo"
	cognome="G."
	codicef="CRLBTT37C33I653G"

nomi possessori=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len (codiceferrato))
print(codiceferrato)


def badge():
    nome="Stefano"
    cognome="G."
    codicef="PPTSNF91A17G388N""

nomi possessori=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len (codiceferrato))
print(codiceferrato)

def badge():
    	nome="Marco"
	cognome="S."
	codicef="CRLBTT37C33I653G"

 nomi possessori=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len (codiceferrato))
print(codiceferrato)

def badge():
    	nome="Manlio"
	cognome="t."
	codicef="PSODNO61B64E600M"

nomi possessori=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len (codiceferrato))
print(codiceferrato)

def badge():
    	nom="Donatello"
	cognome="C."
	codicef="MLO94C91E600 "

 nomi possessori=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len (codiceferrato))
print(codiceferrato)

	nom="Paolo"
	cognome="C."
	codicef="CRLBTT37C33I653G"

nomi possessori=["Stefano","Carlo","Stefano","Marco","Manlio","Donatello","Paolo"]
print(len (codiceferrato))
print(codiceferrato)

while a<b:
	#a=a+1
aggiungonuovapersonaalista=input("nuovocliente ")

personeammesse.append(aggiungonuovapersonaalista)
print(personeammesse)
#print(len(personeammesse))
#print(personeammesse)
i=0

#print(personeammesse)
richiedinome=input("cometichiami ")


while i <len(personeammesse):

		i = i + 1

		print(personeammesse[i])


@@ -272,7 +272,7 @@ def controlloValidita(val):
        with conn:
            cursore = conn.cursor()
            try:
                cursore.execute("UPDATE [Utente] SET Validita=False WHERE NumeroBadge=?",[val])
                cursore.execute("UPDATE [Utente] SET Validita=False WHERE NumeroBadge=?",[val]) #SEGNA NON VALIDO IN CASO SIA SCADUTO

            except sqlite3.Error as error:
                print("Failed to insert data into sqlite table", error)
@@ -284,7 +284,7 @@ def controlloValidita(val):

def Accesso =(nome)
    numero = int(input('Inserire numero Badge: ')) #ACCESSO AI TORNELLI CONTROLLO SE ESISTE O ACCESSO GIA' FATTO
    color = {'verde","blu"}
    color = {'verde", "blu"}   #DIZIONARIO CONTENENTE ID TORNELLI
    with conn:
        cursore = conn.cursor()
        try:
@@ -298,39 +298,65 @@ def AccessoStanza(colore):

                cursore.execute("SELECT Presenza FROM [Utente] WHERE NumeroBadge=?",[numero])
                va = cursore.fetchone()
                if va[0] == 1:
                if va[0] == 1:      #VERIFICO ESISTENZA NUMERO BADGE

                    data = datetime.datetime.now().strftime(date_format)
                    cursore.execute("SELECT Nome FROM [codice fiscaleWHERE Id badge",[color[colore]]) #TROVO NOME STANZA
                    val = cursore.fetchone()
                    nomstanza = val[0]
                    cursore.execute("SELECT  [nome].Idutente From [cod fiscale] JOIN [UtenteRuolo] ON [UtenteRuolo].IdRuolo=[Ruolo].IdRuolo JOIN [Utente] ON [Utente].IdUtente=[UtenteRuolo].IdUtente WHERE [Utente].NumeroBadge=?",[numero])
                    roli = cursore.fetchall()  #TROVO codice fiscale/I UTENTE
                    cont = 0
                    for i in range(len(roli)):
                        cursore.execute(f"SELECT {nome} FROM [codice fiscale] WHERE IdRuolo=?",[roli[i][0]])
                        cursore.execute("SELECT Permesso FROM [Permessi] WHERE Idpossessore codice fiscale=? AND IdStanza=?",[roli[i][0], color[colore]])
                        rol = cursore.fetchone()
                        if rol[0] == 1:
                            cont = cont + 1 #CONTROLLO SE HA IL PERMESSO DI ENTRARE

                    if cont >0:
                    cursore.execute("SELECT EntrataUscita FROM [Accessi] WHERE IdUtente=(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?) ORDER BY IdAccesso DESC",[numero])
                        cursore.execute("SELECT EntrataUscita FROM [Accessi] WHERE IdUtente=(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?) AND IdStanza=? ORDER BY IdAccesso DESC",[numero,color[colore]])
                        acc = cursore.fetchone() #CONTROLLO SE STA ENTRANDO O USCENDO

                        if acc== None:
                            cursore.execute("SELECT Id codice fiscale FROM [Accessi] WHERE IdUtente=(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?)  AND EntrataUscita='Entrata'  ORDER BY IdAccesso DESC",[numero])
                            idstanz = cursore.fetchone() #CONTROLLO se  utente + possessore di codiice fiscale
                                if str(idstanz[0]) != color[colore]:
                                    cursore.execute("INSERT INTO [Accessi] (Idcodice fiscale, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?),?,'Uscita')",[idstanz[0],numero,data])

                            cursore.execute("INSERT INTO [Accessi] (Idcodice fiscale, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] id impronta digitale utente, FROM[Utente] WHERE NumeroBadge=?),?,'Entrata')",[color[colore],numero,data])
                            cursore.execute("SELECT Cognome FROM Utente WHERE NumeroBadge=?",[numero])
                            d = cursore.fetchone()
                            print(f"Ben Arrivato Sig. {d[0]}!")

                        else:

                            if str(acc[0]) == 'Uscita':
                                cursore.execute("SELECT Idcodice fiscale FROM [Accessi] WHERE IdUtente=(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?) AND EntrataUscita='Entrata' ORDER BY IdAccesso DESC",[numero])
                                idstanz = cursore.fetchone()
                                if idstanz != None: #CONTROLLO SE ERA ANCORA PRESENTE IN UN ALTRA STANZA E SEGNO USCITA
                                    if idstanz[0] != color[colore]:
                                        cursore.execute("INSERT INTO [Accessi] (Idcodice fiscale, id impronta digitale utente, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?),?,'Uscita')",[idstanz[0],numero,data])

                                cursore.execute("INSERT INTO [Accessi] (IdStanza, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?),?,'Entrata')",[color[colore],numero,data])
                                cursore.execute("SELECT Cognome FROM Utente WHERE NumeroBadge=?",[numero])
                                d = cursore.fetchone()
                                time.sleep(0.5)
                                print('.',end=' ',flush=True)
                                time.sleep(0.5)
                                print('.',end=' ',flush=True)
                                time.sleep(0.5)
                                print('.',flush=True)
                                print(f"Ben Arrivato Sig. {d[0]}!") #SCRIVO I DATI DELL'ACCESSO

                            else:

                                cursore.execute("INSERT INTO [Accessi] (IdStanza, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?),?,'Uscita')",[color[colore],numero,data])
                                cursore.execute("SELECT Cognome FROM Utente WHERE NumeroBadge=?",[numero])
                                d = cursore.fetchone()
                                time.sleep(0.5)
                                print('.',end=' ',flush=True)
                                time.sleep(0.5)
                                print('.',end=' ',flush=True)
                                time.sleep(0.5)
                                print('.',flush=True)
                                print(f"Arrivederci Sig. {d[0]}!")
                    else:
                        print("Non hai il permesso di passare impronta digitale e codice fiscale non riconosciuti!!!")
@@ -348,13 +374,13 @@ def acesso Tornello(colore):
def main ():













    while True:
        print(' \n ( 1 ) Entra\n ( 2 ) Esci\n ( 3 ) Crea Nuovo Badge\n ( 4 ) Rinnova Badge')
        print(' \n ( 1 ) Entra nel Tornello\n ( 2 ) Esci dal Tornello\n ( 3 ) Crea Nuovo Badge\n ( 4 ) Rinnova Badge')
        scelta = int(input("-> "))
        if scelta>=1 and scelta<=4:
            if scelta == 1:
                if accesso() == True:
                    while True:
                        print(' \n ( 1 ) Entra/Esciin tornello ( 2 ) Entra/Esci nella stanza Blu\n ( 3 ) Entra/Esci nella stanza Verde\n ( 4 ) Entra/Esci nella stanza Rosa\n ( 5 ) Esci')
                        print(' \n ( 1 ) Entra/Esci nella stanza Rossa\n ( 2 ) Entra/Esci nella stanza Blu\n ( 3 ) Entra/Esci nella stanza Verde\n ( 4 ) Entra/Esci nella stanza Rosa\n ( 5 ) Esci dal Tornello')
                        s = int(input("-> "))
                        if s>=1 and s<=5:
                            if s == 1:

	@@ -272,7 +272,7 @@ def controlloValidita(val):
        with conn:
            cursore = conn.cursor()
            try:
                cursore.execute("UPDATE [Utente] SET Validita=False WHERE NumeroBadge=?",[val])
                cursore.execute("UPDATE [Utente] SET Validita=False WHERE NumeroBadge=?",[val]) #SEGNA NON VALIDO IN CASO SIA SCADUTO

            except sqlite3.Error as error:
                print("Failed to insert data into sqlite table", error)
@@ -284,7 +284,7 @@ def controlloValidita(val):

def AccessoStanza(colore):
    numero = int(input('Inserire numero Badge: ')) #ACCESSO AI TORNELLI CONTROLLO SE ESISTE O ACCESSO GIA' FATTO
    color = {'blu',  'verde'}
    color = {'blu' 'verde, }   #DIZIONARIO CONTENENTE ID STANZE
    with conn:
        cursore = conn.cursor()
        try:
@@ -298,39 +298,65 @@ def AccessoStanza(colore):

                cursore.execute("SELECT Presenza FROM [Utente] WHERE NumeroBadge=?",[numero])
                va = cursore.fetchone()
                if va[0] == 1:
                if va[0] == 1:      #VERIFICO ESISTENZA NUMERO BADGE

                    data = datetime.datetime.now().strftime(date_format)
                    cursore.execute("SELECT Nome FROM [codice fiscale] WHERE IdStanza=?",[color[colore]]) #TROVO NOME STANZA
                    val = cursore.fetchone()
                    nomstanza = val[0]
                    cursore.execute("SELECT  [Ruolo].IdRuolo From [Ruolo] JOIN [UtenteRuolo] ON [UtenteRuolo].IdRuolo=[Ruolo].IdRuolo JOIN [Utente] ON [Utente].IdUtente=[UtenteRuolo].IdUtente WHERE [Utente].NumeroBadge=?",[numero])
                    roli = cursore.fetchall()  #TROVO RUOLO/I UTENTE
                    cont = 0
                    for i in range(len(roli)):
                        cursore.execute(f"SELECT {nomstanza} FROM [Permessi] WHERE IdRuolo=?",[roli[i][0]])
                        cursore.execute("SELECT Permesso FROM [Permessi] WHERE IdRuolo=? AND IdStanza=?",[roli[i][0], color[colore]])
                        rol = cursore.fetchone()
                        if rol[0] == 1:
                            cont = cont + 1 #CONTROLLO SE HA IL PERMESSO DI ENTRARE
cursore.execute("SELECT Presenza FROM [Utente] WHERE NumeroBadge=?",[numero])
                va = cursore.fetchone()
                if va[0] == 1:
                if va[0] == 1:      #VERIFICO ESISTENZA NUMERO BADGE

                    data = datetime.datetime.now().strftime(date_format)
                    cursore.execute("SELECT Nome FROM [codice fiscale] WHERE IdStanza=?",[color[colore]]) #TROVO NOME STANZA
                    val = cursore.fetchone()
                    nomstanza = val[0]
                    cursore.execute("SELECT  [codi fiscale].Idnome utente From [impronta digitale] JOIN [UtenteRuolo] ON [UtenteRuolo].IdRuolo=[Ruolo].IdRuolo JOIN [Utente] ON [Utente].IdUtente=[UtenteRuolo].IdUtente WHERE [Utente].NumeroBadge=?",[numero])
                    roli = cursore.fetchall()  #TROVO RUOLO/I UTENTE
                    cont = 0
                    for i in range(len(roli)):
                        cursore.execute(f"SELECT {nomstanza} FROM [Permessi] WHERE IdRuolo=?",[roli[i][0]])
                        cursore.execute("SELECT Permesso FROM [Permessi] WHERE IdRuolo=? AND IdStanza=?",[roli[i][0], color[colore]])
                        rol = cursore.fetchone()
                        if rol[0] == 1:
                            cont = cont + 1 #


                    if cont >0:
                        cursore.execute("SELECT EntrataUscita FROM [Accessi] WHERE IdUtente=(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?) ORDER BY IdAccesso DESC",[numero])
                        cursore.execute("SELECT EntrataUscita FROM [Accessi] WHERE IdUtente=(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?) AND IdStanza=? ORDER BY IdAccesso DESC",[numero,color[colore]])
                        acc = cursore.fetchone() #CONTROLLO SE STA ENTRANDO O USCENDO

                        if acc== None:
                            cursore.execute("SELECT IdStanza FROM [Accessi] WHERE IdUtente=(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?)  AND EntrataUscita='Entrata'  ORDER BY IdAccesso DESC",[numero])
                            idstanz = cursore.fetchone() #CONTROLLO SE ERA ANCORA PRESENTE IN UN ALTRA STANZA E SEGNO USCITA
                            if idstanz != None:
                                if str(idstanz[0]) != color[colore]:
                                    cursore.execute("INSERT INTO [Accessi] (IdStanza, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?),?,'Uscita')",[idstanz[0],numero,data])

                            cursore.execute("INSERT INTO [Accessi] (IdStanza, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?),?,'Entrata')",[color[colore],numero,data])
                            cursore.execute("SELECT Cognome FROM Utente WHERE NumeroBadge=?",[numero])
                            d = cursore.fetchone()
                            print(f"Ben Arrivato Sig. {d[0]}!")

                        else:

                            if str(acc[0]) == 'Uscita':
                                cursore.execute("SELECT Idcodice fiscale FROM [Accessi] WHERE IdUtente=(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?) AND EntrataUscita='Entrata' ORDER BY IdAccesso DESC",[numero])
                                idstanz = cursore.fetchone()
                                if idstanz != None: #CONTROLLO SE ERA ANCORA PRESENTE IN UN ALTRA STANZA E SEGNO USCITA
                                    if idstanz[0] != color[colore]:
                                        cursore.execute("INSERT INTO [Accessi] (Iddcodice fiscale, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?),?,'Uscita')",[idstanz[0],numero,data])

                                cursore.execute("INSERT INTO [Accessi] (Idcodice fiscale, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?),?,'Entrata')",[color[colore],numero,data])
                                cursore.execute("SELECT Cognome FROM Utente WHERE NumeroBadge=?",[numero])
                                d = cursore.fetchone()
                                time.sleep(0.5)
                                print('.',end=' ',flush=True)
                                time.sleep(0.5)
                                print('.',end=' ',flush=True)
                                time.sleep(0.5)
                                print('.',flush=True)
                                print(f"Ben Arrivato Sig. {d[0]}!") #SCRIVO I DATI DELL'ACCESSO

                            else:

                                cursore.execute("INSERT INTO [Accessi] (IdStanza, IdUtente, Quando, EntrataUscita) VALUES (?,(SELECT IdUtente FROM [Utente] WHERE NumeroBadge=?),?,'Uscita')",[color[colore],numero,data])
                                cursore.execute("SELECT Cognome FROM Utente WHERE NumeroBadge=?",[numero])
                                d = cursore.fetchone()
                                time.sleep(0.5)
                                print('.',end=' ',flush=True)
                                time.sleep(0.5)
                                print('.',end=' ',flush=True)
                                time.sleep(0.5)
                                print('.',flush=True)
                                print(f"Arrivederci Sig. {d[0]}!")






















                    else:
                        print("Non hai il permesso di entrare nel tornello !!")
@@ -348,13 +374,13 @@ def AccessoStanza(colore):
def main ():

    while True:
        print(' \n ( 1 ) Entra\n ( 2 ) Esci\n ( 3 ) Crea Nuovo Badge\n ( 4 ) Rinnova Badge')
        print(' \n ( 1 ) Entra nel Tornello\n ( 2 ) Esci dal Tornello\n ( 3 ) Crea Nuovo Badge\n ( 4 ) Rinnova Badge')
        scelta = int(input("-> "))
        if scelta>=1 and scelta<=4:
            if scelta == 1:
                if accesso() == True:
                    while True:
                        print(' \n ( 1 ) Entra/Esci nella stanza Rossa\n ( 2 ) Entra/Esci nella stanza Blu\n ( 3 ) Entra/Esci nella stanza Verde\n ( 4 ) Entra/Esci nella stanza Rosa\n ( 5 ) Esci')
                        print(' \n ( 1 ) Entra/Esci nella stanza Rossa\n ( 2 ) Entra/Esci nella stanza Blu\n ( 3 ) Entra/Esci nella stanza Verde\n ( 4 ) Entra/Esci nella stanza Rosa\n ( 5 ) Esci dal Tornello')
                        s = int(input("-> "))
                        if s>=1 and s<=5:
                            if s == 1:



