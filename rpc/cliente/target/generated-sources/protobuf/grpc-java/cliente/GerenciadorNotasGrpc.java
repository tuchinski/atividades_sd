package cliente;

import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.4.0)",
    comments = "Source: notas.proto")
public final class GerenciadorNotasGrpc {

  private GerenciadorNotasGrpc() {}

  public static final String SERVICE_NAME = "GerenciadorNotas";

  // Static method descriptors that strictly reflect the proto.
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<cliente.Matricula,
      cliente.RetornoDefault> METHOD_INSERIR_NOVA_MATRICULA =
      io.grpc.MethodDescriptor.<cliente.Matricula, cliente.RetornoDefault>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorNotas", "inserirNovaMatricula"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.Matricula.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.RetornoDefault.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<cliente.Matricula,
      cliente.RetornoDefault> METHOD_ALTERAR_NOTAS_MATRICULA =
      io.grpc.MethodDescriptor.<cliente.Matricula, cliente.RetornoDefault>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorNotas", "alterarNotasMatricula"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.Matricula.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.RetornoDefault.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<cliente.Matricula,
      cliente.RetornoDefault> METHOD_ALTERAR_FALTAS_MATRICULA =
      io.grpc.MethodDescriptor.<cliente.Matricula, cliente.RetornoDefault>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorNotas", "alterarFaltasMatricula"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.Matricula.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.RetornoDefault.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<cliente.RequestLista,
      cliente.ReturnListaAlunos> METHOD_LISTA_ALUNOS_DISCIPLINA =
      io.grpc.MethodDescriptor.<cliente.RequestLista, cliente.ReturnListaAlunos>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorNotas", "listaAlunosDisciplina"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.RequestLista.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.ReturnListaAlunos.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<cliente.RequestLista,
      cliente.ReturnListaMatriculas> METHOD_LISTA_DISCIPLINA_ALUNO =
      io.grpc.MethodDescriptor.<cliente.RequestLista, cliente.ReturnListaMatriculas>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorNotas", "listaDisciplinaAluno"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.RequestLista.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              cliente.ReturnListaMatriculas.getDefaultInstance()))
          .build();

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static GerenciadorNotasStub newStub(io.grpc.Channel channel) {
    return new GerenciadorNotasStub(channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static GerenciadorNotasBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    return new GerenciadorNotasBlockingStub(channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static GerenciadorNotasFutureStub newFutureStub(
      io.grpc.Channel channel) {
    return new GerenciadorNotasFutureStub(channel);
  }

  /**
   */
  public static abstract class GerenciadorNotasImplBase implements io.grpc.BindableService {

    /**
     */
    public void inserirNovaMatricula(cliente.Matricula request,
        io.grpc.stub.StreamObserver<cliente.RetornoDefault> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_INSERIR_NOVA_MATRICULA, responseObserver);
    }

    /**
     */
    public void alterarNotasMatricula(cliente.Matricula request,
        io.grpc.stub.StreamObserver<cliente.RetornoDefault> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_ALTERAR_NOTAS_MATRICULA, responseObserver);
    }

    /**
     */
    public void alterarFaltasMatricula(cliente.Matricula request,
        io.grpc.stub.StreamObserver<cliente.RetornoDefault> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_ALTERAR_FALTAS_MATRICULA, responseObserver);
    }

    /**
     */
    public void listaAlunosDisciplina(cliente.RequestLista request,
        io.grpc.stub.StreamObserver<cliente.ReturnListaAlunos> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_LISTA_ALUNOS_DISCIPLINA, responseObserver);
    }

