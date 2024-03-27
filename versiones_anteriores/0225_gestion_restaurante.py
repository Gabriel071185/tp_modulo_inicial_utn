import os
import random
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

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
    print(f"\n\nDiccionario -> \n{diccionario}")
    

def calcular():
    toma_valor()
    global suma
    for cant, prec in diccionario.values():
        suma += cant * prec
    
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
    print("se ejecuto reset menu")
# ---------------------------------- FUNCIONES BOTONES --------------------------------------------






# =============================== COMIENZO DEL PROGRAMA ===========================================
main0 = tk.Tk()
main0.geometry("1366x768")
main0.resizable(0,0)
main0.title("Gestor de comidas v 1.0")
main0.config(bg=c_marron)
# Botones de Comandos y Productos


# Solapa Comandos

barra_menu = tk.Menu(main0)

solapa_registro = tk.Menu(barra_menu, tearoff=0)
solapa_registro.add_command(label="Alta")
solapa_registro.add_command(label="Consulta")
solapa_registro.add_command(label="Modificación")
solapa_registro.add_command(label="Baja")
solapa_registro.add_command(label="Salir", command=main0.quit)
barra_menu.add_cascade(label="Comandos", menu=solapa_registro)

main0.config(menu=barra_menu)

# Solapa Productos

solapa_carga = tk.Menu(main0)

solapa_carga = tk.Menu(barra_menu, tearoff=0)
solapa_carga.add_command(label="Nuevo producto")
solapa_carga.add_command(label="Baja de producto")
solapa_carga.add_command(label="Precio del producto")
barra_menu.add_cascade(label="Productos", menu=solapa_carga)


#================================ PANEL TITULO ====================================================

panel_titulo_principal =  tk.Frame(main0, bg=c_marron_claro, bd=5, relief="ridge")
panel_titulo_principal.place(x=29, y=26, width=1311, height=82)
titulo_principal = tk.Label(panel_titulo_principal, text="Sistema de Gestión de Restaurante", font=("Arial", 30, "bold"), bg=c_marron_claro, fg= c_hueso)
titulo_principal.place(x=326, y=11)

#================================ PANEL MENU ======================================================
panel_menu1 = tk.Frame(main0, width=849, height=608, bg=c_marron_claro, bd=5, relief="ridge")  
panel_menu1.place(x=29, y=134)

pantalla_registro = tk.Label(panel_menu1, text="Los cambios fueron realizados!", font=("Arial", 15), bg=c_hueso, fg=c_marron_osc, bd=3, relief="raised")
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
comida1_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1, justify="center", textvariable=var_comida1)
comida1_entry.place(x=180, y=87, height=25)
comida1_entry.bind("<Return>", lambda event: calcular())

# Comida 2-----------------------------------------------------------------------------------------

var_comida2 = tk.StringVar()
comida2_label = tk.Label(panel_comidas2, text="Carne", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
comida2_label.place(x=14, y=157) 
comida2_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1, justify="center" , textvariable=var_comida2)
comida2_entry.place(x=180 , y=169, height=25)
comida2_entry.bind("<Return>", lambda event:calcular())

# Comida 3-----------------------------------------------------------------------------------------

var_comida3 = tk.StringVar()
comida3_label = tk.Label(panel_comidas2, text="Canelones", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
comida3_label.place(x=14, y=247) 
comida3_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_comida3)
comida3_entry.place(x=180 , y=259, height=25)
comida3_entry.bind("<Return>", lambda event:calcular())

# Comida 4-----------------------------------------------------------------------------------------
var_comida4 = tk.StringVar()
comida4_label = tk.Label(panel_comidas2, text="Lasagna", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
comida4_label.place(x=14, y=337) 
comida4_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_comida4)
comida4_entry.place(x=180 , y=349, height=25)
comida4_entry.bind("<Return>", lambda event:calcular())

# Comida 5-----------------------------------------------------------------------------------------
var_comida5 = tk.StringVar()
comida5_label = tk.Label(panel_comidas2, text="Tortilla", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
comida5_label.place(x=14, y=427) 
comida5_entry = tk.Entry(panel_comidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_comida5)
comida5_entry.place(x=180 , y=439, height=25)
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
bebida1_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida1)
bebida1_entry.place(x=180, y=87, height=25)
bebida1_entry.bind("<Return>", lambda event:calcular())

# Bebida 2-----------------------------------------------------------------------------------------
var_bebida2 = tk.StringVar()
bebida2_label = tk.Label(panel_bebidas2, text="Coca", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
bebida2_label.place(x=14, y=157) 
bebida2_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida2)
bebida2_entry.place(x=180 , y=169, height=25)
bebida2_entry.bind("<Return>", lambda event:calcular())

# Bebida 3-----------------------------------------------------------------------------------------
var_bebida3 = tk.StringVar()
bebida3_label = tk.Label(panel_bebidas2, text="Limonada", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
bebida3_label.place(x=14, y=247) 
bebida3_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida3)
bebida3_entry.place(x=180 , y=259, height=25)
bebida3_entry.bind("<Return>", lambda event:calcular())

