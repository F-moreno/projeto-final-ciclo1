from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QTreeWidgetItem,
    QWidget,
    QLabel,
    QTableWidgetItem,
    QListWidgetItem,
    QListWidget,
)
from infra.data import bd_classes, gerenciamento
from infra.ui.ui_login import Ui_Form
from infra.ui.ui_sistema import Ui_MainWindow
import sys
from infra.func.ocr import TesseractOCR


class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_entrar_login.clicked.connect(self.abrir_sistema)
        self.btn_cadastrar_login.clicked.connect(self.mostrar_pag_cadastro)
        self.btn_config.clicked.connect(self.mostrar_pag_config)
        self.btn_closed.clicked.connect(self.close)
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)
        self.btn_padrao.clicked.connect(self.padrao_configuracao)
        self.btn_salvar.clicked.connect(self.salvar_configuracao)

    def abrir_sistema(self):
        usuario = self.txt_cpf_login.text()
        senha = self.txt_senha_login.text()

        try:
            sessao = gerenciamento.iniciar_sessao(usuario, senha)
            self.abrir_main_window(sessao)
        except:
            QMessageBox.warning(self, "Login", "Usuário ou senha inválidos!")

    def validar_cpf(self, cpf):
        cpf = "".join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9)) % 11
        digito_verif_1 = 0 if soma < 2 else 11 - soma

        if int(cpf[9]) != digito_verif_1:
            return False

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10)) % 11
        digito_verif_2 = 0 if soma < 2 else 11 - soma

        if int(cpf[10]) != digito_verif_2:
            return False

        return True

    def validar_email(self, email):
        # Verifica se o e-mail possui um "@" e pelo menos um ponto após o "@"
        if "@" in email and "." in email[email.index("@") :]:
            return True
        else:
            return False

    def cadastrar_usuario(self):
        nome = self.txt_nome_cadastro.text()
        cpf = self.txt_cpf_cadastro.text()
        email = self.txt_email_cadastro.text()
        telefone = self.txt_telefone_cadastro.text()
        senha = self.txt_senha_cadastro.text()

        if email.lower() != "teste":
            if not self.validar_email(email):
                QMessageBox.warning(
                    self, "E-mail Inválido", "Por favor, insira um e-mail válido."
                )
                return

            if not self.validar_cpf(cpf):
                QMessageBox.warning(
                    self, "CPF Inválido", "Por favor, insira um CPF válido."
                )
                return

        gerenciamento.cadastro_funcionario(
            nome=nome, cpf=cpf, email=email, telefone=telefone, senha=senha
        )

        QMessageBox.information(self, "Cadastro", "Usuário cadastrado com sucesso!")
        self.limpar_campos_cadastro()

    def limpar_campos_cadastro(self):
        self.txt_nome_cadastro.clear()
        self.txt_cpf_cadastro.clear()
        self.txt_email_cadastro.clear()
        self.txt_telefone_cadastro.clear()
        self.txt_senha_cadastro.clear()

    def mostrar_pag_cadastro(self):
        self.Pages.setCurrentWidget(self.pg_cadastrar)

        # Conectar o botão de cadastrar ao método cadastrar_usuario
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)

    def abrir_main_window(self, sessao):
        self.w = MainWindow(sessao)
        self.w.show()
        self.w.showMaximized()
        self.close()

    def mostrar_pag_cadastro(self):
        self.Pages.setCurrentWidget(self.pg_cadastrar)

    def mostrar_pag_config(self):
        self.Pages.setCurrentWidget(self.pg_config)

        configuracao = bd_classes.get_config()
        if configuracao:
            ip = configuracao["db_host"]
            porta = configuracao["db_port"]
            self.txt_ip.setText(ip)
            self.txt_porta.setText(porta)
        else:
            QMessageBox.information(
                self, "Configuração", "Configuração do banco de dados não encontrada!"
            )

    def salvar_configuracao(self):
        ip = self.txt_ip.text()
        porta = self.txt_porta.text()
        bd_classes.set_config(db_host=ip, db_port=porta)
        QMessageBox.information(
            self,
            "Configuração",
            "Configuração do banco de dados atualizada com sucesso!",
        )

    def padrao_configuracao(self):
        self.txt_ip.setText("localhost")
        self.txt_porta.setText("5432")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, sessao):
        super(MainWindow, self).__init__()
        self.sessao = sessao
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro de Áreas Remotas")
        self.btn_toogle.clicked.connect(self.left_menu)
        self.btn_home_menu.clicked.connect(self.mostrar_pag_home)
        self.btn_cadastrar_menu.clicked.connect(self.mostrar_pag_cadastro)
        self.btn_historico_menu.clicked.connect(self.mostrar_pag_historico)
        self.btn_enviar_menu.clicked.connect(self.mostrar_pag_enviar_doc)
        self.btn_perfil_menu.clicked.connect(self.mostrar_pag_perfil)
        self.btn_alterar_dados.clicked.connect(self.mostrar_pag_alteracao_perfil)
        self.btn_carregar_formulario.clicked.connect(self.abrir_arquivo)
        self.btn_encerrar_menu.clicked.connect(self.close)
        self.btn_arquivo_documento.clicked.connect(self.carregar_arquivo)
        self.btn_enviar_arquivo.clicked.connect(self.enviar_docs)
        self.btn_carregar_documentos.clicked.connect(self.carregar_docs_cadastro)
        self.btn_cadastro_enviar.clicked.connect(self.enviar_cadastrar_cliente)
        self.btn_limpar_formulario.clicked.connect(self.limpar_formulario)
        self.btn_remover_doc.clicked.connect(self.remover_documento)
        self.btn_remover_lista_cadastro.clicked.connect(self.remover_doc_cadastro)
        self.btn_limpar_lista_cadastro.clicked.connect(self.limpar_docs_cadastro)
        self.lista_de_imagens = []
        self.documento_selecionado = None

    def left_menu(self):
        width = self.menu.width()

        if width == 0:
            newWidth = 200
        else:
            newWidth = 0
        self.animation = QtCore.QPropertyAnimation(self.menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    def mostrar_pag_home(self):
        self.Pages.setCurrentWidget(self.pg_home)

    ############################################################
    ######## Página de envio de Documentos Genéricos ###########
    # Essas funções terão que permitir ao usuário escolher o tipo
    # do arquivo que vai enviar e ao clicar no botão de envio
    # esse documento subir para o banco.

    def mostrar_pag_enviar_doc(self):
        self.Pages.setCurrentWidget(self.pg_enviar_doc)

    def carregar_arquivo(self):
        options = QFileDialog.Option()
        nomeArquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecione o Arquivo",
            "",
            "Imagens (*.png *.jpg *.jpeg *.bmp *.gif)",
            options=options,
        )
        if nomeArquivo:
            self.documento_selecionado = nomeArquivo
            self.atualizar_documento_selecionado()
            
    def atualizar_documento_selecionado(self):
        if self.documento_selecionado:
            pixmap = QPixmap(self.documento_selecionado)
            self.amostra_imagem.setPixmap(pixmap)
            self.btn_remover_doc.setEnabled(True)
            self.lista_envio_documento.clear()
            self.lista_envio_documento.addItem(self.documento_selecionado)
        else:
            self.amostra_imagem.clear()
            self.btn_remover_doc.setEnabled(False)   
            
    def remover_documento(self):
        self.documento_selecionado = ""
        self.lista_envio_documento.clear()
        self.atualizar_documento_selecionado()    
        
    def mostrar_documento_selecionado(self, item):
        pixmap = QPixmap(item.text())
        self.amostra_imagem.setPixmap(pixmap)  
        
               
    def enviar_docs(self):
        print("Arquivo enviado com sucesso!")
        # btn_arquivo_documento
        # btn_enviar_arquivo
        # tipo_documento

    ##############################################################################
    #########Página de exibição de Perfil e alteração de Dados básicos############
    # Essas funções deverão permitir que ao usuário visualizar seus dados básico de
    # Perfil, que ele ao clicar no botão de alterar perfil a página de alteração
    # seja aberta e o usuário possa adicionar novos valores para os dados que quer
    # alterar. Ao clicar em salvar os dados serão atualizados no Banco de Dados.
    # Um ponto importante é que para exibir esses dados iniciais precisamos ter
    # um retorno do Banco com esses dados do usuário no momento que ele fizer login.

    def mostrar_pag_perfil(self):
        sessao = self.sessao

        if sessao:
            informacoes = sessao.funcionario
            if informacoes:
                self.txt_nome_perfil.setText(informacoes.nome)
                self.txt_email_perfil.setText(informacoes.email)
                self.txt_telefone_perfil.setText(informacoes.telefone)
                self.Pages.setCurrentWidget(self.pg_perfil)
            else:
                QMessageBox.information(
                    self, "Perfil", "Informações do usuário não encontradas!"
                )
        else:
            QMessageBox.information(
                self, "Perfil", "Sessão inválida! Faça login novamente."
            )

    def limpar_campos_alteracao(self):
        self.txt_perfil_alterar_nome.clear()
        self.txt_perfil_alterar_email.clear()
        self.txt_perfil_alterar_telefone.clear()

    def mostrar_pag_alteracao_perfil(self):
        self.Pages.setCurrentWidget(self.pg_alteracao_perfil)
        self.btn_salvar_alteracoes.clicked.connect(self.salvar_alteracoes_perfil)

    def salvar_alteracoes_perfil(self):
        novo_nome = self.txt_perfil_alterar_nome.text()
        novo_email = self.txt_perfil_alterar_email.text()
        novo_telefone = self.txt_perfil_alterar_telefone.text()

        if novo_nome or novo_email or novo_telefone:
            self.sessao.funcionario.atualizar(
                nome=novo_nome, email=novo_email, telefone=novo_telefone
            )
            QMessageBox.information(self, "Sucesso", "Perfil atualizado com sucesso!")
            self.limpar_campos_alteracao()

        else:
            QMessageBox.warning(self, "Aviso", "Nenhuma alteração foi feita.")

    def mostrar_pag_cadastro(self):
        self.Pages.setCurrentWidget(self.pg_cadastrar)

    def carregar_docs_cadastro(self):
        options = QFileDialog.Option()
        nomeArquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecione o Arquivo",
            "",
            "Imagens (*.png *.jpg *.jpeg *.bmp *.gif)",
            options=options,
        )
        if nomeArquivo:
            self.lista_de_imagens.extend([nomeArquivo])
            self.atualizar_lista()
            
    def limpar_formulario(self):
        self.txt_cadastro_nome.clear()
        self.txt_cadastro_cpf.clear()
        self.txt_cadastro_rg.clear()
        self.txt_cadastro_filiacao.clear()
        self.txt_cadastro_endereco.clear()
        self.txt_cadastro_nascimento.clear()
        self.txt_cadastro_cidade.clear()
        self.txt_cadastro_estado.clear()
        self.txt_cadastro_telefone.clear()
        self.txt_cadastro_email.clear()
        
    def remover_doc_cadastro(self):
        if self.lista_documentos_cadastro.currentItem():
            item = self.lista_documentos_cadastro.currentRow()
            del self.lista_de_imagens[item]
            self.lista_documentos_cadastro.takeItem(item)
    def limpar_docs_cadastro(self):
        self.lista_documentos_cadastro.clear()
        self.lista_de_imagens.clear()
        self.limpar_imagem_selecionada()
        self.miniatura_documento.setText("Amostra de Imagem")
        
    def atualizar_lista(self):
        self.lista_documentos_cadastro.clear()

        if self.lista_de_imagens: 
            for imagem in self.lista_de_imagens:
                pixmap = QPixmap(imagem)
                icon = QIcon(pixmap)
                item = QListWidgetItem(icon, imagem)
                item.setSizeHint(QSize(50, 50))
                self.lista_documentos_cadastro.addItem(item)

        self.lista_documentos_cadastro.setViewMode(QListWidget.IconMode)
        self.lista_documentos_cadastro.itemClicked.connect(
            self.mostrar_imagem_selecionada
        )
        
    def limpar_imagem_selecionada(self):
        self.miniatura_documento.clear()

    def enviar_cadastrar_cliente(self):
        nome = self.txt_cadastro_nome.text()
        cpf = self.txt_cadastro_cpf.text()
        rg = self.txt_cadastro_rg.text()
        filiacao = self.txt_cadastro_filiacao.text()
        endereco = self.txt_cadastro_endereco.text()
        data_nascimento = self.txt_cadastro_nascimento.text()
        cidade = self.txt_cadastro_cidade.text()
        estado = self.txt_cadastro_estado.text()
        telefone = self.txt_cadastro_telefone.text()
        email = self.txt_cadastro_email.text()

        # Verifica se todos os campos obrigatórios estão preenchidos
        if not nome or not cpf or not data_nascimento:
            QMessageBox.warning(
                self, "Campos obrigatórios", "Preencha todos os campos obrigatórios."
            )
            return

        # Insere o cliente no banco de dados
        # try:
        #     sessao = gerenciamento.get_sessoes(cpf=cpf)
        #     novo_cliente = session.cadastrar_cliente(
        #         nome=nome,
        #         cpf=cpf,
        #         rg=rg,
        #         filiacao=filiacao,
        #         endereco=endereco,
        #         data_nascimento=data_nascimento,
        #         cidade=cidade,
        #         estado=estado,
        #         telefone=telefone,
        #         email=email,
        #     )
        # except Exception as e:
        #     QMessageBox.critical(self, "Erro", f"Erro ao cadastrar cliente: {str(e)}")
        #     print(e)
        #     return

        # # Insere os documentos associados ao cliente no banco de dados
        # for caminho_documento in self.lista_de_imagens:
        #     try:
        #         documento = session.salvar_documento(
        #             titulo="Formulario de Cadastro",
        #             tipo="Formulario de Cadastro",
        #             arquivo_original=caminho_documento.binarizado,
        #             conteudo="Conteudo do Documento",
        #             cliente=novo_cliente,
        #         )
        #     except Exception as e:
        #         QMessageBox.critical(
        #             self, "Erro", f"Erro ao cadastrar documento: {str(e)}"
        #         )
        #         return

        QMessageBox.information(self, "Sucesso", "Cliente cadastrado com sucesso!")

    def mostrar_imagem_selecionada(self, item):
        pixmap = QPixmap(item.text())
        self.miniatura_documento.setPixmap(pixmap)

    def abrir_arquivo(self):
        options = QFileDialog.Option()
        nomeArquivo, _ = QFileDialog.getOpenFileName(
            self, "Selecione o Arquivo", "", "All Files(*)", options=options
        )
        if nomeArquivo:
            print("Arquivo selecionado", nomeArquivo)
            texto = TesseractOCR().read_text(nomeArquivo)
            image = TesseractOCR().read_image(nomeArquivo)
            json = TesseractOCR().read_json(texto)
            print(json)
            self.txt_cadastro_nome.setText(json.get("nome", ""))
            self.txt_cadastro_cpf.setText(json.get("cpf", ""))
            self.txt_cadastro_rg.setText(json.get("rg", ""))
            self.txt_cadastro_filiacao.setText(json.get("filiacao", ""))
            self.txt_cadastro_nascimento.setText(json.get("nascimento", ""))
            self.txt_cadastro_endereco.setText(json.get("endereco", ""))
            self.txt_cadastro_cidade.setText(json.get("cidade", ""))
            self.txt_cadastro_estado.setText(json.get("estado", ""))
            self.txt_cadastro_telefone.setText(json.get("telefone", ""))
            self.txt_cadastro_email.setText(json.get("email", ""))

    #################################################################################
    ################## Página de Exibição do Histórico ##############################
    # Essas funções tratarão da exibição do histórico de cadastros realizados por
    # aquele usuário. Portanto teremos a necessidade de funções que busquem um SELECT
    # no BD com os cadastros daquele usuário.

    def mostrar_pag_historico(self):
        self.Pages.setCurrentWidget(self.pg_historico)

        # Chama a função do módulo de gerenciamento para buscar os clientes
        documentos = gerenciamento.get_documentos(
            fk_funcionario=self.sessao.funcionario.id
        )
        doc_clientes = gerenciamento.get_documentos(
            fk_funcionario=self.sessao.funcionario.id, tipo="Teste"
        )

        # Configurando o número de linhas e colunas na tabela
        self.tabela_historico_cadastros.setRowCount(len(doc_clientes))
        self.tabela_historico_cadastros.setColumnCount(3)  # Exemplo: 3 colunas
        self.tabela_historico_documentos.setRowCount(len(doc_clientes))
        self.tabela_historico_documentos.setColumnCount(5)

        # Preenchendo a tabela com os dados dos clientes
        for i, documento in enumerate(doc_clientes):
            self.tabela_historico_cadastros.setItem(
                i, 0, QTableWidgetItem(documento.cliente.nome)
            )

            self.tabela_historico_cadastros.setItem(
                i, 1, QTableWidgetItem(documento.cliente.telefone)
            )
            self.tabela_historico_cadastros.setItem(
                i,
                2,
                QTableWidgetItem(
                    documento.registro.horario.strftime("%d/%m/%Y %H:%M:%S")
                ),
            )

        for i, documento in enumerate(documentos):
            if documento.cliente:
                self.tabela_historico_documentos.setItem(
                    i, 0, QTableWidgetItem(documento.cliente.nome)
                )
                self.tabela_historico_documentos.setItem(
                    i, 3, QTableWidgetItem(documento.cliente.telefone)
                )

            self.tabela_historico_documentos.setItem(
                i, 1, QTableWidgetItem(documento.titulo)
            )
            self.tabela_historico_documentos.setItem(
                i, 2, QTableWidgetItem(documento.tipo)
            )
            self.tabela_historico_documentos.setItem(
                i,
                4,
                QTableWidgetItem(
                    documento.registro.horario.strftime("%d/%m/%Y %H:%M:%S")
                ),
            )


def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
