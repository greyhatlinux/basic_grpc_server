# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: message.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'message.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from google.protobuf import message

class Request(message.Message):
    __slots__ = ()
    DESCRIPTOR = None

class Response(message.Message):
    __slots__ = ()
    DESCRIPTOR = None


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\"\x15\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\x05\"\'\n\x08Response\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t2.\n\x08\x45mployee\x12\"\n\x0bGetEmployee\x12\x08.Request\x1a\t.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQUEST']._serialized_start=17
  _globals['_REQUEST']._serialized_end=38
  _globals['_RESPONSE']._serialized_start=40
  _globals['_RESPONSE']._serialized_end=79
  _globals['_EMPLOYEE']._serialized_start=81
  _globals['_EMPLOYEE']._serialized_end=127
# @@protoc_insertion_point(module_scope)