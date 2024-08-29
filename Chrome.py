from selenium import webdriver

class Chrome:
    def driver(self):
        ChromeOptions = webdriver.ChromeOptions()
        download_path = r"C:\TiktokBot\Audios"
        prefs = {"download.default_directory": download_path}
        ChromeOptions.add_experimental_option("prefs", prefs)
        #ChromeOptions.add_argument("--incognito")
        ChromeOptions.add_argument("--headless")
        return webdriver.Chrome(ChromeOptions)