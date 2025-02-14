# 🌍 População Mundial em Tempo Real

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Django-population/population02.png">

---

## 📌 Índice
- [📜 Descrição](#-descrição)
- [🚀 Recursos](#-recursos)
- [🛠 Tecnologias](#-tecnologias)
- [✅ Pré-requisitos](#-pré-requisitos)
- [💾 Instalação](#-instalação)
- [▶️ Uso](#-uso)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)

---

## 📌 Descrição  
Este projeto é uma aplicação web desenvolvida em **Django** que exibe a população mundial em tempo real. Ele coleta dados diretamente do site **Worldometer**, utilizando **Selenium** para web scraping, e exibe estatísticas como população atual, nascimentos, mortes e crescimento populacional do dia.  

---

## 🚀 Recursos  
✔️ Exibição da população mundial em tempo real  
✔️ Atualização automática dos dados a cada 5 segundos  
✔️ Interface moderna e responsiva  
✔️ Coleta de dados via web scraping com Selenium  
✔️ API Django para fornecer dados no formato JSON  

---

## 🛠️ Tecnologias
- **Python 3**  
- **Django** (framework web)  
- **Selenium** (para web scraping)  
- **HTML, CSS e JavaScript** (para frontend)  

---

## ✅ Pré-requisitos  
Antes de começar, você precisará ter instalado:  
- **Python 3.x**  
- **pip** (gerenciador de pacotes do Python)  
- **Virtualenv** (para criar um ambiente virtual isolado)  
- **Google Chrome** e o **ChromeDriver** correspondente  

---


## 1️⃣  Instalação
Siga os passos abaixo para configurar o projeto:

1. Clone o repositório para sua máquina local:

    ```
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie e ative um ambiente virtual:

    ```
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

4. Inicie o servidor de desenvolvimento:

    ```
    python manage.py runserver
    ```

5. Acesse o sistema em http://127.0.0.1:8000/ no seu navegador.


 
## 💻 Uso  

1. Acesse o sistema pelo navegador através do endereço http://127.0.0.1:8000/.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Django-population/population.png">

 
## 🤝 Contribuição
Sinta-se à vontade para contribuir com este projeto. Siga estas etapas:

1. Faça um fork do repositório.

2. Crie uma nova branch para sua feature/bugfix:

    ```
    git checkout -b minha-feature
    ```

3. Envie suas alterações:

    ```
    git push origin minha-feature
    ```

4. Abra um Pull Request neste repositório.

## 📜 Licença

Este projeto é de código aberto e está licenciado sob a MIT License.

📌 Desenvolvido com ❤️ por Alexandre Santos
