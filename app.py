from infra import main as initialize_sys
import infra.data.bd_classes as initialize_db


if __name__ == "__main__":
    # cria o banco caso nao exista
    initialize_db.main()

    # inicializa o sistema
    initialize_sys.main()
