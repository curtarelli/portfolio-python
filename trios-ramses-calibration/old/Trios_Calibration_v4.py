'''
Esta é uma rotina para calibração de dados do sensor TriOS com base em seu manual Rel. 1.1 (Principle of Operation)
http://www.controlcomponents.com.au/Open-File/961/RAMSES%20-%20manual%20(v.1_1_01).pdf

Criado em Outubro de 2019

@author: Victor Pedroso Curtarelli
'''

##  Importando os pacotes necessários para a rotina:
import os
import pandas as pd
import statistics as st
import unicodedata as ud


##  Entrada do nome do sensor a ser calibrado pelo usuário, sendo que os nomes possíveis são restritos e escritos no formato "SAM_xxxx"
##  ou "SAMIP_xxx":
sensor = str(input('Qual sensor gostaria de calibrar? [Ex.: SAM_8404]'))
sensor = ud.normalize('NFD', sensor)            ##  Aqui é feita normalização da string para o caso do usuário
sensor = sensor.encode('ascii', 'ignore')       ##  inserir o nome corretamente porém com acentos ou letras minusculas
sensor = sensor.decode('utf-8')
sensor = sensor.lower()

##  Se usuário inserir nome de sensor inexistente a rotina pedirá que insira o valor novamente:
while sensor not in ['sam_8404', 'sam_83ad', 'sam_83b5', 'sam_839b', 'sam_83fd', 'sam_8424', 'samip_507b', 'samip_5089']:
    print('[Sensor inexistente, escreva novamente, seguindo o exemplo "SAM_8404"]')
    sensor = str(input('Qual sensor gostaria de calibrar? [Ex.: SAM_8404]'))
    sensor = ud.normalize('NFD', sensor)            ##  A normalização é refeita para o novo input
    sensor = sensor.encode('ascii', 'ignore')
    sensor = sensor.decode('utf-8')
    sensor = sensor.lower()

##  Entrada dos ambientes medidos pelo sensor escolhido, isso deve levar em conta a campanha em questão e como o sensor foi utilizado
##  em geral os sensores Es, Ls e Lw ficam foda d'água, sensores Ed, Eu e Lu fazem medidas dentro d'água, mas outras configurações
##  podem ser utilizadas:
amb = str(input('Foram feitas medidas dentro da água com este sensor? [Sim / Não]'))
amb = ud.normalize('NFD', amb)              ##  Segue o modelo de normalização já descrito
amb = amb.encode('ascii', 'ignore')
amb = amb.decode('utf-8')
amb = amb.lower()

##  Se usuário inserir valor para 'amb' incorreto o script pede para o usuário responda novamente:
while amb not in ['sim', 'nao', 's', 'n']:
    print('[POR FAVOR RESPONDA NOVAMENTE!!]')
    amb = str(input('Foram feitas medidas dentro da água com este sensor? [Sim / Não]'))
    amb = ud.normalize('NFD', amb)
    amb = amb.encode('ascii', 'ignore')
    amb = amb.decode('utf-8')
    amb = amb.lower()

##  A partir do nome do sensor a rotina monta as variáveis de chamada para acessar os arquivos ".txt":
back = sensor + '_BACK.txt'	##  Arquivos de entrada sempre escritos em caixa alta;
cal = sensor + '_CAL.txt'
raw = sensor + '_RAW.txt'
data_csv = sensor + '.csv'  ##  Arquivo ".csv" de output;
data_txt = sensor + '.txt'  ##  Arquivo ".txt" de output;
mcol = 'mcol.txt'           ##  Arquivo ".txt" para correção de coluna no arquivo final, deve ficar presente dentro de pasta "input" na
                            ##  pasta raiz da rotina;

##  Chamada dos diretórios "input" e "output" na pasta raiz da rotina, a pasta "input" deve conter os arquivos "mcol.txt" e respectivos 
##  arquivos do sensor a ser calibrado:
dir_i = os.path.join(os.getcwd(), 'input')
dir_o = os.path.join(os.getcwd(), 'output')

os.chdir(dir_i)     ##  Entrando no diretório "input";

##  Usando o pacote pandas para abrir os arquivos completos em Data Frames que vão ser usados na montagem do arquivo final:
df_calibrated = pd.read_csv(raw, delimiter = '\t', na_values = '', engine = 'python')
df_mcol = pd.read_csv(mcol, delimiter = '\t', na_values = '', engine = 'python')

##  Índices a serem usados pelopacote pandas para operações sobre os Data Frames durante a rotina:
i_mcol = df_mcol.loc[df_mcol['[Spectrum]'] == '[Data]'].index[0] + 1                   ##  Índice para a coluna de comprimentos de onda;
i_time = df_calibrated.loc[df_calibrated['[Spectrum]'] == 'IntegrationTime'].index[0]  ##  Índice do tempo de integração da medida;
i_data = df_calibrated.loc[df_calibrated['[Spectrum]'] == '[Data]'].index[0] + 1       ##  Índice de chamada dos dados dentro do Data Frame;
i_data2 = df_calibrated.loc[df_calibrated['[Spectrum]'] == '[Data]'].index[0] + 5      ##  Índice para dados +NAN do arquivo de calibração;
i_data3 = df_calibrated.loc[df_calibrated['[Spectrum]'] == '[Data]'].index[0] + 196    ##  Índice de chamada do final da tabela de dados;
i_data4 = df_calibrated.loc[df_calibrated['[Spectrum]'] == '[END] of [Data]'].index[0] ##  Índice para dados +NAN do final do arquivo de calibração;
i_cal = df_calibrated.loc[df_calibrated['[Spectrum]'] == 'CommentSub2'].index[0]       ##  Índice do ambiente do dado "Sup", "Sub" ou "Prof";
i_type = df_calibrated.loc[df_calibrated['[Spectrum]'] == 'IDDataTypeSub1'].index[0]   ##  Índice de localização do status do dado (RAW, CALIBRATED);
i_range = pd.Series(range(i_data2, i_data3))                         ##  Criando série de dados contendo range do índice dos dados na planilha;

