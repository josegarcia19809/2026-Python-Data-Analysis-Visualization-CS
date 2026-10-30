import pandas as pd

datos = {
    "Sexo": ["Niños", "Niñas"],
    "Buenas_calificaciones": [117, 130],
    "Popularidad": [50, 91],
    "Deportes": [60, 30]
}

df = pd.DataFrame(datos)

df["Total"] = df[
    ["Buenas_calificaciones", "Popularidad", "Deportes"]
].sum(axis=1)

# Agregar los totales generales
totales = df.select_dtypes(include="number").sum()
totales["Sexo"] = "Total"

df.loc[len(df)] = totales

# Guardar el dataset
df.to_csv("../data/objetivos_estudiantes.csv", index=False)

print(df)