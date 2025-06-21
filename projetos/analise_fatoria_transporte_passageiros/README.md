# 📊 Análise Fatorial - Transporte Rodoviário de Passageiros

Este projeto aplica a Análise Fatorial para identificar e interpretar os fatores latentes que influenciam a satisfação e o comportamento dos passageiros no transporte rodoviário. Utilizando um dataset sintético, o objetivo é demonstrar a aplicação da técnica, a validação de suas premissas e a extração de insights acionáveis para o negócio.

## 🔍 Descrição do Projeto

Este notebook detalha a aplicação da Análise Fatorial desde a preparação dos dados até a interpretação dos resultados. As etapas incluem:

-   Geração de um dataset sintético para simular dados de passageiros.
-   Verificação da adequação dos dados para Análise Fatorial (Testes de Bartlett e KMO).
-   Determinação do número ideal de fatores através de autovalores e Gráfico de Cotovelo.
-   Extração e interpretação das cargas fatoriais com rotação Varimax.
-   Análise das comunalidades e da variância explicada pelos fatores.
-   Cálculo e aplicação dos scores fatoriais para cada passageiro.

## 📁 Estrutura
-   `notebook/` → Notebook com toda análise (ex: `analise_fatorial_transporte_passageiros.ipynb`)
-   `dataset_passageiros.csv` → Dataset sintético gerado pelo notebook.

## 📜 Licença
MIT License.

## 🗂️ Etapas Realizadas

1.  **Definição do Problema e Configuração Inicial**
2.  **Geração e Exploração de Dados Sintéticos**
3.  **Verificação da Adequação dos Dados (Testes de Bartlett e KMO)**
4.  **Determinação do Número de Fatores (Autovalores e Scree Plot)**
5.  **Realização da Análise Fatorial e Interpretação das Cargas Fatoriais**
6.  **Análise de Comunalidades e Variação Explicada**
7.  **Cálculo e Análise dos Scores Fatoriais**
8.  **Conclusões e Insights de Negócio**

## 🛠️ Tecnologias e Bibliotecas Utilizadas

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   FactorAnalyzer
-   Watermark
-   Jupyter Notebook

## 💡 Principais Aprendizados

-   Aplicação da Análise Fatorial para descoberta de fatores latentes em dados de clientes.
-   Importância dos testes de adequação (Bartlett e KMO) para validar a aplicabilidade da técnica.
-   Interpretação de autovalores e Gráfico de Cotovelo para determinar o número de fatores.
-   Compreensão e interpretação das cargas fatoriais e o papel da rotação Varimax na interpretabilidade.
-   Avaliação da qualidade do modelo através de comunalidades e variância explicada.
-   Utilização e aplicações práticas dos scores fatoriais para segmentação e análises futuras.
-   Geração de dados sintéticos como ferramenta didática e de validação de modelos.

## 📈 Resultado

O projeto identificou com sucesso dois fatores latentes principais que explicam a satisfação e o comportamento dos passageiros no transporte rodoviário: **Eficiência e Frequência do Serviço** e **Qualidade e Conforto da Viagem**. Esses fatores, extraídos de um dataset sintético, foram capazes de explicar aproximadamente 77% da variância total, demonstrando a eficácia da Análise Fatorial em reduzir a dimensionalidade e fornecer insights acionáveis para o negócio. Os scores fatoriais calculados permitem a segmentação de clientes e a personalização de estratégias.

## 🚀 Como executar

1.  **Clone este repositório**:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```
2.  **Instale as dependências**:
    ```bash
    pip install pandas numpy matplotlib factor_analyzer watermark jupyter
    ```
3.  **Abra o notebook**:
    ```bash
    jupyter notebook notebook/analise_fatorial_transporte_passageiros.ipynb
    ```
4.  **Execute as células** e acompanhe as análises. O dataset sintético será gerado automaticamente na primeira execução.

---

Projeto desenvolvido como parte do meu portfólio de Data Science.

📌 [Veja meu portfólio completo no GitHub](https://github.com/danielmvr/data-science-portfolio)

📌 [Conecte-se comigo no LinkedIn](https://www.linkedin.com/in/daniel-reis-833451304/ )
