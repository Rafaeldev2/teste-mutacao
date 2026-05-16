def calcular_bonus(salario: float, anos_de_casa: int, cargo: str) -> float:
    if anos_de_casa >= 2 and cargo == 'DESENVOLVEDOR':
        return salario * 0.15
    return 0.0