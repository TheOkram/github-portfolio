# TimeBuddy by MC
import json
#ps: Studio python da 2 mesi e mezzo,non esser duro.
#Consulta Readme.txt per vedere ogni mio passo.

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
        
def visualizza_lavoratori():
    global lavoratori
    print("Ecco tutti i lavoratori trovati fin'ora: ", lavoratori)

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
            print("3. Visualizza tutti i lavoratori nel database!.")
            print("4. Esci e salva!.")
            print("0. Esci senza salvare...")

            scelta = input("Cosa desideri?: ")
            if scelta == "1":
                buddy_aggiungi_lavoratoreandorari()
            elif scelta == "2":
                buddy_modifica_lavoratore()
            elif scelta == "3":
                visualizza_lavoratori()
            elif scelta == "4":
                salva_amministratori()
                salva_lavoratori()
                break
            elif scelta == "0":
                print("Arrivederci..")
                break

main()
