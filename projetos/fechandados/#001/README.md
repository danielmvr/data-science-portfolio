# Fechando com Dados #001  
## O pulso recente da economia brasileira

Este é o primeiro episódio da série **Fechando com Dados**, um projeto em que utilizo **dados públicos recentes** para construir análises simples, objetivas e conectadas ao mundo real.

A proposta da série é unir estudo, prática, portfólio e comunicação, transformando bases públicas em pequenos projetos de Ciência de Dados com começo, meio e fim.

---

## Objetivo do episódio

Neste primeiro episódio, o objetivo foi responder a uma pergunta simples:

> **O que os indicadores mais recentes sugerem sobre o momento atual da economia brasileira?**

Para isso, foi montado um recorte exploratório com foco em três indicadores:

- **IPCA**
- **Comércio**
- **Serviços**

---

## Fonte dos dados

Os dados utilizados neste projeto foram obtidos a partir de bases públicas do **IBGE**, por meio do **SIDRA** e da **API oficial**.

### Indicadores utilizados
- **IPCA**
- **Pesquisa Mensal do Comércio (PMC)**
- **Pesquisa Mensal de Serviços (PMS)**

---

## Recorte do estudo

O projeto utiliza uma janela recente de **12 períodos** para observar o comportamento dos indicadores e comparar o valor mais recente com a média do intervalo analisado.

### Observação importante
Há uma pequena defasagem temporal entre os dados utilizados neste episódio:

- **IPCA:** março de 2026
- **Comércio:** fevereiro de 2026
- **Serviços:** fevereiro de 2026

Por isso, esta análise deve ser entendida como uma leitura de **janela recente da economia brasileira**, e não como uma fotografia perfeitamente sincronizada de um único mês.

---

## Pergunta central

> **Os dados mais recentes sugerem aceleração, estabilidade ou perda de fôlego no pulso recente da economia brasileira?**

---

## Ferramentas utilizadas

- **Python**
- **Pandas**
- **Matplotlib**
- **Jupyter Notebook**
- **API do SIDRA / IBGE**

---

## Estrutura da análise

O fluxo do projeto foi organizado em etapas:

1. definição da pergunta
2. coleta dos dados
3. inspeção inicial das tabelas
4. limpeza e padronização
5. seleção das séries mais adequadas
6. construção dos gráficos
7. comparação do valor mais recente com a média de 12 períodos
8. interpretação e conclusão

---

## Principais achados

A leitura mais consistente dos dados foi a seguinte:

- o **IPCA** mais recente ficou **acima da média dos últimos 12 meses**
- o **comércio** mostrou um sinal mais claro de força
- os **serviços** seguiram positivos, mas em ritmo mais moderado

### Insight principal

> **Os dados recentes sugerem um Brasil em que o consumo ainda resiste, os serviços avançam com mais cautela e a inflação volta a pesar mais no presente.**

---

## Interpretação do episódio

O principal contraste observado neste episódio foi entre:

- **atividade ainda relativamente firme**
- **inflação mais pressionada no curto prazo**

O comércio apareceu como o indicador mais forte entre os ligados à atividade, enquanto os serviços mostraram um avanço mais contido. Já o IPCA chamou atenção por indicar uma pressão inflacionária mais forte no dado mais recente.

Em linguagem simples, a leitura deste episódio sugere que:

- a economia não parece paralisada
- o consumo ainda mostra algum grau de resiliência
- a inflação volta a apertar mais o ambiente recente

---

## Limitações

Este projeto tem algumas limitações importantes:

- recorte curto de apenas **12 períodos**
- foco em apenas **três indicadores**
- abordagem **exploratória**
- ausência de modelagem causal ou previsão
- pequena diferença temporal entre os meses analisados

---

## Próximos passos possíveis

Este projeto pode evoluir em episódios futuros com novas frentes, como:

- inclusão de novos indicadores
- comparação entre Brasil e recortes regionais
- ampliação da janela temporal
- aprofundamento em séries específicas
- publicação da análise em formato adaptado para LinkedIn e portfólio
