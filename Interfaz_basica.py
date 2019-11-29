# ------------------------------------------------------------------------------
#   CSV libraries
# ------------------------------------------------------------------------------
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog

# ------------------------------------------------------------------------------
#   Funcion Abrir
# ------------------------------------------------------------------------------
def abrir():
    global Boton_procesar # global para pasar de funcion en funcion
	#global file

    file = filedialog.askopenfilenames(title="Abrir", initialdir="C:", filetypes=(
        ("Archivos .csv", "*.csv"), ("Todos los ficheros", "*.*"))) # abre archivo
    print(file)
    if file!="":
        ruta=""
        direc=file[0]
        direc=direc.split("/") 
        longitud_direc=len(direc)
        longitud_direc=longitud_direc-1
        for i in range (longitud_direc):
            ruta=ruta+direc[i]+"/"
        longitud=len(file)
        frame_directorio = Frame()
        frame_directorio.config(bd=4, relief="groove", bg="#282923")
        frame_directorio.place(x="80", y="20", width="450", height="30")
        directorio = Label(frame_directorio, bg="#282923",text=ruta, fg="white")
        directorio.place(x="0", y="0")
        filetext="Num_Archivos: "+str( longitud)
        frame_archivos = Frame()
        frame_archivos.config(bd=4, relief="groove", bg="#282923")
        frame_archivos.place(x="200", y="60", width="150", height="30")
        archivo_cantidad = Label(frame_archivos, bg="#282923",text=filetext, fg="white")
        archivo_cantidad.place(x="0", y="0")
        Boton_procesar = Button(app, width="20", height="2", text="PROCESAR",
                                font="Verdana 10 bold", fg="white", cursor="hand2", bg="#282923", command=procesar)# genera boton de procesar
        Boton_procesar.place(x="180", y="120") # tama;o del boton
    pass

# ------------------------------------------------------------------------------
#   Funcion Procesar
# ------------------------------------------------------------------------------
def procesar():
	#
    global Boton_procesar
    global Boton_carpeta
    global Boton_nuevo
	#global file
	# Aqui poner la funcion de CSV
    # ---abirir carpeta
    Boton_carpeta = Button(app, width="15", height="1", text="Abrir carpeta",
                           fg="white", cursor="hand2", bg="#282923", command=abrir_carpeta)
    Boton_carpeta.place(x="20", y="150")
    # ---refresh
    Boton_nuevo = Button(app, width="15", height="1", text="Nuevo",
                         fg="white", cursor="hand2", bg="#282923", command=new)
    Boton_nuevo.place(x="410", y="150")
    Boton_procesar.destroy()
    messagebox.showinfo(message="Finalizado", title="Procesado") # msg box de Finalizado
    pass

def abrir_carpeta():
    pass
def new():
    global Boton_procesar
    global Boton_carpeta
    global Boton_nuevo
    Boton_carpeta.destroy()
    Boton_nuevo.destroy()
    # ---directorio
    frame_directorio = Frame()
    frame_directorio.config(bd=4, relief="groove", bg="#282923")
    frame_directorio.place(x="80", y="20", width="450", height="30")
    directorio = Label(frame_directorio, bg="#282923",
                       text="Directorio:   ...	", fg="white")
    directorio.place(x="0", y="0")
    # ---#archivos
    frame_archivos = Frame()
    frame_archivos.config(bd=4, relief="groove", bg="#282923")
    frame_archivos.place(x="200", y="60", width="150", height="30")
    archivo_cantidad = Label(frame_archivos, bg="#282923",
                             text="Num_Archivos: ...	", fg="white")
    archivo_cantidad.place(x="0", y="0")
    # ---procesar

    Boton_carpeta.destroy()
    Boton_nuevo.destroy()
    pass


# ------------------------------------------------------------------------------
#   INICIO DE APLICACION
# ------------------------------------------------------------------------------
app = Tk() # Creamos la App
app.title("APP v1.0") # titulo
app.geometry("550x200") # geometria inicial
app.resizable(0, 0) # no e sposible  agrandar
app.config(bg="#282923") #  background color
# ------------------------------------------------------------------------------
#   BOTON DE ABRIR ARCHIVO
# ------------------------------------------------------------------------------
file_image = PhotoImage(file="file_32.png") # decalara imagen primero como variable
Boton_abrir = Button(app, image=file_image, cursor="hand2",
                     bg="#282923", command=abrir) # command significa que cada vez que es presionado se va a dirigir a la funcion
Boton_abrir.place(x="20", y="20")

# ------------------------------------------------------------------------------
#   Frame del Directorio
# ------------------------------------------------------------------------------
frame_directorio = Frame()
frame_directorio.config(bd=4, relief="groove", bg="#282923")
frame_directorio.place(x="80", y="20", width="450", height="30")
directorio = Label(frame_directorio, bg="#282923",
                   text="Directorio:   ...	", fg="white")
directorio.place(x="0", y="0")
# ------------------------------------------------------------------------------
#   Frame de cantidad de archivos
# ------------------------------------------------------------------------------
frame_archivos = Frame()
frame_archivos.config(bd=4, relief="groove", bg="#282923")
frame_archivos.place(x="200", y="60", width="150", height="30")
archivo_cantidad = Label(frame_archivos, bg="#282923",
                         text="#Archivos:   ...	", fg="white")
archivo_cantidad.place(x="0", y="0")

# ------------------------------------------------------------------------------
#   Fin de App
# ------------------------------------------------------------------------------
app.mainloop()
