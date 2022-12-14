//
//Descrição: Cliente para as requests do protocol buffer
//Autores: Ilzimara e Leonardo
//Data de criação: 07/09/2022
//

package cliente;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class Principal {
    /**
     * Imprime o menu de selecã́o
     */
    public static void imprimeMenu(){
        System.out.println("Digite a opção desejada:");
        System.out.println("1- > Inserir nova matricula");
        System.out.println("2 -> Alterar notas");
        System.out.println("3 -> Alterar faltas");
        System.out.println("4 -> Listar alunos de uma disciplina");
        System.out.println("5 -> Listar disciplinas, faltas e notas de um aluno");
        System.out.println("0 -> Sair");
    }

    /**
     * Imprime de forma "correta" o parametro passado
     * @param retorno parametro para ser impresso na tela
     */
    public static void imprimeRetornoDefault(NotasProtos.RetornoDefault retorno){
        System.out.println("===========================================");
        if (retorno.getSucesso()){
            System.out.println("Sucesso");
        } else {
            System.out.println("Erro ao realizar operação");
        }
        System.out.println(retorno.getMensagem());
        System.out.println("===========================================");
    }

    /**
     * Imprime de forma "correta" o parametro passado
     * @param listaAlunos parametro para ser impresso na tela
     */
    public static void imprimeListaAlunos(NotasProtos.ReturnListaAlunos listaAlunos) {
        System.out.println("===========================================");
        if(listaAlunos.getSucesso()){
            System.out.println("Sucesso");

            for (NotasProtos.Aluno aluno: listaAlunos.getListaAlunos().getAlunosList()){
                System.out.println("----------------------------------------");
                System.out.println("RA: " + aluno.getRA());
                System.out.println("Nome Aluno: " + aluno.getNome());
                System.out.println("Periodo: " + aluno.getPeriodo());
                System.out.println("----------------------------------------");
            }
        } else{
            System.out.println("Erro");
            System.out.println(listaAlunos.getMensagem());
        }
        System.out.println("===========================================");
    }

    /**
     * Imprime de forma "correta" o parametro passado
     * @param listaMatriculas parametro para ser impresso na tela
     */
    public static void imprimeDisciplinasAluno(NotasProtos.ReturnListaMatriculas listaMatriculas) {
        if (listaMatriculas.getSucesso()){
            System.out.println("Sucesso");
            for(NotasProtos.RetornoMatricula mat: listaMatriculas.getMatriculasList()){
                System.out.println("----------------------------------------");
                System.out.println("RA: " + mat.getRa());
                System.out.println("Nome Disciplina: " + mat.getNomeDisciplina());
                System.out.println("Faltas: " + mat.getFaltas());
                System.out.println("Nota: " + mat.getNota());
                System.out.println("----------------------------------------");
            }
        }else{
            System.out.println("Erro");
            System.out.println(listaMatriculas.getMensagem());
        }
    }

    public static void main(String[] args) {
        // Cria a porta de conexao com o server e os datasInputs
        int port = 8080;
        DataInputStream in;
        DataOutputStream out;
        try {
            // cria o socket
            Socket clientSocket = new Socket("127.0.0.1", port);
            in = new DataInputStream(clientSocket.getInputStream());
            out = new DataOutputStream(clientSocket.getOutputStream());

            int escolha = -1;
            // fica dentro do menu até que o usuário saia
            while(escolha != 0){
                // imprime o menu e pega a escolha do cliente
                imprimeMenu();
                Scanner ler = new Scanner(System.in);
                escolha = ler.nextInt();
                System.out.println(escolha);

                // variáveis utilizadas na montagem da request
                byte[] msg;
                byte[] buffer;
                NotasProtos.Header header;
                NotasProtos.RetornoDefault retorno;
                NotasProtos.Header cabecalhoEnvio;
                NotasProtos.RequestLista.Builder requestLista;
                switch (escolha){
                    case 1:
                        // Pegando dados da nova matricula
                        System.out.println("Inserir nova matricula");
                        NotasProtos.Matricula.Builder novaMat = NotasProtos.Matricula.newBuilder();

                        System.out.println("Digite o RA do aluno:");
                        novaMat.setRA(ler.nextInt());

                        System.out.println("Digite o Codigo da disciplina:");
                        novaMat.setCodDisciplina(ler.next());

                        System.out.println("Digite o ano da disciplina:");
                        novaMat.setAno(ler.nextInt());

                        System.out.println("Digite o semestre da disciplina:");
                        novaMat.setSemestre(ler.nextInt());

                        // Criando a request para ser enviada
                        NotasProtos.Request.Builder req = NotasProtos.Request.newBuilder();
                        NotasProtos.RequestMatricula.Builder reqMat = NotasProtos.RequestMatricula.newBuilder();
                        reqMat.setTipoRequest(1);
                        reqMat.setMatricula(novaMat);
                        req.setRm(reqMat);
                        msg = req.build().toByteArray();

                        // Criar cabeçalho para envio
                        cabecalhoEnvio = NotasProtos.Header.newBuilder()
                                .setTamanhoMensagem(msg.length).build();
                        out.write(cabecalhoEnvio.toByteArray());

                        // Enviando a request para o servidor
                        out.write(msg);

                        // Buffer do cabeçalho
                        buffer = new byte[2];

                        // Recebendo o cabeçalho, que vai informar quantos bytes precisam ser lidos
                        in.read(buffer);

                        // Criando buffer para receber a informação de fato
                        header = NotasProtos.Header.parseFrom(buffer);
                        buffer = new byte[header.getTamanhoMensagem()];
                        in.read(buffer);

                        // Recebendo o retorno do servidor
                        imprimeRetornoDefault(NotasProtos.RetornoDefault.parseFrom(buffer));
                        break;

                    case 2:
                        System.out.println("Alterar notas");
                        NotasProtos.Matricula.Builder matNotas = NotasProtos.Matricula.newBuilder();

                        System.out.println("Digite o RA do aluno:");
                        matNotas.setRA(ler.nextInt());

                        System.out.println("Digite o Codigo da disciplina:");
                        matNotas.setCodDisciplina(ler.next());

                        System.out.println("Digite o ano da disciplina:");
                        matNotas.setAno(ler.nextInt());

                        System.out.println("Digite o semestre da disciplina:");
                        matNotas.setSemestre(ler.nextInt());

                        System.out.println("Digite a nota:");
                        matNotas.setNota(ler.nextFloat());

                        // Criando a request para ser enviada
                        NotasProtos.Request.Builder reqNotas = NotasProtos.Request.newBuilder();
                        NotasProtos.RequestMatricula.Builder reqMatNotas = NotasProtos.RequestMatricula.newBuilder();
                        reqMatNotas.setTipoRequest(2);
                        reqMatNotas.setMatricula(matNotas);
                        reqNotas.setRm(reqMatNotas);
                        msg = reqNotas.build().toByteArray();

                        // Criar cabeçalho para envio
                        cabecalhoEnvio = NotasProtos.Header.newBuilder()
                                .setTamanhoMensagem(msg.length).build();
                        out.write(cabecalhoEnvio.toByteArray());

                        // Enviando a request para o servidor
                        out.write(msg);

                        // Buffer do cabeçalho
                        buffer = new byte[2];

                        // Recebendo o cabeçalho, que vai informar quantos bytes precisam ser lidos
                        in.read(buffer);

                        // Criando buffer para receber a informação de fato
                        header = NotasProtos.Header.parseFrom(buffer);
                        buffer = new byte[header.getTamanhoMensagem()];
                        in.read(buffer);


                        // Recebendo o retorno do servidor
                        imprimeRetornoDefault(NotasProtos.RetornoDefault.parseFrom(buffer));
                        break;
                    case 3:
                        System.out.println("Alterar faltas");
                        NotasProtos.Matricula.Builder matFaltas = NotasProtos.Matricula.newBuilder();

                        System.out.println("Digite o RA do aluno:");
                        matFaltas.setRA(ler.nextInt());

                        System.out.println("Digite o Codigo da disciplina:");
                        matFaltas.setCodDisciplina(ler.next());

                        System.out.println("Digite o ano da disciplina:");
                        matFaltas.setAno(ler.nextInt());

                        System.out.println("Digite o semestre da disciplina:");
                        matFaltas.setSemestre(ler.nextInt());

                        System.out.println("Digite as faltas:");
                        matFaltas.setFaltas(ler.nextInt());

                        //Criando a request para ser enviada
                        NotasProtos.Request.Builder reqFaltas = NotasProtos.Request.newBuilder();
                        NotasProtos.RequestMatricula.Builder reqMatFaltas = NotasProtos.RequestMatricula.newBuilder();
                        reqMatFaltas.setTipoRequest(3);
                        reqMatFaltas.setMatricula(matFaltas);
                        reqFaltas.setRm(reqMatFaltas);
                        msg = reqFaltas.build().toByteArray();

                        // Criar cabeçalho para envio
                        cabecalhoEnvio = NotasProtos.Header.newBuilder()
                                .setTamanhoMensagem(msg.length).build();
                        out.write(cabecalhoEnvio.toByteArray());


                        // Enviando a request para o servidor
                        out.write(msg);

                        // Buffer do cabeçalho
                        buffer = new byte[2];

                        // Recebendo o cabeçalho, que vai informar quantos bytes precisam ser lidos
                        in.read(buffer);

                        // Criando buffer para receber a informação de fato
                        header = NotasProtos.Header.parseFrom(buffer);
                        buffer = new byte[header.getTamanhoMensagem()];
                        in.read(buffer);

                        // Recebendo o retorno do servidor
                        imprimeRetornoDefault(NotasProtos.RetornoDefault.parseFrom(buffer));
                        break;
                    case 4:
                        System.out.println("Listar alunos de uma disciplina");
                        NotasProtos.Request.Builder requestAlunos = NotasProtos.Request.newBuilder();
                        requestLista = NotasProtos.RequestLista.newBuilder();

                        System.out.println("Digite o Codigo da disciplina:");
                        requestLista.setCodDisciplina(ler.next());

                        System.out.println("Digite o semestre:");
                        requestLista.setSemestre(ler.nextInt());

                        System.out.println("Digite o ano da disciplina:");
                        requestLista.setAno(ler.nextInt());

                        requestLista.setTipoRequest(1);
                        requestAlunos.setRl(requestLista);
                        msg = requestAlunos.build().toByteArray();


                        // Criar cabeçalho para envio
                        cabecalhoEnvio = NotasProtos.Header.newBuilder()
                                .setTamanhoMensagem(msg.length).build();
                        out.write(cabecalhoEnvio.toByteArray());


                        // Enviando a request para o servidor
                        out.write(msg);

                        // Buffer do cabeçalho
                        buffer = new byte[2];

                        // Recebendo o cabeçalho, que vai informar quantos bytes precisam ser lidos
                        in.read(buffer);

                        // Criando buffer para receber a informação de fato
                        header = NotasProtos.Header.parseFrom(buffer);
                        buffer = new byte[header.getTamanhoMensagem()];
                        in.read(buffer);

                        // Recebendo o retorno do servidor
                        imprimeListaAlunos(NotasProtos.ReturnListaAlunos.parseFrom(buffer));
                        break;
                    case 5:
                        System.out.println("Listar disciplinas, faltas e notas de um aluno");

                        NotasProtos.Request.Builder requestAluno = NotasProtos.Request.newBuilder();
                        requestLista = NotasProtos.RequestLista.newBuilder();

                        System.out.println("Digite o RA:");
                        requestLista.setRa(ler.nextInt());

                        System.out.println("Digite o semestre:");
                        requestLista.setSemestre(ler.nextInt());

                        System.out.println("Digite o ano da disciplina:");
                        requestLista.setAno(ler.nextInt());


                        requestLista.setTipoRequest(2);
                        requestAluno.setRl(requestLista);
                        msg = requestAluno.build().toByteArray();


                        // Criar cabeçalho para envio
                        cabecalhoEnvio = NotasProtos.Header.newBuilder()
                                .setTamanhoMensagem(msg.length).build();
                        out.write(cabecalhoEnvio.toByteArray());


                        // Enviando a request para o servidor
                        out.write(msg);

                        // Buffer do cabeçalho
                        buffer = new byte[2];

                        // Recebendo o cabeçalho, que vai informar quantos bytes precisam ser lidos
                        in.read(buffer);

                        // Criando buffer para receber a informação de fato
                        header = NotasProtos.Header.parseFrom(buffer);
                        buffer = new byte[header.getTamanhoMensagem()];
                        in.read(buffer);

                        // Recebendo o retorno do servidor
                        imprimeDisciplinasAluno(NotasProtos.ReturnListaMatriculas.parseFrom(buffer));
                        break;

                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }




//        NotasProtos.Curso.Builder a = NotasProtos.Curso.newBuilder();
//        a.setCodigo(1);
//        a.setNome("teste");
//
//        System.out.println(a);
    }
}
