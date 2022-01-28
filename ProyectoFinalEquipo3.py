# -*- coding: utf-8 -*-
"""
@author: the best programing Team
"""

#Paquetes
import pandas as pd
import pandasql as ps
#from urllib.request import urlopen
#import urllib.request
#import requests
import time 
import numpy as np
import re
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt


"""
Creamos los Excel
"""

for tiendas in ["df_sears.xlsx", "df_palacio.xlsx", "df_sanborns.xlsx" ]:
    aux=pd.DataFrame()
    aux.to_excel(tiendas,index=False)


"""
Definimos las funciones
"""
#Definimos las funciones
def Buscador_Precios_Selenium_Sears(producto):
    
    ### ingresamos a la pagina web 
    path ="C:\webdriver3\chromedriver.exe"
    #path= mipath
    driver=webdriver.Chrome(path)
    url= "https://www.sears.com.mx/resultados/q="+producto+"/pagina=1"
    driver.get(url)
    
    ####### Accedemos a los elementos que contienen los datos que queremos de la pagina web 
    

    productos= driver.find_elements_by_class_name("cardProduct")
    #productos[0].text       
    ### accedemos a las urls almacenadas en la variable productos

    lista_urls=list()
    for i in range(len(productos)):
        try:
            lista_urls.append(productos[i].find_element_by_tag_name("a").get_attribute("href"))
        except:
            lista_urls.append(np.nan)
            
    ### accedemos a los nombres de los productos

    lista_nombres=list()
    for i in range(len(productos)):
        try:
            lista_nombres.append(productos[i].find_elements_by_class_name("h4")[0].text)
        except:
            lista_nombres.append(np.nan)
            
            
    ### accedemos a los precios base y promo de los productos 

    lista_precios=list()
    lista_promos=list()
    for i in range(len(productos)):
        try:
            lista_promos.append(np.nan)
        except:
            lista_promos.append(np.nan)
        try:
            lista_precios.append(productos[i].find_elements_by_class_name("precio1")[0].text)
        except:
            lista_precios.append(np.nan)


    df_sears =pd.DataFrame({"nombre":lista_nombres,"url":lista_urls,"precio1":lista_promos,"precio2":lista_precios})
    df_sears["autoservicio"]="sears"
    df_sears["marca"]= producto
    df_sears["fecha"]= time.strftime("%d/%m/%y")

    df_sears = df_sears[["fecha","autoservicio","marca","nombre","url","precio1","precio2"]]
    ## este filtro apenas se agrega

    #df_soriana = df_soriana[df_soriana['nombre'].astype(str).str.contains(r'\b{}\b'.format(producto), regex=True, case=False)]
    df_sears  =df_sears.reset_index(drop=True)


    datos_webscraper=pd.read_excel("df_sears.xlsx")

    datos_webscraper= pd.concat([datos_webscraper,df_sears],axis=0)

    datos_webscraper.to_excel("df_sears.xlsx",index=False)

    driver.quit()
    return df_sears


def Buscador_Precios_Selenium_Sanborns(producto):
    
    ### ingresamos a la pagina web 
    path ="C:\webdriver3\chromedriver.exe"
    #path= mipath
    driver=webdriver.Chrome(path)
    url= "https://www.sanborns.com.mx/resultados/q="+producto
    driver.get(url)
    
    ####### Accedemos a los elementos que contienen los datos que queremos de la pagina web 
    

    productos= driver.find_elements_by_class_name("cardProduct")
    
    
    
    ### accedemos a las urls almacenadas en la variable productos

    lista_urls=list()
    for i in range(len(productos)):
        try:
            lista_urls.append(productos[i].find_element_by_tag_name("a").get_attribute("href"))
        except:
            lista_urls.append(np.nan)
            
    ### accedemos a los nombres de los productos

    lista_nombres=list()
    for i in range(len(productos)):
        try:
            lista_nombres.append(productos[i].find_elements_by_class_name("descrip")[0].text)
        except:
            lista_nombres.append(np.nan)
            
            
    ### accedemos a los precios base y promo de los productos 

    lista_precios=list()
    lista_promos=list()
    for i in range(len(productos)):
        try:
            lista_precios.append(str(productos[i].find_elements_by_class_name("infoDesc")[0].text).split('-')[0])
        except:
            lista_precios.append(np.nan)
        try:
            lista_promos.append(str(productos[i].find_elements_by_class_name("infoDesc")[0].text).split('\n')[1])
        except:
            lista_promos.append(np.nan)





    df_sanborns =pd.DataFrame({"nombre":lista_nombres,"url":lista_urls,"precio1":lista_promos,"precio2":lista_precios})
    df_sanborns["autoservicio"]="sanborns"
    df_sanborns["marca"]= producto
    df_sanborns["fecha"]= time.strftime("%d/%m/%y")

    df_sanborns = df_sanborns[["fecha","autoservicio","marca","nombre","url","precio1","precio2"]]
    ## este filtro apenas se agrega

    #df_soriana = df_soriana[df_soriana['nombre'].astype(str).str.contains(r'\b{}\b'.format(producto), regex=True, case=False)]
    df_sanborns  =df_sanborns.reset_index(drop=True)



    datos_webscraper=pd.read_excel("df_sanborns.xlsx")

    datos_webscraper= pd.concat([datos_webscraper,df_sanborns],axis=0)

    datos_webscraper.to_excel("df_sanborns.xlsx",index=False)

    driver.quit()
    return df_sanborns

