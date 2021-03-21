palabra = input("Ingrese la palabra que desea evaluar: ")
if palabra == palabra[::-1]:
    print("Tu palabra es palindroma")
else: print("Tu palabra NO es palindroma")