# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msp/identities.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msp/identities.proto',
  package='msp',
  syntax='proto3',
  serialized_pb=_b('\n\x14msp/identities.proto\x12\x03msp\"5\n\x12SerializedIdentity\x12\r\n\x05mspid\x18\x01 \x01(\t\x12\x10\n\x08id_bytes\x18\x02 \x01(\x0c\x42M\n!org.hyperledger.fabric.protos.mspZ(github.com/foglink/fnkcore/src/protos/mspb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SERIALIZEDIDENTITY = _descriptor.Descriptor(
  name='SerializedIdentity',
  full_name='msp.SerializedIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mspid', full_name='msp.SerializedIdentity.mspid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id_bytes', full_name='msp.SerializedIdentity.id_bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['SerializedIdentity'] = _SERIALIZEDIDENTITY

SerializedIdentity = _reflection.GeneratedProtocolMessageType('SerializedIdentity', (_message.Message,), dict(
  DESCRIPTOR = _SERIALIZEDIDENTITY,
  __module__ = 'msp.identities_pb2'
  # @@protoc_insertion_point(class_scope:msp.SerializedIdentity)
  ))
_sym_db.RegisterMessage(SerializedIdentity)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!org.hyperledger.fabric.protos.mspZ(github.com/foglink/fnkcore/src/protos/msp'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
