from binary_search_tree import BinarySearchTree
arbol: BinarySearchTree[str] = BinarySearchTree()

archivo1 = open("documento1.txt")
lectura = archivo1.read().lower()
convertlec = lectura.split()

archivo2 = open("documento2.txt")
lectura2 = archivo2.read().lower()
convertlect2 = lectura2.split()


for palabra in convertlec:
    arbol.insert(palabra)

for palabra in convertlect2:
    arbol.insert(palabra)

print("Preorder:")
print(arbol.preorder())


print("---Buscar palabra---")
p = input("Ingrese la palabra a buscar: ").lower()
print(arbol.search(p))


cont_documento1 = sum(1 for palabra in convertlec if palabra == p)  # sum para sumar los valores
cont_documento2 = sum(1 for palabra in convertlect2 if palabra == p)
print("Número de veces que la palabra aparece en cada documento:")
print("Documento 1:", cont_documento1)
print("Documento 2:", cont_documento2)


