def Buscador_Precios_Selenium_Palacio(producto):
    
    ### ingresamos a la pagina web 
    path ="C:\webdriver3\chromedriver.exe"
    #path= mipath
    driver=webdriver.Chrome(path)
    url= "https://www.elpalaciodehierro.com/buscar?q="+producto
    driver.get(url)
    
    ####### Accedemos a los elementos que contienen los datos que queremos de la pagina web 
    

    productos= driver.find_elements_by_class_name("b-product")
    
    ### accedemos a las urls almacenadas en la variable productos

    lista_urls=list()
    for i in range(len(productos)):
        try:
            lista_urls.append(productos[i].find_element_by_tag_name("a").get_attribute("href"))
        except:
            lista_urls.append(np.nan)
            
    ### accedemos a los nombres de los productos

    lista_nombres=list()
    for i in range(len(productos)):
        try:
            lista_nombres.append(productos[i].find_elements_by_class_name("b-product_tile-name")[0].text)
        except:
            lista_nombres.append(np.nan)
            
            
    ### accedemos a los precios base y promo de los productos 

    lista_precios=list()
    lista_promos=list()
    for i in range(len(productos)):
        try:
            lista_promos.append(productos[i].find_elements_by_class_name("b-product_price-sales")[0].text)
        except:
            lista_precios.append(np.nan)
        try:
            lista_precios.append(productos[i].find_elements_by_class_name("b-product_price-value")[0].text)
            
        except:
            lista_promos.append(np.nan)





    df_palacio =pd.DataFrame({"nombre":lista_nombres,"url":lista_urls,"precio1":lista_promos,"precio2":lista_precios})
    df_palacio["autoservicio"]="palacio"
    df_palacio["marca"]= producto
    df_palacio["fecha"]= time.strftime("%d/%m/%y")

    df_palacio = df_palacio[["fecha","autoservicio","marca","nombre","url","precio1","precio2"]]
    ## este filtro apenas se agrega

    #df_soriana = df_soriana[df_soriana['nombre'].astype(str).str.contains(r'\b{}\b'.format(producto), regex=True, case=False)]
    df_palacio  =df_palacio.reset_index(drop=True)



    datos_webscraper = pd.read_excel("df_palacio.xlsx")

    datos_webscraper = pd.concat([datos_webscraper,df_palacio],axis=0)

    datos_webscraper.to_excel("df_palacio.xlsx",index=False)

    driver.quit()
    return df_palacio

def precios_floats_sears(datos):

        
    #### eliminamos el signo de pesos de ambas columnas
    
    for i in range(len(datos["precio1"])):
        try:
            datos["precio1"].iloc[i]=datos["precio1"].iloc[i].strip("$")
            datos["precio1"].iloc[i]=datos["precio1"].iloc[i].strip("MXN")
        except:
            pass
        
    for i in range(len(datos["precio2"])):
        try:
            datos["precio2"].iloc[i]=datos["precio2"].iloc[i].strip("$")
            datos["precio2"].iloc[i]=datos["precio2"].iloc[i].strip("MXN")
        except:
            pass
        
    
    ### quitamos la separacion de comas para miles
    
    datos["precio1"]=datos["precio1"].replace(",","",regex=True)
    datos["precio2"]=datos["precio2"].replace(",","",regex=True)
    
     
        
    ### convertimos los precios a numericos    
    datos['precio1'] = pd.to_numeric(datos['precio1'], errors='coerce')
    datos['precio2'] = pd.to_numeric(datos['precio2'], errors='coerce')

    
    
    datos.to_excel("df_sears_limpio.xlsx",index=False)
        
     ### visualizamos los tipos de datos
    print(datos.dtypes)
    return datos

