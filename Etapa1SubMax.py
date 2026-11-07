# forca bruta o(n^2)
def subarranjo_maximo_forca_bruta(vetor):
    tamanho = len(vetor)
    if tamanho == 0: return 0, -1, -1
    
    soma_maxima = float('-inf')
    indice_inicio, indice_fim = 0, 0
    
    for i in range(tamanho):
        soma_atual = 0
        for j in range(i, tamanho):
            soma_atual += vetor[j]
            #esse maior ou igual garante q o ultimo intervalo seja esclhido em empate
            if soma_atual >= soma_maxima:
                soma_maxima = soma_atual
                indice_inicio = i
                indice_fim = j
                
    return soma_maxima, indice_inicio, indice_fim


# implementacao com div e conq, execução o(n log n)
def soma_maxima_cruzamento(vetor, inicio, meio, fim):
    #procura maior soma meio p esqrd
    soma_esquerda = float('-inf')
    soma_temporaria = 0
    max_esquerda = meio
    for i in range(meio, inicio - 1, -1):
        soma_temporaria += vetor[i]
        if soma_temporaria > soma_esquerda:
            soma_esquerda = soma_temporaria
            max_esquerda = i
            
    ##procura maior soma meio p direita
    soma_direita = float('-inf')
    soma_temporaria = 0
    max_direita = meio + 1
    for j in range(meio + 1, fim + 1):
        soma_temporaria += vetor[j]
        if soma_temporaria > soma_direita:
            soma_direita = soma_temporaria
            max_direita = j
            
    return soma_esquerda + soma_direita, max_esquerda, max_direita

def subarranjo_maximo_dc(vetor, inicio, fim):
    if inicio == fim: # array de 1 elemento caso base (recursividade)
        return vetor[inicio], inicio, fim
        
    meio = (inicio + fim) // 2
    
    soma_esq, inicio_esq, fim_esq = subarranjo_maximo_dc(vetor, inicio, meio)
    soma_dir, inicio_dir, fim_dir = subarranjo_maximo_dc(vetor, meio + 1, fim)
    soma_cruz, inicio_cruz, fim_cruz = soma_maxima_cruzamento(vetor, inicio, meio, fim)
    
    # compara 3 retorna vencedor
    if soma_esq >= soma_dir and soma_esq >= soma_cruz:
        return soma_esq, inicio_esq, fim_esq
    elif soma_dir >= soma_esq and soma_dir >= soma_cruz:
        return soma_dir, inicio_dir, fim_dir
    else:
        return soma_cruz, inicio_cruz, fim_cruz