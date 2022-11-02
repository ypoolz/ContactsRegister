import os
import sqlite3

# Criação do DB:
conexao = sqlite3.connect('contatos.db')

c = conexao.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS tb_contatos (
    ID_CONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME_CONTATO CHAR,
    TELEFONE_CONTATO CHAR,
    EMAIL_CONTATO CHAR
    )
    ''')

conexao.commit()

conexao.close()

print('Tabela criada com sucesso')

# =========== Funções ============= #

# Criação da função de insirir dados:
def menuinserir():
    os.system('cls')
    vnome = input("Digite o Nome: ")
    vtelefone = input('Digite o telefone: ')
    vemail = input('Digite o E-mail: ')

    try:
        conexao = sqlite3.connect('contatos.db')
        c = conexao.cursor()

        c.execute("""
                INSERT INTO tb_contatos (NOME_CONTATO, TELEFONE_CONTATO, EMAIL_CONTATO)
                VALUES(?,?,?)
                """, (vnome, vtelefone, vemail))

        conexao.commit()

        conexao.close()
        print('Dados inseridos')
    except:
        print('Não foi possível inserir os dados.')

# Criação da função de consultar os dados:
def menuconsultar():
    os.system('cls')
    try:
        conexao = sqlite3.connect('contatos.db')
        c = conexao.cursor()
        c.execute("""
                SELECT * FROM tb_contatos;
                """)
        res = c.fetchall()
        vlimite = 10
        vcont = 0
        for r in res:
            print("ID: {0:<3} Nome: {1:<30} Telefone: {2:<17} E-mail: {3:<30}".format(r[0], r[1], r[2], r[3]))
            vcont += 1
            if vcont >= vlimite:
                vcont = 0


            os.system('cls')
            os.system('pause')
    except:
        print('Erro')

# Criação da função de consultar os dados pelo nome:
def menuconsultarnome():
    os.system('cls')
    try:
        v_nome = input('Digite o nome do contato: ')
        conexao = sqlite3.connect('contatos.db')
        c = conexao.cursor()
        v_sql = "SELECT * FROM tb_contatos WHERE NOME_CONTATO LIKE '%"+v_nome+"%'"
        c.execute(v_sql)
        res = c.fetchall()
        vlimite = 10
        vcont = 0
        for r in res:
            print("ID: {0:<3} Nome: {1:<30} Telefone: {2:<17} E-mail: {3:<30}".format(r[0],r[1],r[2],r[3]))
            vcont += 1
            if vcont >= vlimite:
                vcont = 0

                os.system('cls')
                os.system('pause')

        print('Resgistros encontrados')
        conexao.close()

        os.system('pause')

    except:
        print('Erro')

# Criação da função de atualizar os dados no DB:
def menuatualizar():
    os.system('cls')
    try:
        v_id_contato = input('Digite o ID do contato: ')
        conexao = sqlite3.connect('contatos.db')
        c = conexao.cursor()
        c.execute("""
        SELECT * FROM tb_contatos 
        WHERE ID_CONTATO = ?
        """, (v_id_contato,))
        r = c.fetchall()
        if len(r) > 0:
            print("ID:{0:_<3} Nome:{1:<30} Telefone: {2:<17} E-mail: {3:<30}".format(r[0][0], r[0][1], r[0][2], r[0][3])
                  )
            print('Resgistro encontrado')
            v_nome = input('Digite o novo Nome: ')
            if len(v_nome) == 0:
                v_nome = r[0][1]

            v_telefone = input('Digite o novo Telefone: ')
            if len(v_telefone) == 0:
                v_telefone = r[0][2]

            v_email = input('Digite o novo E-mail: ')
            if len(v_email) == 0:
                v_email = r[0][3]

            print('=====================================NOVOS DADOS=======================================')
            print(
                "ID:{0:_<3} Nome:{1:<30} Telefone: {2:<17} E-mail: {3:<30}".format(r[0][0], v_nome, v_telefone, v_email))
            decide = input('Confirme a alteração (S/N): ')
            if decide.upper() == 'S':
                try:
                    v_sql_atualiza = """UPDATE tb_contatos SET NOME_CONTATO = ?, TELEFONE_CONTATO = ?, EMAIL_CONTATO = ? 
                    WHERE ID_CONTATO = """ + v_id_contato
                    c.execute(v_sql_atualiza, (v_nome, v_telefone, v_email))
                    conexao.commit()

                    conexao.close()
                    print('Dados atualizados')
                except:
                    print('Erro')
        else:
            print('Registro não encontrado')
            os.system('pause')
    except:
        print('Erro')
        os.system('pause')

# Criação da função de deletar os dados:
def menudeletar():
    os.system('cls')
    try:
        v_id_contato = input('Digite o ID do contato: ')
        conexao = sqlite3.connect('contatos.db')
        c = conexao.cursor()
        c.execute("""SELECT * FROM tb_contatos 
        WHERE ID_CONTATO = ?""", (v_id_contato,))
        r = c.fetchall()
        if len(r) > 0:
            print("ID:{0:_<3} Nome:{1:<30} Telefone: {2:<17} E-mail: {3:<30}".format(r[0][0], r[0][1], r[0][2] ,r[0][3]))
            print('Registro Encontrado!')
            decide = input('Confirme a exclusão do registro acima (S/N):')
            if decide.upper() == 'S':
                try:
                    v_sql_deleta = """DELETE FROM tb_contatos 
                    WHERE ID_CONTATO = """ + v_id_contato
                    c.execute(v_sql_deleta)
                    conexao.commit()
                    conexao.close()
                    print('Registro deletado!')
                except:
                    print('erro')
                    os.system('pause')
        else:
            print('Registro não encontrado')
    except:
        print('Erro')
        os.system('pause')

# ========== MENU ============ #
# Menu a ser apresentado ao usuário: 
def menuprincipal():
    print("1 - Novo Registro")
    print("2 - Consultar Registros")
    print("3 - Consultar por Nome")
    print("4 - Atualizar Registro")
    print("5 - Deletar Registo")
    print("6 - Sair")


# Atribuição dos números as funções desenvolvidas anteriomente:
opc = 0
while opc != 6:
    menuprincipal()

    opc = int(input("Digite uma opcao : "))

    if opc == 1:
        menuinserir()

    elif opc == 2:
        menuconsultar()

    elif opc == 3:
        menuconsultarnome()

    elif opc == 4:
        menuatualizar()

    elif opc == 5:
        menudeletar()

    elif opc == 6:
        os.system('cls')
        print('Programa Finalizado')

    else:
        os.system('cls')
        print('Opção inválida')
        os.system('pause')
