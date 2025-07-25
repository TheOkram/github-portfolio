Ciao io sono Cesaro Marco,
Ho 23 anni.
E studio programmazione da 2 mesi e mezzo.

E questo è il mio primo progetto in autonomo.
Vi guiderò passo dopo passo su cosa faccio,su cosa sbaglio e altro ancora.

Oggi ho intenzione di creare un'applicazione denominata: "TimeBuddy", essa ha come scopo la semplicità nell'aggiungere,rimuovere e modificare l'orario
di un dipendente. Questo è il mio primo linguaggio di scrittura, Ho scelto python poichè versatile semplice e pulito.

Qual ora a qualcuno interessasse il mio codice di quest'applicazione creata da un'autodidatta, fornirò il codice completo prima di inoltrargli l'exe stesso.
Per rispetto.
Creerò questa applicazione senza l'utilizzo di Copilot e Gemini dentro VS code.

Perchè creare questa mini applicazione?
Ho intenszione di creare un'applicazione tale come unico scopo di apprendere meglio la logica e il resto della programmazione stessa.

Dividerò il tutto in step,poichè non conosco i termini giusti per creare un'applicazione aziendale doc.

Step 1.

Inizierò col creare il Login Amministratore, che permetterà all'operatore incaricato di eseguire il login e modificare,aggiungere,rimuovere l'orario del lavoratore.

Dal mio punto di vista l'operatore è colui incaricato nell'accedere tramite nome utente e password e nell'aggiornare in maniera corretta l'orario di un lavoratore stesso.
Quindi banalmente creeremo un sistema di autenticazione base.
Giorno 25/07/2025
ore 07:14

STEP 1:

# TimeBuddy by MC

#Ho creato il dizionario vuoto,dove all'interno metterò nomeutente: password.
amministratori = {}

def buddy_amministratore():
    nome_utente = input("Immetti il nome utente che servirà per eseguire il Login: ")
    password = input("Immetti la password che servirà per eseguire il Login: ")
    amministratori = {
        "Nome_Utente": nome_utente,
        "Password": password
    }
    print(amministratori)

buddy_amministratore()


In questo caso ho creato un dizionario vuoto, ho successivamente creato una definizione chiamata buddy_amministratore():
Con all'interno i due input richiesti dall'operatore per creare un nome utente e password univoca per eseguire il login.

Infine ho creato un print per solo e unico scopo di test,per vedere se tutto funzionasse correttamente.

STEP 2:
ora toccherà a creare un semplice login:


def buddy_eseguilogin():
    global amministratori
    print("Ciao e benvenuto in TimeBuddy, sei attualmente nella sezione Admin, di conseguenza procedi a immettere il tuo nome utente e pass.")
    verifica_nome_utente = input("Immetti il nome utente: ")
    password = input("Immetti la password: ")
    if amministratori["Nome_Utente"][verifica_nome_utente] and amministratori["Password"][password] in amministratori:
        print("Verifica effettuata.")
        print("Login eseguito correttamente.")
    else:
        print("Nome_utente o password ERRATA!, Riprova.")
        print(amministratori)


Sto errando nel verificare semplicemente che nome utente e password siano nel dizionario.
Sono arrivato in questa situazione:


STEP 3:

def buddy_eseguilogin():
    global amministratori
    print("Ciao e benvenuto in TimeBuddy, sei attualmente nella sezione Admin, di conseguenza procedi a immettere il tuo nome utente e pass.")
    verifica_nome_utente = input("Immetti il nome utente: ")
    password = input("Immetti la password: ")
    try:
        if amministratori["Nome_Utente"] ==  verifica_nome_utente:
            print("Verifica effettuata.")
            print("Login eseguito correttamente.")
        else:
            print("Nome_utente o password ERRATA!, Riprova.")
            print(amministratori)
    except ValueError:
        print("Immetti il corretto!.")

