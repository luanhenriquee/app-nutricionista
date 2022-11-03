import lista


def estimativaGordura(valorTotal, genero):
    erro = 'Ops.. Não consegui encontrar o resultado :('
    Homens = lista.Homens
    Mulheres = lista.Mulheres

    if genero == 1:
        if valorTotal in Homens:
            print(f'Milímetros: {Homens[valorTotal]}')
        else:
            print(erro)
    elif genero == 2:
        if valorTotal in Mulheres:
            print(f'Milímetros: {Mulheres[valorTotal]}')
        else:
            print(erro)
    else:
        print('ops.. algo deu errado')


def somaMedias(valorSupra, valorAbdominal, valorTricipital):
    soma = valorSupra + valorAbdominal + valorTricipital
    return soma


def mediaCadaDobra(lista_respostas):
    soma = sum(lista_respostas)
    media = soma / 3
    return media


def verificarInt(lista_resposta, valor, name):
    try:
        resposta = int(input(f'Digite o {valor} valor da {name}: '))
        adicionarResposta(lista_resposta, resposta)
        return resposta
    except:
        print('[ERRO] ~ Valor inválido.')


def verificarResposta(respostas, segundaResposta=None):
    if segundaResposta == respostas[0]:
        print(f'O segundo valor foi: {segundaResposta}\n'
              f'-> Como o segundo valor foi igual ao primeiro, iremos usar esse valor!')
        return True


def adicionarResposta(lista_resposta, resposta):
    lista_resposta.append(resposta)


def pegarValorDobra(name):
    lista_resposta = []
    media = 0
    while True:
        if not lista_resposta:
            verificarInt(lista_resposta, 'primeiro', name)
        elif len(lista_resposta) == 1:
            segundaResposta = verificarInt(lista_resposta, 'segundo', name)
            if verificarResposta(lista_resposta, segundaResposta):
                media += segundaResposta
                break
        elif len(lista_resposta) == 2:
            if verificarInt(lista_resposta, 'terceiro', name):
                media += mediaCadaDobra(lista_resposta)
                break
    return media


def verificarGenero():
    genero = 0
    print('-> Selecione as Opções <-')
    try:
        genero += int(input('1 - Homem\n2 - Mulher\n'
                            'Digite (1/2): '))
        return genero
    except:
        print('\n\n[ERRO] ~ Gênero inválido.\n - Digite 1 (Homem) / 2 (Mulher)\n\n')


def principal():
    while True:
        genero = verificarGenero()
        if genero == 1 or genero == 2:
            dobra_suprailiaca = pegarValorDobra('Dobra Suprailíaca')
            dobra_abdominal = pegarValorDobra('Dobra Abdominal')
            dobra_tricipital = pegarValorDobra('Dobra Tricipital')
            resultado_final = somaMedias(dobra_suprailiaca, dobra_abdominal, dobra_tricipital)
            estimativaGordura(resultado_final, genero)

            print()
            print(f'{resultado_final:.2f}')
            print()


if __name__ == '__main__':
    principal()
