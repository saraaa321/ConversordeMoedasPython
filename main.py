#janela => 600 x 600
#título
#campos para selecionar moedas de origem e destino

#lista de exibição com os nomes das moedas 

#Importar a biblioteca que vai fazer a janela 
import customtkinter 


#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("600x600")


#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text=" Conversor de Moedas ", font=("Times New Roman", 29), text_color=(126, 188, 131))
texto_moeda_origem = customtkinter.CTkLabel(janela, text= "Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text= "Selecione a moeda de destino")
campo_moeda_origem = customtkinter.CTkOptionMenu (janela, values= ["USD", "EUR", "BRL", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu (janela, values= ["USD", "EUR", "BRL", "BTC"])

def converter_moeda():
    print("Converter moeda")
botão_converter = customtkinter.CTkButton(janela, text= "Converter", command=converter_moeda, font=("", 20))

lista_moedas = customtkinter.CTkScrollableFrame(janela)
moedas_disponiveis = ["USD: Dólar americano", "UER: Euro", "BRL: Real Brasileiro", "BTC: Bitcoin"]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()



#colocar os elementos criados na tela
titulo.pack(padx=10, pady=40)
texto_moeda_origem.pack(padx=10, pady=0)
campo_moeda_origem.pack(padx=10, pady=5)
texto_moeda_destino.pack(padx=10, pady=0)
campo_moeda_destino.pack(padx=10, pady=5)
botão_converter.pack(padx=10, pady=40)
lista_moedas.pack(padx=10, pady=0)


#rodar a janela 
janela.mainloop()