dove sto comprendendo ma qui agisce solamente sul nome utente e non sulla password anche.
Devo fixarlo.

Dopo svariati test sembra funzionare:

STEP 4:
def buddy_eseguilogin():
    global amministratori
    print("Ciao e benvenuto in TimeBuddy, sei attualmente nella sezione Admin, di conseguenza procedi a immettere il tuo nome utente e pass.")
    verifica_nome_utente = input("Immetti il nome utente: ")
    password = input("Immetti la password: ")
    try:
        if amministratori["Nome_Utente"] ==  verifica_nome_utente and amministratori["Password"] == password:
            print("Verifica effettuata.")
            print("Login eseguito correttamente.")
        else:
            print("Nome_utente o password ERRATA!, Riprova.")
            print(amministratori)
    except ValueError:
        print("Immetti il corretto!.")


Cosa ho fatto?
l'errore si trovava ovviamente nel codice:
        if amministratori["Nome_Utente"] ==  verifica_nome_utente and amministratori["Password"] == password:

Quindi ho preso il dizionario (key) di nome utente e password vedendo se sono simili alla variabile prima creata dove difatti richiedeva l'input per effettuare il login.
Insomma se il nome utente e la password combacia risulta corretto e andrai avanti,sennò riprova!.
In questo esercizio personale sto cercando di superarmi:

STEP 5:

def buddy_eseguilogin():
    global amministratori
    print("Ciao e benvenuto in TimeBuddy, sei attualmente nella sezione Admin, di conseguenza procedi a immettere il tuo nome utente e pass.")
    while True:
        verifica_nome_utente = input("Immetti il nome utente: ")
        password = input("Immetti la password: ")
        if True:
            try:
                if amministratori["Nome_Utente"] ==  verifica_nome_utente and amministratori["Password"] == password:
                    print("Verifica effettuata.")
                    print("Login eseguito correttamente.")
                else:
                    print("Nome_utente o password ERRATA!, Riprova.")
                    contatore = +1
                    if contatore == "3":
                        break
                    
            except ValueError:
                print("Immetti il corretto!.")

Lasciatemi spiegare,voi che siete esperti so che è estremamente errato,ma come puoi ben supporre,vorrei far si che quando si toccano i 3 tentativi,il programma si chiude!.
Come sto risolvendo?:

STEP 6:

amministratori = {}
contatore = 0

def buddy_amministratore():
    global amministratori
    nome_utente = input("Immetti il nome utente che serve per eseguire il Login: ")
    password = input("Immetti la password che servirà per eseguire il Login: ")
    amministratori = {
        "Nome_Utente": nome_utente,
        "Password": password
    }

def buddy_eseguilogin():
    global amministratori
    global contatore
    print("Ciao e benvenuto in TimeBuddy, sei attualmente nella sezione Admin, di conseguenza procedi a immettere il tuo nome utente e pass.")
    while True:
        verifica_nome_utente = input("Immetti il nome utente: ")
        password = input("Immetti la password: ")
        if True:
            try:
                if amministratori["Nome_Utente"] ==  verifica_nome_utente and amministratori["Password"] == password:
                    print("Verifica effettuata.")
                    print("Login eseguito correttamente.")
                else:
                    print("Nome_utente o password ERRATA!, Riprova.")
                    print(contatore)
                    contatore = +1
                    if contatore == 3:
                        break
                    
            except ValueError:
                print("Immetti il corretto!.")


Ho creato un contatore che quando arriva al 3 vorrei che si fermasse tutto,solo che il contatore rimane fermo a 1.

Sarò sincero:

STEP 7:

