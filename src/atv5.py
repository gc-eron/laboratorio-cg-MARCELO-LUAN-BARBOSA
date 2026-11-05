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


col1.image(img, caption="Imagem original")

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

so_h = hsv.copy()
so_h[:, :, 1] = 255
so_h[:, :, 2] = 255

rgb = cv2.cvtColor(so_h, cv2.COLOR_HSV2RGB)

col2.image(rgb, caption="Imagem HSV (canal H)")

# 2. Mudando o HSV
st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)

fator = col1.slider("Saturação", 0.0, 2.0, 1.0)

s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s.astype(np.uint8)

col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))

fator_brilho = col1.slider("Brilho", 0.0, 2.0, 1.0)

v = hsv[:, :, 2].astype(float)
v = v * fator_brilho
v = np.clip(v, 0, 255)
hsv3 = hsv.copy()
hsv3[:, :, 2] = v.astype(np.uint8)

col1.image(cv2.cvtColor(hsv3, cv2.COLOR_HSV2RGB))

giro = col2.slider("Giro (graus)", 0, 360, 120)

h = hsv[:, :, 0].astype(float)
h = (h + giro / 2) % 180
hsv4 = hsv.copy()
hsv4[:, :, 0] = h.astype(np.uint8)
girada = cv2.cvtColor(hsv4, cv2.COLOR_HSV2RGB)

col2.image(girada)

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