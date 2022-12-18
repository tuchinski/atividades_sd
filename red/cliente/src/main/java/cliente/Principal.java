package cliente;

public class Principal {
    private void imprimeMenu(){
        System.out.println("Digite a opção desejada:");
        System.out.println("1- > Inserir nova matricula");
        System.out.println("2 -> Alterar notas");
        System.out.println("3 -> Alterar faltas");
        System.out.println("4 -> Listar alunos de uma disciplina");
        System.out.println("5 -> Listar disciplinas, faltas e notas de um aluno");
        System.out.println("6 -> Sair");
    }
    public static void main(String[] args) {
        int escolha = 0;
        while(escolha != 6){
            
        }
        NotasProtos.Curso.Builder a = NotasProtos.Curso.newBuilder();
        a.setCodigo(1);
        a.setNome("teste");

        System.out.println(a);


    }
}
