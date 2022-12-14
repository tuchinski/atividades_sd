from concurrent import futures
import logging

import grpc
import notas_pb2_grpc as notas_rpc
import notas_pb2 as proto
import sqlite3


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

class GerenciadorNotas(notas_rpc.GerenciadorNotas):

    def inserirNovaMatricula(self, request:proto.Matricula , context):
        """
        insere uma nova matricula no banco
        """

        print("entrou")
        conexao_bd = "rpc.db"
        db_conn = sqlite3.connect(conexao_bd)
        INSERT_MATRICULA =  'insert into Matricula values(?,?,?,?,?,?)'
        retorno = proto.RetornoDefault()        

        if not valida_codigo_disciplina(request.cod_disciplina, db_conn):
            retorno.mensagem = "Codigo da disciplina invalido"
            return retorno

        cursor = db_conn.cursor()
        try:
            result = cursor.execute(INSERT_MATRICULA, (request.RA, request.cod_disciplina, request.ano, request.semestre, 0, 0))
            if result.rowcount != 1:
                db_conn.rollback()
                retorno.mensagem = "erro ao inserir matricula, validar dados de entrada"
            else: 
                db_conn.commit()
                retorno.mensagem = "Sucesso ao cadastrar matricula"
                retorno.sucesso = True

        except Exception as e:
            print(e)
            retorno.mensagem = "Erro ao inserir matricula"
        return retorno

    def alterarNotasMatricula(self, request, context):
        '''
        altera as notas de uma matricula
        '''
        conexao_bd = "rpc.db"
        conn = sqlite3.connect(conexao_bd)
        UPDATE_NOTA_DISCIPLINA = 'update Matricula set nota = ? where ra = ? and cod_disciplina = ? and ano = ? and semestre = ?'
        retorno = proto.RetornoDefault()

        if not valida_codigo_disciplina(request.cod_disciplina, conn):
            retorno.mensagem = "Codigo da disciplina invalido"
            return retorno

        cursor = conn.cursor()
        result = cursor.execute(UPDATE_NOTA_DISCIPLINA, (request.nota, request.RA, request.cod_disciplina, request.ano, request.semestre))
        if result.rowcount != 1:
            conn.rollback()
            retorno.mensagem = "não foi possível atualizar a nota, validar os dados informados"
        else: 
            retorno.mensagem = "Notas atualizadas com sucesso"
            retorno.sucesso = True
            conn.commit()
        return retorno

    def alterarFaltasMatricula(self, request, context):
        '''
        Altera as faltas da matricula especificada
        '''
        conexao_bd = "rpc.db"
        conn = sqlite3.connect(conexao_bd)
        UPDATE_FALTAS_DISCIPLINA = 'update Matricula set faltas = ? where ra = ? and cod_disciplina = ? and ano = ? and semestre = ?'
        retorno = proto.RetornoDefault()

        if not valida_codigo_disciplina(request.cod_disciplina, conn):
            retorno.mensagem = "Codigo da disciplina invalido"
            return retorno


        cursor = conn.cursor()
        result = cursor.execute(UPDATE_FALTAS_DISCIPLINA, (request.faltas, request.RA, request.cod_disciplina, request.ano, request.semestre))
        if result.rowcount != 1:
            conn.rollback()
            retorno.mensagem = "não foi possível atualizar as faltas, validar os dados informados"
        else: 
            conn.commit()
            retorno.mensagem = "Faltas atualizadas com sucesso"
            retorno.sucesso = True
        return retorno

    def listaAlunosDisciplina(self, request, context):
        
        """
        Busca os alunos de acordo com o cod_disciplina, ano e semestre desejado
        
        Caso encontre ou não, utiliza a message ReturnListaAlunos
        """
        conexao_bd = "rpc.db"
        conn = sqlite3.connect(conexao_bd)

        SELECT_BUSCA_ALUNOS_DISCIPLINA = "select a.* from Aluno A, disciplina d, Matricula m where d.codigo = m.cod_disciplina AND m.ra = a.ra and d.codigo = ? and ano = ? and semestre = ?"
        retorno = proto.ReturnListaAlunos()

        # verifica se o código informado existe
        # se não existir, retorna isso com uma msg padrão
        if not valida_codigo_disciplina(request.cod_disciplina, conn):
            retorno.sucesso = False
            retorno.mensagem = "Codigo da disciplina invalido"
            return retorno                  

        # busca as disciplinas, e insere no response correspondente 
        cursor = conn.cursor()
        result = cursor.execute(SELECT_BUSCA_ALUNOS_DISCIPLINA, (request.cod_disciplina, request.ano, request.semestre))
        for aluno in result.fetchall():
            aluno_curso = retorno.listaAlunos.alunos.add()
            aluno_curso.RA = aluno[0]
            aluno_curso.nome = aluno[1]
            aluno_curso.periodo = aluno[2]
            aluno_curso.cod_curso = aluno[3]
        retorno.sucesso = True
        retorno.mensagem = "Sucesso ao buscar os alunos"
        return retorno
        

    def listaDisciplinaAluno(self, request, context):
        ''''
        Lista as disciplinas de um aluno informando seu RA, ano e semestre desejado
        '''
        conexao_bd = "rpc.db"
        conn = sqlite3.connect(conexao_bd)

        SELECT_DISCIPLINA_ALUNO_POR_SEMESTRE = 'select a.ra, d.nome, m.nota, m.faltas from Aluno a, Disciplina d, Matricula m where d.codigo = m.cod_disciplina and a.ra = m.ra and a.ra = ? and m.ano = ? and m.semestre = ?'
        cursor = conn.cursor()
        result = cursor.execute(SELECT_DISCIPLINA_ALUNO_POR_SEMESTRE,(request.ra, request.ano, request.semestre))
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

def main():
    port = "8181"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notas_rpc.add_GerenciadorNotasServicer_to_server(GerenciadorNotas(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print(f"Servidor iniciou na porta {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    main()