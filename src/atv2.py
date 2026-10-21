import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira do Reino Unido")

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:] = (1, 33, 105)  # fundo azul

for i in range(12):
    bandeira[i, i:i+3] = (255, 255, 255)
    bandeira[i, 17-i-2:17-i+1] = (255, 255, 255)

bandeira[4:8, :] = (255, 255, 255)
bandeira[:, 7:11] = (255, 255, 255)

bandeira[5:7, :] = (200, 16, 46)
bandeira[:, 8:10] = (200, 16, 46)

for i in range(12):
    bandeira[i, i+1:i+2] = (200, 16, 46)
    bandeira[i, 16-i:17-i] = (200, 16, 46)

st.image(ampliar(bandeira))
