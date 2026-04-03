from statistics import median, pstdev
from collections import Counter
from typing import List, Optional, Dict, Any


def checar_pedido(
    item: str,
    quantidade_nova: float,
    historico_quantidades: List[float],
    unidade_nova: Optional[str] = None,
    historico_unidades: Optional[List[str]] = None,
    multiplicador_limite: float = 3.0,
    zscore_limite: float = 3.0,
) -> Dict[str, Any]:
    """
    Valida se um novo pedido está muito fora do comportamento histórico.
    
    Regras:
    1. Alerta se a quantidade for muito maior que a mediana histórica
    2. Alerta se o z-score ultrapassar o limite
    3. Alerta se a unidade atual for diferente da unidade mais comum
    """

    if len(historico_quantidades) < 5:
        return {
            "item": item,
            "status": "sem_base_suficiente",
            "confirmacao_obrigatoria": True,
            "motivos": [
                "Histórico insuficiente para validar padrão com segurança."
            ],
        }

    mediana_hist = median(historico_quantidades)
    desvio_hist = pstdev(historico_quantidades)

    # Evita divisão por zero caso o histórico seja muito estável
    if desvio_hist == 0:
        desvio_hist = 1

    zscore = (quantidade_nova - mediana_hist) / desvio_hist

    motivos = []

    if quantidade_nova > mediana_hist * multiplicador_limite:
        motivos.append(
            f"Quantidade {quantidade_nova} está acima de {multiplicador_limite:.1f}x "
            f"da mediana histórica ({mediana_hist:.2f})."
        )

    if zscore > zscore_limite:
        motivos.append(
            f"Z-score alto ({zscore:.2f}), indicando pedido fora do padrão recente."
        )

    if historico_unidades and unidade_nova:
        unidade_mais_comum = Counter(historico_unidades).most_common(1)[0][0]
        if unidade_nova != unidade_mais_comum:
            motivos.append(
                f"Unidade informada '{unidade_nova}' difere da unidade mais comum "
                f"no histórico ('{unidade_mais_comum}')."
            )

    return {
        "item": item,
        "status": "alerta" if motivos else "ok",
        "confirmacao_obrigatoria": bool(motivos),
        "quantidade_nova": quantidade_nova,
        "mediana_historica": mediana_hist,
        "zscore": round(zscore, 2),
        "motivos": motivos or ["Pedido dentro do padrão esperado."],
    }


# Exemplo de uso
historico_qtd = [360, 390, 410, 375, 395, 402, 388, 405]
historico_und = ["kg", "kg", "kg", "kg", "kg", "kg", "kg", "kg"]

novo_pedido = checar_pedido(
    item="Banana",
    quantidade_nova=380,
    historico_quantidades=historico_qtd,
    unidade_nova="caixas",
    historico_unidades=historico_und,
)

print(novo_pedido)
