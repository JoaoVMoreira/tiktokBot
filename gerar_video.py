from moviepy.editor import AudioFileClip, ImageClip, VideoFileClip, clips_array, concatenate_videoclips, CompositeVideoClip
from IPython.display import display
from time import sleep

class GerarVideo:
    def __init__(self, caminho_video, caminho_audio, caminho_imagem, titulo):
        self.caminho_video = caminho_video
        self.caminho_audio = caminho_audio
        self.caminho_imagem = caminho_imagem
        self.titulo = titulo

    @staticmethod
    def converterVideo(video):
        audio_clip = VideoFileClip(video).audio
        return(audio_clip)
    @staticmethod
    def obter_duracao_audio(audio):
        return(AudioFileClip(audio).duration)
    @staticmethod
    def obter_duracao_video(video):
        return(VideoFileClip(video).duration)
    def juntar_video_audio(self):
        print("JUNTANDO AUDIO E VIDEO...")
        duracao_audio = self.obter_duracao_audio(self.caminho_audio)
        clip = VideoFileClip(self.caminho_video)
        compose = VideoFileClip(self.caminho_video)
        ajust = False
        print("SINCRONIZANDO AUDIO E VIDEO")
        if(duracao_audio > clip.duration):
            while duracao_audio > compose.duration:
                compose = concatenate_videoclips([compose, clip])
                ajust = True

        if(compose.duration > duracao_audio):
            clipVideo = compose.subclip(0, duracao_audio)
        print("AUDIO E VIDEO SINCRONIZADOS COM SUCESSO")
        self.altera_audio(clipVideo)
    def altera_audio(self, video):
        print("CONVERTANDO AUDIO...")
        audio = self.converterVideo(self.caminho_audio)
        new_video = video.set_audio(audio)
        print("AUDIO CONVERTIDO COM SUCESSO")
        self.adicionar_imagem(new_video)
    def adicionar_imagem(self, video):
        print("ADICIONANDO IMAGEM...")
        image_clip = ImageClip(self.caminho_imagem, duration=5)
        image_clip = image_clip.set_position(("center", "center"))
        video_imagem = CompositeVideoClip([video, image_clip])
        print("IMAGEM ADICIONADA COM SUCESSO")
        print("SALVANDO VIDEO")
        video_imagem.write_videofile(f"C:/TiktokBot/Sem_legendas/{self.titulo}-sem-legenda.mp4", codec="libx264", audio_codec="aac")
        print("VIDEO GERADO COM SUCESSO")

"""geraVideo = GerarVideo("C:/TiktokBot/videos_base/0.mp4", "C:/TiktokBot/Audios/caderninho ‐ Feito com o Clipchamp.mp4", "C:/TiktokBot/Title_Images/caderninho.png", "caderninho")
geraVideo.juntar_video_audio()"""