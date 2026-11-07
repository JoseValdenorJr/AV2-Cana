import math

def calcular_distancia(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# forca bruta o(n^2)
def par_mais_proximo_forca_bruta(pontos):
    distancia_minima = float('inf')
    ponto1, ponto2 = None, None
    quantidade = len(pontos)
    
    for i in range(quantidade):
        for j in range(i + 1, quantidade):
            distancia_atual = calcular_distancia(pontos[i], pontos[j])
            if distancia_atual < distancia_minima:
                distancia_minima = distancia_atual
                ponto1, ponto2 = pontos[i], pontos[j]
                
    return distancia_minima, ponto1, ponto2

# div e conquista o(n log n)
def par_mais_proximo_faixa(faixa, delta):
    distancia_minima = delta
    par = None
    
    # pre ordenada no eixo Y
    # checar os proximos 7 pontos na fila
    for i in range(len(faixa)):
        for j in range(i + 1, min(i + 8, len(faixa))): 
            # Se a distância apenas em Y já estourou o delta, o resto também vai estourar
            if (faixa[j][1] - faixa[i][1]) >= distancia_minima:
                break 
            
            distancia_atual = calcular_distancia(faixa[i], faixa[j])
            if distancia_atual < distancia_minima:
                distancia_minima = distancia_atual
                par = (faixa[i], faixa[j])
                
    return distancia_minima, par

def par_mais_proximo_recursivo(pontos_x, pontos_y):
    quantidade = len(pontos_x)
    
    #p reduzir overhead, volta p forca bruta qnd sobrar mt pouco ponto
    if quantidade <= 3:
        return par_mais_proximo_forca_bruta(pontos_x)
        
    meio = quantidade // 2
    ponto_central = pontos_x[meio]
    
    # divide os pontos nso eixos
    esquerda_x = pontos_x[:meio]
    direita_x = pontos_x[meio:]
    
    esquerda_y = [p for p in pontos_y if p[0] <= ponto_central[0]]
    direita_y = [p for p in pontos_y if p[0] > ponto_central[0]]
    
    # calculo recusrivo pros 2 lados
    dist_esq, p1_esq, p2_esq = par_mais_proximo_recursivo(esquerda_x, esquerda_y)
    dist_dir, p1_dir, p2_dir = par_mais_proximo_recursivo(direita_x, direita_y)
    
    # define delta = lado com o par mais próximo
    if dist_esq < dist_dir:
        delta = dist_esq
        melhor_par = (p1_esq, p2_esq)
    else:
        delta = dist_dir
        melhor_par = (p1_dir, p2_dir)
        
     #separar pontos na area de risoc
    faixa_fronteira = [p for p in pontos_y if abs(p[0] - ponto_central[0]) < delta]
    
    dist_faixa, par_faixa = par_mais_proximo_faixa(faixa_fronteira, delta)
    
    #se algum na fronteira superar delta, vence
    if par_faixa:
        return dist_faixa, par_faixa[0], par_faixa[1]
    return delta, melhor_par[0], melhor_par[1]

def par_mais_proximo_dc(pontos):
    #ordenacao inicial 1 vez antes d recursao
    pontos_x = sorted(pontos, key=lambda p: p[0])
    pontos_y = sorted(pontos, key=lambda p: p[1])
    return par_mais_proximo_recursivo(pontos_x, pontos_y)