    /**
     */
    public void listaDisciplinaAluno(cliente.RequestLista request,
        io.grpc.stub.StreamObserver<cliente.ReturnListaMatriculas> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_LISTA_DISCIPLINA_ALUNO, responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            METHOD_INSERIR_NOVA_MATRICULA,
            asyncUnaryCall(
              new MethodHandlers<
                cliente.Matricula,
                cliente.RetornoDefault>(
                  this, METHODID_INSERIR_NOVA_MATRICULA)))
          .addMethod(
            METHOD_ALTERAR_NOTAS_MATRICULA,
            asyncUnaryCall(
              new MethodHandlers<
                cliente.Matricula,
                cliente.RetornoDefault>(
                  this, METHODID_ALTERAR_NOTAS_MATRICULA)))
          .addMethod(
            METHOD_ALTERAR_FALTAS_MATRICULA,
            asyncUnaryCall(
              new MethodHandlers<
                cliente.Matricula,
                cliente.RetornoDefault>(
                  this, METHODID_ALTERAR_FALTAS_MATRICULA)))
          .addMethod(
            METHOD_LISTA_ALUNOS_DISCIPLINA,
            asyncUnaryCall(
              new MethodHandlers<
                cliente.RequestLista,
                cliente.ReturnListaAlunos>(
                  this, METHODID_LISTA_ALUNOS_DISCIPLINA)))
          .addMethod(
            METHOD_LISTA_DISCIPLINA_ALUNO,
            asyncUnaryCall(
              new MethodHandlers<
                cliente.RequestLista,
                cliente.ReturnListaMatriculas>(
                  this, METHODID_LISTA_DISCIPLINA_ALUNO)))
          .build();
    }
  }

  /**
   */
  public static final class GerenciadorNotasStub extends io.grpc.stub.AbstractStub<GerenciadorNotasStub> {
    private GerenciadorNotasStub(io.grpc.Channel channel) {
      super(channel);
    }

    private GerenciadorNotasStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GerenciadorNotasStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new GerenciadorNotasStub(channel, callOptions);
    }

    /**
     */
    public void inserirNovaMatricula(cliente.Matricula request,
        io.grpc.stub.StreamObserver<cliente.RetornoDefault> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_INSERIR_NOVA_MATRICULA, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void alterarNotasMatricula(cliente.Matricula request,
        io.grpc.stub.StreamObserver<cliente.RetornoDefault> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_ALTERAR_NOTAS_MATRICULA, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void alterarFaltasMatricula(cliente.Matricula request,
        io.grpc.stub.StreamObserver<cliente.RetornoDefault> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_ALTERAR_FALTAS_MATRICULA, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void listaAlunosDisciplina(cliente.RequestLista request,
        io.grpc.stub.StreamObserver<cliente.ReturnListaAlunos> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_LISTA_ALUNOS_DISCIPLINA, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void listaDisciplinaAluno(cliente.RequestLista request,
        io.grpc.stub.StreamObserver<cliente.ReturnListaMatriculas> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_LISTA_DISCIPLINA_ALUNO, getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class GerenciadorNotasBlockingStub extends io.grpc.stub.AbstractStub<GerenciadorNotasBlockingStub> {
    private GerenciadorNotasBlockingStub(io.grpc.Channel channel) {
      super(channel);
    }

    private GerenciadorNotasBlockingStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GerenciadorNotasBlockingStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new GerenciadorNotasBlockingStub(channel, callOptions);
    }

    /**
     */
    public cliente.RetornoDefault inserirNovaMatricula(cliente.Matricula request) {
      return blockingUnaryCall(
          getChannel(), METHOD_INSERIR_NOVA_MATRICULA, getCallOptions(), request);
    }

    /**
     */
    public cliente.RetornoDefault alterarNotasMatricula(cliente.Matricula request) {
      return blockingUnaryCall(
          getChannel(), METHOD_ALTERAR_NOTAS_MATRICULA, getCallOptions(), request);
    }

    /**
     */
    public cliente.RetornoDefault alterarFaltasMatricula(cliente.Matricula request) {
      return blockingUnaryCall(
          getChannel(), METHOD_ALTERAR_FALTAS_MATRICULA, getCallOptions(), request);
    }

    /**
     */
    public cliente.ReturnListaAlunos listaAlunosDisciplina(cliente.RequestLista request) {
      return blockingUnaryCall(
          getChannel(), METHOD_LISTA_ALUNOS_DISCIPLINA, getCallOptions(), request);
    }

    /**
     */
    public cliente.ReturnListaMatriculas listaDisciplinaAluno(cliente.RequestLista request) {
      return blockingUnaryCall(
          getChannel(), METHOD_LISTA_DISCIPLINA_ALUNO, getCallOptions(), request);
    }
  }

  /**
   */
  public static final class GerenciadorNotasFutureStub extends io.grpc.stub.AbstractStub<GerenciadorNotasFutureStub> {
    private GerenciadorNotasFutureStub(io.grpc.Channel channel) {
      super(channel);
    }

    private GerenciadorNotasFutureStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GerenciadorNotasFutureStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new GerenciadorNotasFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<cliente.RetornoDefault> inserirNovaMatricula(
        cliente.Matricula request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_INSERIR_NOVA_MATRICULA, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<cliente.RetornoDefault> alterarNotasMatricula(
        cliente.Matricula request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_ALTERAR_NOTAS_MATRICULA, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<cliente.RetornoDefault> alterarFaltasMatricula(
        cliente.Matricula request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_ALTERAR_FALTAS_MATRICULA, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<cliente.ReturnListaAlunos> listaAlunosDisciplina(
        cliente.RequestLista request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_LISTA_ALUNOS_DISCIPLINA, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<cliente.ReturnListaMatriculas> listaDisciplinaAluno(
        cliente.RequestLista request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_LISTA_DISCIPLINA_ALUNO, getCallOptions()), request);
    }
  }

  private static final int METHODID_INSERIR_NOVA_MATRICULA = 0;
  private static final int METHODID_ALTERAR_NOTAS_MATRICULA = 1;
  private static final int METHODID_ALTERAR_FALTAS_MATRICULA = 2;
  private static final int METHODID_LISTA_ALUNOS_DISCIPLINA = 3;
  private static final int METHODID_LISTA_DISCIPLINA_ALUNO = 4;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final GerenciadorNotasImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(GerenciadorNotasImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_INSERIR_NOVA_MATRICULA:
          serviceImpl.inserirNovaMatricula((cliente.Matricula) request,
              (io.grpc.stub.StreamObserver<cliente.RetornoDefault>) responseObserver);
          break;
        case METHODID_ALTERAR_NOTAS_MATRICULA:
          serviceImpl.alterarNotasMatricula((cliente.Matricula) request,
              (io.grpc.stub.StreamObserver<cliente.RetornoDefault>) responseObserver);
          break;
        case METHODID_ALTERAR_FALTAS_MATRICULA:
          serviceImpl.alterarFaltasMatricula((cliente.Matricula) request,
              (io.grpc.stub.StreamObserver<cliente.RetornoDefault>) responseObserver);
          break;
        case METHODID_LISTA_ALUNOS_DISCIPLINA:
          serviceImpl.listaAlunosDisciplina((cliente.RequestLista) request,
              (io.grpc.stub.StreamObserver<cliente.ReturnListaAlunos>) responseObserver);
          break;
        case METHODID_LISTA_DISCIPLINA_ALUNO:
          serviceImpl.listaDisciplinaAluno((cliente.RequestLista) request,
              (io.grpc.stub.StreamObserver<cliente.ReturnListaMatriculas>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static final class GerenciadorNotasDescriptorSupplier implements io.grpc.protobuf.ProtoFileDescriptorSupplier {
    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return cliente.Notas.getDescriptor();
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (GerenciadorNotasGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new GerenciadorNotasDescriptorSupplier())
              .addMethod(METHOD_INSERIR_NOVA_MATRICULA)
              .addMethod(METHOD_ALTERAR_NOTAS_MATRICULA)
              .addMethod(METHOD_ALTERAR_FALTAS_MATRICULA)
              .addMethod(METHOD_LISTA_ALUNOS_DISCIPLINA)
              .addMethod(METHOD_LISTA_DISCIPLINA_ALUNO)
              .build();
        }
      }
    }
    return result;
  }
}
