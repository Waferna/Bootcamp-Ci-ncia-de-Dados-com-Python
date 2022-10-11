#Exemplo 1

saldo = 2000.0
saque = float(input("Informe o valor do saque: \n"))

if saldo >+ saque:
    print("Realizando saque!\n")

if saldo < saque:
    print("Saldo insuficiente!\n")


#Exemplo 2
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: \n"))

if opcao == 1:
    valor = float(imput("Informe a quantia para o saque: \n"))
    # ...

elif opcao ==2:
    print("Exibindo o extrato ... \n")
else:
    sys.exit("Opção invalida\n")




#Exemplo 3

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: \n"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.\n")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.\n")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.\n")

else:
    print("Ainda não pode tirar a CNH.\n")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.\n")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.\n")
else:
    print("Ainda não pode tirar a CNH.\n")



#Exemplo 4
conta_normal = True
conta_universidaria = False

saldo = 2000
saque = 2100
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!\n")
    elif saque <=(saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial!\n")
    else:
        print("Não foi possivel realizar o saque, daldo insuficiente!\n")
elif conta_universidaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!\n")
    else:
        print("Saldo insuficiente!\n")