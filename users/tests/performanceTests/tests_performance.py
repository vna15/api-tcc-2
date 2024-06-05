import requests
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from django.test import TestCase

# URL da API para criar um novo usuário
API_URL = "http://localhost:8000/user/"

# Função para obter um token de autenticação JWT
def obter_token():
    user = User.objects.create_user(username='admin', password='admin')
    token = AccessToken.for_user(user)
    return token

class NovoUsuarioTestCase(TestCase):
    def test_criar_novo_usuario(self):
        # Obtém o token de autenticação
        token = obter_token()

        # Dados do novo usuário a serem enviados na requisição POST
        user_data = {
            "email": "novo_usuario@example.com",
            "fullName": "Novo Usuário",
            "CEP": "12345678",
            "age": 30
        }

        # Adiciona o token de autenticação ao cabeçalho
        headers = {"Authorization": f"Bearer {token.__str__()}"}

        # Envia a requisição POST e mede o tempo de resposta
        response = requests.post(API_URL, json=user_data, headers=headers)

        # Verifica se a requisição foi bem-sucedida
        self.assertEqual(response.status_code, 201)

        # Verifica se a resposta foi recebida em até 1 segundo
        self.assertLessEqual(response.elapsed.total_seconds(), 1, "O tempo de resposta foi maior que 1 segundo")

        # Imprime o tempo de resposta
        print(f"Tempo de resposta: {response.elapsed.total_seconds()} segundos")
