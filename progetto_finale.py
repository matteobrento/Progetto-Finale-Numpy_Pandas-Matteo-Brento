"""
Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà.

Dataset: 

ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)

Caricamento e Esplorazione Iniziale:
Caricare i dati da un file CSV.
Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con
valori mancanti.
Pulizia dei Dati:
Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
Analisi Esplorativa dei Dati (EDA):
Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
Preparazione dei Dati per la Modellazione:
Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
Analisi Statistica e Predittiva:
Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
su altri fattori.
Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve).
"""

import pandas as pd
import numpy as np

def carica_da_csv():
    file_path = 'C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\18.07\\dataframe.csv'
    df = pd.read_csv(file_path)
    return df

df = carica_da_csv()

def distribuzione_dati(df):
    descrizione = df.describe(include='all')
    print("Distribuzione dati con describe: \n", descrizione, "\n")

def informazione_dati(df):
    info = df.info()
    print("Info: \n", info, "\n")

def valori_mancanti(df):
    missing_values = df.isnull().sum()
    print("Valori mancanti per colonna: \n", missing_values, "\n")

def pulizia_dati(df):
    df_cleaned = df.dropna()
    print("Rimozione delle righe dove almeno un elemento è mancante: \n", df_cleaned, "\n")
    return df_cleaned

def verifica_anomalie(df):
    df = df[(df['Età'] > 0) & (df['Età'] <= 100)]
    df = df[df['Tariffa_Mensile'] > 0]
    return df

df_senza_anomalie = verifica_anomalie(df)
print("Dataset dopo la correzione delle anomalie: \n", df_senza_anomalie, "\n")


def aggiungi_colonna(df_senza_anomalie):

    df_senza_anomalie["Costo_per_GB"] = df_senza_anomalie["Tariffa_Mensile"]//df_senza_anomalie["Dati_Consumati"]
    print("DataFrame con colonna Costo_per_GB: \n", df_senza_anomalie, "\n")
    return df_senza_anomalie

df = aggiungi_colonna()





















""" 
distribuzione_dati(df)
informazione_dati(df)
valori_mancanti(df)
pulizia_dati(df) 
"""








    

