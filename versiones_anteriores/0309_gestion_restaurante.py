import os
import random
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import pprint
import sqlite3
import ast
import re
from PIL import ImageTk, Image

import json 

"""
MAQUETACION ----> OKKKKKK!!!!!!
    - Submenus - Comida, bebidas, postres
    - checkbox - Label_titulos - entrys

LIMPIEZA DE CODIGO (variables) -----> OKKKKKKK!!!!!!

FUNCIONALIDAD
    - 5 botones
        BORRAR          -> (resetea el menu) ------> OKKKKKK!!!!!
        ALTA            -> (alta de registro - acepta pedido en bd)
        BAJA            -> (baja de registro - borra pedido en bd)
        CONSULTA        -> (permite la consulta de un registro en bd)
        MODIFICACION    -> (Modificacion y ajuste de un registro)
        
    - BASE DE DATOS
        Crear base de datos
        Crear tabla (id, mesa, pedido, total)
        
    - CALCULA PRECIOS
        Calcular el total del pedido completo y mostrarlo en pantalla -----> OKKKKK!!!!!
        
    - MENU
        Checkbox NO VA!!!!!!
        Entry cantidad (error si ponen una letra - regex) ----> FALTA

DOCUMENTACION
    - Rellenar tablas de tamaños - colores 
    - Diagrama y maquetacion final de la interfaz
    - Division de modelo, vista, controlador
    - Archivo READ ME
================== BASE DE DATOS ===================
ID --- MESA --- PEDIDO --- TOTAL
01      2       ...       $2000
02      1
03      3
04      4
05      5
        6
        7
        8
        9
        10
""" 


""" 
Restaria: 
    - Alinear comida con el box del entry
    - Mensajes en panel var_notificación
    - Scroll bar ( ver funcionamiento )
    - Validar mesa si existe previamente en bbdd.
    - Validar en alta si la mesa fue seleccionada previamente
    - Al apretar "modificar" que salga emergente (message.box) de "are you sure"? Con Y/N.
    - crear tabla con flag por primera vez
"""

mesa = 0
id_db_global = 0
#flag = 0

# FUNCIONES DE BD ==============================================================

def create_open_db(path):
    fd = sqlite3.connect(path)
    return fd


def close_db(fd):
    fd.close()
    exit()

def create_table_db(fd): 
    cursor = fd.cursor()
    sql = f"CREATE TABLE sisgesres(id INTEGER PRIMARY KEY AUTOINCREMENT, mesa INTEGER NOT NULL, pedido TEXT, total INTEGER NOT NULL)"

    #if not tables_exist(cursor, table_name="sisgesres"):
    cursor.execute(sql)
    fd.commit()
    
def elegir_mesa(aux):
    global mesa
    mesa = aux
    var_notificacion.set("Mesa " + str(mesa))

def alta_db(fd):
    
    cursor = fd.cursor()
    sql = f"INSERT INTO sisgesres(mesa, pedido, total) VALUES(?, ?, ?);"
    global mesa
    global diccionario
    global suma
    datos = (int(mesa), str(diccionario), int(suma))

    cursor.execute(sql, datos)
    fd.commit()
    consulta_db(fd)


def consulta_db(fd):
    #limpiar treeview
    for row in grilla.get_children():
        grilla.delete(row) 
    cursor = fd.cursor()
    cursor.execute("SELECT * FROM sisgesres")
    rows = cursor.fetchall()
    for row in rows:
        grilla.insert('', 'end', text=row[0], values=(row[1], row[2], row[3]))

