# Programação com sockets TCP Questão 1
## Descrição
Faça um servidor para processar as seguintes mensagens dos clientes. O servidor deve suportar mensagens
de múltiplos clientes. Use o TCP. As mensagens de solicitação estão no formato String UTF:

- **CONNECT user, password**
  - Conecta o usuário user a sua área no servidor se a senha password conferir e o usuário user existir. Em caso de
  sucesso, devolver SUCCESS como String UTF. Em caso de falha, devolver ERROR. Obs: password deve ser enviado
  o hash em SHA-512.
- **PWD**
  - Devolve o caminho corrente (PATH) usando String UTF separando os diretórios por barra(/).
- **CHDIR path**
  - Altera o diretório corrente para path, retornado uma String UTF, SUCCESS, no caso de sucesso, e ERROR, no caso
    de erro.
- **GETFILES**
  * Devolve os arquivos do diretório corrente no servidor.
  - Formato:
    * devolve um inteiro indicando o número de arquivos como String UTF.
    * devolve cada arquivo como uma String UTF.
- **GETDIRS**
  * Devolve os diretórios do diretório corrente no servidor.
  - Formato:
    * devolve um inteiro indicando o número de diretórios como String UTF.
    * devolve cada diretório como uma String UTF.
- **EXIT**
  * Finaliza a conexão

### Pré Requesitos
- Pontos necessários para a execução
  - Ter dentro do diretório onde se encontra o cliente e servidor, uma pasta com o nome _server_files_
    - Dentro desta pasta, ficam os arquivos e diretórios que o servidor irá consultar
  - Python 3.x instalado

## Execução
- Em um terminal, executar primeiramente o servidor, com o comando `python3 server.py`
- Posteriormente, executar o cliente com o comando `python3 client.py`
- Com isso, cliente e servidor já se conectaram, e agora é só utilizar os comandos disponibilizados
- Obs: para realizar qualquer operação, a sessão precisa estar logada
  - Existem 2 usuários pré cadastrados com as seguintes credenciais:
    - User: admin Senha: admin
    - User: teste Senha: 123
  - Para cadastrar mais usuários, é necessário criar uma nova linha no arquivo `users` separando o usuário e a senha com `:`
    - Obs: a senha precisa estar criptografada em SHA-512