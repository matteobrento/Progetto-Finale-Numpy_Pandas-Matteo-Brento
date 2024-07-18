# Progetto-Finale-Numpy_Pandas-Matteo-Brento
Caso di studio aziendale utilizzando Numpy e Pandas con documentazione.
Documentazione Numpy: https://numpy.org/doc/stable/
Documentazione Pandas: https://pandas.pydata.org/docs/

# Organizzazione del lavoro
Dopo l'importazione del csv del DataFrame, intendo procedere con il punto 1 così da avere una descrizione accurata del DataFrame con cui sto lavorando. 
Pertanto procedo in ordine così come le task sono distribuite.
Suddivisione in funzioni e moduli.

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
Il secondo modulo, 'progetto_finale.py', crea innanzitutto un metodo 'carica_da_csv' per fare un read del dataset generato. Dopodichè nelle varie funzioni sono eseguite tutte le task richieste nella traccia.
Il terzo modulo, 'main_progetto_finale.py', richiama al suo interno i due moduli precedenti. Dopodichè con effettua un controllo dell'esistenza del file csv da inserire in df. Se non lo trova (impossibile perchè il percorso è giusto), va in except, utilizzando salva_dataframe del primo modulo per prelevare un altro df generato casualmente.
Il file 'dataframe.csv' è la base di appoggio per il salvataggio e il caricamento del dataset.