def consulta_particular (grilla):
   # global diccionario 
    global id_db_global
    valor = grilla.selection()[0]
    row = grilla.item(valor)
    print(f"\nPrint 114 -> {row}")
    id_db = row['text']
    print(f"\nPrint 116 -> {id_db}")
    print(f"\nPrint 117 -> {type(ast.literal_eval(row['values'][1]))}")
    #seleccion = {}
    var_notificacion.set(f"La mesa seleccionada es: {row['values'][0]}")
    for keys, values in (ast.literal_eval(row['values'][1])).items():
        #if valores[0] != 0:
        #seleccion.update({keys : valores})
        #print(f"\n\nDICCIONARIO DE SELECCION -> {seleccion}")
        if keys == "pollo":
            var_comida1.set(values[0])
        elif keys == "carne":
            var_comida2.set(values[0])
        elif keys == "canelones":
            var_comida3.set(values[0])
        elif keys == "lasagna":
            var_comida4.set(values[0])
        elif keys == "tortilla":
            var_comida5.set(values[0])
        elif keys == "vino":
            var_bebida1.set(values[0])
        elif keys == "coca":
            var_bebida2.set(values[0])
        elif keys == "limonada":
            var_bebida3.set(values[0])
        elif keys == "agua_sg":
            var_bebida4.set(values[0])
        elif keys == "jugo":
            var_bebida5.set(values[0])
        elif keys == "brownie":          
            var_postre1.set(values[0])
        elif keys == "torta":
            var_postre2.set(values[0])
        elif keys == "flan":
            var_postre3.set(values[0])
        elif keys == "helado":
            var_postre4.set(values[0])
        elif keys == "tiramisu":
            var_postre5.set(values[0])

    id_db_global = id_db
    return id_db_global

def baja_db(fd, grilla):
    valor = grilla.selection()[0]
    row = grilla.item(valor)
    print(row)
    id_db = row['text']
    print(id_db)
    cursor = fd.cursor()
    data = (id_db, )
    sql = "DELETE FROM sisgesres WHERE id = ?;"
    cursor.execute(sql, data)
    fd.commit()
    grilla.delete(valor)

def modificar_db(fd):
    global id_db_global
    cursor = fd.cursor()
    sql = f"UPDATE sisgesres SET pedido = ?, total = ? WHERE id = ?;"
    datos = (str(diccionario), int(suma), int(id_db_global))
    cursor.execute(sql, datos)
    fd.commit()
    consulta_db(fd_base)
    
# FUNCIONES DE BD ==============================================================
"""
def table_exists(cursor, table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None
"""



# PALETA 1
c_hueso = "#F8FAE5"
c_marron_claro = "#B19470"
c_marron = "#3a2313"
c_naranja = "#f6951e"
c_marron_osc = "#282222"

suma = 0

diccionario = {}


# ================================= FUNCIONES ======================================================


# --------------------------------- FUNCIONES BASE DE DATOS ---------------------------------------


# ---------------------------------- FUNCIONES ENTRY ----------------------------------------------


def toma_valor():
    global diccionario
    diccionario.update({"pollo" : [0, 4000]}) if var_comida1.get() == "" else diccionario.update({"pollo" : [int(var_comida1.get()), 4000]})
    diccionario.update({"carne" : [0, 4500]}) if var_comida2.get() == "" else diccionario.update({"carne" : [int(var_comida2.get()), 4500]})
    diccionario.update({"canelones" : [0, 2800]}) if var_comida3.get() == "" else diccionario.update({"canelones" : [int(var_comida3.get()), 2800]})
    diccionario.update({"lasagna" : [0, 2500]}) if var_comida4.get() == "" else diccionario.update({"lasagna" : [int(var_comida4.get()), 2500]})
    diccionario.update({"tortilla" : [0, 1000]}) if var_comida5.get() == "" else diccionario.update({"tortilla" : [int(var_comida5.get()), 1000]})
    diccionario.update({"vino" : [0, 2800]}) if var_bebida1.get() == "" else diccionario.update({"vino" : [int(var_bebida1.get()), 2800]})
    diccionario.update({"coca" : [0, 2200]}) if var_bebida2.get() == "" else diccionario.update({"coca" : [int(var_bebida2.get()), 2200]})
    diccionario.update({"limonada" : [0, 1400]}) if var_bebida3.get() == "" else diccionario.update({"limonada" : [int(var_bebida3.get()), 1400]})
    diccionario.update({"agua_sg" : [0, 800]}) if var_bebida4.get() == "" else diccionario.update({"agua_sg" : [int(var_bebida4.get()), 800]})
    diccionario.update({"jugo" : [0, 950]}) if var_bebida5.get() == "" else diccionario.update({"jugo" : [int(var_bebida5.get()), 950]})
    diccionario.update({"brownie" : [0, 800]}) if var_postre1.get() == "" else diccionario.update({"brownie" : [int(var_postre1.get()), 800]})
    diccionario.update({"torta" : [0, 1800]}) if var_postre2.get() == "" else diccionario.update({"torta" : [int(var_postre2.get()), 1800]})
    diccionario.update({"flan" : [0, 1200]}) if var_postre3.get() == "" else diccionario.update({"flan" : [int(var_postre3.get()), 1200]})
    diccionario.update({"helado" : [0, 2500]}) if var_postre4.get() == "" else diccionario.update({"helado" : [int(var_postre4.get()), 2500]})
    diccionario.update({"tiramisu" : [0, 3500]}) if var_postre5.get() == "" else diccionario.update({"tiramisu" : [int(var_postre5.get()), 3500]})
    return diccionario


