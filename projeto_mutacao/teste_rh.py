import pytest
from rh import calcular_bonus


class TestFraco:

    def test_desenvolvedor_senior_executa(self):
        resultado = calcular_bonus(5000.0, 3, 'DESENVOLVEDOR')
        assert resultado is not None


class TestRobustos:

    def test_desenvolvedor_com_mais_de_2_anos_recebe_bonus(self):
        resultado = calcular_bonus(5000.0, 3, 'DESENVOLVEDOR')
        assert resultado == 750.0

    def test_desenvolvedor_com_exatamente_3_anos_recebe_bonus(self):
        resultado = calcular_bonus(3000.0, 3, 'DESENVOLVEDOR')
        assert resultado == 450.0

    def test_desenvolvedor_com_muitos_anos_recebe_bonus(self):
        resultado = calcular_bonus(8000.0, 10, 'DESENVOLVEDOR')
        assert resultado == 1200.0

    def test_fronteira_exatamente_2_anos_nao_recebe_bonus(self):
        resultado = calcular_bonus(5000.0, 2, 'DESENVOLVEDOR')
        assert resultado == 0.0

    def test_fronteira_1_ano_nao_recebe_bonus(self):
        resultado = calcular_bonus(5000.0, 1, 'DESENVOLVEDOR')
        assert resultado == 0.0

    def test_fronteira_0_anos_nao_recebe_bonus(self):
        resultado = calcular_bonus(5000.0, 0, 'DESENVOLVEDOR')
        assert resultado == 0.0

    def test_analista_com_mais_de_2_anos_nao_recebe_bonus(self):
        resultado = calcular_bonus(5000.0, 5, 'ANALISTA')
        assert resultado == 0.0

    def test_gerente_com_mais_de_2_anos_nao_recebe_bonus(self):
        resultado = calcular_bonus(10000.0, 10, 'GERENTE')
        assert resultado == 0.0

    def test_estagiario_com_mais_de_2_anos_nao_recebe_bonus(self):
        resultado = calcular_bonus(1500.0, 3, 'ESTAGIARIO')
        assert resultado == 0.0

    def test_cargo_case_sensitive_minusculo_nao_recebe_bonus(self):
        resultado = calcular_bonus(5000.0, 3, 'desenvolvedor')
        assert resultado == 0.0

    def test_analista_com_menos_de_2_anos_nao_recebe_bonus(self):
        resultado = calcular_bonus(5000.0, 1, 'ANALISTA')
        assert resultado == 0.0

    def test_bonus_zero_com_salario_alto_cargo_errado(self):
        resultado = calcular_bonus(50000.0, 5, 'DIRETOR')
        assert resultado == 0.0
