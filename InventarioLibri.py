inventario = []
while True:
    print("Cosa scegli?")
    print("1. Aggiungi un libro, l'autore e le pagine.")
    print("2. Visualizza inventario.")
    print("3. Cerca libri per Autore.")
    print("4. Calcola il numero totale di pagine nell'inventario.")
    print("5. Salva e carica l'inventario da un file di testo.")
    scelta = input("Immetti cosa cerchi: ")
    if scelta == "1":
        nome_del_libro = input("Immetti il nome del tuo libro da aggiungere: ")
        nome_del_autore = input("Immetti il nome dell'autore: ")
        pagine = int(input("Quante pagine ci sono?: "))
        inventario.append({"titolo": nome_del_libro, "autore": nome_del_autore, "pagine": pagine})
        print(f"Aggiunto {nome_del_libro} all'inventario.")
    elif scelta == "2":
        for libro in inventario:
            print(f"Titolo: {libro['titolo']}, Autore: {libro['autore']}, Pagine: {libro['pagine']}")
    elif scelta == "3":
        cerca = input("Cosa intendi cercare, immetti il nome del tuo autore: ")
        for libro in inventario:
            if libro["autore"] == cerca:
                print(f"Titolo: {libro['titolo']}, Autore: {libro['autore']}, Pagine: {libro['pagine']}")
                break
        else:
            print("Il tuo libro non è nell'inventario!.")
    elif scelta == "4":
        totale_pagine = sum(libro["pagine"] for libro in inventario)
        print(f"Il numero totale di pagine nell'inventario è: {totale_pagine}")
    elif scelta == "5":
        # Implementazione del salvataggio e caricamento da file
        pass  # Da implementare
    else:
        print("Scelta non valida.")