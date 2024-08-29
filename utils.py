import os.path
class Utils:
    @staticmethod
    def criarPastasIniciasi(pasta_titulos):
        pasta_origem = "C:/TiktokBot"
        pasta_log = "C:/TiktokBot/log"
        pasta_audio = "C:/TiktokBot/Audios"
        pasta_imagens = "C:/TiktokBot/Title_Images"
        pasta_sem_legendas = "C:/TiktokBot/Sem_legendas"
        if (not os.path.exists(pasta_origem)):
            os.mkdir(pasta_origem)
        if (not os.path.exists(pasta_titulos)):
            os.mkdir(pasta_titulos)
        if (not os.path.exists(pasta_log)):
            os.mkdir(pasta_log)
        if (not os.path.exists(pasta_audio)):
            os.mkdir(pasta_audio)
        if (not os.path.exists(pasta_imagens)):
            os.mkdir(pasta_imagens)
        if (not os.path.exists(pasta_sem_legendas)):
            os.mkdir(pasta_sem_legendas)
    @staticmethod
    def primeira_linha(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding='utf-8') as file:
            titulo = file.readline()
        return titulo.strip()