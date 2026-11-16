# 🚗 Dashboard de Anúncios de Venda de Carros

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Express-3F4F75?logo=plotly&logoColor=white)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render&logoColor=white)

Aplicativo web interativo para explorar um conjunto de dados de anúncios de venda de carros usados. Projeto da **Sprint 5** do bootcamp de Análise de Dados da **TripleTen**, com foco em engenharia de software: ambientes virtuais, desenvolvimento de um app web e deploy em nuvem.

## 🔗 Acesse o app

**👉 [https://project-s5-tq4v.onrender.com/](https://project-s5-tq4v.onrender.com/)**

> O app está hospedado no plano gratuito do Render. Se ele estiver "dormindo" por inatividade, a primeira carga pode levar alguns minutos. Basta aguardar e recarregar a página.

## 📌 Sobre o projeto

O dashboard permite visualizar rapidamente o comportamento dos anúncios de carros, como preço, quilometragem, ano do modelo e tempo de anúncio, por meio de gráficos interativos criados com Plotly Express.

## ✨ Funcionalidades

- **Amostra dos dados:** caixa de seleção que mostra uma tabela com os primeiros anúncios do conjunto de dados.
- **Histograma:** caixa de seleção que cria um histograma, com escolha da coluna a ser analisada (`price`, `odometer`, `model_year` ou `days_listed`).
- **Gráfico de dispersão:** caixa de seleção que cria um gráfico de dispersão, com escolha dos eixos X e Y e opção de colorir os pontos pela condição do carro (`condition`).
- **Gráficos interativos:** é possível passar o mouse sobre os pontos, ampliar áreas e explorar os valores diretamente no gráfico.

## 🛠️ Tecnologias

- [Python](https://www.python.org/)
- [pandas](https://pandas.pydata.org/) para leitura e manipulação dos dados
- [Plotly Express](https://plotly.com/python/plotly-express/) para as visualizações
- [Streamlit](https://streamlit.io/) para o aplicativo web
- [Render](https://render.com/) para o deploy
- [Git e GitHub](https://github.com/) para o controle de versão

## 📊 Conjunto de dados

O arquivo `vehicles_us.csv` reúne anúncios de venda de carros, com as seguintes colunas:

| Coluna | Descrição |
|---|---|
| `price` | Preço do anúncio |
| `model_year` | Ano do modelo |
| `model` | Modelo do carro |
| `condition` | Condição do veículo |
| `cylinders` | Número de cilindros |
| `fuel` | Tipo de combustível |
| `odometer` | Quilometragem |
| `transmission` | Tipo de transmissão |
| `type` | Tipo de veículo |
| `paint_color` | Cor da pintura |
| `is_4wd` | Se o carro tem tração 4x4 |
| `date_posted` | Data de publicação do anúncio |
| `days_listed` | Dias em que o anúncio ficou no ar |

## 📁 Estrutura do repositório

```
.
├── .streamlit/
│   └── config.toml      # configuração do Streamlit para o Render
├── notebooks/
│   └── EDA.ipynb        # análise exploratória com plotly-express
├── app.py               # código do aplicativo web
├── requirements.txt     # dependências do projeto
├── vehicles_us.csv      # conjunto de dados
└── README.md
```

## ▶️ Como executar localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/Alvionx/Project-S5.git
   cd Project-S5
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv vehicles_env

   # Windows (PowerShell)
   vehicles_env\Scripts\Activate.ps1

   # Mac/Linux
   source vehicles_env/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Rode o aplicativo:

   ```bash
   streamlit run app.py
   ```

   O app abre no navegador, normalmente em `http://localhost:8501`.

> Para executar o notebook `notebooks/EDA.ipynb` no VS Code, instale também o `ipykernel` (`pip install ipykernel`).

## ☁️ Deploy no Render

O app foi publicado como um **Web Service** no Render, vinculado a este repositório, com as seguintes configurações:

- **Build Command:** `pip install --upgrade pip && pip install -r requirements.txt`
- **Start Command:** `streamlit run app.py`

O arquivo `.streamlit/config.toml` configura o servidor para escutar na porta que o Render espera.

## 👤 Autor

Feito por [Alvionx](https://github.com/Alvionx) como parte do bootcamp da TripleTen.