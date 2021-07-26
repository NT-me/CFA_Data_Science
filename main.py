# %% Import des modules
import pandas as pd

# %% Récupérations de la donnée
rawData = pd.read_csv("dataset/athlete_events.csv")

rawData.describe()

rawData.head()
# %% md
# Données qu'on considère comme ne pouvant pas être null à cause :
# **Du non sens physique**
# - Age
# - Height
# - Weight
# - Sex
# **Pour les besoins du process de traitement**
# - Sport
#
# Au contraire ce que qui peut rester null :
# - Medal
# %% Nettoyage de la donnée
rawData.isnull()

print("Taille pré nettoyage :" + str(len(rawData)))
clearData = clearData.drop_duplicates()
clearData = rawData[(rawData["Height"].isnull() == False) & \
                    (rawData["Age"].isnull() == False) & \
                    (rawData["Weight"].isnull() == False) & \
                    (rawData["Sex"].isnull() == False) & \
                    (rawData["Sport"].isnull() == False)
                    ]
print("Taille post nettoyage :" + str(len(clearData)))
print("Il y'a donc une perte de " + str(len(rawData) - len(clearData)))
clearData.head()
