from turtle import title
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_parques = pd.read_csv('Data/arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('Data/arbolado-publico-lineal-2017-2018.csv')

df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][["altura_tot", "diametro"]].copy()
df_tipas_parques = df_tipas_parques.rename(columns={"altura_tot": "altura", "diametro": "diametro"})
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][["diametro_altura_pecho", "altura_arbol"]].copy()
df_tipas_veredas = df_tipas_veredas.rename(columns={"diametro_altura_pecho": "diametro", "altura_arbol": "altura"})

df_tipas_parques["ambiente"] = "parque"
df_tipas_veredas["ambiente"] = "vereda"

df_tipas = pd.concat([df_tipas_parques, df_tipas_veredas])

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
sns.boxplot(x="ambiente", y="altura", data=df_tipas, ax=ax[0])
sns.boxplot(x="ambiente", y="diametro", data=df_tipas, ax=ax[1])

ax[0].set_title("Altura de las tipas en parques y veredas")
ax[1].set_title("Diámetro de las tipas en parques y veredas")

plt.show()