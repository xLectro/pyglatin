import time		# Importa el tiempo para parar cuando sea necesario
import sys		# Importa el sistema para salir si se elige la opción 3
from colorama import init, Fore, Back, Style
init(convert=True)

print(Back.MAGENTA + Style.BRIGHT +"Welcome to the Piglatin translator." + Back.BLACK)

a = True			# Permite el bucle
while a == True:	# Hace un bucle con todo lo siguiente
	print("")		# Separador
	print("")		# Separador
	print(Fore.CYAN + "Enter 1 to English to Piglatin.")		# Opción 1
	print("Enter 2 to Piglatin to English." + Fore.WHITE)		# Opción 2
	print(Back.RED + "Enter 3 to Exit." + Fore.WHITE + Back.BLACK)
	mode = int(input())		# Pregunta el modo

	if mode == 1:			# Si el modo es igual a 1, hace lo siguiente
		print("")		# Separador
		print("")		# Separador
		print("")		# Separador
		print("")		# Separador
		print(Fore.WHITE + "Please, enter the word you want to translate:")
		word1 = input()		# Pregunta qué palaba quiere traducir
		if word1.isalpha() == True:		# Comprueba si el input es una única palabra con caracteres normales, sin números ni símbolos
			newword = word1[1:len(word1)] + word1[0] + "ay."		# Coge la primera letra, la pone al final y añade "ay" después
			print("")		# Separador
			print("")		# Separador
			print(Back.YELLOW + "==> " + newword + Back.BLACK)		# Imprime la palabra traducida
			time.sleep(1)		# Detiene el script durante un segundo
		else:		# Si el input no es válido
			print("")		# Separador
			print(Fore.RED + "Please, enter a valid word.")		# Imprime que introduzca una palabra válida

	elif mode == 2:		# Si el modo es igual a 2, hace lo siguiente
		print("")		# Separador
		print("")		# Separador
		print("")		# Separador
		print("")		# Separador
		print(Fore.WHITE + "Please, enter the word you want to translate")
		word2 = input()		# Pregunta qué palabra quiere traducir
		if (word2.isalpha() == True) and (word2[len(word2)-1] == "y") and (word2[len(word2)-2] == "a"):		# Comprueba que es una única palabra sin números ni simbolos y que los dos últimos caracteres son "ay"
			first = word2[len(word2)-3]		# Guarda en la variable first la nueva primera letra de la nueva palabra
			newword2 = first + word2[0:len(word2)-3] + "."		# Guarda la nueva palabra con la nueva primera letra y elimina el "ay" final
			print("")		# Separador
			print("")		# Separador
			print(Back.YELLOW + "==> " + newword2 + Back.BLACK)		# Imprime la palabra traducida
		else:		# Si el input no es válido hace lo siguiente
			print("")		# Separador
			print(Fore.RED + "Please, enter a valid word.")		# Imprime que introduzca una palabra válida
	elif mode == 3:		# Si el modo es igual a 3 hace lo siguiente
		print(Back.CYAN + "Thanks for using this software. Exiting...")
		time.sleep(2)
		sys.exit()
	else:		# Si el modo elegido no es válido
		print("")		# Separador
		print(Fore.RED + "Please, enter a valid number.")		# Imprime que introduzca un modo válido
