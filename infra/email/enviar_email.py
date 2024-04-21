import smtplib
import os
from dotenv import load_dotenv
import email.message


def enviar(destinatario, codigo):
    corpo_email = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            .container {{
                width: 80%;
                margin: auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f9f9f9;
            }}
            .logo {{
                text-align: center;
                margin-bottom: 20px;
            }}
            img {{
                max-width: 100%;
                height: auto;
            }}
            .message {{
                margin-bottom: 20px;
            }}
            .code {{
                font-size: 20px;
                font-weight: bold;
                background-color: #f5f5f5;
                padding: 10px;
                border-radius: 5px;
                display: inline-block;
            }}
            .signature {{
                margin-top: 20px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="message">
                <p>Olá,</p>
                <p>Você solicitou a recuperação da senha. Utilize o seguinte código para alterá-la:</p>
                <p class="code">{codigo}</p>
            </div>
            <div class="signature">
                <p>Atenciosamente,</p>
                <p>Equipe de Suporte</p>
            </div>
        </div>
    </body>
    </html>
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

