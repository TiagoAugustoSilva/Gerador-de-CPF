from flask import Flask, jsonify
import random

app = Flask(__name__)

# Função para gerar CPF válido
def gerar_cpf():
    def calcular_digito(cpf_parcial, pesos):
        soma = 0
        for i in range(len(cpf_parcial)):
            soma += int(cpf_parcial[i]) * pesos[i]
        digito = (soma * 10) % 11
        return digito if digito != 10 else 0

    # Gerar os 9 primeiros dígitos
    cpf = ''.join([str(random.randint(0, 9)) for _ in range(9)])

    # Calcular o 10º dígito
    pesos1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    digito1 = calcular_digito(cpf, pesos1)
    cpf += str(digito1)

    # Calcular o 11º dígito
    pesos2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    digito2 = calcular_digito(cpf, pesos2)
    cpf += str(digito2)

    return cpf

@app.route('/gerar_cpf', methods=['GET'])
def gerar_cpf_api():
    cpf_gerado = gerar_cpf()
    return jsonify({'cpf': cpf_gerado})

if __name__ == '__main__':
    app.run(debug=True)
