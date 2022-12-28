import requests
import pandas as pd

url = "https://statusinvest.com.br/category/advancedsearchresult"

querystring = {"search":"{\"Sector\":\"\",\"SubSector\":\"\",\"Segment\":\"\",\"my_range\":\"-20;100\",\"forecast\":{\"upsideDownside\":{\"Item1\":null,\"Item2\":null},\"estimatesNumber\":{\"Item1\":null,\"Item2\":null},\"revisedUp\":true,\"revisedDown\":true,\"consensus\":[]},\"dy\":{\"Item1\":null,\"Item2\":null},\"p_L\":{\"Item1\":null,\"Item2\":null},\"peg_Ratio\":{\"Item1\":null,\"Item2\":null},\"p_VP\":{\"Item1\":null,\"Item2\":null},\"p_Ativo\":{\"Item1\":null,\"Item2\":null},\"margemBruta\":{\"Item1\":null,\"Item2\":null},\"margemEbit\":{\"Item1\":null,\"Item2\":null},\"margemLiquida\":{\"Item1\":null,\"Item2\":null},\"p_Ebit\":{\"Item1\":null,\"Item2\":null},\"eV_Ebit\":{\"Item1\":null,\"Item2\":null},\"dividaLiquidaEbit\":{\"Item1\":null,\"Item2\":null},\"dividaliquidaPatrimonioLiquido\":{\"Item1\":null,\"Item2\":null},\"p_SR\":{\"Item1\":null,\"Item2\":null},\"p_CapitalGiro\":{\"Item1\":null,\"Item2\":null},\"p_AtivoCirculante\":{\"Item1\":null,\"Item2\":null},\"roe\":{\"Item1\":null,\"Item2\":null},\"roic\":{\"Item1\":null,\"Item2\":null},\"roa\":{\"Item1\":null,\"Item2\":null},\"liquidezCorrente\":{\"Item1\":null,\"Item2\":null},\"pl_Ativo\":{\"Item1\":null,\"Item2\":null},\"passivo_Ativo\":{\"Item1\":null,\"Item2\":null},\"giroAtivos\":{\"Item1\":null,\"Item2\":null},\"receitas_Cagr5\":{\"Item1\":null,\"Item2\":null},\"lucros_Cagr5\":{\"Item1\":null,\"Item2\":null},\"liquidezMediaDiaria\":{\"Item1\":null,\"Item2\":null},\"vpa\":{\"Item1\":null,\"Item2\":null},\"lpa\":{\"Item1\":null,\"Item2\":null},\"valorMercado\":{\"Item1\":null,\"Item2\":null}}","CategoryType":"1"}

payload = ""
headers = {
    "authority": "statusinvest.com.br",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer": "https://statusinvest.com.br/acoes/busca-avancada",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

json_res = response.json()

res = []

# Iterando para deixar linha a linha
for i in json_res:
    res.append(i)

# Criando o dataframe no modo json
df = pd.json_normalize(res)
# transformando em DataFrame
df = pd.DataFrame(df)
# Convertendo para csv só com as colunas que eu quero 
df.to_csv('acoes.csv', encoding='utf-8', index=False, sep=';', decimal=',')