def calcular():
    global suma
    suma = 0
    toma_valor()
    for cant, prec in diccionario.values():
        suma += cant * prec
        pantalla_registro.config(text="Precio en pantalla")
    suma_total_var.set("".join('$' + str(suma)))


def reset_menu():
    var_comida1.set("")
    var_comida2.set("")
    var_comida3.set("")
    var_comida4.set("")
    var_comida5.set("")
    var_bebida1.set("")
    var_bebida2.set("")
    var_bebida3.set("")
    var_bebida4.set("")
    var_bebida5.set("")
    var_postre1.set("")
    var_postre2.set("")
    var_postre3.set("")
    var_postre4.set("")
    var_postre5.set("")
    suma_total_var.set("$0")

    global suma
    suma = 0
    var_notificacion.set("Borrón y cuenta nueva!")
  
# Función para validar la entrada
def validar_entrada(P):
    # Patrón regex para permitir solo números
    #patron = r'^[0-9]*$'
    patron = r'\d'
    if re.match(patron, P):
        return True
    elif P == "":
        return True
    else:
        return False

# =============================== COMIENZO DEL PROGRAMA ===========================================
    
main0 = tk.Tk()
main0.geometry("1366x768")
main0.resizable(0,0)
main0.title("Gestor de comidas v 1.0")

path_img2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs", "fondo_app2.jpg")
imagen = Image.open(path_img2)
imagen_f = ImageTk.PhotoImage(imagen)
imagen_fondo = tk.Label(main0, image=imagen_f)
imagen_fondo.place(x=0, y=0)
#main0.config(bg=c_marron)


name_base = "sisgesresdb.db"
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "base_de_datos", name_base)
path_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs", "favicom.ico")
fd_base = create_open_db(path)
main0.iconbitmap(path_img)

#create_table_db(fd_base)

#Ejecucion de la funcion de validacion de entrada para no permitir letras
vcmd = (main0.register(validar_entrada), '%P')

# Solapa Comandos

barra_menu = tk.Menu(main0)
var_notificacion = tk.StringVar()
solapa_mesa = tk.Menu(barra_menu, tearoff=0)
solapa_mesa.add_command(label="1", command= lambda : elegir_mesa(aux=1))
solapa_mesa.add_command(label="2", command= lambda : elegir_mesa(aux=2))
solapa_mesa.add_command(label="3", command= lambda : elegir_mesa(aux=3))
solapa_mesa.add_command(label="4", command= lambda : elegir_mesa(aux=4))
solapa_mesa.add_command(label="5", command= lambda : elegir_mesa(aux=5))
solapa_mesa.add_command(label="6", command= lambda : elegir_mesa(aux=6))
solapa_mesa.add_command(label="7", command= lambda : elegir_mesa(aux=7))
solapa_mesa.add_command(label="8", command= lambda : elegir_mesa(aux=8)) 
solapa_mesa.add_command(label="9", command= lambda : elegir_mesa(aux=9))
solapa_mesa.add_command(label="10", command= lambda : elegir_mesa(aux=10))
solapa_mesa.add_command(label="Salir", command= lambda: close_db(fd_base))
barra_menu.add_cascade(label="Mesas", menu=solapa_mesa)


main0.config(menu=barra_menu)

# Solapa superior

solapa_carga = tk.Menu(main0)

solapa_carga = tk.Menu(barra_menu, tearoff=0)
solapa_carga.add_command(label="Nuevo producto")
solapa_carga.add_command(label="Baja de producto")
solapa_carga.add_command(label="Precio del producto")


