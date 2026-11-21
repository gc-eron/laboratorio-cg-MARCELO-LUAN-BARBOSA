
import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/poster.jpg")
img = np.array(foto)

st.header("4. Tons de cinza")

col1, col2 = st.columns(2)

r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)

#Média simples
media = ((r + g + b) / 3).astype(np.uint8)

col1.subheader("Média simples")
col1.image(media, caption="Tons de cinza")

#Média ponderada
col2.subheader("Média ponderada")

peso_r = col2.slider("Peso do vermelho", 0.0, 1.0, 0.299)
peso_g = col2.slider("Peso do verde", 0.0, 1.0, 0.587)
peso_b = col2.slider("Peso do azul", 0.0, 1.0, 0.114)

ponderada = (r * peso_r + g * peso_g + b * peso_b)
ponderada = np.clip(ponderada, 0, 255).astype(np.uint8)

col2.image(ponderada, caption="Tons de cinza ponderados")


st.header("5. Canais")

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

col1, col2, col3 = st.columns(3)

col1.subheader("Vermelho")
col1.image(r, caption="Canal R")

col2.subheader("Verde")
col2.image(g, caption="Canal G")

col3.subheader("Azul")
col3.image(b, caption="Canal B")

st.subheader("Visualizar canal colorido")

canal = st.selectbox("Escolha um canal", ["Vermelho", "Verde", "Azul"])

cor = np.zeros(img.shape, dtype=np.uint8)

if canal == "Vermelho":
    cor[:, :, 0] = r
elif canal == "Verde":
    cor[:, :, 1] = g
else:
    cor[:, :, 2] = b

st.image(cor, caption="Canal selecionado")

st.header("8. Negativo")

negativo = 255 - img

st.image(negativo, caption="Imagem em negativo")

st.header("11. Espelhamento")

col1, col2 = st.columns(2)

horizontal = img[:, ::-1]
vertical = img[::-1, :]

col1.subheader("Espelhamento horizontal")
col1.image(horizontal)

col2.subheader("Espelhamento vertical")
col2.image(vertical)

st.header("12. Simetria")

altura, largura = img.shape[0], img.shape[1]

metade = largura // 2

lado = img[:, :metade]

lado_espelhado = lado[:, ::-1]

simetria = img.copy()

simetria[:, largura - metade:] = lado_espelhado

st.image(simetria, caption="Imagem com simetria")

