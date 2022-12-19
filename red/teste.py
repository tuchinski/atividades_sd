# FEITO! • Inserção na tabela Matricula (notas e faltas são inseridas com valor padrão 0).
# FEITO! • Alteração notas na tabela Matricula.
# FEITO! • Alteração faltas na tabela Matricula.
# FEITO! • Listagem de alunos (RA, nome, período) de uma disciplina informado a disciplina, ano e semestre. 
# FEITO! • Listagem de disciplinas, faltas e notas (RA, nome, nota, faltas) de um aluno informado o ano e semestre.

import socket
import threading
import pythoncode.notas_pb2 as proto
import sqlite3

conexao_bd = "database_com_dados-contrib-Daniel-Farina.db"

GET_ALL_CURSOS = "SELECT * FROM curso"

def mainTeste():

    testeheader = proto.Header()
    testeheader.tamanhoMensagem = 5000
    print(len(testeheader.SerializeToString()))
    # conn = sqlite3.connect(conexao_bd)
    # cursor = conn.cursor()
    # cursos = cursor.execute(GET_ALL_CURSOS)

    # lista_cursos = proto.ListaCursos()

    # print(cursos.fetchall())

    # for curso in cursos.fetchall():
    #     curso_proto = lista_cursos.cursos.add()
    #     curso_proto.codigo = curso[0]
    #     curso_proto.nome = curso[1]
        # print(curso)

    # print(lista_cursos)

    # for t in lista_cursos.cursos:
    #     print(t.codigo)

    # coisa_teste = proto.Curso()
    # coisa_teste.codigo = 1
    # coisa_teste.nome = "teste"

    # msg = coisa_teste.SerializeToString()

    # teste = coisa_teste = proto.Curso()

    # teste.ParseFromString(msg)
    # print("---------------------")
    # print(teste)


    # print(busca_alunos_por_disciplina("GA3X11", 2018, 6, conn))
    # print(lista_disciplinas_aluno_por_semestre(18, 2019, 3, conn))
    # print(alterar_faltas_matricula(23, "BCC36B", 2019, 7, 5, conn))
    # print(alterar_nota_matricula(23, "BCC36B", 2019, 7, 1.2, conn))
    # print(inserir_matricula(49, 'LM31A', "2022", 2, conn))

    # req = proto.Request()
    # # req.rm = proto.RequestMatricula()
    # req.rm.tipoRequest = 1
    # req.rm.matricula.RA = 49
    # req.rm.matricula.cod_disciplina = 'LM31A'
    # req.rm.matricula.ano = 2022
    # req.rm.matricula.semestre = 3

    # a = req.SerializeToString()
    # print(a)

    # req2 = proto.Request()
    # req2.rl.tipoRequest = 1
    # req2.rl.ano = 2019
    # req2.rl.semestre = 2
    # req2.rl.ra = 12
    
    # a2 = req2.SerializeToString()
    # print(a2)

    # # print(req)

    # teste = proto.Request()
    # print("-----------------")
    # print(teste.ParseFromString(a2))
    # print(teste)
    # print(teste.HasField("rm"))


def processa_request(request: bytes, db_conn: sqlite3.Connection):
    req_proto = proto.Request()
    req_proto.ParseFromString(request)

    if req_proto.HasField("rm"):
        tipo_request = req_proto.rm.tipoRequest
        ra = req_proto.rm.matricula.RA
        cod_disciplina = req_proto.rm.matricula.cod_disciplina
        ano = req_proto.rm.matricula.ano
        semestre = req_proto.rm.matricula.semestre
        nota = req_proto.rm.matricula.nota
        faltas = req_proto.rm.matricula.faltas

        if tipo_request == 1:
            # Inserindo matricula
            return inserir_matricula(ra, cod_disciplina, ano, semestre, db_conn).SerializeToString()

        elif tipo_request == 2:
            # Alterando nota
            return alterar_nota_matricula(ra, cod_disciplina, ano, semestre, nota, db_conn).SerializeToString()

        elif tipo_request == 3:
            # Alterando falta
            return alterar_faltas_matricula(ra, cod_disciplina, ano, semestre, faltas, db_conn).SerializeToString()

        else:
            pass
    elif req_proto.HasField("rl"):
        tipo_request = req_proto.rl.tipoRequest
        ano = req_proto.rl.ano
        semestre = req_proto.rl.semestre
        ra = req_proto.rl.ra
        cod_disciplina = req_proto.rl.cod_disciplina
        if tipo_request == 1:
            # lista alunos
            return busca_alunos_por_disciplina(cod_disciplina, ano, semestre, db_conn)
        elif tipo_request == 2:
            # Lista disciplina, notas e faltas do aluno
            return lista_disciplinas_aluno_por_semestre(ra, ano, semestre, db_conn)
        else:
            pass

