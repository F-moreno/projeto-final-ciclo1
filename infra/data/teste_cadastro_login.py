from gestao_usuarios import *

cadastro_cliente("Artur",
                    "12345678912",
                    "1234567",
                    "Gedeão Dias de Sousa",
                    "Rua Sofia Imbiriba, 18, Liberdade, Santarém-PA, Brasil",
                    "30-05-2005",
                    "93988149930",
                    "art@gmail.com"
                     )

cadastro_funcionario("Artur",
                    "12345678912",
                    "93988149930",
                    "art@gmail.com",
                    "artur123"
                    )

sessao = iniciar_sessao("12345678912", "artur123")
print(sessao.funcionario.cpf)

encerrar_sessao(sessao)
