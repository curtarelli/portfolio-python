##  Importando os pacotes necessários para a rotina
import numpy as np
from sklearn import cluster
from osgeo import gdal, gdal_array
import matplotlib.pyplot as plt

##  Dizendo ao GDAL para registrar todas as exceções do Python
gdal.UseExceptions()
gdal.AllRegister()

##  Abrindo as imagens raster
dir_img = gdal.Open(r'D:\prog\master_py37\K_Means\input\utm_mask_T23KMV_20190701T131251_B02.TIF', gdal.GA_ReadOnly)
img = dir_img.ReadAsArray()

##  Shape da imagem
print(img.shape(1))

##
img_reshape = img.reshape((-1, 1))

img_reshape = img_reshape

##  Aplicando K MÉDIAS para "N" classes (n_clusters), seguindo para o ajuste na imagem da banda normalizada
k_means = cluster.KMeans(n_clusters = 10)
k_means.fit(img_reshape)

##  Adicionando rótulos e voltando a imagem ao shape original
img_cluster = k_means.labels_
img_cluster = img_cluster.reshape(img.shape)

plt.figure(figsize = (20, 20))
plt.imshow(img_cluster, cmap = 'hsv')
plt.show()