def buddy_eseguilogin():
    global amministratori
    contatore = 0
    print("Ciao e benvenuto in TimeBuddy, sei attualmente nella sezione Admin, di conseguenza procedi a immettere il tuo nome utente e pass.")
    while True:
        contatore += 1
        verifica_nome_utente = input("Immetti il nome utente: ")
        password = input("Immetti la password: ")
        if amministratori["Nome_Utente"] ==  verifica_nome_utente and amministratori["Password"] == password:
            print("Verifica effettuata.")
            print("Login eseguito correttamente.")
        else:
            print("Nome_utente o password ERRATA!, Riprova.")
            print(contatore)
            if contatore >= 3:
                print("La terza volta consecutiva prefeiramo chiuderci!.")
                break

Ci ho messo 15 minuti per capire che il contatore va messo subito dopo while.
Perchè?:
Precedentemente ho messo il contatore solamente quando funzionava l'else,e in qualche modo pur sembrandomi giusto,la giusta risposta era metterla (ovviamente) all'inizio
del ciclo while facendo subito conteggiare il contatore,che a 3 avrebbe chiuso tutto.

Ora mi limiterò a creare la funzione che permette di aggiungere un lavoratore!.


STEP 8:

def aggiungi_lavoratoreandorari():
    global amministratori
    global lavoratori
    print("Questa è la sezione dove aggiungerai Orario e Lavoratore!.")
    nome_lavoratore = input("Immetti il nome del lavoratore da aggiungere!: ")
    orario_inizio = input(f"immetti a che ora {nome_lavoratore} inizierà a lavorare: ")
    orario_fine = input(f"Immetti a che ora {nome_lavoratore} finisce di lavorare: ")
    lavoratori = {
        "Nome_Lavoratore": nome_lavoratore,
        "Orario_inizio": orario_inizio,
        "Orario_fine": orario_fine
    }
    print(f"Aggiunto al database: {nome_lavoratore} con i rispettivi orari: Inizio {orario_inizio}:{orario_fine}.")


é stato abbastanza semplice. Ho difatti creato un nuovo dizionario che permette di creare lavoratori,presto permetterà la modifica e la rimozione di essi.


STEP 9:
def modifica_lavoratore():
    global amministratori
    global lavoratori
    while True:
        print("In questa sezione potrai semplicemente modificare un lavoratore!.")
        verifica_nome = input("Verifichiamo prima se il lavoratore che cerchi esiste: ")
        if verifica_nome in lavoratori["Nome_Lavoratore"]:
            print("Eccolo!, lo abbiamo trovato!.")
            print("1. Elimina")
            print("2. Cambia Nome.")
            print("3. Torna indietro!.")
            scelta = input("Specificaci cosa desideri!: ")
            if scelta == "1":
                rimozione = lavoratori.remove(verifica_nome)
                print("Rimosso con successo", lavoratori)
        else:
            print("Nessun lavoratore trovato con questo nome!.")

Nella rimozione del lavoratore sto trovando difficoltà.

STEP 10:
def modifica_lavoratore():
    global lavoratori
    while True:
        print("In questa sezione potrai semplicemente modificare un lavoratore!.")
        print("Scrivi 0 per uscire!.")
        verifica_nome = input("Verifichiamo prima se il lavoratore che cerchi esiste: ")
        if verifica_nome == "0":
            print("Uscita...")
            break
        if lavoratori.get("Nome_Lavoratore") == verifica_nome:
            print("Eccolo!, lo abbiamo trovato!.")
            print("1. Elimina")
            print("2. Cambia Nome.")
            print("3. Torna indietro!.")
            scelta = input("Specificaci cosa desideri!: ")

            if scelta == "1":
                lavoratori.clear()
                print("Rimosso con successo")
                print(lavoratori)
            elif scelta == "2":
                nuovo_nome = input("Inserisci il nuovo nome del lavoratore!: ")
                lavoratori["Nome_Lavoratore"] = nuovo_nome
                print("Nome cambiato con successo!.")
            elif scelta == "3":
                print("Chiusura..")
                break
            else:
                print("Opzione non valida!") 
        else:
                print("Nessun lavoratore trovato con questo nome!.")