def conexao_recebida(conn: socket.socket, addr: tuple):
    db_conn = sqlite3.connect(conexao_bd)
    print(f"Conexao de {addr}")
    while True:
        # Recebe o cabecalho do cliente pra saber qual o tamanho da request
        cabecalho = conn.recv(2)
        if not cabecalho:
            break
        cabecalho_proto = proto.Header()
        cabecalho_proto.ParseFromString(cabecalho)

        # Espera a request com o tamanho enviado no cabeçalho
        request = conn.recv(cabecalho_proto.tamanhoMensagem)
        teste = proto.Request()
        teste.ParseFromString(request)

        # processa a request e retorna para o user
        retorno = processa_request(request, db_conn)

        # cria o cabeçalho de retorno, para informar ao cliente o tamanho da request
        header = proto.Header()
        header.tamanhoMensagem = len(retorno)

        # envia o cabeçalho
        conn.sendall(header.SerializeToString())

        # envia o response
        conn.sendall(retorno)

def main():

    HOST = "127.0.0.1"  
    PORT = 8080

    print("Iniciando server")
    db_conn = sqlite3.connect(conexao_bd)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # desocupa a porta assim que o server é finalizado
        s.bind((HOST,PORT))
        s.listen()

        while True:
            conn,addr = s.accept()
            threading.Thread(target=conexao_recebida, args=(conn,addr,)).start()
        
            


def valida_codigo_disciplina(cod_disciplina: str, conn: sqlite3.Connection):
    """
    Valida se o código de uma disciplina existe
    """
    SELECT_VALIDA_DISCIPLINA = "select 1 from Disciplina where codigo = ?"
    
    cursor = conn.cursor()
    result = cursor.execute(SELECT_VALIDA_DISCIPLINA, (cod_disciplina,))
    if result.fetchall():
        return True
    else: 
        return False


# Listagem de alunos (RA, nome, período) de uma disciplina informado a disciplina, ano e semestre. 
def busca_alunos_por_disciplina(cod_disciplina: str, ano:int, semestre: int, conn:sqlite3.Connection) -> proto.ListaAlunos:
    """
    Busca os alunos de acordo com o cod_disciplina, ano e semestre desejado
    
    Caso encontre ou não, utiliza a message ReturnListaAlunos
    """
    SELECT_BUSCA_ALUNOS_DISCIPLINA = "select a.* from Aluno A, disciplina d, Matricula m where d.codigo = m.cod_disciplina AND m.ra = a.ra and d.codigo = ? and ano = ? and semestre = ?"
    retorno = proto.ReturnListaAlunos()

    # verifica se o código informado existe
    # se não existir, retorna isso com uma msg padrão
    if not valida_codigo_disciplina(cod_disciplina, conn):
        retorno.sucesso = False
        retorno.mensagem = "Codigo da disciplina invalido"
        return retorno

    # busca as disciplinas, e insere no response correspondente 
    cursor = conn.cursor()
    result = cursor.execute(SELECT_BUSCA_ALUNOS_DISCIPLINA, (cod_disciplina, ano, semestre))
    for aluno in result.fetchall():
        aluno_curso = retorno.listaAlunos.alunos.add()
        aluno_curso.RA = aluno[0]
        aluno_curso.nome = aluno[1]
        aluno_curso.periodo = aluno[2]
        aluno_curso.cod_curso = aluno[3]
    retorno.sucesso = True
    retorno.mensagem = "Sucesso ao buscar os alunos"
    return retorno

