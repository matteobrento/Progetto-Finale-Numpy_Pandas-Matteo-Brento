import progetto_finale as pf
import crea_dataset as cd

def menu():

    print("Menu: ")
    print("1. Distribuzione dei dati ed identificazione dati mancanti")
    print("2. Pulizia dei dati e verifica delle anomalie")
    print("3. Analisi Esplorativa dei Dati (EDA)")
    print("4. Preparazione dati per la modellazione")

try:
    df = pf.carica_da_csv()
except:
    df = cd.salva_dataframe()

while True:

    menu_finale = menu()
    opzione = input("\nScegli l'operazione che desideri effettuare: ") 
    if opzione == "1":
        pf.distribuzione_dati(df)
        pf.informazione_dati(df)
        pf.valori_mancanti(df)
    elif opzione == "2":
        pf.pulizia_dati(df)
        print("\nDataFrame senza anomalie: \n")
        print(pf.verifica_anomalie(df))
    elif opzione == "3":
        df_senza_anomalie = pf.verifica_anomalie(df)
        print("\nDataFrame con colonna aggiunta: \n")
        print(pf.aggiungi_colonna(df_senza_anomalie))
        df = pf.aggiungi_colonna(df_senza_anomalie)
        pf.raggruppamento(df)
        df = pf.conversione_valore_categorico_in_numerico(df)
        pf.correlazione(df)
    elif opzione == "4": 
        print("\nDataFrame con conversione di valori categorici in numerici (Churn): \n")
        print(pf.conversione_valore_categorico_in_numerico(df))
    else:
        print("Scelta non disponibile")

    continua = input("Vuoi effettuare un'altra operazione? ")   #ripetibilità
    if continua.lower() != "si":
        print("\nArrivederci")
        break