from selenium import webdriver
from django.shortcuts import render
from django.http import JsonResponse
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_population_data():
    # Configuração do Selenium para rodar sem erros de GPU/WebGL
    options = Options()
    options.add_argument("--headless")  # Modo sem interface gráfica
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-gpu")  # Desativa a GPU
    options.add_argument("--disable-software-rasterizer")  # Evita erro de WebGL
    options.add_argument("--disable-extensions")  # Desativa extensões
    options.add_argument("--disable-dev-shm-usage")  # Evita problemas de memória
    options.add_argument("--disable-setuid-sandbox")  # Evita problemas no Linux
    options.add_argument("--disable-logging")  # Reduz logs desnecessários
    options.add_argument("--log-level=3")  # Define nível de log mínimo (somente erros críticos)

    # Inicializa o WebDriver do Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Acessa a página de dados populacionais
    url = "https://www.worldometers.info/world-population/"
    driver.get(url)

    try:
        # Aguarda o carregamento do elemento principal
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "maincounter-number")))

        # Captura os dados principais da população
        population = driver.find_element(By.CLASS_NAME, "maincounter-number").text.strip()
        numbers = driver.find_elements(By.CLASS_NAME, "rts-counter")

        if len(numbers) >= 4:
            # Obtém os dados de nascimentos e mortes de hoje
            birth_today = int(numbers[1].text.replace(",", "").strip())
            deaths_today = int(numbers[3].text.replace(",", "").strip())

            # Calcula o crescimento populacional de hoje
            growth_today = birth_today - deaths_today  

            # Formata os números com separadores de milhares (pontos)
            data = {
                "population": f"{int(population.replace(',', '')):,}".replace(",", "."),
                "birth_today": f"{birth_today:,}".replace(",", "."),
                "deaths_today": f"{deaths_today:,}".replace(",", "."),
                "growth_today": f"{growth_today:,}".replace(",", ".")
            }
        else:
            data = {"error": "Nem todos os dados foram encontrados corretamente."}

    except Exception as e:
        # Retorna um erro caso algo dê errado
        data = {"error": str(e)}

    # Fecha o navegador
    driver.quit()
    return data


# View principal que renderiza a página HTML
def index(request):
    return render(request, "population/index.html")

# View que retorna os dados da API em formato JSON
def get_data(request):
    data = get_population_data()
    return JsonResponse(data)
