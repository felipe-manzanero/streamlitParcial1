import pandas as pd

import streamlit as st

dfCalificaciones = pd.read_excel("tareas.xlsx")

dfCalificaciones["promedio"]=(dfCalificaciones["tarea1"]+dfCalificaciones["tarea2"]+dfCalificaciones["tarea3"]+dfCalificaciones["tarea4"])/4

def statusAlumno(promedio):
  if promedio >=70:
    return "APROBADO"
  else:
    return "REPROBADO"

dfResultados = dfCalificaciones[['matricula','promedio','status']]

dfResultados

st.dataframe(dfResultados)