Ho modificato molto poichè ho cercato online su come trovare un elemento in un dizionario, ho usato .get().
Infine ho corretto tramite un'ai ,ho errato molto l'indentazione.
Prima eseguendo ogni ciclo:
            else:
                print("Nessun lavoratore trovato con questo nome!.")

Che l'avevo messo come vedi su,poi ho cercato online: .clear()
anche se non sono molto sicuro poichè si limita a ripulire tutto quanto!.

lavoratori["Nome_Lavoratore"] = nuovo_nome

STEP 11:
Poi ho appreso che è banalmente semplice il cambio di un valore all'interno di un dizionario.

Errori effettuati:
errore di indentazione.
elementi sconosciuti:
.clear()
.get()

Anche se facilmente intuibile .clear continuo a non preferirlo.


def buddy_salvataggio_in_json():
    file = open("Informazioni TimeBuddyByMarco", "w")
    file.write(amministratori, lavoratori)
    file.close()
    print("Salvato tutto in un JSON.")

def main():
    print("Benvenuto in BuddyTime")
    print("\n OPZIONI")
    print("1. Procedi nel creare un utente amministratore.")
    print("2. Procedi nell'effettuare il login come amministratore!.")
    print("3. Procedi nell'aggiungere lavoratori e i rispettivi orari.")
    print("4. Modifica e rimozione del lavoratore!.")
    print("5. Procedi nel salvare il tutto in un JSON.")
    print("6. Esci senza salvare...")

    scelta = input("Cosa desideri?: ")
    if scelta == 1


STEP 12:
Ora mi sto limitando a creare il succo dell'applicazione che permette di andare avanti,indietro e specificare quel che si vuole fare!.
def main():
        print("Scrivi 0 per")
        password = input("immetti la password corretta prima di accedere ad admin: ")
        if password in key:
            print("Password corretta, autenticazione Effettuata!.")
            buddy_amministratore()
            print("Nome utente e password amministratore creati!.")
        else:
            print("Password errata!")
        while True:
            print("Benvenuto in BuddyTime")
            print("\n OPZIONI")
            print("1. Procedi nell'aggiungere lavoratori e i rispettivi orari.")
            print("2. Modifica e rimozione del lavoratore!.")
            print("3. Esci e salva!.")
            print("0. Esci senza salvare...")

            scelta = input("Cosa desideri?: ")
            if scelta == "1":
                buddy_aggiungi_lavoratoreandorari()
            elif scelta == "2":
                buddy_modifica_lavoratore()
            elif scelta == "3":
                salva_amministratori(), salva_lavoratori()
                break
            elif scelta == "0":
                print("Arrivederci..")
                break

main()


Terminato il main che permette di andare avanti e indietro, ho terminato questo semplice esercizio.
Ammetto di aver avuto bisogno di aiuto nel json,che poi sinceramente ho scritto:

STEP 13:
def salva_amministratori():
    global amministratori
    with open("amministratori.txt", "w") as f:
        json.dump(amministratori, f, indent=4)
    print("Salvataggio amministratori e lavoratori completato.")

def salva_lavoratori():
    global lavoratori
    with open("lavoratori.txt", "w") as f:
        json.dump(lavoratori, f, indent=4)


STEP 14:
Quando poi è un semplice txt.
Io so usare la gestione dei file su python,anzi sai cosa? penso lo rifarò questa parte,la farò io in formato json.
Infine è pressochè uguale non trovi?!.

def salva_amministratori():
    global amministratori
    with open("amministratore.json", "w") as file:
        file.write(str(amministratori))

def salva_lavoratori():
    global lavoratori
    with open ("lavoratori.json", "w") as file:
        file.write(str(lavoratori))
    print("Salvataggio amministratori e lavoratori completato.")


Ho semplicemente aggiunto che quando viene aperto come file:
scriviamo sottoforma di stringa i dizionari specificati.
L'errore madornale è stato non trasformare prima in stringa il tutto!.




