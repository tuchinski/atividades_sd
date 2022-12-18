# FEITO! • Inserção na tabela Matricula (notas e faltas são inseridas com valor padrão 0).
# FEITO! • Alteração notas na tabela Matricula.
# FEITO! • Alteração faltas na tabela Matricula.
# FEITO! • Listagem de alunos (RA, nome, período) de uma disciplina informado a disciplina, ano e semestre. 
# FEITO! • Listagem de disciplinas, faltas e notas (RA, nome, nota, faltas) de um aluno informado o ano e semestre.

import socket
import pythoncode.notas_pb2 as proto
import sqlite3

conexao_bd = "database_com_dados-contrib-Daniel-Farina.db"

GET_ALL_CURSOS = "SELECT * FROM curso"

def main():
    conn = sqlite3.connect(conexao_bd)
    cursor = conn.cursor()
    cursos = cursor.execute(GET_ALL_CURSOS)

    lista_cursos = proto.ListaCursos()

    # print(cursos.fetchall())

    for curso in cursos.fetchall():
        curso_proto = lista_cursos.cursos.add()
        curso_proto.codigo = curso[0]
        curso_proto.nome = curso[1]
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

    # print(valida_codigo_disciplina("GA3X1", conn))


    print(busca_alunos_por_disciplina("GA3X11", 2018, 6, conn))
    # print(lista_disciplinas_aluno_por_semestre(18, 2019, 3, conn))
    # alterar_faltas_matricula(23, "BCC36B", 5, conn)
    # alterar_nota_matricula(23, "BCC36B", 5.2, conn)
    # inserir_matricula(49, 'LM31A', 2022, 1, conn)

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
    lista_disciplinas = proto.ListaMatriculas()
    for resultado in result:
        retorno_matricula = lista_disciplinas.matriculas.add()
        retorno_matricula.ra = resultado[0]
        retorno_matricula.nome_disciplina = resultado[1]
        retorno_matricula.nota = resultado[2]
        retorno_matricula.faltas = resultado[3]
    return lista_disciplinas

# Alteração faltas na tabela Matricula.
def alterar_faltas_matricula(ra: int, cod_disciplina: str, faltas: int, conn: sqlite3.Connection): 
    '''
    Retorna um bool dizendo se conseguiu ou não atualizar o registro
    '''
    UPDATE_FALTAS_DISCIPLINA = 'update Matricula set faltas = ? where ra = ? and cod_disciplina = ?'

    cursor = conn.cursor()
    result = cursor.execute(UPDATE_FALTAS_DISCIPLINA, (faltas, ra, cod_disciplina))
    if result.rowcount != 1:
        conn.rollback()
        return False
    else: 
        conn.commit()
        return True
    
# Alteração notas na tabela Matricula.
def alterar_nota_matricula(ra: int, cod_disciplina: str, nota: int, conn: sqlite3.Connection): 
    '''
    Retorna um bool dizendo se conseguiu ou não atualizar o registro
    '''
    UPDATE_NOTA_DISCIPLINA = 'update Matricula set nota = ? where ra = ? and cod_disciplina = ?'

    cursor = conn.cursor()
    result = cursor.execute(UPDATE_NOTA_DISCIPLINA, (nota, ra, cod_disciplina))
    if result.rowcount != 1:
        conn.rollback()
        return False
    else: 
        conn.commit()
        return True

# Inserção na tabela Matricula (notas e faltas são inseridas com valor padrão 0).
def inserir_matricula(ra: int, cod_disciplina: str, ano: int, semestre: int, conn: sqlite3.Connection):
    # -- RA, cod_disciplina, ano, semestre, nota, faltas
    INSERT_MATRICULA =  'insert into Matricula values(?,?,?,?,?,?)'
    cursor = conn.cursor()
    result = cursor.execute(INSERT_MATRICULA, (ra, cod_disciplina, ano, semestre, 0, 0))
    if result.rowcount != 1:
        conn.rollback()
        return False
    else: 
        conn.commit()
        return True

if __name__ == "__main__":
    main()