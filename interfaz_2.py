# ------------------------------------------------------------------------------
#libraries
# ------------------------------------------------------------------------------
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
# ------------------------------------------------------------------------------
#variables
# ------------------------------------------------------------------------------
lista=["","",""]
# ------------------------------------------------------------------------------
#Funciones
# ------------------------------------------------------------------------------
def abrir1():
	global lista
	global label_1
	file=""
	file = filedialog.askopenfilename(title="Abrir", filetypes=( ("Archivos .csv", "*.csv"),("Archivos .txt", "*.txt"),("Todos los ficheros", "*.*")))  # abre archivo
	lista.pop(0)
	lista.insert(0,file)
	file=file.split("/")
	archivo=file[len(file)-1]
	texto1="Archivo 1: " + str(archivo)
	label_1.destroy()
	label_1 = Label(frame_archivo1, bg="#282923",text=texto1, fg="white")
	label_1.place(x="0", y="0")
	print (lista)
	pass
def abrir2():
	global lista
	global label_2
	file=""
	file = filedialog.askopenfilename(title="Abrir", filetypes=(("Archivos .csv", "*.csv"),("Archivos .txt", "*.txt"),("Todos los ficheros", "*.*")))  # abre archivo
	lista.pop(1)
	lista.insert(1,file)
	file=file.split("/")
	archivo=file[len(file)-1]
	texto1="Archivo 2: " + str(archivo)
	label_2.destroy()
	label_2 = Label(frame_archivo2, bg="#282923",text=texto1, fg="white")
	label_2.place(x="0", y="0")
	print (lista)
	pass
def abrir3():
	global lista
	global label_3
	file=""
	file = filedialog.askopenfilename(title="Abrir", filetypes=(("Archivos .csv", "*.csv"), ("Archivos .txt", "*.txt"),("Todos los ficheros", "*.*")))  # abre archivo
	lista.pop(2)
	lista.append(file)
	file=file.split("/")
	archivo=file[len(file)-1]
	texto1="Archivo 3: " + str(archivo)
	label_3.destroy()
	label_3 = Label(frame_archivo3, bg="#282923",text=texto1, fg="white")
	label_3.place(x="0", y="0")
	print (lista)
	pass
def procesar():

	pass
def clear():
	global lista
	global label_1
	global label_2
	global label_3
	lista=["","",""]
	label_1.destroy()
	label_1 = Label(frame_archivo1, bg="#282923",text="Archivo 1:   ...	", fg="white")
	label_1.place(x="0", y="0")
	label_2.destroy()
	label_2 = Label(frame_archivo2, bg="#282923",text="Archivo 2:   ...	", fg="white")
	label_2.place(x="0", y="0")
	label_3.destroy()
	label_3 = Label(frame_archivo3, bg="#282923",text="Archivo 3:   ...	", fg="white")
	label_3.place(x="0", y="0")
	pass
def ubicacion():

	pass
# ------------------------------------------------------------------------------
#   INICIO DE APLICACION
# ------------------------------------------------------------------------------
app = Tk() # Creamos la App
app.title("Interfaz 2") # titulo
app.geometry("580x280") # geometria inicial
app.resizable(0, 0) # no e sposible  agrandar
app.config(bg="#282923") #  background color
# ------------------------------------------------------------------------------
#   BOTON DE ABRIR ARCHIVO
# ------------------------------------------------------------------------------
file_image = PhotoImage(file="more2.png") # decalara imagen primero como variable
Boton_abrir1 = Button(app, image=file_image, cursor="hand2",
                     bg="#282923", command=abrir1) # command significa que cada vez que es presionado se va a dirigir a la funcion
Boton_abrir1.place(x="330", y="60")

Boton_abrir2 = Button(app, image=file_image, cursor="hand2",
                     bg="#282923", command=abrir2) # command significa que cada vez que es presionado se va a dirigir a la funcion
Boton_abrir2.place(x="330", y="120")

Boton_abrir3 = Button(app, image=file_image, cursor="hand2",
                     bg="#282923", command=abrir3) # command significa que cada vez que es presionado se va a dirigir a la funcion
Boton_abrir3.place(x="330", y="180")
# ------------------------------------------------------------------------------
#   BOTON DE PROCESADO LIMPIADO Y ABRIR UBICACION
# ------------------------------------------------------------------------------
Boton_proceso = Button(app, text="PROCESAR", cursor="hand2",
                     bg="#282923", command=procesar, width="15",height="2",font="Verdana 10 bold", fg="white") # command significa que cada vez que es presionado se va a dirigir a la funcion
Boton_proceso.place(x="410", y="65")

Boton_limpiado = Button(app, text="LIMPIAR", cursor="hand2",
                     bg="#282923", command=clear, width="15",height="2",font="Verdana 10 bold", fg="white") # command significa que cada vez que es presionado se va a dirigir a la funcion
Boton_limpiado.place(x="410", y="115")

Boton_abrir = Button(app, text="ABRIR UBICACION", cursor="hand2",
                     bg="#282923", command=ubicacion, width="15",height="2",font="Verdana 10 bold", fg="white") # command significa que cada vez que es presionado se va a dirigir a la funcion
Boton_abrir.place(x="410", y="165")


# ------------------------------------------------------------------------------
#   Frame de los archivos 
# ------------------------------------------------------------------------------
frame_archivo1 = Frame()
frame_archivo1.config(bd=4, relief="groove", bg="#282923")
frame_archivo1.place(x="20", y="60", width="300", height="30")
label_1 = Label(frame_archivo1, bg="#282923",text="Archivo 1:   ...	", fg="white")
label_1.place(x="0", y="0")
frame_archivo2 = Frame()
frame_archivo2.config(bd=4, relief="groove", bg="#282923")
frame_archivo2.place(x="20", y="120", width="300", height="30")
label_2 = Label(frame_archivo2, bg="#282923",text="Archivo 2:   ...	", fg="white")
label_2.place(x="0", y="0")
frame_archivo3 = Frame()
frame_archivo3.config(bd=4, relief="groove", bg="#282923")
frame_archivo3.place(x="20", y="180", width="300", height="30")
label_3 = Label(frame_archivo3, bg="#282923",text="Archivo 3:   ...	", fg="white")
label_3.place(x="0", y="0")
# ------------------------------------------------------------------------------
#   Fin de App
# ------------------------------------------------------------------------------
app.mainloop()