Quindi dopo 2 mesi e mezzo son riuscito a creare ciò:

# TimeBuddy by MC
import json

#Ho creato il dizionario vuoto,dove all'interno metterò nomeutente: password.
amministratori = {}
lavoratori = {}
key = ["TimeBuddyCraNcky"]


def buddy_amministratore():
    global amministratori
    nome_utente = input("Immetti il nome utente che serve per eseguire il Login: ")
    password = input("Immetti la password che servirà per eseguire il Login: ")
    amministratori = {
        "Nome_Utente": nome_utente,
        "Password": password
    }

def buddy_eseguilogin():
    global amministratori
    contatore = 0
    print("Ciao e benvenuto in TimeBuddy, sei attualmente nella sezione Admin, di conseguenza procedi a immettere il tuo nome utente e pass.")
    while True:
        contatore += 1
        verifica_nome_utente = input("Immetti il nome utente: ")
        password = input("Immetti la password: ")
        if amministratori["Nome_Utente"] ==  verifica_nome_utente and amministratori["Password"] == password:
            print("Verifica effettuata.")
            print("Login eseguito correttamente.")
        else:
            print("Nome_utente o password ERRATA!, Riprova.")
            print("Hai solamente 3 tentativi totali!.")
            if contatore >= 3:
                print("La terza volta consecutiva preferiamo chiuderci!.")
                break
        


def buddy_aggiungi_lavoratoreandorari():
    global amministratori
    global lavoratori
    print("Questa è la sezione dove aggiungerai Orario e Lavoratore!.")
    nome_lavoratore = input("Immetti il nome del lavoratore da aggiungere!: ")
    orario_inizio = input(f"immetti a che ora {nome_lavoratore} inizierà a lavorare: ")
    orario_fine = input(f"Immetti a che ora {nome_lavoratore} finisce di lavorare: ")
    lavoratori = {
        "Nome_Lavoratore": nome_lavoratore,
        "Orario_inizio": orario_inizio,
        "Orario_fine": orario_fine
    }
    print(f"Aggiunto al database: {nome_lavoratore} con i rispettivi orari: Inizio: {orario_inizio}, fine: {orario_fine}.")



def buddy_modifica_lavoratore():
    global lavoratori
    while True:
        print("In questa sezione potrai semplicemente modificare un lavoratore!.")
        print("Scrivi 0 per tornare indietro!.")
        verifica_nome = input("Verifichiamo prima se il lavoratore che cerchi esiste: ")
        if verifica_nome == "0":
            print("Uscita...")
            break
        if lavoratori.get("Nome_Lavoratore") == verifica_nome:
            print("Eccolo!, lo abbiamo trovato!.")
            print("1. Elimina")
            print("2. Cambia Nome.")
            print("3. Torna indietro!.")
            scelta = input("Specificaci cosa desideri!: ")

            if scelta == "1":
                lavoratori.clear()
                print("Rimosso con successo")
                print(lavoratori)
            elif scelta == "2":
                nuovo_nome = input("Inserisci il nuovo nome del lavoratore!: ")
                lavoratori["Nome_Lavoratore"] = nuovo_nome
                print("Nome cambiato con successo!.")
            elif scelta == "3":
                print("Chiusura..")
                break
            else:
                print("Opzione non valida!") 
        else:
                print("Nessun lavoratore trovato con questo nome!.")

def salva_amministratori():
    global amministratori
    with open("amministratore.json", "w") as file:
        file.write(str(amministratori))

def salva_lavoratori():
    global lavoratori
    with open ("lavoratori.json", "w") as file:
        file.write(str(lavoratori))
    print("Salvataggio amministratori e lavoratori completato.")



