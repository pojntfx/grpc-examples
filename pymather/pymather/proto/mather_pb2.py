# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pymather/proto/mather.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pymather/proto/mather.proto',
  package='com.pojtinger.felix.grpcExamples.gomather',
  syntax='proto3',
  serialized_options=b'Z:github.com/pojntfx/grpc-examples/gomather/pkg/api/proto/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bpymather/proto/mather.proto\x12)com.pojtinger.felix.grpcExamples.gomather\">\n\x0f\x41\x64\x64InputMessage\x12\x14\n\x0c\x46irstSummand\x18\x01 \x01(\x03\x12\x15\n\rSecondSummand\x18\x02 \x01(\x03\"\x1f\n\x10\x41\x64\x64OutputMessage\x12\x0b\n\x03Sum\x18\x01 \x01(\x03\x32\x88\x01\n\x06Mather\x12~\n\x03\x41\x64\x64\x12:.com.pojtinger.felix.grpcExamples.gomather.AddInputMessage\x1a;.com.pojtinger.felix.grpcExamples.gomather.AddOutputMessageB<Z:github.com/pojntfx/grpc-examples/gomather/pkg/api/proto/v1b\x06proto3'
)




_ADDINPUTMESSAGE = _descriptor.Descriptor(
  name='AddInputMessage',
  full_name='com.pojtinger.felix.grpcExamples.gomather.AddInputMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='FirstSummand', full_name='com.pojtinger.felix.grpcExamples.gomather.AddInputMessage.FirstSummand', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SecondSummand', full_name='com.pojtinger.felix.grpcExamples.gomather.AddInputMessage.SecondSummand', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=136,
)


_ADDOUTPUTMESSAGE = _descriptor.Descriptor(
  name='AddOutputMessage',
  full_name='com.pojtinger.felix.grpcExamples.gomather.AddOutputMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Sum', full_name='com.pojtinger.felix.grpcExamples.gomather.AddOutputMessage.Sum', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=169,
)

DESCRIPTOR.message_types_by_name['AddInputMessage'] = _ADDINPUTMESSAGE
DESCRIPTOR.message_types_by_name['AddOutputMessage'] = _ADDOUTPUTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddInputMessage = _reflection.GeneratedProtocolMessageType('AddInputMessage', (_message.Message,), {
  'DESCRIPTOR' : _ADDINPUTMESSAGE,
  '__module__' : 'pymather.proto.mather_pb2'
  # @@protoc_insertion_point(class_scope:com.pojtinger.felix.grpcExamples.gomather.AddInputMessage)
  })
_sym_db.RegisterMessage(AddInputMessage)

AddOutputMessage = _reflection.GeneratedProtocolMessageType('AddOutputMessage', (_message.Message,), {
  'DESCRIPTOR' : _ADDOUTPUTMESSAGE,
  '__module__' : 'pymather.proto.mather_pb2'
  # @@protoc_insertion_point(class_scope:com.pojtinger.felix.grpcExamples.gomather.AddOutputMessage)
  })
_sym_db.RegisterMessage(AddOutputMessage)


DESCRIPTOR._options = None

_MATHER = _descriptor.ServiceDescriptor(
  name='Mather',
  full_name='com.pojtinger.felix.grpcExamples.gomather.Mather',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=172,
  serialized_end=308,
  methods=[
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='com.pojtinger.felix.grpcExamples.gomather.Mather.Add',
    index=0,
    containing_service=None,
    input_type=_ADDINPUTMESSAGE,
    output_type=_ADDOUTPUTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MATHER)

DESCRIPTOR.services_by_name['Mather'] = _MATHER

# @@protoc_insertion_point(module_scope)
