// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: notas.proto

package cliente;

/**
 * Protobuf type {@code ReturnListaMatriculas}
 */
public  final class ReturnListaMatriculas extends
    com.google.protobuf.GeneratedMessageV3 implements
    // @@protoc_insertion_point(message_implements:ReturnListaMatriculas)
    ReturnListaMatriculasOrBuilder {
  // Use ReturnListaMatriculas.newBuilder() to construct.
  private ReturnListaMatriculas(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
    super(builder);
  }
  private ReturnListaMatriculas() {
    matriculas_ = java.util.Collections.emptyList();
    sucesso_ = false;
    mensagem_ = "";
  }

  @java.lang.Override
  public final com.google.protobuf.UnknownFieldSet
  getUnknownFields() {
    return com.google.protobuf.UnknownFieldSet.getDefaultInstance();
  }
  private ReturnListaMatriculas(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    this();
    int mutable_bitField0_ = 0;
    try {
      boolean done = false;
      while (!done) {
        int tag = input.readTag();
        switch (tag) {
          case 0:
            done = true;
            break;
          default: {
            if (!input.skipField(tag)) {
              done = true;
            }
            break;
          }
          case 10: {
            if (!((mutable_bitField0_ & 0x00000001) == 0x00000001)) {
              matriculas_ = new java.util.ArrayList<cliente.RetornoMatricula>();
              mutable_bitField0_ |= 0x00000001;
            }
            matriculas_.add(
                input.readMessage(cliente.RetornoMatricula.parser(), extensionRegistry));
            break;
          }
          case 16: {

            sucesso_ = input.readBool();
            break;
          }
          case 26: {
            java.lang.String s = input.readStringRequireUtf8();

            mensagem_ = s;
            break;
          }
        }
      }
    } catch (com.google.protobuf.InvalidProtocolBufferException e) {
      throw e.setUnfinishedMessage(this);
    } catch (java.io.IOException e) {
      throw new com.google.protobuf.InvalidProtocolBufferException(
          e).setUnfinishedMessage(this);
    } finally {
      if (((mutable_bitField0_ & 0x00000001) == 0x00000001)) {
        matriculas_ = java.util.Collections.unmodifiableList(matriculas_);
      }
      makeExtensionsImmutable();
    }
  }
  public static final com.google.protobuf.Descriptors.Descriptor
      getDescriptor() {
    return cliente.Notas.internal_static_ReturnListaMatriculas_descriptor;
  }

  protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internalGetFieldAccessorTable() {
    return cliente.Notas.internal_static_ReturnListaMatriculas_fieldAccessorTable
        .ensureFieldAccessorsInitialized(
            cliente.ReturnListaMatriculas.class, cliente.ReturnListaMatriculas.Builder.class);
  }

  private int bitField0_;
  public static final int MATRICULAS_FIELD_NUMBER = 1;
  private java.util.List<cliente.RetornoMatricula> matriculas_;
  /**
   * <code>repeated .RetornoMatricula matriculas = 1;</code>
   */
  public java.util.List<cliente.RetornoMatricula> getMatriculasList() {
    return matriculas_;
  }
  /**
   * <code>repeated .RetornoMatricula matriculas = 1;</code>
   */
  public java.util.List<? extends cliente.RetornoMatriculaOrBuilder> 
      getMatriculasOrBuilderList() {
    return matriculas_;
  }
  /**
   * <code>repeated .RetornoMatricula matriculas = 1;</code>
   */
  public int getMatriculasCount() {
    return matriculas_.size();
  }
  /**
   * <code>repeated .RetornoMatricula matriculas = 1;</code>
   */
  public cliente.RetornoMatricula getMatriculas(int index) {
    return matriculas_.get(index);
  }
  /**
   * <code>repeated .RetornoMatricula matriculas = 1;</code>
   */
  public cliente.RetornoMatriculaOrBuilder getMatriculasOrBuilder(
      int index) {
    return matriculas_.get(index);
  }

  public static final int SUCESSO_FIELD_NUMBER = 2;
  private boolean sucesso_;
  /**
   * <code>bool sucesso = 2;</code>
   */
  public boolean getSucesso() {
    return sucesso_;
  }

  public static final int MENSAGEM_FIELD_NUMBER = 3;
  private volatile java.lang.Object mensagem_;
  /**
   * <code>string mensagem = 3;</code>
   */
  public java.lang.String getMensagem() {
    java.lang.Object ref = mensagem_;
    if (ref instanceof java.lang.String) {
      return (java.lang.String) ref;
    } else {
      com.google.protobuf.ByteString bs = 
          (com.google.protobuf.ByteString) ref;
      java.lang.String s = bs.toStringUtf8();
      mensagem_ = s;
      return s;
    }
  }
  /**
   * <code>string mensagem = 3;</code>
   */
  public com.google.protobuf.ByteString
      getMensagemBytes() {
    java.lang.Object ref = mensagem_;
    if (ref instanceof java.lang.String) {
      com.google.protobuf.ByteString b = 
          com.google.protobuf.ByteString.copyFromUtf8(
              (java.lang.String) ref);
      mensagem_ = b;
      return b;
    } else {
      return (com.google.protobuf.ByteString) ref;
    }
  }

  private byte memoizedIsInitialized = -1;
  public final boolean isInitialized() {
    byte isInitialized = memoizedIsInitialized;
    if (isInitialized == 1) return true;
    if (isInitialized == 0) return false;

    memoizedIsInitialized = 1;
    return true;
  }

  public void writeTo(com.google.protobuf.CodedOutputStream output)
                      throws java.io.IOException {
    for (int i = 0; i < matriculas_.size(); i++) {
      output.writeMessage(1, matriculas_.get(i));
    }
    if (sucesso_ != false) {
      output.writeBool(2, sucesso_);
    }
    if (!getMensagemBytes().isEmpty()) {
      com.google.protobuf.GeneratedMessageV3.writeString(output, 3, mensagem_);
    }
  }

  public int getSerializedSize() {
    int size = memoizedSize;
    if (size != -1) return size;

    size = 0;
    for (int i = 0; i < matriculas_.size(); i++) {
      size += com.google.protobuf.CodedOutputStream
        .computeMessageSize(1, matriculas_.get(i));
    }
    if (sucesso_ != false) {
      size += com.google.protobuf.CodedOutputStream
        .computeBoolSize(2, sucesso_);
    }
    if (!getMensagemBytes().isEmpty()) {
      size += com.google.protobuf.GeneratedMessageV3.computeStringSize(3, mensagem_);
    }
    memoizedSize = size;
    return size;
  }

  private static final long serialVersionUID = 0L;
  @java.lang.Override
  public boolean equals(final java.lang.Object obj) {
    if (obj == this) {
     return true;
    }
    if (!(obj instanceof cliente.ReturnListaMatriculas)) {
      return super.equals(obj);
    }
    cliente.ReturnListaMatriculas other = (cliente.ReturnListaMatriculas) obj;

    boolean result = true;
    result = result && getMatriculasList()
        .equals(other.getMatriculasList());
    result = result && (getSucesso()
        == other.getSucesso());
    result = result && getMensagem()
        .equals(other.getMensagem());
    return result;
  }

  @java.lang.Override
  public int hashCode() {
    if (memoizedHashCode != 0) {
      return memoizedHashCode;
    }
    int hash = 41;
    hash = (19 * hash) + getDescriptor().hashCode();
    if (getMatriculasCount() > 0) {
      hash = (37 * hash) + MATRICULAS_FIELD_NUMBER;
      hash = (53 * hash) + getMatriculasList().hashCode();
    }
    hash = (37 * hash) + SUCESSO_FIELD_NUMBER;
    hash = (53 * hash) + com.google.protobuf.Internal.hashBoolean(
        getSucesso());
    hash = (37 * hash) + MENSAGEM_FIELD_NUMBER;
    hash = (53 * hash) + getMensagem().hashCode();
    hash = (29 * hash) + unknownFields.hashCode();
    memoizedHashCode = hash;
    return hash;
  }

  public static cliente.ReturnListaMatriculas parseFrom(
      java.nio.ByteBuffer data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static cliente.ReturnListaMatriculas parseFrom(
      java.nio.ByteBuffer data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static cliente.ReturnListaMatriculas parseFrom(
      com.google.protobuf.ByteString data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static cliente.ReturnListaMatriculas parseFrom(
      com.google.protobuf.ByteString data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static cliente.ReturnListaMatriculas parseFrom(byte[] data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static cliente.ReturnListaMatriculas parseFrom(
      byte[] data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static cliente.ReturnListaMatriculas parseFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static cliente.ReturnListaMatriculas parseFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }
  public static cliente.ReturnListaMatriculas parseDelimitedFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input);
  }
  public static cliente.ReturnListaMatriculas parseDelimitedFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input, extensionRegistry);
  }
  public static cliente.ReturnListaMatriculas parseFrom(
      com.google.protobuf.CodedInputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static cliente.ReturnListaMatriculas parseFrom(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }

  public Builder newBuilderForType() { return newBuilder(); }
  public static Builder newBuilder() {
    return DEFAULT_INSTANCE.toBuilder();
  }
  public static Builder newBuilder(cliente.ReturnListaMatriculas prototype) {
    return DEFAULT_INSTANCE.toBuilder().mergeFrom(prototype);
  }
  public Builder toBuilder() {
    return this == DEFAULT_INSTANCE
        ? new Builder() : new Builder().mergeFrom(this);
  }

  @java.lang.Override
  protected Builder newBuilderForType(
      com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
    Builder builder = new Builder(parent);
    return builder;
  }
  /**
   * Protobuf type {@code ReturnListaMatriculas}
   */
  public static final class Builder extends
      com.google.protobuf.GeneratedMessageV3.Builder<Builder> implements
      // @@protoc_insertion_point(builder_implements:ReturnListaMatriculas)
      cliente.ReturnListaMatriculasOrBuilder {
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return cliente.Notas.internal_static_ReturnListaMatriculas_descriptor;
    }

    protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return cliente.Notas.internal_static_ReturnListaMatriculas_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              cliente.ReturnListaMatriculas.class, cliente.ReturnListaMatriculas.Builder.class);
    }

    // Construct using cliente.ReturnListaMatriculas.newBuilder()
    private Builder() {
      maybeForceBuilderInitialization();
    }

    private Builder(
        com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
      super(parent);
      maybeForceBuilderInitialization();
    }
    private void maybeForceBuilderInitialization() {
      if (com.google.protobuf.GeneratedMessageV3
              .alwaysUseFieldBuilders) {
        getMatriculasFieldBuilder();
      }
    }
    public Builder clear() {
      super.clear();
      if (matriculasBuilder_ == null) {
        matriculas_ = java.util.Collections.emptyList();
        bitField0_ = (bitField0_ & ~0x00000001);
      } else {
        matriculasBuilder_.clear();
      }
      sucesso_ = false;

      mensagem_ = "";

      return this;
    }

    public com.google.protobuf.Descriptors.Descriptor
        getDescriptorForType() {
      return cliente.Notas.internal_static_ReturnListaMatriculas_descriptor;
    }

    public cliente.ReturnListaMatriculas getDefaultInstanceForType() {
      return cliente.ReturnListaMatriculas.getDefaultInstance();
    }

    public cliente.ReturnListaMatriculas build() {
      cliente.ReturnListaMatriculas result = buildPartial();
      if (!result.isInitialized()) {
        throw newUninitializedMessageException(result);
      }
      return result;
    }

    public cliente.ReturnListaMatriculas buildPartial() {
      cliente.ReturnListaMatriculas result = new cliente.ReturnListaMatriculas(this);
      int from_bitField0_ = bitField0_;
      int to_bitField0_ = 0;
      if (matriculasBuilder_ == null) {
        if (((bitField0_ & 0x00000001) == 0x00000001)) {
          matriculas_ = java.util.Collections.unmodifiableList(matriculas_);
          bitField0_ = (bitField0_ & ~0x00000001);
        }
        result.matriculas_ = matriculas_;
      } else {
        result.matriculas_ = matriculasBuilder_.build();
      }
      result.sucesso_ = sucesso_;
      result.mensagem_ = mensagem_;
      result.bitField0_ = to_bitField0_;
      onBuilt();
      return result;
    }

    public Builder clone() {
      return (Builder) super.clone();
    }
    public Builder setField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        Object value) {
      return (Builder) super.setField(field, value);
    }
    public Builder clearField(
        com.google.protobuf.Descriptors.FieldDescriptor field) {
      return (Builder) super.clearField(field);
    }
    public Builder clearOneof(
        com.google.protobuf.Descriptors.OneofDescriptor oneof) {
      return (Builder) super.clearOneof(oneof);
    }
    public Builder setRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        int index, Object value) {
      return (Builder) super.setRepeatedField(field, index, value);
    }
    public Builder addRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        Object value) {
      return (Builder) super.addRepeatedField(field, value);
    }
    public Builder mergeFrom(com.google.protobuf.Message other) {
      if (other instanceof cliente.ReturnListaMatriculas) {
        return mergeFrom((cliente.ReturnListaMatriculas)other);
      } else {
        super.mergeFrom(other);
        return this;
      }
    }

    public Builder mergeFrom(cliente.ReturnListaMatriculas other) {
      if (other == cliente.ReturnListaMatriculas.getDefaultInstance()) return this;
      if (matriculasBuilder_ == null) {
        if (!other.matriculas_.isEmpty()) {
          if (matriculas_.isEmpty()) {
            matriculas_ = other.matriculas_;
            bitField0_ = (bitField0_ & ~0x00000001);
          } else {
            ensureMatriculasIsMutable();
            matriculas_.addAll(other.matriculas_);
          }
          onChanged();
        }
      } else {
        if (!other.matriculas_.isEmpty()) {
          if (matriculasBuilder_.isEmpty()) {
            matriculasBuilder_.dispose();
            matriculasBuilder_ = null;
            matriculas_ = other.matriculas_;
            bitField0_ = (bitField0_ & ~0x00000001);
            matriculasBuilder_ = 
              com.google.protobuf.GeneratedMessageV3.alwaysUseFieldBuilders ?
                 getMatriculasFieldBuilder() : null;
          } else {
            matriculasBuilder_.addAllMessages(other.matriculas_);
          }
        }
      }
      if (other.getSucesso() != false) {
        setSucesso(other.getSucesso());
      }
      if (!other.getMensagem().isEmpty()) {
        mensagem_ = other.mensagem_;
        onChanged();
      }
      onChanged();
      return this;
    }

    public final boolean isInitialized() {
      return true;
    }

    public Builder mergeFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      cliente.ReturnListaMatriculas parsedMessage = null;
      try {
        parsedMessage = PARSER.parsePartialFrom(input, extensionRegistry);
      } catch (com.google.protobuf.InvalidProtocolBufferException e) {
        parsedMessage = (cliente.ReturnListaMatriculas) e.getUnfinishedMessage();
        throw e.unwrapIOException();
      } finally {
        if (parsedMessage != null) {
          mergeFrom(parsedMessage);
        }
      }
      return this;
    }
    private int bitField0_;

    private java.util.List<cliente.RetornoMatricula> matriculas_ =
      java.util.Collections.emptyList();
    private void ensureMatriculasIsMutable() {
      if (!((bitField0_ & 0x00000001) == 0x00000001)) {
        matriculas_ = new java.util.ArrayList<cliente.RetornoMatricula>(matriculas_);
        bitField0_ |= 0x00000001;
       }
    }

    private com.google.protobuf.RepeatedFieldBuilderV3<
        cliente.RetornoMatricula, cliente.RetornoMatricula.Builder, cliente.RetornoMatriculaOrBuilder> matriculasBuilder_;

    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public java.util.List<cliente.RetornoMatricula> getMatriculasList() {
      if (matriculasBuilder_ == null) {
        return java.util.Collections.unmodifiableList(matriculas_);
      } else {
        return matriculasBuilder_.getMessageList();
      }
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public int getMatriculasCount() {
      if (matriculasBuilder_ == null) {
        return matriculas_.size();
      } else {
        return matriculasBuilder_.getCount();
      }
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public cliente.RetornoMatricula getMatriculas(int index) {
      if (matriculasBuilder_ == null) {
        return matriculas_.get(index);
      } else {
        return matriculasBuilder_.getMessage(index);
      }
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public Builder setMatriculas(
        int index, cliente.RetornoMatricula value) {
      if (matriculasBuilder_ == null) {
        if (value == null) {
          throw new NullPointerException();
        }
        ensureMatriculasIsMutable();
        matriculas_.set(index, value);
        onChanged();
      } else {
        matriculasBuilder_.setMessage(index, value);
      }
      return this;
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public Builder setMatriculas(
        int index, cliente.RetornoMatricula.Builder builderForValue) {
      if (matriculasBuilder_ == null) {
        ensureMatriculasIsMutable();
        matriculas_.set(index, builderForValue.build());
        onChanged();
      } else {
        matriculasBuilder_.setMessage(index, builderForValue.build());
      }
      return this;
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public Builder addMatriculas(cliente.RetornoMatricula value) {
      if (matriculasBuilder_ == null) {
        if (value == null) {
          throw new NullPointerException();
        }
        ensureMatriculasIsMutable();
        matriculas_.add(value);
        onChanged();
      } else {
        matriculasBuilder_.addMessage(value);
      }
      return this;
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public Builder addMatriculas(
        int index, cliente.RetornoMatricula value) {
      if (matriculasBuilder_ == null) {
        if (value == null) {
          throw new NullPointerException();
        }
        ensureMatriculasIsMutable();
        matriculas_.add(index, value);
        onChanged();
      } else {
        matriculasBuilder_.addMessage(index, value);
      }
      return this;
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public Builder addMatriculas(
        cliente.RetornoMatricula.Builder builderForValue) {
      if (matriculasBuilder_ == null) {
        ensureMatriculasIsMutable();
        matriculas_.add(builderForValue.build());
        onChanged();
      } else {
        matriculasBuilder_.addMessage(builderForValue.build());
      }
      return this;
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public Builder addMatriculas(
        int index, cliente.RetornoMatricula.Builder builderForValue) {
      if (matriculasBuilder_ == null) {
        ensureMatriculasIsMutable();
        matriculas_.add(index, builderForValue.build());
        onChanged();
      } else {
        matriculasBuilder_.addMessage(index, builderForValue.build());
      }
      return this;
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public Builder addAllMatriculas(
        java.lang.Iterable<? extends cliente.RetornoMatricula> values) {
      if (matriculasBuilder_ == null) {
        ensureMatriculasIsMutable();
        com.google.protobuf.AbstractMessageLite.Builder.addAll(
            values, matriculas_);
        onChanged();
      } else {
        matriculasBuilder_.addAllMessages(values);
      }
      return this;
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public Builder clearMatriculas() {
      if (matriculasBuilder_ == null) {
        matriculas_ = java.util.Collections.emptyList();
        bitField0_ = (bitField0_ & ~0x00000001);
        onChanged();
      } else {
        matriculasBuilder_.clear();
      }
      return this;
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public Builder removeMatriculas(int index) {
      if (matriculasBuilder_ == null) {
        ensureMatriculasIsMutable();
        matriculas_.remove(index);
        onChanged();
      } else {
        matriculasBuilder_.remove(index);
      }
      return this;
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public cliente.RetornoMatricula.Builder getMatriculasBuilder(
        int index) {
      return getMatriculasFieldBuilder().getBuilder(index);
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public cliente.RetornoMatriculaOrBuilder getMatriculasOrBuilder(
        int index) {
      if (matriculasBuilder_ == null) {
        return matriculas_.get(index);  } else {
        return matriculasBuilder_.getMessageOrBuilder(index);
      }
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public java.util.List<? extends cliente.RetornoMatriculaOrBuilder> 
         getMatriculasOrBuilderList() {
      if (matriculasBuilder_ != null) {
        return matriculasBuilder_.getMessageOrBuilderList();
      } else {
        return java.util.Collections.unmodifiableList(matriculas_);
      }
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public cliente.RetornoMatricula.Builder addMatriculasBuilder() {
      return getMatriculasFieldBuilder().addBuilder(
          cliente.RetornoMatricula.getDefaultInstance());
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public cliente.RetornoMatricula.Builder addMatriculasBuilder(
        int index) {
      return getMatriculasFieldBuilder().addBuilder(
          index, cliente.RetornoMatricula.getDefaultInstance());
    }
    /**
     * <code>repeated .RetornoMatricula matriculas = 1;</code>
     */
    public java.util.List<cliente.RetornoMatricula.Builder> 
         getMatriculasBuilderList() {
      return getMatriculasFieldBuilder().getBuilderList();
    }
    private com.google.protobuf.RepeatedFieldBuilderV3<
        cliente.RetornoMatricula, cliente.RetornoMatricula.Builder, cliente.RetornoMatriculaOrBuilder> 
        getMatriculasFieldBuilder() {
      if (matriculasBuilder_ == null) {
        matriculasBuilder_ = new com.google.protobuf.RepeatedFieldBuilderV3<
            cliente.RetornoMatricula, cliente.RetornoMatricula.Builder, cliente.RetornoMatriculaOrBuilder>(
                matriculas_,
                ((bitField0_ & 0x00000001) == 0x00000001),
                getParentForChildren(),
                isClean());
        matriculas_ = null;
      }
      return matriculasBuilder_;
    }

    private boolean sucesso_ ;
    /**
     * <code>bool sucesso = 2;</code>
     */
    public boolean getSucesso() {
      return sucesso_;
    }
    /**
     * <code>bool sucesso = 2;</code>
     */
    public Builder setSucesso(boolean value) {
      
      sucesso_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>bool sucesso = 2;</code>
     */
    public Builder clearSucesso() {
      
      sucesso_ = false;
      onChanged();
      return this;
    }

    private java.lang.Object mensagem_ = "";
    /**
     * <code>string mensagem = 3;</code>
     */
    public java.lang.String getMensagem() {
      java.lang.Object ref = mensagem_;
      if (!(ref instanceof java.lang.String)) {
        com.google.protobuf.ByteString bs =
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        mensagem_ = s;
        return s;
      } else {
        return (java.lang.String) ref;
      }
    }
    /**
     * <code>string mensagem = 3;</code>
     */
    public com.google.protobuf.ByteString
        getMensagemBytes() {
      java.lang.Object ref = mensagem_;
      if (ref instanceof String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        mensagem_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }
    /**
     * <code>string mensagem = 3;</code>
     */
    public Builder setMensagem(
        java.lang.String value) {
      if (value == null) {
    throw new NullPointerException();
  }
  
      mensagem_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>string mensagem = 3;</code>
     */
    public Builder clearMensagem() {
      
      mensagem_ = getDefaultInstance().getMensagem();
      onChanged();
      return this;
    }
    /**
     * <code>string mensagem = 3;</code>
     */
    public Builder setMensagemBytes(
        com.google.protobuf.ByteString value) {
      if (value == null) {
    throw new NullPointerException();
  }
  checkByteStringIsUtf8(value);
      
      mensagem_ = value;
      onChanged();
      return this;
    }
    public final Builder setUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return this;
    }

    public final Builder mergeUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return this;
    }


    // @@protoc_insertion_point(builder_scope:ReturnListaMatriculas)
  }

  // @@protoc_insertion_point(class_scope:ReturnListaMatriculas)
  private static final cliente.ReturnListaMatriculas DEFAULT_INSTANCE;
  static {
    DEFAULT_INSTANCE = new cliente.ReturnListaMatriculas();
  }

  public static cliente.ReturnListaMatriculas getDefaultInstance() {
    return DEFAULT_INSTANCE;
  }

  private static final com.google.protobuf.Parser<ReturnListaMatriculas>
      PARSER = new com.google.protobuf.AbstractParser<ReturnListaMatriculas>() {
    public ReturnListaMatriculas parsePartialFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
        return new ReturnListaMatriculas(input, extensionRegistry);
    }
  };

  public static com.google.protobuf.Parser<ReturnListaMatriculas> parser() {
    return PARSER;
  }

  @java.lang.Override
  public com.google.protobuf.Parser<ReturnListaMatriculas> getParserForType() {
    return PARSER;
  }

  public cliente.ReturnListaMatriculas getDefaultInstanceForType() {
    return DEFAULT_INSTANCE;
  }

}

