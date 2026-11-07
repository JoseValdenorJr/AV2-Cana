

# AV2-Cana

(OBS: O trabalho foi feito individualmente e com muito atraso, logo, o uso de IA (Google Gemini chatbot e Antigravity Agent) como uma ferramenta de Auxílio foi feito nas seguintes estapas:
  - ajuda com lógica e interpretação dos códigos
  - formatação de norma padrão do relatório
  - ajuda na estrutura da planilha de resultados
  - ajuda para formatação dos gráficos de complexidade)

Este repositório contém as implementações e a análise experimental de algoritmos baseados na técnica de Divisão e Conquista.
O objetivo do projeto é resolver problemas algorítmicos clássicos, comparando a eficiência da abordagem de divisão e conquista com soluções de força bruta.

1 - Subarranjo de Soma MáximaDado um array de números inteiros, o algoritmo encontra o subarranjo contíguo que possui a maior soma.Força Bruta: Testa todos os subarranjos possíveis. Complexidade: O(n^2).
Divisão e Conquista: Divide o array recursivamente para encontrar as maiores somas nas metades ou cruzando o centro. Complexidade: O(n \log n).

2 - Par de Pontos Mais PróximosDado um conjunto de coordenadas em um plano 2D, o algoritmo identifica as duas estações (pontos) com a menor distância Euclidiana entre si.Força Bruta: Calcula a distância entre todos os pares de pontos. Complexidade: O(n^2)
Divisão e Conquista: Ordena os pontos e divide o plano em metades. A combinação dos resultados analisa uma faixa central restrita, realizando no máximo 7 comparações por ponto na área de fronteira. Complexidade: O(n \log n).



Tecnologias Utilizadas:
  - Python 3.
  - Módulo math (Biblioteca padrão)


Como Executar
Clone o repositório:
  - git clone https://github.com/seu-usuario/seu-repositorio.git](https://github.com/JoseValdenorJr/AV2-Cana.git
Acesse a pasta do projeto pelo terminal via CD, e execute os arquivos:
  - Etapa1SubMax.py
  - Etapa2DoisPontos.py
