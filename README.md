# Cadastro_Veiculos
 Sistema de controle de locação de veiculos integrado com banco de dados MySQL


Descrição do Projeto

Este projeto consiste em um aplicativo de interface gráfica desenvolvido em Python utilizando a biblioteca PyQt5 e que se conecta a um banco de dados MySQL. O aplicativo permite o cadastro de informações sobre aluguel de veículos.

Funcionalidades

Interface Gráfica: Desenvolvida com PyQt5, onde o usuário pode inserir dados.

Banco de Dados: Conexão com um banco de dados MySQL para armazenar as informações de cadastro.

Cadastro de Informações: Insere os dados de dias alugados, quilômetros rodados e modelo/veículo no banco de dados.

Como Funciona
O usuário preenche os campos na interface gráfica (dias alugados, quilômetros rodados e modelo/veículo).

Ao clicar no botão de envio, os dados são capturados e exibidos no console.

Em seguida, os dados são inseridos na tabela loja do banco de dados cadastro no MySQL.

Os campos da interface são resetados para novos cadastros.

Requisitos:

Python 3.x

PyQt5

mysql-connector-python