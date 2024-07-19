import progetto_finale as pf
import crea_dataset as cd

def menu():

    print("Menu: ")
    print("1. Distribuzione dei dati ed identificazione dati mancanti")
    print("2. Pulizia dei dati e verifica delle anomalie")
    print("3. Analisi Esplorativa dei Dati (EDA)")
    print("4. Preparazione dati per la modellazione")

compagnia = pf.Compagnia_Telefonica()

try:
    df = compagnia.carica_da_csv()
    print("DataFrame Iniziale: \n", df, "\n")
except FileNotFoundError:
    print("Nessun DataFrame caricato. Recuperalo tramite Salvataggio: \n")
    df = cd.salva_dataframe()

while True:

    menu_finale = menu()
    opzione = input("\nScegli l'operazione che desideri effettuare: ") 
    if opzione == "1":
        compagnia.distribuzione_dati()
        compagnia.informazione_dati()
        compagnia.valori_mancanti()
    elif opzione == "2":
        compagnia.conversione_valore_categorico_in_numerico()
        strategia = input("\nInserisci strategia scegliendo tra rimuovi, mean o median: ")
        compagnia.pulizia_dati(strategia)
        compagnia.verifica_anomalie()
    elif opzione == "3":
        compagnia.verifica_anomalie()
        compagnia.aggiungi_colonna()
        compagnia.raggruppamento()
        compagnia.correlazione()
    elif opzione == "4": 
        compagnia.normalizzazione()
    else:
        print("Scelta non disponibile")

    continua = input("\nVuoi effettuare un'altra operazione? ")   #ripetibilità
    if continua.lower() != "si":
        print("\nArrivederci")
        break