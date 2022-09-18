import email
from http import server
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Importando informações como porta, email do remetente e destinatário, login e senha
from bd import senha, port as porta, host as hospedagem, login as remetente, to as destinatario, nome

# S M T P - Simple Mail Transfere Protocol
# para criar o servidor e enviar o email

# starta o servidor smtp
    # Declaração de valores de entrada e acesso 
host = hospedagem
port = porta
login = remetente
to = destinatario
password = senha

# Faz a conexão com servidor
server = smtplib.SMTP(host, port)

# Starta os requisitos de segurança para ativação
    #  fornece endereço IP do servidor SMTP
server.ehlo()
    # Inicializa a função de segurança "ransport layer security
server.starttls()

# Acessa a conta com os dados de login
server.login(login, password)

    #CORPO DE EMAIL TIPO MIME
corpo = f'''
            Olá, {nome}!
            segue abaixo seus dados para acessar nossa plataforma
            email: {to}
            senha: 

            não compartilhe sua senha com ninguêm!

            este é uma email automático, favor não responder :)
            '''

# Codifica a mensagem do email em tipo MIME
email_msg = MIMEMultipart()
email_msg ['From'] = login
email_msg ['To'] = to
email_msg ['Subject'] = "E-mail automático - Dados para acesso da plataforma"
email_msg.attach(MIMEText(corpo, 'Plain'))

# Envia o email tipo MIME no SERVIDOR SMTP
server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())

# Ecerra conexão com o servidor
server.quit()