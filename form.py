import pandas as pd
import streamlit as st
import numpy as np
import time
st.title("Histoire des faits économiques et sociaux")
question = pd.read_csv('dataquestionreponse.csv')
np.random.seed(0)
i= st.slider('Question No:',0,60,43)
N = np.arange(60)
np.random.shuffle(N)
name = st.text_input(f"{question.loc[N[i]]['questions']}")
if not name:
  st.warning('saisir votre réponse.')
  st.stop()
else:
    st.markdown(f"### :green[{question.loc[N[i]]['reponses']}]")
