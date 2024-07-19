# Progetto-Finale-Numpy_Pandas-Matteo-Brento
Caso di studio aziendale utilizzando Numpy e Pandas con documentazione.
Documentazione Numpy: https://numpy.org/doc/stable/
Documentazione Pandas: https://pandas.pydata.org/docs/

# Organizzazione del lavoro
Dopo l'importazione del csv del DataFrame, intendo procedere con il punto 1 così da avere una descrizione accurata del DataFrame con cui sto lavorando. 
Pertanto procedo in ordine così come le task sono distribuite.
Suddivisione in funzioni, classi e moduli.

# Gestione dei tempi
Analisi Funzionale: 10min
Considero un tempo complessivo di 2 ore, per esaminare e testare in modo approfondito tutte le task, prima di passare all'automatizzazione del sistema.
Automatizzazione del sistema: 1 ora.
Previsioni dei tempi prima dell'inizio: 
Tempo Task1 : 10min  (Se il df è da importare, altrimenti 20min)
Tempo Task2 : 20min
Tempo Task 3: 30min
Tempo Task 4: 30min
Tempo Task 5: 40min  (Punto facoltativo, ma voglio provare a realizzarlo)

# Analisi del lavoro
Ho deciso di suddividere il mio codice in moduli. 
Il primo modulo, 'crea_dataset.py', verte sulla generazione dei valori di riempimento del dataset, la creazione del dataset e il salvataggio di quest'ultimo su un file 'dataframe.csv'.
Il secondo modulo, 'progetto_finale.py', crea una classe principale Compagnia_Telefonica. All'interno crea il costruttore e successivamente un metodo 'carica_da_csv' per fare un read del dataset generato. Dopodichè nelle varie funzioni sono eseguite tutte le task richieste nella traccia.
Sono stati utilizzati diversi metodi numpy in combinazione con random per garantire randomicità dei dati nel dataset, per la generazione dei valori. Pandas è stato utilizzato per gestire invece tutte le operazioni delle task richieste come descrizione del dataset, pulizia dei dati, operazioni avanzate di raggruppamento e correlazione e normalizzazione dei dati.
Inoltre ho aggiunto un metodo nel modulo che permette il salvataggio (su scelta nel menu) in un file.csv nuovo, così da avere una panoramica del csv iniziale e di quello lavorato.
Nel codice c'è un piccolo accenno di matplotlib per la visualizzazione di plot della distribuzione dei dati.
Il terzo modulo, 'main_progetto_finale.py', richiama al suo interno i due moduli precedenti. Dopodichè effettua un controllo dell'esistenza del file csv da inserire in df. Se non lo trova (impossibile perchè il percorso è giusto), va in except, utilizzando salva_dataframe del primo modulo per prelevare un altro df generato casualmente.
Il file 'dataframe.csv' è la base di appoggio per il salvataggio e il caricamento del dataset.






