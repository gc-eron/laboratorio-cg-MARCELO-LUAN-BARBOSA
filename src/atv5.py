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
st.header("3. Máscara por faixa de matiz")
col1, col2 = st.columns(2)

escala = np.zeros((1, 12, 3), dtype=np.uint8)
escala[0, :, 0] = np.arange(0, 180, 15)
escala[0, :, 1] = 255
escala[0, :, 2] = 255

rgb = cv2.cvtColor(escala, cv2.COLOR_HSV2RGB)
col1.image(rgb.repeat(40, axis=0).repeat(40, axis=1), caption="escala")

mascara = cv2.inRange(escala, (90, 0, 0), (130, 255, 255))
col2.image(mascara.repeat(40, axis=0).repeat(40, axis=1), caption="mascara")

st.text(mascara.shape)
st.text(mascara)

h = escala[:, :, 0]
s = escala[:, :, 1]
v = escala[:, :, 2]

dentro = (h >= 90) & (h <= 130) & (s >= 0) & (s <= 255) & (v >= 0) & (v <= 255)

mascara = np.zeros(h.shape, dtype=np.uint8)
mascara[dentro] = 255

h = np.arange(0, 180, 15)

dentro = (h >= 90) & (h <= 130)

mascara = np.zeros(12, dtype=np.uint8)
mascara[dentro] = 255

st.text(mascara)

# 4. Máscara de cor
st.header("4. Máscara de cor")
col1, col2 = st.columns(2)

h_min, h_max = col1.slider("Faixa de H", 0, 179, (140, 179))

mascara = cv2.inRange(hsv, (h_min, 60, 40), (h_max, 255, 255))

col1.image(mascara, caption="Máscara")

so_cor = img.copy()
fora = mascara == 0
so_cor[fora] = 0

col2.image(so_cor, caption="Somente a cor selecionada")

# 5. Recorte
st.header("5. Recorte")
col1, col2 = st.columns(2)

altura, largura = img.shape[0], img.shape[1]

y = col1.slider("y", 0, altura - 1, altura // 4)
x = col1.slider("x", 0, largura - 1, largura // 4)
t = col1.slider("tamanho", 10, min(altura, largura), min(altura, largura) // 3)

recorte = img[y:y + t, x:x + t]

col1.image(recorte, caption="Recorte")
st.text(recorte.shape)

#Negativo dentro da região recortada
nova = img.copy()

regiao = nova[y:y + t, x:x + t]
negativo = 255 - regiao

nova[y:y + t, x:x + t] = negativo

col2.image(nova, caption="Imagem com negativo no recorte")

# 6. Espelhamento
st.header("6. Espelhamento")
col1, col2 = st.columns(2)

#Espelhamento horizontal
horizontal = img[:, ::-1]

col1.image(horizontal, caption="Espelhamento horizontal")

#Espelhamento vertical
vertical = img[::-1, :]

col2.image(vertical, caption="Espelhamento vertical")