# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message_gnss.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import message_header_pb2 as message__header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12message_gnss.proto\x12\x0crbk.protocol\x1a\x14message_header.proto\"G\n\x17Message_GnssInstallInfo\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\x0b\n\x03yaw\x18\x04 \x01(\x01\"L\n\x13Message_GnssRefInfo\x12\x11\n\tlongitude\x18\x01 \x01(\x01\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x01\"\x85\x03\n\x0cMessage_GNSS\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.rbk.protocol.Message_Header\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\t\n\x01x\x18\x03 \x01(\x01\x12\t\n\x01y\x18\x04 \x01(\x01\x12\t\n\x01z\x18\x05 \x01(\x01\x12\x14\n\x0cubx_2d_acc_h\x18\x07 \x01(\x01\x12\x14\n\x0cubx_2d_acc_v\x18\x08 \x01(\x01\x12\x12\n\nubx_3d_acc\x18\t \x01(\x01\x12\x11\n\tlongitude\x18\n \x01(\x01\x12\x10\n\x08latitude\x18\x0b \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x0c \x01(\x01\x12;\n\x0cinstall_info\x18\r \x01(\x0b\x32%.rbk.protocol.Message_GnssInstallInfo\x12\x33\n\x08ref_info\x18\x0e \x01(\x0b\x32!.rbk.protocol.Message_GnssRefInfo\x12\r\n\x05\x65nu_x\x18\x0f \x01(\x01\x12\r\n\x05\x65nu_y\x18\x10 \x01(\x01\x12\x0f\n\x07heading\x18\x11 \x01(\x01\";\n\x0fMessage_AllGNSS\x12(\n\x04gnss\x18\x01 \x03(\x0b\x32\x1a.rbk.protocol.Message_GNSSb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_gnss_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MESSAGE_GNSSINSTALLINFO']._serialized_start=58
  _globals['_MESSAGE_GNSSINSTALLINFO']._serialized_end=129
  _globals['_MESSAGE_GNSSREFINFO']._serialized_start=131
  _globals['_MESSAGE_GNSSREFINFO']._serialized_end=207
  _globals['_MESSAGE_GNSS']._serialized_start=210
  _globals['_MESSAGE_GNSS']._serialized_end=599
  _globals['_MESSAGE_ALLGNSS']._serialized_start=601
  _globals['_MESSAGE_ALLGNSS']._serialized_end=660
# @@protoc_insertion_point(module_scope)
