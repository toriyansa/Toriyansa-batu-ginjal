import pickle
import streamlit as st

# membaca model
kidney_stone_model =  pickle.load(open('kidney_stone_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Batu Ginjal Berdasarkan Analisa Urin')

gravity = st.text_input('kepadatan urin relatif terhadap air')

ph = st.text_input('logaritma negatif ion hidrogen')

osmo = st.text_input('Osmolaritas sebanding dengan konsentrasi molekul dalam larutan')

cond = st.text_input('Konduktivitas sebanding dengan konsentrasi muatan ion dalam larutan')

urea = st.text_input('konsentrasi urea dalam milimol per liter')

calc = st.text_input('kalsium konsentrasi (CALC) dalam milimol-liter')

# code untuk kelompok jenis bunga
kidney_stone_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    kidney_prediction = kidney_stone_model.predict([[gravity, ph, osmo, cond, urea, calc]])
    
    if(kidney_prediction[0] == 1):
        kidney_stone_diagnosis = 'Pasien mengidap batu ginjal'
    else :
        kidney_stone_diagnosis = 'Pasien tidak mengidap batu ginjal'

    st.success(kidney_stone_diagnosis)