##  Coluna com comprimentos de onda em nanômetros e inserção em arquivo final:
df_mcol = df_mcol.iloc[i_mcol:, 0]
df_calibrated.iloc[i_data:, 0] = df_mcol      ##  Data Frame para montagem do arquivo de saída pronto para receber os dados calibrados;

##  Abrindo os arquivos contendo apenas os dados a serem calibrados passando pelas operações:
data_back = pd.read_csv(back, delimiter = '\t', na_values = '', engine = 'python',skiprows = i_data, skipfooter = 2)
data_cal = pd.read_csv(cal, delimiter = '\t', na_values = '', engine = 'python', skiprows = i_data2, skipfooter = 62)
data_raw = pd.read_csv(raw, delimiter = '\t', na_values = '', engine = 'python', skiprows = i_data, skipfooter = 2)

##  Preparação de parâmetros de cálculos a serem utilizados na rotina de calibração, a calibração nada mais é que uma
##  operação de offset e subtração de background, normalização pelo tempo de integração da medida e constante de
##  calibração do aparelho:
t0 = 8192                           ##  Tempo de integração máximo do aparelho em [ms];
b16 = (2 ** 16) - 1                 ##  16 bits contados a partir de 0 para normalização dos dados crús;
S_air = data_cal.iloc[:, 1]         ##  Constantes de calibração "AIR" (arquivo);
S_aqua =  data_cal.iloc[:, 2]       ##  Constantes de calibração "AQUA" (arquivo);

##  Etapas do cálculo de calibração:
M = data_raw.iloc[:, 1:] / b16           ##  Normalização dos dados crús 16 bits;
M_count = M.iloc[0, :].count() - 1       ##  Contagem de medições (colunas de dados);
C = pd.DataFrame()                       ##  Data Frame vazio para subtração de "background";

##  Subtração de "background" e inserção de novos dados em Data Frame "C":
x = 0
while x <= M_count:
    i = 'Unnamed: ' + str(x + 1)
    t = int(df_calibrated.iloc[i_time, x + 1])                    ##  Tempo de integração das medidas;
    coef_t = t / t0                                               ##  Coeficiente para o cálculo de B;
    B = data_back.iloc[0:, 1] + (data_back.iloc[0:, 2] * coef_t)  ##  Cálculo do "background" a ser subtraído;
    C[i] = M.iloc[:, x] - B
    x += 1

## Índices para cálculo da média de (B - C) como "offset", relacionados à corrente escura dos aparelhos:
n1 = 237 - 1
n2 = 254

D = pd.DataFrame()      ##  Data Frame vazio para subtração de "offset";

##  Subtração de "offset" e inserção de novos dados em Data Frame "D":
y = 0
while y <= M_count:
    j = 'Unnamed: ' + str(y + 1)
    D[j] = C.iloc[:, y] - st.mean(C.iloc[n1:n2, y])
    y += 1

E = pd.DataFrame()      ##  Data Frame vazio para normalização K;

##  Normalização K e inserção de novos dados em Data Frame "E":
z = 0

while z <= M_count:
    q = 'Unnamed: ' + str(z + 1)
    t = int(df_calibrated.iloc[i_time, z + 1])      ##  Tempo de integração das medidas;
    k = t0 / t                                      ##  Coeficiente K da fórmula de calibração.
    E[q] = D.iloc[:, z] * k
    z += 1

F = E.iloc[4:195]    ##  Dataframe cópia de "E" para divisão por "S_air" ou "S_aqua";
F = F.reset_index()  ##  Resetando o índice do Data Frame;
del F['index']       ##  Deletando coluna gerada pelo código;

##  Calibração dos dados segundo o ambiente "AIR" ou "AQUA":
if amb in ['nao', 'n']:
    S_aqua = S_air

u = 0
while u <= M_count:
    if df_calibrated.iloc[i_cal, u + 1] in ['Sup', 'sup']:
        F.iloc[:, u] = F.iloc[:, u] / S_air
    elif df_calibrated.iloc[i_cal, u + 1] in ['Sub', 'sub', 'sub2', 'Prof', 'prof', 'Perf', 'perf']:
        F.iloc[:, u] = F.iloc[:, u] / S_aqua
    u += 1

F = F.set_index(i_range)    ##  Setando os índices do Data Frame "F";

df_calibrated.iloc[i_data2:i_data3, 1:] = F         ##  Cópia dos dados calibrados para a planilha final;
df_calibrated.iloc[i_data:i_data2, 1:] = '+NAN'     ##  Comprimentos de onda com dados inválidos devido à calibração;
df_calibrated.iloc[i_data3:i_data4, 1:] = '+NAN'    ##  Comprimentos de onda com dados inválidos devido à calibração;
df_calibrated.iloc[i_type, 1:] = 'CALIBRATED'       ##  Alteração do status do dado;

os.chdir(dir_o)     ##  Entrando no diretório de "output";

##  Salvando o Data Frame final em arquivos ".csv" e ".txt" no diretório "output":
df_calibrated.to_csv(data_txt, sep = '\t', encoding = 'utf-8', index = False)       ## Arquivo TXT idêntico ao "original" calibrado
                                                                                    ## extraído do software MSDA_XE do TriOS;
df_calibrated.to_csv(data_csv, encoding = 'utf-8', index = False)