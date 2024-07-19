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
import matplotlib.pyplot as plt

class Compagnia_Telefonica:

    def __init__(self): #costruttore con self.df impostato a none perchè va ancora caricato
        self.df = None

    def carica_da_csv(self):    #funzione per caricare il csv
        self.file_path = 'C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\18.07\\dataframe.csv'
        self.df = pd.read_csv(self.file_path)
        return self.df

    def distribuzione_dati(self):   #descrizione statistica
        self.descrizione = self.df.describe(include='all')
        print("Distribuzione dati con describe: \n", self.descrizione, "\n")

    def informazione_dati(self):    #info sul dataset
        self.info = self.df.info()
        print("Info: \n", self.info, "\n")

    def valori_mancanti(self):  #is null controlla i valori mancanti per colonna e sum ne restituisce la somma per colonna in output
        self.missing_values = self.df.isnull().sum()
        print("Somma valori mancanti per colonna: \n", self.missing_values, "\n")

    def pulizia_dati(self, strategia):  #strategia è il tipo di operazione che si vuole effettuare per gestire i dati mancanti
        
        if strategia == 'rimuovi':
            self.df = self.df.dropna()  #dropna è la piu drastica perchè rimuove l'intera riga laddove trova un valore mancante
            print("Rimozione delle righe con valore mancante: \n", self.df, "\n")
        elif strategia == 'mean':   #sostituisce i valori mancanti con la media
            self.df.fillna(self.df.mean(), inplace=True)
            print("Sostituzioni dei valori mancanti con la media dei valori in colonna: \n", self.df, "\n")
        elif strategia == 'median': #sostituisce i valori mancanti con la mediana
            self.df.fillna(self.df.median(), inplace=True)
            print("Sostituzioni dei valori mancanti con la mediana dei valori in colonna: \n", self.df, "\n")
        else:
            print("Opzione non valida!")

        print("\nDataframe dopo la pulizia dei dati: \n", self.df, "\n")
        return self.df

    def verifica_anomalie(self):    #restituisce un database che esclude le righe che non rispettano questi parametri
        self.df = self.df[(self.df['Età'] > 0) & (self.df['Età'] <= 100)]
        self.df = self.df[self.df['Tariffa_Mensile'] > 0]
        print("DataFrame dopo la verifica delle anomalie: \n", self.df, "\n")
        return self.df

    def aggiungi_colonna(self): #aggiunge una colonna nuova, costo gb calcolando da altre due colonne già esistenti

        self.df["Costo_per_GB"] = self.df["Tariffa_Mensile"]/self.df["Dati_Consumati"]
        #self.df["Costo_per_GB"] = self.df["Costo_per_GB"].fillna(self.df["Costo_per_GB"].mean())
        print("DataFrame con colonna Costo_per_GB: \n", self.df, "\n")
        return self.df

    def raggruppamento(self):   #raggruppamento per churn ritornando media, mediana e std delle colonne selezionate

        self.raggruppamento = self.df.groupby('Churn').agg({
            'Età': ['mean', 'median', 'std'],
            'Durata_Abbonamento': ['mean', 'median', 'std'],
            'Tariffa_Mensile': ['mean', 'median', 'std']
        })
        print("\nRelazione tra Età, Durata_Abbonamento, Tariffa_Mensile raggruppando per Churn: \n", self.raggruppamento, "\n")

    def conversione_valore_categorico_in_numerico(self):    #1: si, 0: no

        self.df['Churn'] = self.df['Churn'].map(lambda x: 1 if x == 'si' else 0)
        print("Conversione di Churn da Categorico a Numerico: \n", self.df, "\n")
        return self.df

    def correlazione(self): #correlazione

        self.correlazione = self.df.corr()
        print("Correlazione dei dati tramite coefficiente di Pearson tra 1  e -1: \n", self.correlazione, "\n")

    def normalizzazione(self):  #normalizzazione dei valori sulle colonne selezionate

        self.colonne = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Churn', 'Costo_per_GB']
        
        for colonna in self.colonne:
            min_value = self.df[colonna].min()
            max_value = self.df[colonna].max()
            self.df[colonna] = (self.df[colonna] - min_value) / (max_value - min_value)
        
        print("DataFrame con colonne numeriche normalizzate: \n", self.df[self.colonne], "\n")
        return self.df
    
    def grafici(self):  #plot generati con l'utilizzo di matplotlib, i primi due sono grafici a barre che mostrano la distribuzione dei dati della colonna selezionata (Tariffa ed Età)

        plt.figure(figsize=(10,5))
        self.df['Tariffa_Mensile'].plot(kind='bar')
        plt.title('Distribuzione delle Tariffe Mensili')
        plt.xlabel('Indice')
        plt.ylabel('Tariffa Mensile\n')
        plt.show()

        plt.figure(figsize=(10,5))
        self.df['Età'].plot(kind='bar')
        plt.title('Distribuzione delle Età')
        plt.xlabel('Indice')
        plt.ylabel('Età\n')
        plt.show()

        plt.figure(figsize=(10,5))  #questo mostra la relazione tra le due colonne selezionate
        plt.scatter(self.df['Età'], self.df['Tariffa_Mensile'])
        plt.title('Relazione tra Età e Tariffa Mensile')
        plt.xlabel('Età')
        plt.ylabel('Tariffa Mensile')
        plt.show()

    def salva_dataframe_aggiornato(self):   #salvataggio 
        
        self.df.to_csv('C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\18.07\\dataframe_finale.csv', index=False)
        print("DataFrame salvato")
        return self.df


    


   









    

