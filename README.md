# Envio Automático de E-mails

Este é um aplicativo Streamlit para automação do envio de e-mails a partir de um arquivo Excel. A aplicação permite que os usuários carreguem um arquivo Excel com os destinatários e enviem e-mails personalizados utilizando as credenciais de e-mail fornecidas.

## Funcionalidades disponíveis:

- **Upload de arquivo Excel**: Faça o upload de um arquivo Excel contendo os nomes e e-mails dos destinatários.
- **Envio Automático de E-mails**: O aplicativo envia e-mails personalizados para cada destinatário, substituindo o nome no corpo da mensagem.
- **Corpo de E-mail Padrão**: A mensagem e o assunto dos e-mails são predefinidos, garantindo consistência e rapidez no envio.

## Como usar :

### Instalação do Python:

Certifique-se de ter o Python 3.x instalado em seu computador. Se não tiver, você pode baixá-lo em [Python.org](https://www.python.org/).

### Executando o programa:

1. Clone ou baixe o arquivo `envio_email.py` deste repositório.
2. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo `envio_email.py` está localizado..
3. Digite `streamlit run envio_email.py` para iniciar o programa.

### Operações disponíveis:

Siga as instruções na interface para inserir suas credenciais de e-mail, carregar o arquivo Excel e enviar os e-mails.

## Funcionamento da Senha do E-mail:

A senha do seu e-mail é utilizada para autenticar sua conta no servidor SMTP e permitir o envio dos e-mails. A aplicação usa uma conexão segura (TLS) para proteger suas credenciais durante o envio. Por questões de segurança, é recomendado utilizar senhas de aplicativo (quando disponível), em vez da senha principal da sua conta de e-mail.

### Gerando Senhas de Aplicativo:

Para contas do Gmail:

1. Acesse sua conta Google e vá para as configurações de segurança.
2. Ative a verificação em duas etapas, se ainda não estiver ativada.
3. Crie uma senha de aplicativo específica para esta aplicação.

Utilize essa senha de aplicativo na entrada de senha da aplicação Streamlit.

## Contribuições:

Contribuições são bem-vindas! Sinta-se à vontade para sugerir melhorias, relatar problemas ou enviar pull requests.

## Autor:

- [Gustavo Coelho](https://github.com/Gustavo-gcr)
