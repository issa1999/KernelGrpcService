# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: KernelSetterService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19KernelSetterService.proto\"\x1a\n\x07REQUEST\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x18\n\x05REPLY\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\rKERNEL_OBJECT\x12\r\n\x05\x63hunk\x18\x01 \x03(\x0c\x32\xa5\x01\n\x06SETTER\x12#\n\rREMOVE_MODULE\x12\x08.REQUEST\x1a\x06.REPLY\"\x00\x12\x1e\n\x08MODPROBE\x12\x08.REQUEST\x1a\x06.REPLY\"\x00\x12#\n\rDEPLOY_MODULE\x12\x08.REQUEST\x1a\x06.REPLY\"\x00\x12\x31\n\x15INSTALL_KERNEL_OBJECT\x12\x0e.KERNEL_OBJECT\x1a\x06.REPLY\"\x00\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['REQUEST']
_REPLY = DESCRIPTOR.message_types_by_name['REPLY']
_KERNEL_OBJECT = DESCRIPTOR.message_types_by_name['KERNEL_OBJECT']
REQUEST = _reflection.GeneratedProtocolMessageType('REQUEST', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'KernelSetterService_pb2'
  # @@protoc_insertion_point(class_scope:REQUEST)
  })
_sym_db.RegisterMessage(REQUEST)

REPLY = _reflection.GeneratedProtocolMessageType('REPLY', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'KernelSetterService_pb2'
  # @@protoc_insertion_point(class_scope:REPLY)
  })
_sym_db.RegisterMessage(REPLY)

KERNEL_OBJECT = _reflection.GeneratedProtocolMessageType('KERNEL_OBJECT', (_message.Message,), {
  'DESCRIPTOR' : _KERNEL_OBJECT,
  '__module__' : 'KernelSetterService_pb2'
  # @@protoc_insertion_point(class_scope:KERNEL_OBJECT)
  })
_sym_db.RegisterMessage(KERNEL_OBJECT)

_SETTER = DESCRIPTOR.services_by_name['SETTER']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=29
  _REQUEST._serialized_end=55
  _REPLY._serialized_start=57
  _REPLY._serialized_end=81
  _KERNEL_OBJECT._serialized_start=83
  _KERNEL_OBJECT._serialized_end=113
  _SETTER._serialized_start=116
  _SETTER._serialized_end=281
# @@protoc_insertion_point(module_scope)
