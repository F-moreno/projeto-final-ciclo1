from infra import main as initialize_sys
import infra.data.entidades as initialize_db
import tests.bd.teste_bd as test


if __name__ == "__main__":
    # cria o banco caso nao exista
    initialize_db.main()

    # inicializa o sistema
    initialize_sys.main()
    
    # test.main()
