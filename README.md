# BankPython 🐍 - Sistema de Banco Digital (CLI)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/ISO%2029148-Requisitos-green?style=for-the-badge" alt="ISO 29148">
  <img src="https://img.shields.io/badge/Ambiente-CLI-orange?style=for-the-badge" alt="Ambiente CLI">
</p>

O **BankPython** é uma aplicação de Linha de Comando (CLI) que simula um sistema de banco digital moderno, dinâmico e seguro. O projeto foi desenvolvido como o entregável final da disciplina de **Levantamento de Requisitos (LER)**, unindo uma especificação de software rigorosa com uma implementação limpa e robusta em Python.

---

## 📌 Sobre o Projeto

O objetivo principal deste projeto foi aplicar as diretrizes de engenharia de requisitos da norma **ISO/IEC/IEEE 29148:2018** em um cenário prático. O software gerencia de forma volátil as operações bancárias essenciais de um cliente único, integrando taxas automatizadas, controle inteligente de limite de cheque especial e gerenciamento otimizado de histórico em memória RAM.

### 🚀 Funcionalidades Principais
* **Abertura de Conta Prática (RF-001):** Cadastro rápido do titular com validação de aporte inicial e ativação opcional de limite emergencial.
* **Depósitos Instantâneos (RF-002):** Incremento de saldo em tempo real com validações de segurança para valores numéricos positivos.
* **Saque Inteligente (RF-003):** Processamento automatizado de saques calculando o custo da transação somado à **taxa fixa de R$ 2,50 (RN-002)**.
* **Integração com Cheque Especial (RN-001):** Permite a continuidade das operações de débito mesmo se o saldo real zerar, utilizando o limite de crédito aprovado.
* **Extrato Dinâmico Otimizado (RF-004 / RN-003):** Apresentação das **3 últimas movimentações** cronológicas, utilizando descarte em fila para otimização de memória.
* **Interface Fluida (RF-005 / RNF-004):** Terminal limpo automaticamente a cada operação, garantindo usabilidade e foco visual.

---

## 📐 Engenharia de Requisitos (Padrão ISO 29148)

A arquitetura do software foi totalmente guia pela documentação de requisitos. Abaixo estão destacados os pilares regulatórios do sistema:

### Regras de Negócio Fundamentais (RN)
* **RN-001 (Validação de Margem):** Um saque só é validado se $\text{Valor do Saque} + \text{Taxa} \le \text{Saldo Atual} + \text{Limite do Cheque Especial}$.
* **RN-002 (Tarifa Fixa):** Incidência fixa de **R$ 2,50** deduzida a cada saque bem-sucedido.
* **RN-003 (Fila de Extrato):** Retenção estrita das últimas 3 operações para simular restrição física de memória volátil.

### Requisitos Não-Funcionais de Destaque (RNF)
* **RNF-002 (Volatilidade):** Persistência de dados executada 100% em memória RAM através de estruturas nativas do Python.
* **RNF-003 (Robustez - *Anti-Crash*):** Tratamento preventivo de exceções (`try-except`) para erros de tipo `ValueError` (ex: digitação de letras em campos numéricos), impedindo a queda do sistema.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído de forma puramente nativa para demonstrar o domínio da lógica de programação e portabilidade da arquitetura:

* **Linguagem:** Python 3.x
* **Bibliotecas Nativas Utilizadas:**
    * `os`: Para manipulação e limpeza inteligente de buffers do terminal de acordo com o Sistema Operacional instalado (`cls` ou `clear`).