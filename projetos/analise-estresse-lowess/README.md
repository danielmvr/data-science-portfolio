# Análise de Padrões Não Lineares no Nível de Estresse

Este projeto explora a variação diária do nível de estresse de indivíduos ao longo do tempo. Durante a análise, identificamos que os dados possuem comportamento não linear, apresentando oscilações no formato de "zig-zag".

Aplicamos técnicas de regressão linear e não paramétrica (LOWESS) para modelagem dos dados, avaliando seus desempenhos e ajustando hiperparâmetros.

## 🔧 Ferramentas e Tecnologias
- Python
- Pandas
- Matplotlib & Seaborn
- Statsmodels
- LOWESS (Regressão não paramétrica)
- Jupyter Notebook

## 📁 Estrutura
- `notebook/` → Notebook com toda análise

## 🚀 Resultado
O modelo LOWESS se mostrou muito mais eficaz na captura dos padrões não lineares dos dados, enquanto a regressão linear apresentou R² próximo de zero, evidenciando sua ineficácia neste cenário.

## 📜 Licença
MIT License.
