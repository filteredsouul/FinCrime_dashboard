import pandas as pd
from sqlalchemy import create_engine 

#Connexion SQLite (Création du fichier de la basse de données inexistante)
engine = create_engine('sqlite:///fincrime.db')

#Chargement des dataframes Kaggles
print("Chargement des fichiers CSV ...") 
users = pd.read_csv('/Users/charles-francoisfouti-loemba/Documents/Documents/Projets/FInCrime/data/users.csv')
transactions = pd.read_csv('/Users/charles-francoisfouti-loemba/Documents/Documents/Projets/FInCrime/data/transactions.csv')
fraudsters = pd.read_csv('/Users/charles-francoisfouti-loemba/Documents/Documents/Projets/FInCrime/data/fraudsters.csv')

#Création des tables dans la base de données
print("Insertion dans SQLite ...")
users.to_sql('users', engine, if_exists="replace", index=False)
transactions.to_sql('transactions', engine, if_exists="replace", index=False)
fraudsters.to_sql('fraudsters', engine, if_exists="replace", index=False)

print('Success !')