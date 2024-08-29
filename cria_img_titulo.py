import logging

from PIL import Image, ImageDraw, ImageFont
from title_functions import TitleFunctions

def criarImagemInicial(text):
    tamanho_texto = len(text)
    largura = 550

    if(tamanho_texto <= 50):
        altura = tamanho_texto / 2 + 30
    elif(tamanho_texto > 50 and tamanho_texto < 250):
        print("hm")
        altura = tamanho_texto / 2
    else:
        altura = tamanho_texto / 2.25

    background_color = "white"
    text_color = "black"
    tamanho_fonte = 18
    imagem = Image.new('RGB', (largura, round(altura)), background_color)

    max_caracteres_por_linha = 55
    texto_quebrado = [text[i:i + max_caracteres_por_linha] for i in range(0, len(text), max_caracteres_por_linha)]
    texto_quebrado = '\n'.join(texto_quebrado)

    juntaImagens(imagem, texto_quebrado)

def juntaImagens(imagem, text):
    imagem_a = Image.open("../imagemA.png")
    imagem_c = Image.open("../imagemC.png")
    img_final = Image.new('RGB', (imagem_a.width, imagem_a.height + imagem.height + imagem_c.height))

    img_final.paste(imagem_a, (0, 0))
    img_final.paste(imagem, (0, imagem_a.height))
    img_final.paste(imagem_c, (0, imagem_a.height + imagem.height))

    escreveTitulo(img_final, text)

def escreveTitulo(imagem, text):
    draw = ImageDraw.Draw(imagem)
    font = ImageFont.truetype('ROBOTO.ttf', 20)
    draw.text((19, 55), text, font=font, fill='black')

    imagem.save(f'C:/TiktokBot/Title_Images/{TitleFunctions.FormatarTitulo(text)}.png')
    print("IMAGEM TITULO CRIADA COM SUCESSO")
    logging.info("IMAGEM TITULO CRIADA COM SUCESSO")