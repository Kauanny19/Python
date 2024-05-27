import time

beatles = []
print("Etapa 1:", beatles)

#Acrescenta os nomes na lista
beatles.append("John Lennon") 
beatles.append("Paul McCartney") 
beatles.append("George Harrison")
print("Etapa 2:", beatles)

#Solicita que o usuário digite o nome dos cantores
for i in range(2):
    beatles.append(input("Digite o nome dos cantores Stu Stucliffe ou Pete Best: "))
print("Etapa 3:", beatles)

#deleta o nome dos cantores da lista
del beatles[-1]
del beatles[-1]
print("Etapa 4:", beatles)

#acrescenta o nome no primeiro lugar da lista 
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)

time.sleep(3)