# media de aluno

def calcular_media(notas):
    soma = 0
    qtde = 0 
    for nota in notas:
        soma += nota
        qtde += 1

    media = soma / qtde
    return media

def classificar_aluno(notas):
    media = calcular_media(notas)

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"