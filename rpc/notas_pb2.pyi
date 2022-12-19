from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Aluno(_message.Message):
    __slots__ = ["RA", "cod_curso", "nome", "periodo"]
    COD_CURSO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    PERIODO_FIELD_NUMBER: _ClassVar[int]
    RA: int
    RA_FIELD_NUMBER: _ClassVar[int]
    cod_curso: int
    nome: str
    periodo: int
    def __init__(self, RA: _Optional[int] = ..., nome: _Optional[str] = ..., periodo: _Optional[int] = ..., cod_curso: _Optional[int] = ...) -> None: ...

class Curso(_message.Message):
    __slots__ = ["codigo", "nome"]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    codigo: int
    nome: str
    def __init__(self, codigo: _Optional[int] = ..., nome: _Optional[str] = ...) -> None: ...

class Disciplina(_message.Message):
    __slots__ = ["cod_curso", "codigo", "nome", "professor"]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    COD_CURSO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    PROFESSOR_FIELD_NUMBER: _ClassVar[int]
    cod_curso: int
    codigo: str
    nome: str
    professor: str
    def __init__(self, codigo: _Optional[str] = ..., nome: _Optional[str] = ..., professor: _Optional[str] = ..., cod_curso: _Optional[int] = ...) -> None: ...

class ListaAlunos(_message.Message):
    __slots__ = ["alunos"]
    ALUNOS_FIELD_NUMBER: _ClassVar[int]
    alunos: _containers.RepeatedCompositeFieldContainer[Aluno]
    def __init__(self, alunos: _Optional[_Iterable[_Union[Aluno, _Mapping]]] = ...) -> None: ...

class Matricula(_message.Message):
    __slots__ = ["RA", "ano", "cod_disciplina", "faltas", "nota", "semestre"]
    ANO_FIELD_NUMBER: _ClassVar[int]
    COD_DISCIPLINA_FIELD_NUMBER: _ClassVar[int]
    FALTAS_FIELD_NUMBER: _ClassVar[int]
    NOTA_FIELD_NUMBER: _ClassVar[int]
    RA: int
    RA_FIELD_NUMBER: _ClassVar[int]
    SEMESTRE_FIELD_NUMBER: _ClassVar[int]
    ano: int
    cod_disciplina: str
    faltas: int
    nota: float
    semestre: int
    def __init__(self, RA: _Optional[int] = ..., cod_disciplina: _Optional[str] = ..., ano: _Optional[int] = ..., semestre: _Optional[int] = ..., nota: _Optional[float] = ..., faltas: _Optional[int] = ...) -> None: ...

class RequestLista(_message.Message):
    __slots__ = ["ano", "cod_disciplina", "ra", "semestre"]
    ANO_FIELD_NUMBER: _ClassVar[int]
    COD_DISCIPLINA_FIELD_NUMBER: _ClassVar[int]
    RA_FIELD_NUMBER: _ClassVar[int]
    SEMESTRE_FIELD_NUMBER: _ClassVar[int]
    ano: int
    cod_disciplina: str
    ra: int
    semestre: int
    def __init__(self, ano: _Optional[int] = ..., semestre: _Optional[int] = ..., ra: _Optional[int] = ..., cod_disciplina: _Optional[str] = ...) -> None: ...

class RetornoDefault(_message.Message):
    __slots__ = ["mensagem", "sucesso"]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    SUCESSO_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    sucesso: bool
    def __init__(self, sucesso: bool = ..., mensagem: _Optional[str] = ...) -> None: ...

class RetornoMatricula(_message.Message):
    __slots__ = ["faltas", "nome_disciplina", "nota", "ra"]
    FALTAS_FIELD_NUMBER: _ClassVar[int]
    NOME_DISCIPLINA_FIELD_NUMBER: _ClassVar[int]
    NOTA_FIELD_NUMBER: _ClassVar[int]
    RA_FIELD_NUMBER: _ClassVar[int]
    faltas: int
    nome_disciplina: str
    nota: float
    ra: int
    def __init__(self, ra: _Optional[int] = ..., nome_disciplina: _Optional[str] = ..., nota: _Optional[float] = ..., faltas: _Optional[int] = ...) -> None: ...

class ReturnListaAlunos(_message.Message):
    __slots__ = ["listaAlunos", "mensagem", "sucesso"]
    LISTAALUNOS_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    SUCESSO_FIELD_NUMBER: _ClassVar[int]
    listaAlunos: ListaAlunos
    mensagem: str
    sucesso: bool
    def __init__(self, sucesso: bool = ..., mensagem: _Optional[str] = ..., listaAlunos: _Optional[_Union[ListaAlunos, _Mapping]] = ...) -> None: ...

class ReturnListaMatriculas(_message.Message):
    __slots__ = ["matriculas", "mensagem", "sucesso"]
    MATRICULAS_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    SUCESSO_FIELD_NUMBER: _ClassVar[int]
    matriculas: _containers.RepeatedCompositeFieldContainer[RetornoMatricula]
    mensagem: str
    sucesso: bool
    def __init__(self, matriculas: _Optional[_Iterable[_Union[RetornoMatricula, _Mapping]]] = ..., sucesso: bool = ..., mensagem: _Optional[str] = ...) -> None: ...
