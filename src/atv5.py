import cv2
import numpy as np
import streamlit as st
from PIL import Image
st.title("Atv 5: HSV e recorte")
foto = Image.open("imagens/poster.jpg")
img = np.array(foto)

# 1. HSV
st.header("1. HSV")
col1, col2 = st.columns(2)

# Imagem original
col1.image(img, caption="Imagem original")

# Conversão para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# Exibindo apenas o canal H
so_h = hsv.copy()
so_h[:, :, 1] = 255
so_h[:, :, 2] = 255

rgb = cv2.cvtColor(so_h, cv2.COLOR_HSV2RGB)

col2.image(rgb, caption="Imagem HSV (canal H)")

# 2. Mudando o HSV
st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)

# 3. Faixa na escala
st.header("3. Faixa na escala")
col1, col2 = st.columns(2)

# 4. Máscara de cor
st.header("4. Máscara de cor")
col1, col2 = st.columns(2)

# 5. Recorte
st.header("5. Recorte")
col1, col2 = st.columns(2)

# 6. Espelhamento
st.header("6. Espelhamento")
col1, col2 = st.columns(2)