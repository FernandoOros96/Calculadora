from tkinter import * 

raiz = Tk()
framePrincipal  = Frame(raiz)
framePrincipal.pack()
opcion  = StringVar()
operacion = ""
ultimaOpcionPulsada = ""
resultado = 0

raiz.geometry("150x200")
raiz.resizable(0, 0)

#Pantalla
pantalla = Entry(framePrincipal, font=('arial', 8, 'bold'), textvariable=opcion)
pantalla.grid(row=1,column=1,padx=8, pady=8, columnspan=4, sticky="NS")
pantalla.config(background="#DFDFDF", fg="black", justify="right")

def opcionPulsada(num):
    global operacion
    if operacion != "":
        opcion.set(num)
        operacion = ""
    else:
        opcion.set(opcion.get() + num)

def suma(num):
    global operacion
    global resultado
    global ultimaOpcionPulsada
    if operacion == "":
        resultado += int(num)
        operacion  = "suma"
        opcion.set(resultado)
    ultimaOpcionPulsada = "suma"

def resultadoFinal(num):
    global operacion
    global ultimaOpcionPulsada

    if operacion == "" and ultimaOpcionPulsada == "suma":
        suma(num)
    elif operacion == "" and ultimaOpcionPulsada == "resta":
        resta(num)
    elif operacion == "" and ultimaOpcionPulsada == "division":
        division(num)
    elif operacion == "" and ultimaOpcionPulsada == "multiplicacion":
        multiplicacion(num)

def resta(num):
    global operacion
    global resultado 
    global ultimaOpcionPulsada

    if operacion == "" and ultimaOpcionPulsada != "resta":
        resultado = int(num)
        operacion  = "resta"
        opcion.set(resultado)
    elif operacion == "":
        resultado -= int(num)
        operacion  = "resta"
        opcion.set(resultado)
    ultimaOpcionPulsada = "resta"

def division(num):
    global operacion
    global resultado
    global ultimaOpcionPulsada

    if operacion == "" and ultimaOpcionPulsada != "division":
        resultado += int(num)
        operacion  = "division"
        opcion.set(resultado)
    elif operacion == "":
        resultado //= int(num)
        operacion  = "division"
        opcion.set(resultado)
    ultimaOpcionPulsada = "division"

def multiplicacion(num):
    global operacion
    global resultado
    global ultimaOpcionPulsada

    if operacion == "" and ultimaOpcionPulsada != "multiplicacion":
        resultado += int(num)
        operacion  = "multiplicacion"
        opcion.set(resultado)
    elif operacion == "":
        resultado *= int(num)
        operacion  = "multiplicacion"
        opcion.set(resultado)
    ultimaOpcionPulsada = "multiplicacion"

def borrarTodaOperacion():
    global operacion
    global resultado
    global ultimaOpcionPulsada

    operacion = ""
    resultado = 0
    ultimaOpcionPulsada = ""
    opcion.set("")

def borrarNumero():
    opcion.set("")

def porcentaje(num):
    global operacion
    global resultado
    global ultimaOpcionPulsada

    if ultimaOpcionPulsada == "multiplicacion":
        resultado = resultado * (int(num)*0.01)
        operacion  = "porcentaje"
        opcion.set(resultado)
    elif ultimaOpcionPulsada == "resta":
        resultado = resultado - (resultado*int(num)*0.01)
        operacion  = "porcentaje"
        opcion.set(resultado)
    elif ultimaOpcionPulsada == "suma":
        resultado = resultado + (resultado*int(num)*0.01)
        operacion  = "porcentaje"
        opcion.set(resultado)
    
#Botones fila 2
botonC = Button(framePrincipal ,text="C", width=3, command=lambda:borrarNumero())
botonC.grid(row=2,column=1,padx=2, pady=2)

botonDivision = Button(framePrincipal ,text="/", width=3, command=lambda:division(opcion.get()))
botonDivision.grid(row=2,column=2,padx=2, pady=2)

botonMultiplicacion = Button(framePrincipal ,text="X", width=3, command=lambda:multiplicacion(opcion.get()))
botonMultiplicacion.grid(row=2,column=3,padx=2, pady=2)

botonBorrar = Button(framePrincipal ,text="AC", width=3, command=lambda:borrarTodaOperacion())
botonBorrar.grid(row=2,column=4,padx=2, pady=2)

#Botones fila 3
boton7 = Button(framePrincipal, text="7", width=3, command=lambda:opcionPulsada("7"))
boton7.grid(row=3,column=1,padx=2, pady=2)

boton8 = Button(framePrincipal, text="8", width=3, command=lambda:opcionPulsada("8"))
boton8.grid(row=3,column=2,padx=2, pady=2)

boton9 = Button(framePrincipal ,text="9", width=3, command=lambda:opcionPulsada("9"))
boton9.grid(row=3,column=3,padx=2, pady=2)

botonMenos = Button(framePrincipal ,text="-", width=3, command=lambda:resta(opcion.get()))
botonMenos.grid(row=3,column=4,padx=2, pady=2)

#Botones fila 4
boton4 = Button(framePrincipal, text="4", width=3, command=lambda:opcionPulsada("4"))
boton4.grid(row=4,column=1,padx=2, pady=2)

boton5 = Button(framePrincipal, text="5", width=3, command=lambda:opcionPulsada("5"))
boton5.grid(row=4,column=2,padx=2, pady=2)

boton6 = Button(framePrincipal ,text="6", width=3, command=lambda:opcionPulsada("6"))
boton6.grid(row=4,column=3,padx=2, pady=2)

botonMas = Button(framePrincipal ,text="+", width=3, command=lambda:suma(opcion.get()))
botonMas.grid(row=4,column=4,padx=2, pady=2)

#Botones fila 5
boton1 = Button(framePrincipal, text="1", width=3, command=lambda:opcionPulsada("1"))
boton1.grid(row=5,column=1,padx=2, pady=2)

boton2 = Button(framePrincipal, text="2", width=3, command=lambda:opcionPulsada("2"))
boton2.grid(row=5,column=2,padx=2, pady=2)

boton3 = Button(framePrincipal ,text="3", width=3, command=lambda:opcionPulsada("3"))
boton3.grid(row=5,column=3,padx=2, pady=2)

botonIgual = Button(framePrincipal ,text="=", width=3,bg='#28AFCD', command=lambda:resultadoFinal(opcion.get()))
botonIgual.grid(row=5,column=4,padx=2, pady=2,rowspan=2,sticky="NS")

#Botones fila 6
botonPorcentaje = Button(framePrincipal, text="%", width=3, command=lambda:porcentaje(opcion.get()))
botonPorcentaje.grid(row=6,column=1,padx=2, pady=2)

boton0 = Button(framePrincipal, text="0", width=3, command=lambda:opcionPulsada("0"))
boton0.grid(row=6,column=2,padx=2, pady=2)

botonPunto = Button(framePrincipal ,text=".", width=3, command=lambda:opcionPulsada("."))
botonPunto.grid(row=6,column=3,padx=2, pady=2)

raiz.mainloop()