def main():
        print("Scrivi 0 per")
        password = input("immetti la password corretta prima di accedere ad admin: ")
        if password in key:
            print("Password corretta, autenticazione Effettuata!.")
            buddy_amministratore()
            print("Nome utente e password amministratore creati!.")
        else:
            print("Password errata!")
        while True:
            print("Benvenuto in BuddyTime")
            print("\n OPZIONI")
            print("1. Procedi nell'aggiungere lavoratori e i rispettivi orari.")
            print("2. Modifica e rimozione del lavoratore!.")
            print("3. Esci e salva!.")
            print("0. Esci senza salvare...")

            scelta = input("Cosa desideri?: ")
            if scelta == "1":
                buddy_aggiungi_lavoratoreandorari()
            elif scelta == "2":
                buddy_modifica_lavoratore()
            elif scelta == "3":
                salva_amministratori()
                salva_lavoratori()
                break
            elif scelta == "0":
                print("Arrivederci..")
                break

main()




So che non è qualcosa di pazzesco,anzi molto lieve e semplice,ma aggiungerò lo stesso questo esercizio al mio portfolio poichè reputo che sia molto ben strutturato seppur gli errori già citati 
sono:

Errori effettuati:
errore di indentazione.
elementi sconosciuti o errati in questo esercizio:
.clear() (Aiutato da CLAUDE AI)
.get() (Aiutato da CLAUDE AI)
Errore nel salvare i file in json.
Problema nella gestione e modifica di Dizionario,
creazione di un dizionario becero:

amministratori = {
        "Nome_Utente": nome_utente,
        "Password": password
    }

Errato rispetto a come dovrebbe esser creato.

Ho aggiunto anche la possibilità di visualizzare tutti i lavoratori:
def visualizza_lavoratori():
    global lavoratori
    print("Ecco tutti i lavoratori trovati fin'ora: ", lavoratori)



Relativamente semplice.
AL programmino manca ancora molto,ma penso mi fermerò qui limitandomi ad apprendere ancora e ancora.
Mancano in maniera importante:

Nel codice mancano i controlli per gestire diverse eccezioni tipiche.
Questo è solo un prototipo cercando di comprendere se in questi 2 mesi e mezzo ho appreso qualcosa oppure no.
Grazie per aver letto e tenterò di effettuare altri esercizi simili che condividerò senz'altro!.


Errori totali:

Ho chiesto un parere da Claude ai:

1. Architettura dei dati

Il problema più importante è che puoi gestire solo UN amministratore e UN lavoratore alla volta:
# Questo sovrascrive il lavoratore precedente
lavoratori = {
    "Nome_Lavoratore": nome_lavoratore,
    "Orario_inizio": orario_inizio,
    "Orario_fine": orario_fine
}

2. Gestione JSON impropria

pythonfile.write(str(amministratori))  # Questo non è JSON valido
Dovrebbe essere:
pythonjson.dump(amministratori, file, indent=2)

3. Flusso di autenticazione
Il login non viene mai chiamato nel main - l'utente crea credenziali ma non può usarle.


Quindi ricapitolando ecco la mia risposta agli errori maggiori:

Il numero 1, ho capito fin dall'inizio che avrei creato qualcosa a monouso e non continuativo.
Non comprendendo al massimo i dizionari mi confondo facilmente.

Il numero 2, ho preferito strafare e ho mischiato json con il mio modo di modifica di file.
Ripasserò senz'altro.

Il numero 3, non avendo continuato nell'applicazione ovviamente le credenziali usate per un'ipotetico admin non vengono usate.
Se avessi continuato avrei creato tkinter un pannello admin etc etc..

In un ipotetico futuro ricreerò questo esercizio rendendolo funzionale.
Per ora il mio scopo sarà concentrarmi su dizionari e tkinter.

Dove ho usato AI?:
.clear() (Aiutato da CLAUDE AI)
.get() (Aiutato da CLAUDE AI)

Grazie per la comprensione,se hai intravisto altri errori oltre quelli da me riportati,ti prego di spiegarmeli,sono alle prime armi.
