import smtplib
import os
from dotenv import load_dotenv
import email.message


def enviar(destinatario, codigo):
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

    from_email = msg["From"]
    to_email = msg["To"]


    s = smtplib.SMTP("smtp.gmail.com:587")
    s.starttls()
    s.login(email_rem, senha)
    s.sendmail(from_email, [to_email], msg.as_string().encode("utf-8"))


load_dotenv()

email_rem = os.getenv("EMAIL")
senha = os.getenv("SENHA")
