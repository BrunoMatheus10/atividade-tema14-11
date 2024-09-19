# programa_principal.py

# Importa o módulo calculo_imc
import calculo_imc


# Função para classificar o IMC
def classificar_imc(imc):
    """
    Classifica o IMC de acordo com os valores padrão.

    Parâmetros:
    imc (float): O valor do IMC.

    Retorna:
    str: A classificação do IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


# Leitura dos valores do usuário
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

# Calcula o IMC usando a função importada do módulo
imc = calculo_imc.calcular_imc(peso, altura)

# Classifica o IMC
classificacao = classificar_imc(imc)

# Exibe o resultado
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")
