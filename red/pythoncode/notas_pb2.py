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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bnotas.proto\"%\n\x05\x43urso\x12\x0e\n\x06\x63odigo\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\"E\n\x05\x41luno\x12\n\n\x02RA\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x0f\n\x07periodo\x18\x03 \x01(\x05\x12\x11\n\tcod_curso\x18\x04 \x01(\x05\"l\n\tMatricula\x12\n\n\x02RA\x18\x01 \x01(\x05\x12\x16\n\x0e\x63od_disciplina\x18\x02 \x01(\t\x12\x0b\n\x03\x61no\x18\x03 \x01(\x05\x12\x10\n\x08semestre\x18\x04 \x01(\x05\x12\x0c\n\x04nota\x18\x05 \x01(\x02\x12\x0e\n\x06\x66\x61ltas\x18\x06 \x01(\x05\"P\n\nDisciplina\x12\x0e\n\x06\x63odigo\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x11\n\tprofessor\x18\x03 \x01(\t\x12\x11\n\tcod_curso\x18\x04 \x01(\x05\"%\n\x0bListaAlunos\x12\x16\n\x06\x61lunos\x18\x01 \x03(\x0b\x32\x06.Aluno\"8\n\x0fListaMatriculas\x12%\n\nmatriculas\x18\x01 \x03(\x0b\x32\x11.RetornoMatricula\"U\n\x10RetornoMatricula\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x17\n\x0fnome_disciplina\x18\x02 \x01(\t\x12\x0c\n\x04nota\x18\x03 \x01(\x02\x12\x0e\n\x06\x66\x61ltas\x18\x04 \x01(\x05\"%\n\x0bListaCursos\x12\x16\n\x06\x63ursos\x18\x01 \x03(\x0b\x32\x06.Cursob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notas_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CURSO._serialized_start=15
  _CURSO._serialized_end=52
  _ALUNO._serialized_start=54
  _ALUNO._serialized_end=123
  _MATRICULA._serialized_start=125
  _MATRICULA._serialized_end=233
  _DISCIPLINA._serialized_start=235
  _DISCIPLINA._serialized_end=315
  _LISTAALUNOS._serialized_start=317
  _LISTAALUNOS._serialized_end=354
  _LISTAMATRICULAS._serialized_start=356
  _LISTAMATRICULAS._serialized_end=412
  _RETORNOMATRICULA._serialized_start=414
  _RETORNOMATRICULA._serialized_end=499
  _LISTACURSOS._serialized_start=501
  _LISTACURSOS._serialized_end=538
# @@protoc_insertion_point(module_scope)