def precios_floats_sanborns(datos):

        
    #### eliminamos el signo de pesos de ambas columnas
    
    for i in range(len(datos["precio1"])):
        try:
            datos["precio1"].iloc[i]=datos["precio1"].iloc[i].strip("$")
        except:
            pass
        
    for i in range(len(datos["precio2"])):
        try:
            datos["precio2"].iloc[i]=datos["precio2"].iloc[i].strip("$")
        except:
            pass
        
    
    ### quitamos la separacion de comas para miles
    
    datos["precio1"]=datos["precio1"].replace(",","",regex=True)
    datos["precio2"]=datos["precio2"].replace(",","",regex=True)

    
     
        
    ### convertimos los precios a numericos    
    datos['precio1'] = pd.to_numeric(datos['precio1'], errors='coerce')
    datos['precio2'] = pd.to_numeric(datos['precio2'], errors='coerce')
    
    
    
    
    datos.to_excel("df_sanborns_limpio.xlsx",index=False)
        
     ### visualizamos los tipos de datos
    print(datos.dtypes)
    return datos

def precios_floats_palacio(datos):

        
    #### eliminamos el signo de pesos de ambas columnas
    
    for i in range(len(datos["precio1"])):
        try:
            datos["precio1"].iloc[i]=datos["precio1"].iloc[i].strip("$")
        except:
            pass
        
    for i in range(len(datos["precio2"])):
        try:
            datos["precio2"].iloc[i]=datos["precio2"].iloc[i].strip("$")
        except:
            pass
        
    
    ### quitamos la separacion de comas para miles
    
    datos["precio1"]=datos["precio1"].replace(",","",regex=True)
    datos["precio2"]=datos["precio2"].replace(",","",regex=True)
    
     
        
    ### convertimos los precios a numericos    
    datos['precio1'] = pd.to_numeric(datos['precio1'], errors='coerce')
    datos['precio2'] = pd.to_numeric(datos['precio2'], errors='coerce')

    
    
    datos.to_excel("df_palacio_limpio.xlsx",index=False)
        
     ### visualizamos los tipos de datos
    print(datos.dtypes)
    return datos


"""
Hacemos las busquedas de los datos/articulos
"""

for productos in ["celular samsung","pantalla LG","laptop HP"]:
    Buscador_Precios_Selenium_Sanborns(productos)
    Buscador_Precios_Selenium_Sears(productos)
    Buscador_Precios_Selenium_Palacio(productos)
    
 
"""
Checamos DataFrames
"""
    
df_sanborns=pd.read_excel("df_sanborns.xlsx")
df_sanborns

df_palacio=pd.read_excel("df_palacio.xlsx")
df_palacio

df_sears=pd.read_excel("df_sears.xlsx")
df_sears

"""
Conversion de los precios de los DF a int o float
"""

precios_floats_sanborns(df_sanborns)
df_sanborns=pd.read_excel("df_sanborns_limpio.xlsx")
df_sanborns

precios_floats_palacio(df_palacio)
df_palacio=pd.read_excel("df_palacio_limpio.xlsx")
df_palacio


precios_floats_sears(df_sears)
df_sears=pd.read_excel("df_sears_limpio.xlsx")
df_sears


"""
Concatenamos los DF en uno total
"""
df_total = pd.concat([df_sanborns, df_palacio, df_sears], sort = False, ignore_index=True)
df_total
df_total.to_excel("df_total.xlsx", index = False)



'''
Consultas SQL
'''

print(ps.sqldf("select autoservicio, precio1, precio2 from df_total where(autoservicio = 'palacio') and(marca = 'pantalla LG') and precio2 is not null and precio1<11000"))
#Regresa una tabla con pantallas LG de palacio de hierro con precio menor a $11,000

print(ps.sqldf("select count(*) from df_total where(autoservicio = 'sanborns')and Precio2<7000 and (marca = 'celular samsung')"))
#Regresa la cantidad de celulares samsung con precio menos a 7000 de la tienda sears

print(ps.sqldf("select marca,autoservicio, precio2 from df_total where(marca = 'laptop HP') and (autoservicio = 'sanborns') and 15000<precio2"))
#Regresa laptop HP e sanborns con un precio mayor a $15,000

