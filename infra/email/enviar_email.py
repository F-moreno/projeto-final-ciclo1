import smtplib
import os
from dotenv import load_dotenv
import email.message

# criar um .env 
# EMAIL=sys.python.alpha@gmail.com
# SENHA=cblh wpyx qypg qcot

def enviar_email(destinatario, codigo):
    corpo_email = f"""
    <p>Olá,</p>
    <p>Você solicitou a recuperação da senha. Utilize o seguinte código para alterá-la: {codigo}</p>
    <p>Atenciosamente,</p>
    <p>Equipe de Suporte</p>
    """

    msg = email.message.Message()
    msg["Subject"] = "Recuperação de Senha"
    msg["From"] = email_rem
    msg["To"] = destinatario
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    s = smtplib.SMTP("smtp.gmail.com:587")
    s.starttls()
    s.login(email_rem, senha)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
    print("Email enviado com sucesso para", destinatario)


load_dotenv()

email_rem = os.getenv("email")
senha = os.getenv("senha")