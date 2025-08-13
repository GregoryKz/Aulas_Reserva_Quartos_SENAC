from conexao_db import conectar


def listar():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id,numero_quarto,status,nome_cliente FROM quartos")
    for  id_, numero, status, cliente in cursor.fetchall():
        print(f"{id_} | {numero} | {status} | {cliente if cliente else '-'}")
    con.close

def adicionar():
    numero = input("Digite o numero do quarto:")
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO quartos(numero_quarto) VALUES (%s)", (numero,))
    con.commit()
    con.close()

def reservar():
    listar()
    id_ = input("Digite o ID do quarto:")
    nome = input("Digite o nome do cliente:")
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT status FROM quartos WHERE id=%s", (id_,))
    status = cursor.fetchone()
    if status and status[0] == 'Disponível':
        cursor.execute("UPDATE quartos SET  status = 'Reservado', nome_cliente = %s", (nome, id_))
        con.commit()
        print("Reserva feita!")
    else:
        print("Quarto indisponivel ou ivalido.")
        con.close()

def canecelar():
    listar()
    id_ = input("Digite o ID para cancelar a reserva:")
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT status FROM quartos WHERE id=%s", (id_))
    status = cursor.fetchone()
    if status and status[0] == 'Reservado':
        cursor.execute("SELECT status FROM quartos SET status ='Disponível', nome_cliente = NULL WHERE id=%s", (id_))    
        con.commit()
        print("Reserva Cancelada!")
    else:
        print("Quarto não esta reservado ou ivalido")
    con.close()

def menu ():
    

        