print( ps.sqldf("select autoservicio, nombre, precio1 from df_total where marca = 'celular samsung' order by precio1 desc limit 10"))
#Regresa los 10 celulares más caros con descuento con nombre

print(ps.sqldf("select autoservicio, nombre, precio2 from df_total where marca = 'celular samsung' order by precio2 desc limit 10"))
#Regresa los 10 celulares más caros sin descuento con nombre

print(ps.sqldf("select * from df_total where (marca = 'laptop HP') and (autoservicio = 'sanborns') and precio1 between 20000 and 30000"))
#Regresa los precios de laptop HP de sanborns que estan entre 20000 y 30000 pesos

print(ps.sqldf("select autoservicio, nombre, precio2 from df_total where (marca = 'pantalla LG') order by precio2 desc limit 10"))
#Regresa las 10 pantallas más costosas de los sitios web 


"""
GRAFICAS
"""

#Grafica 1 Nos dice los precios en promedio por artículo tomando en cuenta los 3 sitios web
sql1 = ps.sqldf("select marca as Productos,avg(precio2) as PrecioPromedioDeProductos from df_total group by marca ")
colores1=['lightblue','cornflowerblue','steelblue']
my_plot1 = sql1.plot("Productos", "PrecioPromedioDeProductos", kind="bar",color=colores1,label='Precio Promedio De Productos')
plt.title("Precio promedio en Sanborns, Palacio de Hierro y Sears")
plt.ylabel("Precio en MXN")
plt.xlabel("Productos en los 3 sitios web")
plt.show()
plt.show()



#Gráfica 2 Nos dice por tienda los precios de  una Laptop HP con un costo mayor a $20000
sql2 = ps.sqldf("select marca,autoservicio, precio2 as Precios from df_total where (marca='laptop HP' and precio2>20000) order by precio2")
my_plot2 = sql2.plot("autoservicio", "Precios", kind="bar",color='mediumpurple')
plt.title("Precio de Laptop HP en las tiendas")
plt.ylabel("Precio en MXN")
plt.xlabel("Tiendas")
plt.show()


#Grafica 3 la cantidad de artículos en sanborns esta no me gustó
sql3 = ps.sqldf("select marca as Producto,autoservicio,count(marca) as Artículos from df_total group by marca ")
my_plot3 = sql3.plot("Producto", "Artículos", kind="barh",color=colores1)
plt.title("Artículos en Sanborns")
plt.xlabel("Cantidad de Productos")
plt.text(80,0, "99 celulares")
plt.text(80,1, "67 laptop HP")
plt.text(80,2, "80 pantallas")
plt.show()


#Gráfica 4 precio máximo de Celular sansung por tienda
colores=['darkmagenta','lavenderblush','thistle']
maxPalacio2=ps.sqldf("select marca,autoservicio as Tienda,MAX(precio2) as PrecioMáximo from df_total where (marca='celular samsung') and (autoservicio='palacio')")
maxSears2=ps.sqldf("select marca,autoservicio as Tienda,MAX(precio2) as PrecioMáximo from df_total where (marca='celular samsung') and (autoservicio='sears')")
maxSanborns2=ps.sqldf("select marca,autoservicio as Tienda,MAX(precio2) as PrecioMáximo from df_total where (marca='celular samsung') and (autoservicio='sanborns')")
maxTodos2=pd.concat([maxSears2,maxPalacio2,maxSanborns2])
MAXTODOS2=maxTodos2.plot("Tienda", "PrecioMáximo", kind="barh",color=colores,label='Precio Máximo')
plt.title("Precio máximo de celular Samsung por tienda")
plt.ylabel("Tienda")
plt.xlabel("Precio en MXN")
plt.show()
plt.show()


#Gráfica 5 porcentaje de productos con respecto a tiendas
df_Cel = ps.sqldf("""select precio2 from df_sanborns where marca = 'laptop HP' and precio2 > 6000""")
df_COUNTCel = ps.sqldf("""select COUNT(*) as cantidad from df_Cel """)
y = df_COUNTCel.iloc[0]['cantidad']

lista1 = []

for x in range(y):
    lista1.append(x)
    
lista2 = []

w = 0

for x in range(y):
    w = df_Cel.iloc[x-1]['precio2']
    lista2.append(w)
    
plt.scatter(lista1,lista2,c='darkmagenta')
plt.xlabel("Lugar en la tabla del producto")
plt.ylabel("Precio del Producto")
plt.title("Precios de laptops HP en Sanborns")
plt.show()



















