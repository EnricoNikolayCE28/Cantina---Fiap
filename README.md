# Cantina---Fiap
CP 1 ENGENHARIA DE SOFTWARE 3° ANO CE FIAP

# 🍔 Sistema de Pedidos da Cantina FIAP

## 📌 Descrição do Problema
Os alunos enfrentam filas e demora no atendimento da cantina, causando perda de tempo entre aulas.

## 💡 Solução Proposta
Desenvolvemos um sistema em Python que permite realizar pedidos antecipados, visualizar pedidos, atualizar status e cancelar pedidos, simulando o funcionamento real de uma cantina.

## 🛠 Tecnologias Utilizadas
- Python
- JSON (persistência de dados)

## 📁 Estrutura do Projeto
- main.py → código principal
- pedidos.json → armazenamento dos pedidos
- README.md → documentação

✅ Funcionalidades Implementadas
Criar pedido
Listar pedidos
Atualizar status do pedido
Cancelar pedido
Buscar pedido por nome
Editar pedido

📋 Requisitos Funcionais
RF01: O sistema deve permitir criar pedidos.
RF02: O sistema deve permitir listar pedidos cadastrados.
RF03: O sistema deve permitir atualizar o status de um pedido.
RF04: O sistema deve permitir cancelar pedidos.
RF05: O sistema deve permitir buscar pedidos pelo nome do aluno.
RF06: O sistema deve permitir editar o item de um pedido existente.

⚙️ Requisitos Não Funcionais
RNF01: O sistema deve funcionar via terminal.
RNF02: O sistema deve armazenar os dados em arquivo JSON.
RNF03: O sistema deve apresentar tratamento de erros e validação de entrada.
RNF04: O código deve estar organizado em funções.
RNF05: O sistema deve ser simples e de fácil utilização.
RNF06: O projeto deve estar versionado no GitHub.

👤 Atores do Sistema
Aluno
Atendente da cantina
🧩 Casos de Uso
Aluno
Fazer pedido
Listar pedidos
Buscar pedido
Cancelar pedido
Editar pedido
Atendente da cantina
Listar pedidos
Atualizar status do pedido
Cancelar pedido
📘 Especificação de Caso de Uso
UC-01: Gerenciar Pedidos da Cantina

Ator Principal:
Aluno

Atores Secundários:
Atendente da cantina

Pré-condições:

O sistema deve estar em execução.
O usuário deve acessar o menu principal.

Fluxo Principal:

O usuário acessa o sistema.
O sistema exibe o menu principal.
O usuário escolhe uma das operações disponíveis.
O sistema executa a ação selecionada.
O sistema exibe uma mensagem de confirmação ou resultado.
O sistema retorna ao menu principal.

Casos contemplados no gerenciamento de pedidos:

Criar pedido
Listar pedidos
Atualizar status do pedido
Cancelar pedido
Buscar pedido por nome
Editar pedido

Fluxos de Exceção:

Caso o nome ou item não sejam preenchidos, o sistema informa erro.
Caso não existam pedidos cadastrados, o sistema informa que a lista está vazia.
Caso o número do pedido informado não exista, o sistema exibe mensagem de erro.
Caso o valor digitado seja inválido, o sistema solicita nova entrada.

Pós-condições:

O pedido pode ser criado, alterado, atualizado, consultado ou removido.
Os dados permanecem armazenados no arquivo JSON.
O sistema mantém os pedidos atualizados para futuras consultas.
🎥 Demonstração

Adicionar prints da execução do sistema ou link do vídeo demonstrando:

criação de pedido
listagem de pedidos
busca de pedido
edição de pedido
atualização de status
cancelamento de pedido

👥 Integrantes do Grupo
Enrico Nikolay
Giuliano Venceslau
Lucas Sanson
Eric Perez
