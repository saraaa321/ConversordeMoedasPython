import xmltodict

def nomes_moedas():

    with open("moedas.xml", "rb") as arquivos_moedas :
        dic_moedas =  xmltodict.parse(arquivos_moedas)

    moedas = dic_moedas["xml"]
    return moedas


with open("conversoes.xml", "rb") as arquivo_conversoes:
    dic_conversoes = xmltodict.parse(arquivo_conversoes)
    conversoes = dic_conversoes["xml"]
    dic_conversoes_disponiveis = {} #cria um dicionário vazio

def conversoes_disponiveis():

        for par_conversao in conversoes:
            #USD-BRL
            moeda_origem, moeda_destino = par_conversao.split("-")
            if moeda_origem in dic_conversoes_disponiveis:
                dic_conversoes_disponiveis[moeda_origem].append(moeda_destino)
            else:
                dic_conversoes_disponiveis[moeda_origem] = [moeda_destino]
        return dic_conversoes_disponiveis

#{"USD":["BRL", "AED", "CAD", "EUR", "GBP"], "BRL":}


#link = "https://economia.awesomeapi.com.br/last/USD-BRL" 