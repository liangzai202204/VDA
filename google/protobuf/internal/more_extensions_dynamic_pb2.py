# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/more_extensions_dynamic.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf.internal import more_extensions_pb2 as google_dot_protobuf_dot_internal_dot_more__extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/protobuf/internal/more_extensions_dynamic.proto\x12\x18google.protobuf.internal\x1a.google/protobuf/internal/more_extensions.proto\"\x1f\n\x12\x44ynamicMessageType\x12\t\n\x01\x61\x18\x01 \x01(\x05:J\n\x17\x64ynamic_int32_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x64 \x01(\x05:z\n\x19\x64ynamic_message_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x65 \x01(\x0b\x32,.google.protobuf.internal.DynamicMessageType:\x83\x01\n\"repeated_dynamic_message_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x66 \x03(\x0b\x32,.google.protobuf.internal.DynamicMessageType')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.protobuf.internal.more_extensions_dynamic_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_internal_dot_more__extensions__pb2.ExtendedMessage.RegisterExtension(dynamic_int32_extension)
  google_dot_protobuf_dot_internal_dot_more__extensions__pb2.ExtendedMessage.RegisterExtension(dynamic_message_extension)
  google_dot_protobuf_dot_internal_dot_more__extensions__pb2.ExtendedMessage.RegisterExtension(repeated_dynamic_message_extension)

  DESCRIPTOR._options = None
  _globals['_DYNAMICMESSAGETYPE']._serialized_start=132
  _globals['_DYNAMICMESSAGETYPE']._serialized_end=163
# @@protoc_insertion_point(module_scope)
