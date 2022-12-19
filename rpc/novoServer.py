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
        conexao_bd = "rpc.db"
        db_conn = sqlite3.connect(conexao_bd)
        """
        insere uma nova matricula no banco
        """
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
        retorno = proto.RetornoDefault()
        retorno.mensagem = "teste"
        retorno.sucesso = True

    def alterarFaltasMatricula(self, request, context):
        retorno = proto.RetornoDefault()
        retorno.mensagem = "teste"
        retorno.sucesso = True
        return retorno

    def listaAlunosDisciplina(self, request, context):
        retorno = proto.ReturnListaAlunos()
        retorno.sucesso = True
        retorno.mensagem = "teste"
        return retorno

    def listaDisciplinaAluno(self, request, context):
        retorno = proto.ReturnListaMatriculas()
        retorno.sucesso = True
        retorno.mensagem = "teste"
        return retorno

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