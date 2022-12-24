import pandas as pd
import streamlit as st
import numpy as np

st.title('Question')
question = pd.read_csv('dataquestionreponse.csv')

print(question.describe())
print(question.head())

i= np.random.randint(0,60)
st.markdown(f"### {question.loc[i]['questions']}")
form = st.form(key='Mes-qyestions')
name = form.text_input('saisir votre réponse')
submit = form.form_submit_button('Submit')

st.write('Appuyer sur entre pour voir la reponse')

if submit:
    st.markdown('## Votre reponse')
    st.markdown(f'*{name}*')
    st.write('## La vraie réponse')
    st.markdown(f"### :green[{question.loc[i]['reponses']}]")
