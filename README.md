# ChatBot com IA usando Python, Streamlit e OpenAI

## Sobre o projeto

Este projeto consiste em um **chatbot com Inteligência Artificial** desenvolvido em Python, utilizando **Streamlit** para criação da interface web e integração com a **API da OpenAI** para geração das respostas.

O usuário pode conversar diretamente com a IA através de uma interface semelhante a um chat. Durante a sessão, o histórico da conversa é armazenado utilizando o `session_state` do Streamlit, permitindo que o modelo receba o contexto das mensagens anteriores e mantenha a continuidade da conversa.

---

## Objetivo

O principal objetivo do projeto foi praticar a integração entre:

- aplicação Python;
- interface web;
- API externa;
- gerenciamento de estado;
- variáveis de ambiente;
- tratamento de erros.

O projeto também demonstra como construir uma aplicação simples de IA generativa utilizando Python do início ao fim.

---

## Tecnologias utilizadas

- Python
- Streamlit
- OpenAI API
- python-dotenv
- Git / GitHub

---

## Como funciona

O fluxo da aplicação é:

1. O usuário digita uma mensagem no campo de chat.
2. A mensagem é exibida na interface.
3. A mensagem é adicionada ao histórico da sessão.
4. O histórico da conversa é enviado para a API da OpenAI.
5. O modelo gera uma resposta.
6. A resposta é exibida na tela.
7. A resposta também é armazenada no histórico.
8. Na próxima mensagem, todo o contexto anterior é enviado novamente ao modelo.

Fluxo simplificado:

```text
Usuário
   ↓
Streamlit
   ↓
Histórico da conversa
   ↓
OpenAI API
   ↓
Resposta da IA
   ↓
Streamlit
   ↓
Usuário
```

---

# Gerenciamento do histórico

O histórico da conversa é armazenado através do `st.session_state`.

```python
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []
```

Cada mensagem possui duas informações principais:

```python
{
    "role": "user",
    "content": "Mensagem do usuário"
}
```

ou:

```python
{
    "role": "assistant",
    "content": "Resposta da IA"
}
```

Dessa forma, o modelo consegue identificar quem enviou cada mensagem.

---

## Exibição das mensagens

Antes de receber uma nova mensagem, o programa percorre todo o histórico e exibe as mensagens anteriores:

```python
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]

    st.chat_message(role).write(content)
```

Isso permite manter a conversa visível durante toda a sessão.

---

# Integração com a OpenAI

A conexão com a OpenAI é realizada utilizando o SDK oficial:

```python
from openai import OpenAI

modelo = OpenAI(api_key=api_key)
```

Quando o usuário envia uma mensagem, todo o histórico da conversa é enviado para o modelo:

```python
resposta_modelo = modelo.chat.completions.create(
    messages=st.session_state["lista_mensagens"],
    model="gpt-4o"
)
```

A resposta gerada é então recuperada:

```python
resposta_ia = resposta_modelo.choices[0].message.content
```

E exibida na interface:

```python
st.chat_message("assistant").write(resposta_ia)
```

---

# Proteção da API Key

A chave da API da OpenAI **não fica escrita diretamente no código**.

Ela é armazenada em um arquivo `.env`:

```env
OPENAI_API_KEY=sua_chave_da_openai_aqui
```

O projeto utiliza `python-dotenv` para carregar a variável:

```python
from dotenv import load_dotenv

load_dotenv()
```

Depois, a chave é acessada através das variáveis de ambiente:

```python
api_key = os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY")
```

Isso evita expor credenciais sensíveis no repositório.

> O arquivo `.env` não deve ser enviado para o GitHub.

O repositório utiliza um arquivo `.env.example` apenas como referência de configuração.

---

# Tratamento de erros

O projeto também possui tratamento de erros durante a comunicação com a API.

```python
try:
    resposta_modelo = modelo.chat.completions.create(...)
except OpenAIError:
    st.error(
        "Não foi possível obter uma resposta da OpenAI."
    )
```

Caso aconteça algum problema com:

- chave inválida;
- limite da API;
- conexão;
- erro na requisição;

a aplicação exibe uma mensagem amigável para o usuário em vez de encerrar inesperadamente.

---

# Interface com Streamlit

A interface foi construída utilizando componentes nativos do Streamlit.

### Título

```python
st.markdown(
    "<h1 style='text-align: center;'>ChatBot com IA</h1>",
    unsafe_allow_html=True
)
```

### Entrada de mensagens

```python
mensagem_usuario = st.chat_input(
    "Escreva sua mensagem aqui"
)
```

### Mensagem do usuário

```python
st.chat_message("user").write(mensagem_usuario)
```

### Mensagem da IA

```python
st.chat_message("assistant").write(resposta_ia)
```

---

# Executando o projeto localmente

## 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd CHAT_BOT
```

---

## 2. Crie um ambiente virtual

Windows:

```powershell
python -m venv .venv
```

Ative:

```powershell
.venv\Scripts\activate
```

---

## 3. Instale as dependências

```powershell
python -m pip install -r requirements.txt
```

---

## 4. Configure a API Key

Crie um arquivo `.env` baseado no `.env.example`.

Exemplo:

```env
OPENAI_API_KEY=sua_chave_da_openai_aqui
```

---

## 5. Execute a aplicação

```powershell
python -m streamlit run main.py
```

---

## 6. Abra no navegador

Normalmente o Streamlit será iniciado em:

```text
http://localhost:8501
```

---

# Estrutura do projeto

```text
CHAT_BOT/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### `main.py`

Contém a aplicação principal e toda a lógica do chatbot.

### `requirements.txt`

Contém as bibliotecas necessárias para executar o projeto.

### `.env.example`

Exemplo de configuração da variável de ambiente.

### `.gitignore`

Impede que arquivos sensíveis como `.env` sejam enviados ao GitHub.

---

# Conceitos praticados

Durante o desenvolvimento deste projeto foram utilizados conceitos como:

- integração com APIs;
- requisições para modelos de Inteligência Artificial;
- gerenciamento de estado;
- listas e dicionários em Python;
- estruturas condicionais;
- loops;
- tratamento de exceções;
- variáveis de ambiente;
- proteção de credenciais;
- desenvolvimento de interface web;
- gerenciamento de dependências.

---

# Possíveis melhorias futuras

O projeto pode evoluir com funcionalidades como:

- botão para limpar o histórico;
- seleção do modelo de IA;
- streaming das respostas;
- customização do comportamento da IA;
- mensagens de sistema;
- controle de limite de contexto;
- persistência das conversas em banco de dados;
- autenticação de usuários;
- histórico de conversas;
- deploy em nuvem;
- interface mais personalizada;
- integração com documentos e arquivos.

---

# Competências demonstradas

Este projeto demonstra conhecimentos em:

**Python • Streamlit • APIs REST • OpenAI API • IA Generativa • Gerenciamento de Estado • Tratamento de Erros • Variáveis de Ambiente • Git/GitHub**

---

## Conclusão

O projeto demonstra a construção de uma aplicação funcional de Inteligência Artificial, conectando uma interface web desenvolvida com Streamlit à API da OpenAI.

Além da integração com IA, foram aplicadas boas práticas como gerenciamento de estado, tratamento de erros e proteção de credenciais através de variáveis de ambiente.
