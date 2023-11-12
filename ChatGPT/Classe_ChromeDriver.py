from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class ChromeDriver():
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('--headles')
        options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options= options)

    def acessa_site(self, site):
        self.driver.get(site)

    def exibe_opcs_menu(self):
        elementos_1 = self.driver.find_elements(By.CLASS_NAME, 'menu_item')
        cont = 0
        for item in elementos_1:
            if cont == 3 or cont == 6 or cont == 7:
                actions = ActionChains(self.driver)
                actions.move_to_element(item)
                actions.perform()
                self.driver.implicitly_wait(1)
                time.sleep(0.5)

                cont += 1
            else:
                item.click()
                time.sleep(1)
                cont += 1

    def abre_menu(self):
        elementos_1 = self.driver.find_elements(By.CLASS_NAME, 'menu_item')
        elementos_1[2].click()
        
        elementos_2 = self.driver.find_elements(By.CSS_SELECTOR, "body > header > div.container_header > div.menu_header.hide-mobile > div:nth-child(3) > div")
        elementos_2[0].click()

        elementos_3 = self.driver.find_elements(By.CLASS_NAME, 'dropdown-container')
        elementos_3[1].click()
    
    def navega_ate_uma_solucao(self, xpaths, indice):
        try:
            self.abre_menu()
        except:
            self.abre_menu()

        elementos_4 = self.driver.find_element(By.XPATH, xpaths[indice])
        elementos_4.click()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.implicitly_wait(5)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.driver.implicitly_wait(5)

    def entra_chat_duvida(self):
        search_box = self.driver.find_element(By.XPATH, '//*[@id="contato_banner"]')
        search_box.click()
        self.driver.implicitly_wait(50)

    def encerra_processo(self):
        self.driver.quit()
