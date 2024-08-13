import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st
import pandas as pd

# Título da Aplicação
st.title('Envio de E-mails')

# Entradas do usuário
st.header('Insira suas credenciais de e-mail:')
email_user = st.text_input('Seu e-mail', placeholder='exemplo@gmail.com')
email_pass = st.text_input('Sua senha', type='password')

# Carregar o arquivo Excel com os destinatários
st.header('Carregue o arquivo Excel com os destinatários:')
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])

# Assunto do e-mail padrão
assunto = "Assunto do E-mail Padrão"

# Mensagem do e-mail padrão
mensagem_base = """
Olá <Nome>,

Email automático de teste,
"""

# Botão de Enviar E-mails
if st.button('Enviar E-mails'):
    if uploaded_file is not None and email_user and email_pass:
        # Ler os destinatários do Excel
        df = pd.read_excel(uploaded_file)

        # Configurações do servidor de e-mail
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        
        # Função para enviar e-mail
        def enviar_email(destinatario, assunto, mensagem):
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = destinatario
            msg['Subject'] = assunto

            # Corpo do e-mail
            msg.attach(MIMEText(mensagem, 'plain'))

            # Conectar ao servidor SMTP e enviar o e-mail
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()  # Conectar ao servidor usando TLS
                server.login(email_user, email_pass)  # Logar no servidor
                text = msg.as_string()
                server.sendmail(email_user, destinatario, text)  # Enviar e-mail
                st.success(f'E-mail enviado para {destinatario}')
            except Exception as e:
                st.error(f'Erro ao enviar e-mail para {destinatario}, verifique se sua senha foi gerada pelo Google app, a senha do seu email pessoal não irá funcionar. Verifique na sua conta do Google se a verificação de dois fatores está ligada e pesuise em "Senhas de app" para gerar a senha que funcionara para a API funcionar.: {str(e)}')
            finally:
                server.quit()  # Fechar a conexão com o servidor

        # Loop para enviar e-mails para todos os destinatários
        for index, row in df.iterrows():
            nome_destinatario = row['Nome']
            email_destinatario = row['Email']
            # Substituir <Nome> pelo nome do destinatário
            mensagem_personalizada = mensagem_base.replace('<Nome>', nome_destinatario)
            enviar_email(email_destinatario, assunto, mensagem_personalizada)
    else:
        st.warning('Por favor, preencha todos os campos e carregue o arquivo Excel.')
