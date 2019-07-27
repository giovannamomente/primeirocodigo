
# criando uma lista vazia
list = []
#iniciando contador
ct = 0

while ct < 4: # iniciando loop com while
    ct = ct + 1 #"enquanto o número de resultados for menor que 4, é adicionado mais uma possibilidade"
    valor1 = int(input("insira o valor 1: ")) #pedindo para o usuário inserir o primeiro valor
    valor2 = int(input("insira o valor 2: ")) #pedindo para o usuário inserir o segundo valor
    resultado = valor1 + valor2 #identificando o somatório dos números
    print("resultado {} igual a: {} ".format(ct,resultado)) #usando a função format para printar o resultado
    list.append(resultado) #listado todos os resultados

print(list) #mostrando lista
print(max(list)) #mostrando maior número da listado
print (sum (list)) #somando a lista
print (len (list)) #mostrando o número de variáveis da lista
soma_dos_valores = sum(list) #mostrando a soma de valores
quantidade_de_valores = len(list) #mostrando o número de variáveis da lista
media = soma_dos_valores / quantidade_de_valores #fazendo a média dos resultados
print(media) #mostrando o resultado da média
menor = min(list) #atribuindo menor valor da lista a variável menor
list.remove(menor) #removendo a menor variável
print(list) #printando a lista
