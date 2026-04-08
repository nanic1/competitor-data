import pandas as pd
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

empresas = [
    {
        "nome": "APSA",
        "reclame_aqui": "https://www.reclameaqui.com.br/empresa/apsa/",
        "glassdoor": "https://www.glassdoor.com.br/Vis%C3%A3o-geral/Trabalhar-na-APSA-Brazil-EI_IE2483872.13,24.htm",
        "cnpj": "28350338000192"
    },
    {
        "nome": "CONAC",
        "reclame_aqui": "https://www.reclameaqui.com.br/empresa/conac/",
        "glassdoor": "https://www.glassdoor.com.br/Vis%C3%A3o-geral/Trabalhar-na-CONAC-EI_IE9149904.13,18.htm",
        "cnpj": "27825983000151"
    },
    {
        "nome": "Estasa",
        "reclame_aqui": "https://www.reclameaqui.com.br/empresa/estasa/",
        "glassdoor": "https://www.glassdoor.com.br/Vis%C3%A3o-geral/Trabalhar-na-Estasa-Solu%C3%A7%C3%B5es-Imobili%C3%A1rias-EI_IE2488634.13,41.htm",
        "cnpj": "42181669000177"
    },
    {
        "nome": "Protest",
        "reclame_aqui": "https://www.reclameaqui.com.br/empresa/protest-imoveis-e-condominios/",
        "glassdoor": "https://www.glassdoor.com.br/Avalia%C3%A7%C3%B5es/Protest-Rio-de-Janeiro-Avalia%C3%A7%C3%B5es-EI_IE2616583.0,7_IL.8,22_IC2402386.htm",
        "cnpj": "29471778000160"
    },
    {
        "nome": "Master Business",
        "reclame_aqui": "https://www.reclameaqui.com.br/empresa/master-business/",
        "glassdoor": "https://www.glassdoor.com.br/Vis%C3%A3o-geral/Trabalhar-na-Master-Business-EI_IE2777723.13,28.htm",
        "cnpj": "11221526000118"
    },
    {
        "nome": "Precisão",
        "reclame_aqui": "https://www.reclameaqui.com.br/empresa/precisao-administradora/",
        "glassdoor": "",
        "cnpj": "01024225000140"
    },
    {
        "nome": "CIPA",
        "reclame_aqui": "https://www.reclameaqui.com.br/empresa/cipa-administracao-e-participacoes-s-a/",
        "glassdoor": "https://www.glassdoor.com.br/Vis%C3%A3o-geral/Trabalhar-na-Cipa-EI_IE2488384.13,17.htm",
        "cnpj": "33590134000169"
    },
    {
        "nome": "Crase Sigma",
        "reclame_aqui": "https://www.reclameaqui.com.br/empresa/crase-sigma/",
        "glassdoor": "https://www.glassdoor.com.br/Vis%C3%A3o-geral/Trabalhar-na-Crase-Sigma-EI_IE2682683.13,24.htm",
        "cnpj": "42541052000115"
    },
    {
        "nome": "Fernando e Fernandes",
        "reclame_aqui": "https://www.reclameaqui.com.br/empresa/fernando-e-fernandes-imobiliaria/lista-reclamacoes/",
        "glassdoor": "https://www.glassdoor.com.br/Vis%C3%A3o-geral/Trabalhar-na-Fernando-and-Fernandes-Imobili%C3%A1ria-EI_IE2725801.13,47.htm",
        "cnpj": "01268958000120"
    }
]

def score_reclame_aqui(path):
        try:
            driver = webdriver.Chrome()
            driver.get(path)
            time.sleep(5)

            score_get = driver.find_element(By.CLASS_NAME, "go3621686408")
            score_text = score_get.text
            driver.quit()
            time.sleep(1)
            return score_text
        except:
            score_text = "--"
            driver.quit()
            time.sleep(1)
            return score_text


def score_glassdoor(path):
    try:
        if path == "":
            return "--"
        driver = webdriver.Chrome()
        driver.get(path)
        time.sleep(5)

        score_get = driver.find_element(By.CLASS_NAME, "CompanyOverview_overallRating__TKVRp")
        score_text = score_get.text
        driver.quit()
        time.sleep(1)
        return score_text
    except:
        driver.quit()
        time.sleep(1)
        score_text = "--"
        return score_text
        
def dados_rf(cnpj):
    try:
        url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
        response = requests.get(url)
        data = response.json()

        return {
            "data_inicio": data.get("abertura", "--"),
            "capital_social": data.get("capital_social", "--"),
            "qtd_filiais": data.get("qsa", "--")
        }

    except:
        return {
            "data_inicio": "--",
            "capital_social": "--"
        }

def main():
    resultados = []

    for empresa in empresas:
        print(f"Coletando: {empresa['nome']}")

        score_ra = score_reclame_aqui(empresa["reclame_aqui"])
        score_gd = score_glassdoor(empresa["glassdoor"])
        dados = dados_rf(empresa["cnpj"])

        resultados.append({
            "Empresa": empresa["nome"],
            "Score ReclameAqui": score_ra,
            "Score Glassdoor": score_gd,
            "Data Início": dados["data_inicio"],
            "Capital Social": dados["capital_social"],
        })

    df = pd.DataFrame(resultados)
    df.to_excel("empresas.xlsx", index=False)

    print("Arquivo gerado com sucesso!")


if __name__ == "__main__":
    main()