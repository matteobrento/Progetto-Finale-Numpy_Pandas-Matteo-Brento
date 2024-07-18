import pandas as pd
import numpy as np
import random

def genera_valori():

    id_cliente = np.arange(0,20)
    eta = np.random.randint(15, 90, size=20)
    durata_abbonamento = np.random.randint(1, 60, size=20)
    tariffa_mensile = np.random.randint(5,15, size=20)
    dati_consumati = np.random.randint(0, 1000, size=20)
    servizio_clienti_contatti = np.random.randint(0, 10, size=20)
    churn = ["si", "no"]
    churn_df = []
    for i in range(20):
        rinuncia = random.choice(churn)
        churn_df.append(rinuncia)

    return id_cliente, eta, durata_abbonamento, tariffa_mensile, dati_consumati, servizio_clienti_contatti, churn_df

def crea_dataset():

    id_cliente, eta, durata_abbonamento, tariffa_mensile, dati_consumati, servizio_clienti_contatti, churn_df = genera_valori()

    data = {
        "Id":id_cliente,
        "Età":eta,
        "Durata_Abbonamento":durata_abbonamento,
        "Tariffa_Mensile":tariffa_mensile,
        "Dati_Consumati":dati_consumati,
        "Servizio_Clienti_Contatti":servizio_clienti_contatti,
        "Churn":churn_df
    }

    df = pd.DataFrame(data)
    print("DataFrame Iniziale: \n", df.to_string(index=False), "\n")
    return df

def salva_dataframe():
    df = crea_dataset()
    df.to_csv('C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\18.07\\dataframe.csv', index=False)
    print("DataFrame salvato")
    return df

#salva_dataframe()

