# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\"\x1a\n\x07Request\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t2\xbf\x01\n\x0e\x45xampleService\x12\x1f\n\x08SayHello\x12\x08.Request\x1a\t.Response\x12-\n\x14SayHelloClientStream\x12\x08.Request\x1a\t.Response(\x01\x12-\n\x14SayHelloServerStream\x12\x08.Request\x1a\t.Response0\x01\x12.\n\x13SayHelloByDicStream\x12\x08.Request\x1a\t.Response(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=17
  _globals['_REQUEST']._serialized_end=43
  _globals['_RESPONSE']._serialized_start=45
  _globals['_RESPONSE']._serialized_end=72
  _globals['_EXAMPLESERVICE']._serialized_start=75
  _globals['_EXAMPLESERVICE']._serialized_end=266
# @@protoc_insertion_point(module_scope)
