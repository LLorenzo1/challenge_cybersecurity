# Challenge Cybersecurity

Este projeto foi desenvolvido como parte do **Challenge da disciplina de Cybersecurity** no curso de Engenharia de Software. O objetivo foi criar uma aplicação funcional com interface gráfica que implementasse **boas práticas de segurança**, desde autenticação até análise estática do código.

---

## Sobre o sistema

O sistema é composto por:

- Tela de login e cadastro
- Validação segura de senha e e-mail
- Interface feita com a biblioteca customtkinter
- Formulário de perfil de apostador
- Tela final com análise do perfil
- Registro de logs
- Token de sessão para controle de acessos
- Relatório de análise estática com bandit

---

## Requisitos de Segurança do Sistema

| Critério de Segurança                               | Atendido |
|-----------------------------------------------------|----------|
| Sanitização e validação de entradas                 | ✅       |
| Uso de SAST - análise estática (`bandit`)           | ✅       |
| Criptografia de senhas em repouso (`bcrypt`)        | ✅       |
| Geração de logs e auditoria (`logs.txt`)            | ✅       |
| Sessão segura com token (`session.json`)            | ✅       |

---

## Tecnologias utilizadas para montagem do sistema

- Python 3.10+
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- bcrypt
- pyjwt (para token)
- bandit (para SAST)

---

## Como rodar o projeto localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/LLorenzo1/challenge_cybersecurity.git
cd challenge_cybersecurity
```

2. **Crie e ative um ambiente virtual  (recomendado fazer):**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **Instale as dependências necessárias:**

```bash
pip install -r requirements.txt
```

4. **Execute o projeto:**

```bash
python main.py
```

5. **Importante: faça o cadastro antes de efetivamente logar no sistema**

Antes de acessar o sistema, é necessário **se cadastrar** utilizando o botão "Cadastre-se" na tela de login.

> O login só funcionará após o cadastro ser concluído com sucesso.


6. **Verifique os arquivos na pasta `/data`**

Após o uso do sistema, você pode conferir os dados que foram gerados na pasta `data/`, como:

- `users.json`: usuários que foram cadastrados e as senhas criptografadas
- `session.json`: controle de sessão ativa
- `logs.txt`: registro de ações que foram feitas no sistema

---

## Rodando o relatório de segurança com Bandit (SAST)

> Bandit é uma ferramenta de análise estática de código que detecta vulnerabilidades em projetos Python.

1. **Instale o Bandit:**

```bash
pip install bandit
```

2. **Rode a análise no projeto:**

```bash
bandit -r . > relatorio_bandit.txt
```

> O arquivo `relatorio_bandit.txt` será gerado automaticamente com todos os alertas e verificações.

---

## Estrutura de Diretórios

```plaintext
.
├── auth/
│   ├── login.py
│   └── register.py
├── form/
│   └── questions.py
├── logs/
│   └── logger.py
├── security/
│   ├── hashing.py
│   └── token.py
├── data/
│   ├── users.json
│   ├── session.json
│   └── logs.txt
├── main.py
├── requirements.txt
└── relatorio_bandit.txt
```

---

## Segurança implementada

- Criptografia forte com `bcrypt`
- Validação de senha com número e caractere especial
- Tokens de sessão UUID
- Verificação de sessão ativa antes de acessar o formulário
- Registro de logs de todas as ações relevantes
- Análise estática com `bandit`

---

## Projeto Desenvolvido por:

- Lorenzo Ferreira (RM 97318)
- Fabrício Saavedra (RM 97631)
- Guilherme Morais (RM 551981)
- Açussena Macedo (RM 552568)
- Guilherme Akio (RM 98582)
- 3º Ano de Engenharia de Software – FIAP  
- Disciplina: Cybersecurity
