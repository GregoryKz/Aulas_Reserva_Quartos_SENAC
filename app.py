from conexao_db import conectar

def listar():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id, numero_quarto, status, nome_cliente FROM quartos")
    for id_, numero, status, cliente in cursor.fetchall():
        print(f"{id_} | {numero} | {status} | {cliente if cliente else '-'}")
    con.close()


def adicionar():
    numero = input("Digite o número do quarto: ")
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO quartos (numero_quarto, status) VALUES (%s, 'Disponível')", (numero,))
    con.commit()
    con.close()
    print("Quarto adicionado com sucesso!")


def reservar():
    listar()
    id_ = input("Digite o ID do quarto: ")
    nome = input("Digite o nome do cliente: ")
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT status FROM quartos WHERE id=%s", (id_,))
    status = cursor.fetchone()
    if status and status[0] == 'Disponível':
        cursor.execute("UPDATE quartos SET status = 'Reservado', nome_cliente = %s WHERE id = %s", (nome, id_))
        con.commit()
        print("Reserva feita com sucesso!")
    else:
        print("Quarto indisponível ou inválido.")
    con.close()


def cancelar():
    listar()
    id_ = input("Digite o ID para cancelar a reserva: ")
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT status FROM quartos WHERE id=%s", (id_,))
    status = cursor.fetchone()
    if status and status[0] == 'Reservado':
        cursor.execute("UPDATE quartos SET status = 'Disponível', nome_cliente = NULL WHERE id=%s", (id_,))
        con.commit()
        print("Reserva cancelada com sucesso!")
    else:
        print("Quarto não está reservado ou inválido.")
    con.close()


def menu():
    while True:
        print("=== MENU ===")
        print("1 - Inserir Quarto")
        print("2 - Listar Quartos")
        print("3 - Reservar Quarto")
        print("4 - Cancelar Reserva")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            reservar()
        elif opcao == "4":
            cancelar()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")



if __name__ == "__main__":
    menu()

        

