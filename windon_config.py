from tkinter import *
import customtkinter as ctk
class WindonConfigs:
    @staticmethod
    def JanelaConfig(windon, largura, altura, centralizar):
        largura_janela = largura
        altura_janela = altura
        if (centralizar):
            largura_tela = windon.winfo_screenwidth()
            altura_tela = windon.winfo_screenheight()
            pos_x = largura_tela // 2 - largura_janela // 2
            pos_y = altura_tela // 2 - altura_janela // 2
            windon.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
            windon.title("Tiktok Reddit Bot")
            windon.resizable(False, False)
        else:
            windon.geometry(f"{largura_janela}x{altura_janela}")
        # windon.iconbitmap()
    @staticmethod
    def customConfig():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")