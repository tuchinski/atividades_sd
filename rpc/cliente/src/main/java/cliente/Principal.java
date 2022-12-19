//
//Descrição: Cliente para as requests do protocol buffer
//Autores: Ilzimara e Leonardo
//Data de criação: 07/09/2022
//

package cliente;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

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
    public static void imprimeRetornoDefault(RetornoDefault retorno){
        System.out.println("===========================================");
        if (retorno.getSucesso()){
            System.out.println("Sucesso");
        } else {
            System.out.println("Erro ao realizar operação");
        }
        System.out.println(retorno.getMensagem());
        System.out.println("===========================================");
    }
//
//    /**
//     * Imprime de forma "correta" o parametro passado
//     * @param listaAlunos parametro para ser impresso na tela
//     */
//    public static void imprimeListaAlunos(NotasProtos.ReturnListaAlunos listaAlunos) {
//        System.out.println("===========================================");
//        if(listaAlunos.getSucesso()){
//            System.out.println("Sucesso");
//
//            for (NotasProtos.Aluno aluno: listaAlunos.getListaAlunos().getAlunosList()){
//                System.out.println("----------------------------------------");
//                System.out.println("RA: " + aluno.getRA());
//                System.out.println("Nome Aluno: " + aluno.getNome());
//                System.out.println("Periodo: " + aluno.getPeriodo());
//                System.out.println("----------------------------------------");
//            }
//        } else{
//            System.out.println("Erro");
//            System.out.println(listaAlunos.getMensagem());
//        }
//        System.out.println("===========================================");
//    }

//    /**
//     * Imprime de forma "correta" o parametro passado
//     * @param listaMatriculas parametro para ser impresso na tela
//     */
//    public static void imprimeDisciplinasAluno(NotasProtos.ReturnListaMatriculas listaMatriculas) {
//        if (listaMatriculas.getSucesso()){
//            System.out.println("Sucesso");
//            for(NotasProtos.RetornoMatricula mat: listaMatriculas.getMatriculasList()){
//                System.out.println("----------------------------------------");
//                System.out.println("RA: " + mat.getRa());
//                System.out.println("Nome Disciplina: " + mat.getNomeDisciplina());
//                System.out.println("Faltas: " + mat.getFaltas());
//                System.out.println("Nota: " + mat.getNota());
//                System.out.println("----------------------------------------");
//            }
//        }else{
//            System.out.println("Erro");
//            System.out.println(listaMatriculas.getMensagem());
//        }
//    }

    public static void main(String[] args) {
        // Cria a porta de conexao com o server e os datasInputs

        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 8181)
                .usePlaintext()
                .build();

        GerenciadorNotasGrpc.GerenciadorNotasBlockingStub stub = GerenciadorNotasGrpc.newBlockingStub(channel);


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
//            NotasProtos.Header header;
//            NotasProtos.RetornoDefault retorno;
//            NotasProtos.Header cabecalhoEnvio;
//            NotasProtos.RequestLista.Builder requestLista;
            switch (escolha){
                case 1:
                    // Pegando dados da nova matricula
                    Matricula mat = Matricula.newBuilder().setAno(2022).setRA(2).setSemestre(4).setCodDisciplina("GA3X1").build();

                    System.out.println("Inserir nova matricula");
                    Matricula.Builder novaMat = Matricula.newBuilder();

                    System.out.println("Digite o RA do aluno:");
                    novaMat.setRA(ler.nextInt());

                    System.out.println("Digite o Codigo da disciplina:");
                    novaMat.setCodDisciplina(ler.next());

                    System.out.println("Digite o ano da disciplina:");
                    novaMat.setAno(ler.nextInt());

                    System.out.println("Digite o semestre da disciplina:");
                    novaMat.setSemestre(ler.nextInt());

                    RetornoDefault ret =  stub.inserirNovaMatricula(novaMat.build());
                    imprimeRetornoDefault(ret);

                    break;

                case 2:
                    System.out.println("Alterar notas");
                    break;

                case 3:
                    System.out.println("Alterar faltas");
                    break;

                case 4:
                    System.out.println("Listar alunos de uma disciplina");
                    break;

                case 5:
                    System.out.println("Listar disciplinas, faltas e notas de um aluno");
                    break;

                }
            }

    }
}