#================================ PANEL TITULO ====================================================

panel_titulo_principal =  tk.Frame(main0, bg=c_marron_claro, bd=5, relief="ridge")
panel_titulo_principal.place(x=29, y=26, width=1311, height=82)
titulo_principal = tk.Label(panel_titulo_principal, text="Sistema de Gestión de Restaurante", font=("Arial", 30, "bold"), bg=c_marron_claro, fg= c_hueso)
titulo_principal.place(x=326, y=11)

#================================ PANEL MENU ======================================================


panel_menu1 = tk.Frame(main0, width=849, height=608, bg=c_marron_claro, bd=5, relief="ridge")  
panel_menu1.place(x=29, y=134)

pantalla_registro = tk.Label(panel_menu1, textvariable=var_notificacion , font=("Arial", 15), bg=c_hueso, fg=c_marron_osc, bd=3, relief="raised")
pantalla_registro.place(x=14, y=548, width=536, height=42)


#================================ PANEL COMIDAS ===================================================

panel_comidas2 = tk.Frame(panel_menu1, bg=c_hueso, relief="raised",bd=3)  
panel_comidas2.place(x=14, y=14, width=260, height=525)  
titulo_comidas2 = tk.Label(panel_comidas2, text="Comidas", font=("Arial", 25, "bold"), fg=c_marron_claro, bg=c_hueso)
titulo_comidas2.place(x=50, y=14)


# Comida 1-----------------------------------------------------------------------------------------
var_comida1 = tk.StringVar()
comida1_label = tk.Label(panel_comidas2, text="Pollo", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
comida1_label.place(x=14, y=75) 
comida1_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3 ,relief="solid", bd=1, justify="center", textvariable=var_comida1, validate="key", validatecommand=vcmd)
comida1_entry.place(x=180, y=80, height=25)
comida1_entry.bind("<Return>", lambda event: calcular())

# Comida 2-----------------------------------------------------------------------------------------

var_comida2 = tk.StringVar()
comida2_label = tk.Label(panel_comidas2, text="Carne", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
comida2_label.place(x=14, y=157) 
comida2_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1, justify="center" , textvariable=var_comida2, validate="key", validatecommand=vcmd)
comida2_entry.place(x=180 , y=162, height=25)
comida2_entry.bind("<Return>", lambda event:calcular())

# Comida 3-----------------------------------------------------------------------------------------

var_comida3 = tk.StringVar()
comida3_label = tk.Label(panel_comidas2, text="Canelones", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
comida3_label.place(x=14, y=247) 
comida3_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_comida3, validate="key", validatecommand=vcmd)
comida3_entry.place(x=180 , y=252, height=25)
comida3_entry.bind("<Return>", lambda event:calcular())

# Comida 4-----------------------------------------------------------------------------------------
var_comida4 = tk.StringVar()
comida4_label = tk.Label(panel_comidas2, text="Lasagna", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
comida4_label.place(x=14, y=337) 
comida4_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_comida4, validate="key", validatecommand=vcmd)
comida4_entry.place(x=180 , y=342, height=25)
comida4_entry.bind("<Return>", lambda event:calcular())

# Comida 5-----------------------------------------------------------------------------------------
var_comida5 = tk.StringVar()
comida5_label = tk.Label(panel_comidas2, text="Tortilla", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
comida5_label.place(x=14, y=427) 
comida5_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_comida5, validate="key", validatecommand=vcmd)
comida5_entry.place(x=180 , y=432, height=25)
comida5_entry.bind("<Return>", lambda event:calcular())

#================================ PANEL BEBIDAS ===================================================

panel_bebidas2 = tk.Frame(panel_menu1, bg=c_hueso, relief="raised",bd=3)  
panel_bebidas2.place(x=290, y=14, width=260, height=525) 
titulo_bebidas2 = tk.Label(panel_bebidas2, text="Bebidas", font=("Montserrat", 25, "bold"), fg=c_marron_claro, bg=c_hueso)
titulo_bebidas2.place(x=60, y=14) 


