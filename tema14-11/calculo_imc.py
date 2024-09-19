# calculo_imc.py

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).

    Parâmetros:
    peso (float): O peso da pessoa em quilogramas.
    altura (float): A altura da pessoa em metros.

    Retorna:
    float: O valor do IMC.
    """
    return peso / (altura ** 2)
