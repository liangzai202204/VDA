# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/pyext/python.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"google/protobuf/pyext/python.proto\x12\x1fgoogle.protobuf.python.internal\"\xbc\x02\n\x0cTestAllTypes\x12\\\n\x17repeated_nested_message\x18\x01 \x03(\x0b\x32;.google.protobuf.python.internal.TestAllTypes.NestedMessage\x12\\\n\x17optional_nested_message\x18\x02 \x01(\x0b\x32;.google.protobuf.python.internal.TestAllTypes.NestedMessage\x12\x16\n\x0eoptional_int32\x18\x03 \x01(\x05\x1aX\n\rNestedMessage\x12\n\n\x02\x62\x62\x18\x01 \x01(\x05\x12;\n\x02\x63\x63\x18\x02 \x01(\x0b\x32/.google.protobuf.python.internal.ForeignMessage\"&\n\x0e\x46oreignMessage\x12\t\n\x01\x63\x18\x01 \x01(\x05\x12\t\n\x01\x64\x18\x02 \x03(\x05\"\x1d\n\x11TestAllExtensions*\x08\x08\x01\x10\x80\x80\x80\x80\x02:\x9a\x01\n!optional_nested_message_extension\x12\x32.google.protobuf.python.internal.TestAllExtensions\x18\x01 \x01(\x0b\x32;.google.protobuf.python.internal.TestAllTypes.NestedMessage:\x9a\x01\n!repeated_nested_message_extension\x12\x32.google.protobuf.python.internal.TestAllExtensions\x18\x02 \x03(\x0b\x32;.google.protobuf.python.internal.TestAllTypes.NestedMessageB\x02H\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.protobuf.pyext.python_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  TestAllExtensions.RegisterExtension(optional_nested_message_extension)
  TestAllExtensions.RegisterExtension(repeated_nested_message_extension)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001'
  _globals['_TESTALLTYPES']._serialized_start=72
  _globals['_TESTALLTYPES']._serialized_end=388
  _globals['_TESTALLTYPES_NESTEDMESSAGE']._serialized_start=300
  _globals['_TESTALLTYPES_NESTEDMESSAGE']._serialized_end=388
  _globals['_FOREIGNMESSAGE']._serialized_start=390
  _globals['_FOREIGNMESSAGE']._serialized_end=428
  _globals['_TESTALLEXTENSIONS']._serialized_start=430
  _globals['_TESTALLEXTENSIONS']._serialized_end=459
# @@protoc_insertion_point(module_scope)
