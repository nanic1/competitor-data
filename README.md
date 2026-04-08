# 📊 Coletor de Dados de Empresas

Este projeto em Python realiza a coleta automatizada de informações sobre empresas a partir de diferentes fontes online, consolidando os dados em uma planilha Excel.

## Funcionalidades

- 🔍 Coleta de avaliações no **Reclame Aqui**
- 💼 Coleta de avaliações no **Glassdoor**
- 🏢 Consulta de dados empresariais via **API da Receita Federal**
- 📁 Geração automática de arquivo **Excel** com os resultados

---

## 🧰 Tecnologias utilizadas

- Python
- Pandas
- Selenium
- Requests

---

## 📦 Instalação

### 1- Clone o repositório:

```bash
git clone https://github.com/nanic1/competitor-data
cd competitor-data
```

### 2- Instale as dependências:

```bash
pip install pandas selenium requests
```

---

## ▶️ Como executar

```bash
python app.py
```

---

## 📊 Saída

O script gera um arquivo chamado:

```
empresas.xlsx
```

Com as seguintes colunas:

- Empresa
- Score ReclameAqui
- Score Glassdoor
- Data de Início
- Capital Social

---

## 🏢 Empresas analisadas

- APSA  
- CONAC  
- Estasa  
- Protest  
- Master Business  
- Precisão  
- CIPA  
- Crase Sigma  
- Fernando e Fernandes  

---

## ⚠️ Observações importantes

- O scraping depende da estrutura das páginas (classes HTML), que pode mudar a qualquer momento.
- O site **Glassdoor** pode bloquear acessos automatizados.
- A API utilizada da Receita Federal (`receitaws`) possui limites de requisição.
- É necessário ter o navegador Google Chrome instalado.
- Caso deseje alterar ou adicionar empresas na pesquisa, adicione na lista `empresas` no mesmo formato utilizado.

---

## 👨‍💻 Autor

Pedro Kurtz
