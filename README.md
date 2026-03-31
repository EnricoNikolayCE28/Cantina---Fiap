# 🍔 Sistema de Pedidos da Cantina FIAP

Projeto desenvolvido para o Checkpoint 1 da disciplina de Engenharia de Software do 3º ano de Engenharia de Computação da FIAP.

---

## 📌 Descrição do Problema

Nos intervalos entre aulas, os alunos enfrentam filas e demora no atendimento da cantina, o que gera perda de tempo e dificulta a organização dos pedidos.

---

## 🚀 Solução Proposta

O projeto propõe um sistema em Python, executado via terminal, para simular o gerenciamento de pedidos da cantina. O sistema permite cadastrar pedidos, listar pedidos cadastrados, buscar pedidos por nome, editar itens, atualizar o status para “Pronto” e cancelar pedidos.

---

## 📏 Escopo do Sistema

O sistema permite o gerenciamento de pedidos da cantina, incluindo cadastro, listagem, busca, edição, cancelamento e atualização de status dos pedidos. A aplicação simula o funcionamento de uma cantina acadêmica, focando no fluxo básico de pedidos.

---

## ⚠️ Limitações do Sistema

* O sistema funciona apenas via terminal, sem interface gráfica.
* Não há autenticação de usuários (qualquer pessoa pode operar o sistema).
* O status dos pedidos é limitado a “Preparando” e “Pronto”.
* Os dados são armazenados localmente em arquivo JSON, sem uso de banco de dados.
* Não há integração com sistemas de pagamento ou sistemas reais da cantina.

---

## 🛠️ Tecnologias Utilizadas

* Python
* JSON
* GitHub
* Miro

---

## ⚙️ Como Executar

1. Certifique-se de ter o Python instalado.
2. Baixe ou clone este repositório.
3. Execute o arquivo principal com o comando:

```bash
python main.py
```

4. Utilize o menu exibido no terminal para interagir com o sistema.

---

## 📂 Estrutura do Projeto

```bash
Cantina-FIAP/
├── main.py
├── pedidos.json
└── README.md
```

---

## 🧩 Funcionalidades Implementadas

* Criar pedido
* Listar pedidos
* Atualizar status do pedido para “Pronto”
* Cancelar pedido
* Buscar pedido por nome do aluno
* Editar item do pedido
* Persistir pedidos em arquivo JSON
* Validar campos obrigatórios

---

## 📋 Requisitos Funcionais

* **RF01:** O sistema deve permitir cadastrar um novo pedido informando nome do aluno e item solicitado.
* **RF02:** O sistema deve permitir listar todos os pedidos cadastrados.
* **RF03:** O sistema deve permitir atualizar o status de um pedido para “Pronto”.
* **RF04:** O sistema deve permitir cancelar um pedido existente.
* **RF05:** O sistema deve permitir buscar pedidos pelo nome do aluno.
* **RF06:** O sistema deve permitir editar o item de um pedido já cadastrado.
* **RF07:** O sistema deve validar se os campos obrigatórios foram preenchidos antes de registrar ou editar um pedido.
* **RF08:** O sistema deve salvar e recuperar os pedidos por meio de um arquivo JSON, mantendo os dados entre execuções.

---

## 🔒 Requisitos Não Funcionais

* **RNF01:** O sistema deve ser executado em ambiente terminal, sem necessidade de interface gráfica.
* **RNF02:** O sistema deve persistir os dados localmente em arquivo JSON, garantindo armazenamento entre execuções.
* **RNF03:** O sistema deve validar entradas inválidas e impedir operações com dados incorretos ou incompletos.
* **RNF04:** O sistema deve apresentar mensagens claras de erro e confirmação ao usuário.
* **RNF05:** O código deve ser estruturado de forma modular e legível, facilitando manutenção e evolução.
* **RNF06:** O sistema deve ser simples e intuitivo, permitindo uso sem necessidade de treinamento prévio.

---

## 👤 Atores do Sistema

* Aluno
* Atendente da Cantina

---

## 🧠 Casos de Uso

* Fazer pedido
* Listar pedidos
* Buscar pedido
* Editar pedido
* Cancelar pedido
* Atualizar status do pedido

---

## 📘 Caso de Uso Exemplo

### UC-01 – Fazer Pedido

**Ator principal:** Aluno

**Pré-condições:**

* Sistema em execução
* Usuário no menu principal

**Fluxo principal:**

1. O usuário seleciona a opção de criar pedido.
2. O sistema solicita o nome do aluno.
3. O sistema solicita o item desejado.
4. O sistema valida os dados informados.
5. O sistema registra o pedido com status “Preparando”.
6. O sistema salva o pedido no arquivo JSON.
7. O sistema exibe mensagem de sucesso.

**Fluxos de exceção:**

* Nome ou item não preenchidos → exibir erro
* Falha ao salvar dados → exibir erro

**Pós-condições:**

* Pedido registrado e armazenado no sistema

---

## 👨‍💻 Integrantes do Grupo

* Enrico Nikolay
* Giuliano Venceslau
* Lucas Sanson
* Eric Perez
