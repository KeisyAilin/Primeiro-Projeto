excelente = 0
ruim = 0

for i in range(50):
    print ("\n"+"-"*20)
    print(f"Entrevistado n° {i + 1}")
    print("-"*20)
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("Qual é a sua opinião sobre o atendimento? (1 para Excelente, 2 para Bom, 3 para Ruim): "))

    if opiniao == 1:
        excelente +=1
    elif opiniao ==3:
        ruim += 1

    print("    RESULTADOS    ")
    print("-"*20)
    print("Quantidade de respostas 'Excelente':", excelente)
    print("\nQuantidade de respostas 'Ruim':", ruim)