# %% Import des modules
import pandas as pd
import matplotlib.pyplot as plt


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
clearData = rawData[(rawData["Height"].isnull() == False) & \
                    (rawData["Age"].isnull() == False) & \
                    (rawData["Weight"].isnull() == False) & \
                    (rawData["Sex"].isnull() == False) & \
                    (rawData["Sport"].isnull() == False)
                    ]
clearData = clearData.drop_duplicates()
print("Taille post nettoyage :" + str(len(clearData)))
print("Il y'a donc une perte de " + str(len(rawData) - len(clearData)))
clearData.head()




#%%%
# Normalisation des données

# %%

plt.hist(clearData["Height"], bins=100, label=['Taille'])
plt.legend(loc="upper right")
plt.show()

#normalisation de la taille 
clearData["Height"]=((clearData["Height"]-clearData["Height"].min())/(clearData["Height"].max()-clearData["Height"].min()))*1

plt.hist(clearData["Height"], bins=100, label=['Taille'])
plt.legend(loc="upper right")
plt.show()

# %%



plt.hist(clearData["Weight"], bins=100, label=['Poids'])
plt.legend(loc="upper right")
plt.show()

#normalisation du poids 
clearData["Weight"]=((clearData["Weight"]-clearData["Weight"].min())/(clearData["Weight"].max()-clearData["Weight"].min()))*1

plt.hist(clearData["Weight"], bins=100, label=['Poids'])
plt.legend(loc="upper right")
plt.show()
# %%




plt.hist(clearData["Age"], bins=60, label=['Age'])
plt.legend(loc="upper right")
plt.show()

#normalisation de l'age 
clearData["Age"]=((clearData["Age"]-clearData["Age"].min())/(clearData["Age"].max()-clearData["Age"].min()))*1

plt.hist(clearData["Age"], bins=60, label=['Age'])
plt.legend(loc="upper right")
plt.show()

# %%
