import os
import tkinter

class DivideTexto:
    voz = ""
    titulo = ""
    texto = ""
    @staticmethod
    def voz(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            return linhas[1].strip()

    @staticmethod
    def titulo(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            return linhas[0].strip()

    @staticmethod
    def texto(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            text = ''.join(linhas[2:])
            return text.strip()