# Listagem de disciplinas, faltas e notas (RA, nome, nota, faltas) de um aluno informado o ano e semestre.
def lista_disciplinas_aluno_por_semestre(ra: int, ano: int, semestre: int, conn: sqlite3.Connection):
    ''''
    Lista as disciplinas de um aluno informando seu RA, ano e semestre desejado
    '''
    SELECT_DISCIPLINA_ALUNO_POR_SEMESTRE = 'select a.ra, d.nome, m.nota, m.faltas from Aluno a, Disciplina d, Matricula m where d.codigo = m.cod_disciplina and a.ra = m.ra and a.ra = ? and m.ano = ? and m.semestre = ?'
    cursor = conn.cursor()
    result = cursor.execute(SELECT_DISCIPLINA_ALUNO_POR_SEMESTRE,(ra, ano, semestre))
    lista_disciplinas = proto.ReturnListaMatriculas()
    for resultado in result:
        retorno_matricula = lista_disciplinas.matriculas.add()
        retorno_matricula.ra = resultado[0]
        retorno_matricula.nome_disciplina = resultado[1]
        retorno_matricula.nota = resultado[2]
        retorno_matricula.faltas = resultado[3]
    lista_disciplinas.sucesso = True
    lista_disciplinas.mensagem = "Sucesso ao buscar disciplinas do aluno"
    return lista_disciplinas

# Alteração faltas na tabela Matricula.
def alterar_faltas_matricula(ra: int, cod_disciplina: str, ano: str, semestre:str, faltas: int, conn: sqlite3.Connection): 
    '''
    Altera as faltas da matricula especificada
    '''
    UPDATE_FALTAS_DISCIPLINA = 'update Matricula set faltas = ? where ra = ? and cod_disciplina = ? and ano = ? and semestre = ?'
    retorno = proto.RetornoDefault()

    if not valida_codigo_disciplina(cod_disciplina, conn):
        retorno.mensagem = "Codigo da disciplina invalido"
        return retorno


    cursor = conn.cursor()
    result = cursor.execute(UPDATE_FALTAS_DISCIPLINA, (faltas, ra, cod_disciplina, ano, semestre))
    if result.rowcount != 1:
        conn.rollback()
        retorno.mensagem = "não foi possível atualizar as faltas, validar os dados informados"
    else: 
        conn.commit()
        retorno.mensagem = "Faltas atualizadas com sucesso"
        retorno.sucesso = True
    return retorno
    
# Alteração notas na tabela Matricula.
def alterar_nota_matricula(ra: int, cod_disciplina: str, ano: str, semestre:str, nota: int, conn: sqlite3.Connection): 
    '''
    Retorna um bool dizendo se conseguiu ou não atualizar o registro
    '''
    UPDATE_NOTA_DISCIPLINA = 'update Matricula set nota = ? where ra = ? and cod_disciplina = ? and ano = ? and semestre = ?'
    retorno = proto.RetornoDefault()

    if not valida_codigo_disciplina(cod_disciplina, conn):
        retorno.mensagem = "Codigo da disciplina invalido"
        return retorno


    cursor = conn.cursor()
    result = cursor.execute(UPDATE_NOTA_DISCIPLINA, (nota, ra, cod_disciplina, ano, semestre))
    if result.rowcount != 1:
        conn.rollback()
        retorno.mensagem = "não foi possível atualizar a nota, validar os dados informados"
    else: 
        retorno.mensagem = "Notas atualizadas com sucesso"
        retorno.sucesso = True
        conn.commit()
    return retorno

# Inserção na tabela Matricula (notas e faltas são inseridas com valor padrão 0).
def inserir_matricula(ra: int, cod_disciplina: str, ano: int, semestre: int, conn: sqlite3.Connection) -> proto.RetornoDefault:
    # -- RA, cod_disciplina, ano, semestre, nota, faltas
    INSERT_MATRICULA =  'insert into Matricula values(?,?,?,?,?,?)'
    retorno = proto.RetornoDefault()

    if not valida_codigo_disciplina(cod_disciplina, conn):
        retorno.mensagem = "Codigo da disciplina invalido"
        return retorno

    cursor = conn.cursor()
    try:
        result = cursor.execute(INSERT_MATRICULA, (ra, cod_disciplina, ano, semestre, 0, 0))
        if result.rowcount != 1:
            conn.rollback()
            retorno.mensagem = "erro ao inserir matricula, validar dados de entrada"
        else: 
            conn.commit()
            retorno.mensagem = "Sucesso ao cadastrar matricula"
            retorno.sucesso = True

    except Exception as e:
        print(e)
        retorno.mensagem = "Erro ao inserir matricula"
    return retorno

if __name__ == "__main__":
    main()