# Bebida 1-----------------------------------------------------------------------------------------
var_bebida1 = tk.StringVar()
bebida1_label = tk.Label(panel_bebidas2, text="Vino", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
bebida1_label.place(x=14, y=75) 
bebida1_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida1, validate="key", validatecommand=vcmd)
bebida1_entry.place(x=180, y=80, height=25)
bebida1_entry.bind("<Return>", lambda event:calcular())

# Bebida 2-----------------------------------------------------------------------------------------
var_bebida2 = tk.StringVar()
bebida2_label = tk.Label(panel_bebidas2, text="Coca", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
bebida2_label.place(x=14, y=157) 
bebida2_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida2, validate="key", validatecommand=vcmd)
bebida2_entry.place(x=180 , y=162, height=25)
bebida2_entry.bind("<Return>", lambda event:calcular())

# Bebida 3-----------------------------------------------------------------------------------------
var_bebida3 = tk.StringVar()
bebida3_label = tk.Label(panel_bebidas2, text="Limonada", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
bebida3_label.place(x=14, y=247) 
bebida3_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida3, validate="key", validatecommand=vcmd)
bebida3_entry.place(x=180 , y=252, height=25)
bebida3_entry.bind("<Return>", lambda event:calcular())

# Bebida 4-----------------------------------------------------------------------------------------
var_bebida4 = tk.StringVar()
bebida4_label = tk.Label(panel_bebidas2, text="Agua S/G", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
bebida4_label.place(x=14, y=337) 
bebida4_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida4, validate="key", validatecommand=vcmd)
bebida4_entry.place(x=180 , y=342, height=25)
bebida4_entry.bind("<Return>", lambda event:calcular())

# Bebida 5-----------------------------------------------------------------------------------------

var_bebida5 = tk.StringVar()
bebida5_label = tk.Label(panel_bebidas2, text="Jugo", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
bebida5_label.place(x=14, y=427) 
bebida5_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida5, validate="key", validatecommand=vcmd)
bebida5_entry.place(x=180 , y=432, height=25)
bebida5_entry.bind("<Return>", lambda event:calcular())


#================================ PANEL POSTRES ===================================================

panel_postres2 = tk.Frame(panel_menu1, bg=c_hueso, relief="raised",bd=3)  
panel_postres2.place(x=566, y=14, width=260, height=525)  
titulo_postres2 = tk.Label(panel_postres2, text="Postres", font=("Montserrat", 25, "bold"), fg=c_marron_claro, bg= c_hueso)
titulo_postres2.place(x=60, y=14)

# Postre 1-----------------------------------------------------------------------------------------
var_postre1 = tk.StringVar()
postre1_label = tk.Label(panel_postres2, text="Brownie", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
postre1_label.place(x=14, y=75) 
postre1_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre1, validate="key", validatecommand=vcmd)
postre1_entry.place(x=180, y=80, height=25)
postre1_entry.bind("<Return>", lambda event:calcular())


# Postre 2-----------------------------------------------------------------------------------------
var_postre2 = tk.StringVar()
postre2_label = tk.Label(panel_postres2, text="Torta", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
postre2_label.place(x=14, y=157) 
postre2_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre2, validate="key", validatecommand=vcmd)
postre2_entry.place(x=180 , y=162, height=25)
postre2_entry.bind("<Return>", lambda event:calcular())

# Postre 3-----------------------------------------------------------------------------------------
var_postre3 = tk.StringVar()
postre3_label = tk.Label(panel_postres2, text="Flan", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
postre3_label.place(x=14, y=247) 
postre3_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre3, validate="key", validatecommand=vcmd)
postre3_entry.place(x=180 , y=252, height=25)
postre3_entry.bind("<Return>", lambda event:calcular())

# Postre 4-----------------------------------------------------------------------------------------
var_postre4 = tk.StringVar()
postre4_label = tk.Label(panel_postres2, text="Helado", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
postre4_label.place(x=14, y=337) 
postre4_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre4, validate="key", validatecommand=vcmd)
postre4_entry.place(x=180 , y=342, height=25)
postre4_entry.bind("<Return>", lambda event:calcular())

# Postre 5-----------------------------------------------------------------------------------------

var_postre5 = tk.StringVar()
postre5_label = tk.Label(panel_postres2, text="Tiramisu", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
postre5_label.place(x=14, y=427) 
postre5_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre5, validate="key", validatecommand=vcmd)
postre5_entry.place(x=180 , y=432, height=25)
postre5_entry.bind("<Return>", lambda event:calcular())