# Bebida 4-----------------------------------------------------------------------------------------
var_bebida4 = tk.StringVar()
bebida4_label = tk.Label(panel_bebidas2, text="Agua S/G", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
bebida4_label.place(x=14, y=337) 
bebida4_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida4)
bebida4_entry.place(x=180 , y=349, height=25)
bebida4_entry.bind("<Return>", lambda event:calcular())

# Bebida 5-----------------------------------------------------------------------------------------

var_bebida5 = tk.StringVar()
bebida5_label = tk.Label(panel_bebidas2, text="Jugo", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
bebida5_label.place(x=14, y=427) 
bebida5_entry = tk.Entry(panel_bebidas2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_bebida5)
bebida5_entry.place(x=180 , y=439, height=25)
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
postre1_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre1)
postre1_entry.place(x=180, y=87, height=25)
postre1_entry.bind("<Return>", lambda event:calcular())


# Postre 2-----------------------------------------------------------------------------------------
var_postre2 = tk.StringVar()
postre2_label = tk.Label(panel_postres2, text="Torta", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
postre2_label.place(x=14, y=157) 
postre2_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre2)
postre2_entry.place(x=180 , y=169, height=25)
postre2_entry.bind("<Return>", lambda event:calcular())

# Postre 3-----------------------------------------------------------------------------------------
var_postre3 = tk.StringVar()
postre3_label = tk.Label(panel_postres2, text="Flan", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
postre3_label.place(x=14, y=247) 
postre3_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre3)
postre3_entry.place(x=180 , y=259, height=25)
postre3_entry.bind("<Return>", lambda event:calcular())

# Postre 4-----------------------------------------------------------------------------------------
var_postre4 = tk.StringVar()
postre4_label = tk.Label(panel_postres2, text="Helado", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
postre4_label.place(x=14, y=337) 
postre4_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre4)
postre4_entry.place(x=180 , y=349, height=25)
postre4_entry.bind("<Return>", lambda event:calcular())

# Postre 5-----------------------------------------------------------------------------------------

var_postre5 = tk.StringVar()
postre5_label = tk.Label(panel_postres2, text="Tiramisu", font=("Montserrat", 20, "bold"), fg=c_marron, bg=c_hueso)
postre5_label.place(x=14, y=427) 
postre5_entry = tk.Entry(panel_postres2, font=("Montserrat", 20), width=3, relief="solid", bd=1,justify="center", textvariable=var_postre5)
postre5_entry.place(x=180 , y=439, height=25)
postre5_entry.bind("<Return>", lambda event:calcular())

#================================ PANEL PRECIOS ===================================================
suma_total_var = tk.StringVar()

panel_precios1 = tk.Frame(main0, width=445, height=100, bg=c_marron_claro, bd=5, relief="ridge")
panel_precios1.place(x=895, y=134)

titulo_precio1 = tk.Label(panel_precios1, text="TOTAL:", font=("Montserrat", 25, "bold"), bg=c_marron_claro, fg= "black")
titulo_precio1.place(x=35, y=25)

titulo_precio2 = tk.Label(panel_precios1, textvariable=suma_total_var, font=("Montserrat", 25, "bold"), bg=c_marron_claro, fg= "black")
titulo_precio2.place(x=230, y=25)

#================================ PANEL BOTONES PRINCIPALES =======================================

panel_botones = tk.Frame(main0, width=445 , height=114, bg=c_marron_claro, bd=5, relief="ridge")
panel_botones.place(x= 895, y=260)

boton_consultar = tk.Button(panel_botones, bg=c_marron, fg=c_naranja, text="Alta", font=("Montserrat", 15, "bold"), relief="raised",bd=5)
boton_consultar.place(x=36, y=7, height=42, width=165)

boton_alta = tk.Button(panel_botones, bg=c_marron, fg=c_naranja, text="Baja", font=("Montserrat", 15, "bold"), relief="raised",bd=5)
boton_alta.place(x=241, y=7, height=42, width=165)

boton_baja = tk.Button(panel_botones, bg=c_marron, fg=c_naranja, text="Consulta", font=("Montserrat", 15, "bold"), relief="raised",bd=5)
boton_baja.place(x=36, y=55, height=42, width=165)

boton_modificar = tk.Button(panel_botones, bg=c_marron, fg=c_naranja, text="Modificar", font=("Montserrat", 15, "bold"), relief="raised",bd=5)
boton_modificar.place(x=241, y=55, height=42, width=165)

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

boton_borrado = tk.Button(panel_menu1,bg=c_marron, fg=c_naranja, text="Reset", font=("Arial", 15, "bold"), relief="raised",bd=5, command= lambda : reset_menu())
boton_borrado.place(x=613, y=548, height=42, width=165)

main0.mainloop()
