# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notas.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bnotas.proto\"!\n\x06Header\x12\x17\n\x0ftamanhoMensagem\x18\x01 \x01(\x05\"N\n\x07Request\x12\x1f\n\x02rm\x18\x01 \x01(\x0b\x32\x11.RequestMatriculaH\x00\x12\x1b\n\x02rl\x18\x02 \x01(\x0b\x32\r.RequestListaH\x00\x42\x05\n\x03req\"F\n\x10RequestMatricula\x12\x13\n\x0btipoRequest\x18\x01 \x01(\x05\x12\x1d\n\tmatricula\x18\x02 \x01(\x0b\x32\n.Matricula\"f\n\x0cRequestLista\x12\x13\n\x0btipoRequest\x18\x01 \x01(\x05\x12\x0b\n\x03\x61no\x18\x02 \x01(\x05\x12\x10\n\x08semestre\x18\x03 \x01(\x05\x12\n\n\x02ra\x18\x04 \x01(\x05\x12\x16\n\x0e\x63od_disciplina\x18\x05 \x01(\t\"%\n\x05\x43urso\x12\x0e\n\x06\x63odigo\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\"E\n\x05\x41luno\x12\n\n\x02RA\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x0f\n\x07periodo\x18\x03 \x01(\x05\x12\x11\n\tcod_curso\x18\x04 \x01(\x05\"l\n\tMatricula\x12\n\n\x02RA\x18\x01 \x01(\x05\x12\x16\n\x0e\x63od_disciplina\x18\x02 \x01(\t\x12\x0b\n\x03\x61no\x18\x03 \x01(\x05\x12\x10\n\x08semestre\x18\x04 \x01(\x05\x12\x0c\n\x04nota\x18\x05 \x01(\x02\x12\x0e\n\x06\x66\x61ltas\x18\x06 \x01(\x05\"P\n\nDisciplina\x12\x0e\n\x06\x63odigo\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x11\n\tprofessor\x18\x03 \x01(\t\x12\x11\n\tcod_curso\x18\x04 \x01(\x05\"%\n\x0bListaAlunos\x12\x16\n\x06\x61lunos\x18\x01 \x03(\x0b\x32\x06.Aluno\"a\n\x15ReturnListaMatriculas\x12%\n\nmatriculas\x18\x01 \x03(\x0b\x32\x11.RetornoMatricula\x12\x0f\n\x07sucesso\x18\x02 \x01(\x08\x12\x10\n\x08mensagem\x18\x03 \x01(\t\"U\n\x10RetornoMatricula\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x17\n\x0fnome_disciplina\x18\x02 \x01(\t\x12\x0c\n\x04nota\x18\x03 \x01(\x02\x12\x0e\n\x06\x66\x61ltas\x18\x04 \x01(\x05\"3\n\x0eRetornoDefault\x12\x0f\n\x07sucesso\x18\x01 \x01(\x08\x12\x10\n\x08mensagem\x18\x02 \x01(\t\"Y\n\x11ReturnListaAlunos\x12\x0f\n\x07sucesso\x18\x01 \x01(\x08\x12\x10\n\x08mensagem\x18\x02 \x01(\t\x12!\n\x0blistaAlunos\x18\x03 \x01(\x0b\x32\x0c.ListaAlunosB\x16\n\x07\x63lienteB\x0bNotasProtosb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notas_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\007clienteB\013NotasProtos'
  _HEADER._serialized_start=15
  _HEADER._serialized_end=48
  _REQUEST._serialized_start=50
  _REQUEST._serialized_end=128
  _REQUESTMATRICULA._serialized_start=130
  _REQUESTMATRICULA._serialized_end=200
  _REQUESTLISTA._serialized_start=202
  _REQUESTLISTA._serialized_end=304
  _CURSO._serialized_start=306
  _CURSO._serialized_end=343
  _ALUNO._serialized_start=345
  _ALUNO._serialized_end=414
  _MATRICULA._serialized_start=416
  _MATRICULA._serialized_end=524
  _DISCIPLINA._serialized_start=526
  _DISCIPLINA._serialized_end=606
  _LISTAALUNOS._serialized_start=608
  _LISTAALUNOS._serialized_end=645
  _RETURNLISTAMATRICULAS._serialized_start=647
  _RETURNLISTAMATRICULAS._serialized_end=744
  _RETORNOMATRICULA._serialized_start=746
  _RETORNOMATRICULA._serialized_end=831
  _RETORNODEFAULT._serialized_start=833
  _RETORNODEFAULT._serialized_end=884
  _RETURNLISTAALUNOS._serialized_start=886
  _RETURNLISTAALUNOS._serialized_end=975
# @@protoc_insertion_point(module_scope)