#================================ PANEL PRECIOS ===================================================
suma_total_var = tk.StringVar()

panel_precios1 = tk.Frame(main0, width=445, height=100, bg=c_marron_claro, bd=5, relief="ridge")
panel_precios1.place(x=895, y=134)

titulo_precio1 = tk.Label(panel_precios1, text="TOTAL:", font=("Montserrat", 25, "bold"), bg=c_marron_claro, fg= "black")
titulo_precio1.place(x=35, y=25)

titulo_precio2 = tk.Label(panel_precios1, textvariable=suma_total_var, font=("Montserrat", 25, "bold"), bg=c_marron_claro, fg= "black")
titulo_precio2.place(x=230, y=25)

#================================ PANEL BASE DE DATOS =============================================
panel_db = tk.Frame(main0, width=445 , height=350, bg=c_marron_claro, bd=5, relief="ridge")
panel_db.place(x=895, y=392)


#================================ TREEVIEWS =======================================================
grilla = ttk.Treeview(panel_db) # Declaro la variable que va a contener el treeview
grilla["columns"] = ("mesa", "pedido", "total") # Debe escribirse asi el tree en sus parametros
grilla.column("#0", width=93, anchor='w') # Sirve para un id o numero global incremental
grilla.column("mesa", width=93, anchor='w') # Sirve para las columnas que tendrán strings y datos
grilla.column("pedido", width=95, anchor='w') # Sirve para un id o numero global incremental
grilla.column("total", width=93, anchor='w') # Sirve para las columnas que tendrán strings y datos
grilla.place(x=14, y=14, height=280)

# SCROLLBAR - VERTICAL
scrollbar_grilla_v = ttk.Scrollbar(panel_db, orient='vertical', command=grilla.yview)
scrollbar_grilla_v.place(x=411, y=14, height=280)
grilla.configure(yscrollcommand=scrollbar_grilla_v.set)


# SCROLLBAR - HORIZONTAL
scrollbar_grilla_h = ttk.Scrollbar(panel_db, orient='horizontal', command=grilla.xview)
scrollbar_grilla_h.place(x=14, y=310, width=374)
grilla.configure(xscrollcommand=scrollbar_grilla_h.set)

""" # Ajustar automáticamente el ancho de las columnas según su contenido
for col in grilla["columns"]:
    grilla.column(col, width=150) """

consulta_db(fd_base)
#================================ PANEL BOTONES PRINCIPALES =======================================

panel_botones = tk.Frame(main0, width=445 , height=114, bg=c_marron_claro, bd=5, relief="ridge")
panel_botones.place(x= 895, y=260)

boton_alta = tk.Button(panel_botones, bg=c_marron, fg=c_naranja, text="Alta", font=("Montserrat", 15, "bold"), relief="raised",bd=5, command= lambda : alta_db(fd=fd_base))
boton_alta.place(x=36, y=7, height=42, width=165)

boton_baja = tk.Button(panel_botones, bg=c_marron, fg=c_naranja, text="Baja", font=("Montserrat", 15, "bold"), relief="raised",bd=5, command= lambda : baja_db(fd=fd_base, grilla=grilla))
boton_baja.place(x=241, y=7, height=42, width=165)

boton_consulta = tk.Button(panel_botones, bg=c_marron, fg=c_naranja, text="Consulta", font=("Montserrat", 15, "bold"), relief="raised",bd=5, command= lambda : consulta_particular(grilla))
boton_consulta.place(x=36, y=55, height=42, width=165)

boton_modificar = tk.Button(panel_botones, bg=c_marron, fg=c_naranja, text="Modificar", font=("Montserrat", 15, "bold"), relief="raised", bd=5, command= lambda : modificar_db(fd=fd_base))
boton_modificar.place(x=241, y=55, height=42, width=165)



# BOTÓN RESET

boton_borrado = tk.Button(panel_menu1,bg=c_marron, fg=c_naranja,  text="Reset", font=("Arial", 15, "bold"), relief="raised",bd=5, command= lambda : reset_menu())
boton_borrado.place(x=613, y=548, height=42, width=165)

main0.mainloop()
