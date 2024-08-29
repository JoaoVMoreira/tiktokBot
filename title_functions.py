from src.utils import Utils
import tkinter as tk
import os.path
import re

class TitleFunctions:
    @staticmethod
    def RemoveTitulo(text_list, pasta_titulos):
        if(text_list.curselection() == None):
            pass
        else:
            titulo = text_list.get(text_list.curselection())
            titulo_formatado = TitleFunctions.FormatarTitulo(titulo)
            os.remove(f"{pasta_titulos}/{titulo_formatado}.txt")
            TitleFunctions.ListarTitulos(text_list, pasta_titulos)
    @staticmethod
    def FormatarTitulo(titulo):
        retira_caracteres = re.sub(r'[^a-zA-Z0-9\s]', '', titulo)
        return retira_caracteres.replace(" ", "_")
    @staticmethod
    def ListarTitulos(text_list, pasta_titulos, createPath):
        if(createPath == True):
            Utils.criarPastasIniciasi(pasta_titulos)
        text_list.delete(0, tk.END)
        for arquivo in os.listdir(pasta_titulos):
            if arquivo.endswith(".txt"):
                caminho_arquivo = os.path.join(pasta_titulos, arquivo)
                titulo = Utils.primeira_linha(caminho_arquivo)
                text_list.insert(tk.END, titulo)
    @staticmethod
    def SalvaTexto(title, text, text_list, pasta_titulos, popUp, voz):
        titulo_formatado = TitleFunctions.FormatarTitulo(title)
        content = f"{title}\n{voz}\n{text}"
        caminho = f"{pasta_titulos}/{titulo_formatado}.txt"
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(content)
        TitleFunctions.ListarTitulos(text_list, pasta_titulos, True)
        popUp.destroy()