
import os

from selenium.webdriver.common.by import By
from Chrome import Chrome
from time import sleep
from time import time
from selenium.webdriver.common.keys import Keys
from divide_texto import DivideTexto
from title_functions import TitleFunctions
import pygetwindow as gw
import pyautogui
import logging
import datetime
from cria_img_titulo import criarImagemInicial

class CriaAudio():
    def __init__(self, username, password):
        driver = Chrome().driver()

        hora = datetime.datetime.now()
        logging.basicConfig(
            level=logging.INFO,
            format= " [%(asctime)s] [%(filename)s] [%(lineno)d] %(message)s",
            filename = f"C:/TiktokBot/log/{str(datetime.date.today())}-{str(hora.hour)}-{str(hora.minute)}-{str(hora.second)}.txt"
        )

        self.username = username
        self.password = password
        self.driver = driver
        self.repeticao = False
        self.audios_finalizados = []
        self.titulo = ''
    def login(self):
        print("INICIANDO LOGIN")
        logging.info("INICIANDO LOGIN")
        try:
            driver = self.driver
            driver.maximize_window()
            driver.get("https://app.clipchamp.com/login/email")
            sleep(4)
            username_input = driver.find_element(By.NAME, "email")
            username_input.clear()
            username_input.send_keys(self.username)

            use_senha = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/main/section/div/form/div[2]/button[1]")
            use_senha.click()
            sleep(1)

            password_input = driver.find_element(By.NAME, "password")
            password_input.clear()
            password_input.send_keys(self.password)

            enter_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/main/section/div/form/div[2]/button[2]")
            enter_btn.click()
            sleep(2)
            print("LOGIN EFETUADO COM SUCESSO")
            logging.info("LOGIN EFETUADO COM SUCESSO")
            self.acessar_audio_generator()
        except:
            logging.critical("ERRO AO REALIZAR LOGIN")
            return print("ERRO AO REALIZAR LOGIN")
    def acessar_audio_generator(self):
        driver = self.driver
        element_cria_audio = "/html/body/div[1]/div/div/div[2]/div[2]/main/div/section[1]/button[1]"
        print("ACESSANDO ÁREA DE CRIAÇÃO")
        logging.info("ACESSANDO ÁREA DE CRIAÇÃO")
        try:
            btn_cria_audio = driver.find_element(By.XPATH, element_cria_audio)
            print("BOTÃO DE CRIAÇÃO DE VIDEO LOCALIZADO COM SUCESSO VIA HTML")
            logging.info("BOTÃO DE CRIAÇÃO DE VIDEO LOCALIZADO COM SUCESSO VIA HTML")
            btn_cria_audio.click()
        except:
            try:
                element_cria_audio = "#root > div > div > div.sc-jgyXzG.gQFKHq > div.sc-IqJVf.fXmlpW > main > div > section.sc-khYOSX.ejgAWY > button.fui-Button.r1alrhcs.sc-eXAmlR.hGzWvu.create.___174y5pl.ffp7eso.f1p3nwhy.f11589ue.f1q5o8ev.f1pdflbu.f1phragk.f15wkkf3.f1s2uweq.fr80ssc.f1ukrpxl.fecsdlb.f1rq72xc.fnp9lpt.f1h0usnq.fs4ktlq.f16h9ulv.fx2bmrt.f1d6v5y2.f1rirnrt.f1uu00uk.fkvaka8.f1ux7til.f9a0qzu.f1lkg8j3.fkc42ay.fq7113v.ff1wgvm.fiob0tu.f1j6scgf.f1x4h75k.f4xjyn1.fbgcvur.f1ks1yx8.f1o6qegi.fcnxywj.fmxjhhp.f9ddjv3.f14es27b.fp9bwmr.fjodcmx.f150uoa4.fhx4nu.f1aa9q02.f16jpd5f.f1jar5jt.fyu767a.fod5ikn.fl43uef.faaz57k.f17t0x8g.f194v5ow.f1qgg65p.fk7jm04.fhgccpy.f32wu9k.fu5nqqq.f13prjl2.f1czftr5.f1nl83rv.f12k37oa.fr96u23.ft3lys4.f1la4x2g.f156y0zm.fakimq4.fwdcejq.f7o03ib.fnsygzv.ffzw24k"
                btn_cria_audio = driver.find_element(By.CSS_SELECTOR, element_cria_audio)
                print("BOTÃO DE CRIAÇÃO DE VIDEO LOCALIZADO COM SUCESSO VIA CSS SELECTOR")
                logging.info("BOTÃO DE CRIAÇÃO DE VIDEO LOCALIZADO COM SUCESSO VIA CSS SELECTOR")
                btn_cria_audio.click()
            except :
                try:
                    btn_cria_audio = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div[2]/main/div/section[1]/button[1]").click()
                except:
                    logging.critical("BOTÃO Criar Novo Video NÃO LOCALIZADO")
                    return print("BOTÃO Criar Novo Video NÃO LOCALIZADO")
        print("ÁREA DE CRIAÇÃO DE VIDEO ACESSADA COM SUCESSO")
        logging.info("ÁREA DE CRIAÇÃO DE VIDEO ACESSADA COM SUCESSO")
        sleep(3)

        try:
            btn_entendi = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/button")
            print("FECHANDO POP-UP VIA HTML")
            logging.info("FECHANDO POP-UP VIA HTML")
        except:
            try:
                btn_entendi = driver.find_element(By.CSS_SELECTOR, "body > div.sc-gEvEer.hpZJmD.sc-gsFSXq.cFjfUK > div > div > div > div > button")
                print("FECHANDO POP-UP VIA CSS SELECTOR")
                logging.info("FECHANDO POP-UP VIA CSS SELECTOR")
            except Exception:
                logging.critical("FECHAMENTO DE POP-UP NÃO REALZIADO")
                return print("FECHAMENTO DE POP-UP NÃO REALZIADO")
        btn_entendi.click()
        sleep(1)

        try:
            btn_gravar = driver.find_element(By.CSS_SELECTOR, "#sidebar-button-recordCreate")
            print("ELEMENTO LOCALIZADO VIA CSS SELECTOR")
            logging.info("ELEMENTO LOCALIZADO VIA CSS SELECTOR")
            btn_gravar.click()
        except:
            try:
                btn_gravar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[2]/div[1]/nav/div/div[1]/div/button[2]")
                print("ELEMENTO LOCALIZADO VIA HTML")
                logging.info("ELEMENTO LOCALIZADO VIA HTML")
                btn_gravar.click()
            except:
                logging.critical("ELEMENTO GRAVAR NÃO LOCALIZADO")
                return print("ELEMENTO GRAVAR NÃO LOCALIZADO")
        sleep(3)

        try:
            btn_conversor = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/div[4]/button/div")
            print("CONVERSOR LOCALIZADO VIA HTML")
            logging.info("CONVERSOR LOCALIZADO VIA HTML")
            btn_conversor.click()
        except:
            try:
                btn_conversor = driver.find_element(By.XPATH, "#voiceover > div")
                print("CONVERSOR LOCALIZADO VIA CSS SELECTOR")
                logging.info("CONVERSOR LOCALIZADO VIA CSS SELECTOR")
                btn_conversor.click()
            except Exception:
                logging.critical("BOTÃO CONVERSOR NÃO LOCALIZADO")
                return print("BOTÃO CONVERSOR NÃO LOCALIZADO")
        sleep(3)

        self.converte_audio()
    def converte_audio(self):
        driver = self.driver
        arquivos = os.listdir("C:/TiktokBot/titulos")
        for text in arquivos:
            caminho_arquivo = f"C:/TiktokBot/titulos/{text}"
            if (DivideTexto.voz(caminho_arquivo) == "Antonio"):
                btn_voz = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[2]/button[1]")
                btn_voz.click()
                print("SELECIONANDO VOZ MASCULINA")
                logging.info("SELECIONANDO VOZ MASCULINA")
                sleep(5)
                for i in range (1, 6, 1):
                    btn_voz.send_keys(Keys.ARROW_UP)
                btn_voz.send_keys(Keys.ENTER)
                sleep(0.5)
                print("VOZ DO MASCULINA SELECIONADA COM SUCESSO")
                logging.info("VOZ DO MASCULINA SELECIONADA COM SUCESSO")
            else:
                print("VOZ DO FEMININA SELECIONADA COM SUCESSO")
                logging.info("VOZ DO FEMININA SELECIONADA COM SUCESSO")
            text_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[2]/div[3]/div/div/div/div/div[2]/div/div[5]/span[1]/textarea")
            print("SELECIONANDO INPUT DE TEXTO")
            logging.info("SELECIONANDO INPUT DE TEXTO")

            text_input.clear()
            text_input.send_keys(f"{DivideTexto.titulo(caminho_arquivo)}\n{DivideTexto.texto(caminho_arquivo)}")
            sleep(1)
            print("TEXTO COLADO COM SUCESSO")
            logging.info("TEXTO COLADO COM SUCESSO")

            btn_salvar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[2]/div[3]/div/div/div/div/div[2]/div/div[6]/div/button[2]")
            btn_salvar.click()
            print("BOTÃO SALVAR CLICADO COM SUCESSO")
            logging.info("BOTÃO SALVAR CLICADO COM SUCESSO")

            sleep(10)
            self.altera_nome(DivideTexto.titulo(caminho_arquivo))
            sleep(1)
            self.exportar_arquivo()
            self.fechar_janela()
            criarImagemInicial(DivideTexto.titulo(caminho_arquivo))
    def exportar_arquivo(self):
        driver = self.driver

        btn_exportar = driver.find_element(By.XPATH,
                                           "/html/body/div[1]/div/div/div[2]/main/div/div[1]/div[4]/button[2]/span[2]")
        btn_exportar.click()
        print("BOTÃO EXPORTAR CLICADO COM SUCESSO")
        logging.info("BOTÃO EXPORTAR CLICADO COM SUCESSO")

        try:
            btn_1080 = driver.find_element(By.XPATH, "/html/body/div[27]/nav/div/fieldset/ul/div/li[3]/button")
            logging.info("LOCALIZANDO OPÇÃO 1080 VIA HTML")
            btn_1080.click()
        except:
            try:
                btn_1080 = driver.find_element(By.CSS_SELECTOR,
                                               "body > div.sc-gEvEer.hzvUcZ.sc-ibQAlb.kdxhGv > nav > div > fieldset > ul > div > li:nth-child(4) > button")
                print("LOCALIZANDO OPÇÃO 1080 VIA CSS SELECTOR")
                logging.info("LOCALIZANDO OPÇÃO 1080 VIA CSS SELECTOR")
                btn_1080.click()
            except:
                try:
                    sleep(10)
                    print("AGUARDANDO...")
                    logging.info("AGUARDANDO...")
                except:
                    print("ELEMENTO NÃO CARREGOU A TEMPO")
                    logging.critical("ELEMENTO NÃO CARREGOU A TEMPO")
        sleep(5)
        print("ELEMENTO CONVERTIDO COM SUCESSO")
        logging.info("ELEMENTO CONVERTIDO COM SUCESSO")
    def altera_nome(self, titulo):
        driver = self.driver
        print("ALTERANDO TITULO DO ARQUIVO")
        logging.info("ALTERANDO TITULO DO ARQUIVO")
        titulo_formatado = TitleFunctions.FormatarTitulo(titulo)
        title_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[1]/div[3]/div/div[1]/div/span/input")
        title_input.clear()
        title_input.send_keys(titulo_formatado)
        print("TITULO DO ARQUIVO ALTERADO COM SUCESSO")
        logging.info("TITULO DO ARQUIVO ALTERADO COM SUCESSO")
        self.titulo = titulo_formatado
    def fechar_janela(self):
        driver = self.driver
        timeout = 30
        start_time = time()
        sleep(1)
        while True:
            try:
                sleep(1)
                janela = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div[1]/div/div[2]/div[2]/button")
                janela.click()
                print("DOWNLOAD REALZIADO COM SUCESSO")
                logging.info("DOWNLOAD REALZIADO COM SUCESSO")
                sleep(2)
                break
            except:
                try:
                    sleep(1)
                    janela = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.fui-FluentProvider.fui-FluentProviderri.___prvyko0.f19n0e5.fxugw4r.fpgzoln.fk6fouc.fkhj508.figsok6.fp6vxd > main > div > div > div.sc-cmFSZD.dLMnMf > div.sc-goDuUA.fvDHKw > div > div.sc-kBcFBM.etdDxc > div:nth-child(2) > button")
                    print("DOWNLOAD REALZIADO COM SUCESSO")
                    janela.click()
                    logging.info("DOWNLOAD REALZIADO COM SUCESSO")
                    sleep(2)
                    break
                except:
                    sleep(1)
                    print("Aguardando mais")
                    logging.info("Aguardando mais")
                    try:
                        element_try_again = "body > div.sc-gEvEer.hpZJmD.sc-gsFSXq.cFjfUK > div > div > div > button"
                        btn_try_again = driver.find_element(By.CSS_SELECTOR, element_try_again)
                        btn_try_again.click()
                        logging.info("ERRO AO BAIXAR ARQUIVO. TENTANDO NOVAMENTE")
                        print("ERRO AO BAIXAR ARQUIVO. TENTANDO NOVAMENTE")
                        self.exportar_arquivo()
                    except:
                        continue

        print("ARQUIVO SALVO COM SUCESSO")
        logging.info("ARQUIVO SALVO COM SUCESSO")
        self.audios_finalizados.append(self.titulo)
        self.voltar()
    def voltar(self):
        print("RETORNANDO A ÁREA DE EDIÇÃO")
        logging.info("RETORNANDO A ÁREA DE EDIÇÃO")
        driver = self.driver
        btn_retornar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div/button[1]")
        btn_retornar.click()
        sleep(2)
        self.repeticao = True
        print(self.audios_finalizados)

