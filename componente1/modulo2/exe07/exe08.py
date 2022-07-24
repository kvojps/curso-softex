import pandas as pd

df = pd.read_csv("./componente1/modulo2/exe07/notas_alunos.csv")
media = (df["nota_1"] + df["nota_2"]) / 2
df["media"] = media

df.to_csv("./componente1/modulo2/exe07/notas_alunos.csv")

df.loc[df["media"] >= 7 , "situacao"] =  "APROVADO"
df.loc[df["faltas"] <= 5 , "situacao"] =  "APROVADO"
df.loc[df["media"] < 7, "situacao"] = "REPROVADO"
df.loc[df["faltas"] > 5 , "situacao"] =  "REPROVADO"

df.to_csv("./componente1/modulo2/exe07/alunos_situacao.csv")
