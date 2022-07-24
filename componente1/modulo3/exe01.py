def insertionSort(array):
    for step in range(1, len(array)):
        #Guarda o elemento posterior ao que vamos comparar.
        key = array[step]
        #Posição do elemento que vai ser comparado.
        j = step - 1
        # Se o elemento posterior for menor que o anterior, entra no laço.
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key

lista = [5,2,3,4,1]
insertionSort(lista)
print(lista)

#key = 2
#j = 0
#key(2) < array[0](5) Inicio do while
#array[1](2) = array[0](5)
#array[1] = 5
#j = -1 Fim do while
#[5,5,3,4,1]
#array[-1 + 1] = 2
#[2,5,3,4,1]

#key = array[2](3)
#j = 1
#key(3) < array[1](5) Inicio do while
#array[2](3) = array[1](5)
#array[2] = 5
#[2,5,5,4,1]
#j = 0
#key(3) < array[j(0)] Fim do while
#array[j(0) + 1] = 3
#[2,3,5,4,1]

#[...]

#[1,2,3,4,5]

