import os
import sys
import tkinter as tk
from CTkListbox import CTkListbox
import customtkinter as ctk
from tkinter import *
from src.windon_config import WindonConfigs
from title_functions import TitleFunctions
from cria_audio import CriaAudio
import threading
from text_redirect import TextRedirect
from gerar_video import GerarVideo
from utils import Utils


janela = ctk.CTk()
class MainView():
    def __init__(self):
        self.janela = janela
        self.pasta_titulos = "C:/TiktokBot/titulos"
        WindonConfigs.customConfig()
        WindonConfigs.JanelaConfig(janela, 1200, 800, True)
        self.Widgets()
        TitleFunctions.ListarTitulos(self.text_texto_list, self.pasta_titulos, True)
        janela.mainloop()
    def Widgets(self):
        self.entry_clip_username = ctk.CTkEntry(master=janela, placeholder_text="ClipChamp Username", width=240, height=50)
        self.entry_clip_username.place(x=60, y=50)

        self.entry_clip_password = ctk.CTkEntry(master=janela, placeholder_text="ClipChamp Password", width=240, height=50, show="*")
        self.entry_clip_password.place(x=320, y=50)

        self.text_texto_list = CTkListbox(master=janela, width=530, height=550)
        self.text_texto_list.place(x=30, y=120)

        self.btn_adiciona_texto = ctk.CTkButton(master=janela, width=220, height=60, text="ADICIONAR TEXTO", command=self.popup_adicionar_text)
        self.btn_adiciona_texto.place(x=80, y=720)

        self.btn_remove_texto = ctk.CTkButton(master=janela, width=220, height=60, text="REMOVER TEXTO", command=lambda: TitleFunctions.RemoveTitulo(self.text_texto_list, self.pasta_titulos))
        self.btn_remove_texto.place(x=320, y=720)

        # Frame Configs
        frame = ctk.CTkFrame(master=janela, width=600, height=800)
        frame.pack(side=RIGHT)

        # Frame Widgets
        self.btn_iniciar = ctk.CTkButton(master=frame, width=220, height=60, text="INICIAR APLICAÇÃO", command=lambda: threading.Thread(target=self.iniciarAplicacao).start())
        self.btn_iniciar.place(x=60, y=40)

        self.btn_limpar_log = ctk.CTkButton(master=frame, width=220, height=60, text="LIMPAR LOG", command=self.LimparLog)
        self.btn_limpar_log.place(x=320, y=40)

        self.text_log = ctk.CTkTextbox(master=frame, width=530, height=660)
        self.text_log.place(x=30, y=120)
    def popup_adicionar_text(self):

        self.popup_add_text = ctk.CTkToplevel(janela)
        self.popup_add_text.title("Adicionar texto")
        WindonConfigs.JanelaConfig(self.popup_add_text, 520, 700, False)

        self.title_entry = ctk.CTkEntry(master=self.popup_add_text, width=500, height=40, placeholder_text="Titulo")
        self.title_entry.place(x=10, y=10)

        self.combo_box = ctk.CTkComboBox(master=self.popup_add_text, values=["Antonio", "Fancisca"], width=500, height=40)
        self.combo_box.place(x=10, y=60)

        self.text_add = ctk.CTkTextbox(master=self.popup_add_text, width=500, height=500)
        self.text_add.place(x=10, y=110)

        self.btn_salvar = ctk.CTkButton(master=self.popup_add_text, width=220, height=60, text="SALVAR", command=lambda: TitleFunctions.SalvaTexto(self.title_entry.get(), self.text_add.get("1.0", tk.END), self.text_texto_list, self.pasta_titulos,  self.popup_add_text, self.combo_box.get()) )
        self.btn_salvar.place(x=150, y=630)

        self.popup_add_text.lift()
        self.popup_add_text.focus_set()
    def iniciarAplicacao(self):
        sys.stdout = TextRedirect(self.text_log)
        self.entry_clip_username.configure(state=tk.DISABLED)
        self.entry_clip_password.configure(state=tk.DISABLED)
        self.btn_remove_texto.configure(state=tk.DISABLED)
        self.btn_adiciona_texto.configure(state=tk.DISABLED)

        criaAudio = CriaAudio("jvittormoreira@outlook.pt", "Semprejv@11")
        criaAudio.login()

        print("INICIANDO GERAÇÃO DO VIDEO")
        for arquivo in os.listdir(self.pasta_titulos):
            if arquivo.endswith(".txt"):
                caminho_arquivo = os.path.join(self.pasta_titulos, arquivo)
                titulo = Utils.primeira_linha(caminho_arquivo)
                tituloFormatado = TitleFunctions.FormatarTitulo(titulo)
                print(f"VIDEO {titulo} SENDO GERADO")
                criaVideo = GerarVideo(fr"C:\TiktokBot\videos_base\{0}",
                                       fr"C:\TiktokBot\Audios\{tituloFormatado} ‐ Feito com o Clipchamp",
                                       fr"C:\TiktokBot\Title_Images\{tituloFormatado}", tituloFormatado)
                criaVideo.juntar_video_audio()
                print(f"VIDEO {titulo} FINALIZADO")
        print("FINALIZADO")

        self.entry_clip_username.configure(state=tk.NORMAL)
        self.entry_clip_password.configure(state=tk.NORMAL)
        self.btn_remove_texto.configure(state=tk.NORMAL)
        self.btn_adiciona_texto.configure(state=tk.NORMAL)
    def LimparLog(self):
        self.text_log.configure(state='normal')
        self.text_log.delete(1.0, tk.END)
        self.text_log.configure(state='disabled')

MainView()