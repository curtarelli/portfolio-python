# -*- coding: utf-8 -*-
"""
@author: Victor
"""

# Import dos pacotes necessários

# Pacotes padrão
import os
import pandas as pd
import glob
from matplotlib import pyplot as plt
# Pacote para suavizar uma série de dados
from scipy.signal import medfilt

##  v2 - Pastas onde ficam os arquivos de entrada e saída, estas pastassempre devem ficar na pasta raiz do script;
dir_i = os.path.join(os.getcwd(), 'input')
dir_o = os.path.join(os.getcwd(), 'output')

df_csv = pd.DataFrame()     ##  v2 - Cria um dataframe vazio para inserção dos dados suavizados ao longo da rotina em loop;
i = 1                       ##  v2 - índice de chamada para adição de cada coluna no dataframe a ser salvado em .CSV;

#listando os CSV dentro da pasta;
os.chdir(dir_i)                         ##  Entrando na pasta de arquivos de entrada;
nomes_arquivos = glob.glob('*.csv')

### Loop para fazer cada arquivo que estiver na pasta;
# nomes_arquivos = lista com nomes de cada arquivo
# nome = um nome retirado da lista acima
for nome in nomes_arquivos:
    os.chdir(dir_i)                         ##  v2 - Entrando na pasta de arquivos de entrada;
    
    ### Lendo o arquivo .CSV;

    # index_col = diz qual coluna deve ser colocada com indice (se não começa do 0)
    # header = pegar primeira linha como cabeçalho
    
    dado_original = pd.read_csv(nome, header = None)
    dado_original_plot = pd.read_csv(nome, index_col = 0, header = None)

    # extraindo o dado de forma correta a aceitar na função;
    wl_array = dado_original[0].values          ##  v2 - Cria uma coluna com comprimentos de onda;
    dado_array = dado_original[1].values

    # aplicando a função  *medfilt* e salvando em 'dados_reduzidos';
    wl_reduzidas = medfilt(wl_array, 5)         ##  v2 - Cria uma coluna com comprimentos de onda reduzidos para escala;
    dados_reduzidos = medfilt(dado_array, 5)

    # transformando de volta em tabela;
    dado_redu = pd.DataFrame()              ##  v2 - Cria dataframe vazio para inserir dados reduzidos;
    dado_redu[0] = wl_reduzidas             ##  v2 - Insere no dataframe a coluna de comprimentos de onda;
    dado_redu[1] = dados_reduzidos          ##  v2 - Insere no dataframe a coluna de dados;

    dado_redu_serie = dado_redu.set_index(0)    ##  v2 - Reseta a coluna de comprimentos de onda como coluna índice;

    df_csv[0] = dado_redu[0]        ##  v2 - Insere no dataframe final a coluna de comprimentos de onda reduzidos;
    df_csv[i] = dado_redu[1]        ##  v2 - Adiciona no dataframe final a coluna de dados da rodada na sua devida coluna;
    i += 1                          ##  v2 - Sobe um nível no índice para a coluna da próxima rodada;

    ##### criando o gráfico do resultado;
    # abrindo uma Figura vazia;
    plt.figure()
    # dizendo para o plot o local do primeiro grafico;
    plt.subplot(2, 1, 1)
    # plotando o grafico 1;
    plt.plot(dado_original_plot, c = 'k', label = 'original')
    # dizendo para o plot o local do segundo grafico;
    plt.subplot(2, 1, 2)
    #plotando o grafico 2 ;
    plt.plot(dado_redu_serie, c = 'b', label = 'reduzido')
    
    # arrumando os eixos e a legenda;
    plt.xlabel('Comprimento de Onda',size = 20)
    plt.legend(fontsize = 12)

    os.chdir(dir_o)  ##  v2 - Entrando na pasta de saída de arquivos;
    #salvando a figura;
    plt.savefig(nome + '.png')

df_csv.to_csv('saida.csv', encoding='utf-8', header = None, index=False)     ##  Salva o dataframe final em arquivo .CSV;
