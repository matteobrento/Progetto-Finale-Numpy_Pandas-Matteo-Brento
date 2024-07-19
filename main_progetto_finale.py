import progetto_finale as pf
import crea_dataset as cd

def menu():

    print("Menu: ")
    print("1. Distribuzione dei dati ed identificazione dati mancanti")
    print("2. Pulizia dei dati e verifica delle anomalie")
    print("3. Analisi Esplorativa dei Dati (EDA)")
    print("4. Preparazione dati per la modellazione")
    print("5. Visualizzazione grafici")

compagnia = pf.Compagnia_Telefonica()

try:
    df = compagnia.carica_da_csv()
    print("DataFrame Iniziale: \n", df, "\n")
except FileNotFoundError:
    print("Nessun DataFrame caricato. Recuperalo tramite Salvataggio: \n")
    df = cd.salva_dataframe()
    print("DataFrame Iniziale: \n", df, "\n")

compagnia.conversione_valore_categorico_in_numerico()   #converto da categorico a numerico all'inizio così da poter effettuare tutte le operazioni matematiche in tranquillità

while True:

    menu_finale = menu()
    opzione = input("\nScegli l'operazione che desideri effettuare: ") 
    if opzione == "1":
        compagnia.distribuzione_dati()
        compagnia.informazione_dati()
        compagnia.valori_mancanti()
    elif opzione == "2":
        strategia = input("\nInserisci strategia scegliendo tra rimuovi, mean o median: ")
        compagnia.pulizia_dati(strategia)
        compagnia.verifica_anomalie()
        salvataggio = input("\nVuoi salvare il df ? ")
        if salvataggio.lower() == "si":
            compagnia.salva_dataframe_aggiornato()
        else:
            print("\nHai deciso di non salvarlo!")
    elif opzione == "3":
        compagnia.verifica_anomalie()
        compagnia.aggiungi_colonna()
        compagnia.raggruppamento()
        compagnia.correlazione()
        salvataggio = input("\nVuoi salvare il df ? ")
        if salvataggio.lower() == "si":
            compagnia.salva_dataframe_aggiornato()
        else:
            print("Hai deciso di non salvarlo!")
    elif opzione == "4": 
        compagnia.aggiungi_colonna()
        compagnia.normalizzazione()
        salvataggio = input("\nVuoi salvare il df ? ")
        if salvataggio.lower() == "si":
            compagnia.salva_dataframe_aggiornato()
        else:
            print("Hai deciso di non salvarlo!")
    elif opzione == "5":
        compagnia.grafici()
    else:
        print("Scelta non disponibile")

    continua = input("\nVuoi effettuare un'altra operazione? ")   #ripetibilità
    if continua.lower() != "si":
        print("\nArrivederci")
        break