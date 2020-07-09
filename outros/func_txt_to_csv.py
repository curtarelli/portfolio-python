def txt_to_csv(txt, csv):
    import pandas as pd

    df = pd.read_csv(txt, delimiter = '\t', na_values = 'NaN')
    df.to_csv(csv, encoding = 'utf-8', index = False)

txt = str(input('Qual o caminho para o arquivo .TXT de entrada?'))
csv = str(input('Qual o caminho para o arquivo .CSV de saída?'))

txt_to_csv(txt, csv)
