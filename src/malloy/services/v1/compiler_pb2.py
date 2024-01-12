# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/v1/compiler.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aservices/v1/compiler.proto\x12\x12malloy.services.v1\"\x13\n\x11ThirdPartyRequest\"%\n\x12ThirdPartyResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\xf9\x02\n\x0e\x43ompileRequest\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.malloy.services.v1.CompileRequest.Type\x12\x35\n\x08\x64ocument\x18\x02 \x01(\x0b\x32#.malloy.services.v1.CompileDocument\x12\x37\n\nreferences\x18\x03 \x03(\x0b\x32#.malloy.services.v1.CompileDocument\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12=\n\x11sql_block_schemas\x18\x05 \x03(\x0b\x32\".malloy.services.v1.SqlBlockSchema\x12\r\n\x05query\x18\x06 \x01(\t\x12\x13\n\x0bnamed_query\x18\x07 \x01(\t\"M\n\x04Type\x12\x0b\n\x07\x43OMPILE\x10\x00\x12\x0e\n\nREFERENCES\x10\x01\x12\x11\n\rTABLE_SCHEMAS\x10\x02\x12\x15\n\x11SQL_BLOCK_SCHEMAS\x10\x03\"-\n\x0f\x43ompileResponse\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\"/\n\x0f\x43ompileDocument\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"=\n\x0bTableSchema\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nconnection\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\t\"\xfb\x02\n\x0f\x43ompilerRequest\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.malloy.services.v1.CompilerRequest.Type\x12\x13\n\x0bimport_urls\x18\x02 \x03(\t\x12\x36\n\rtable_schemas\x18\x03 \x03(\x0b\x32\x1f.malloy.services.v1.TableSchema\x12/\n\tsql_block\x18\x04 \x01(\x0b\x32\x1c.malloy.services.v1.SqlBlock\x12\x12\n\nconnection\x18\x05 \x01(\t\x12\x17\n\x0fprepared_result\x18\x06 \x01(\t\x12\x10\n\x08problems\x18\x07 \x03(\t\x12\x0f\n\x07\x63ontent\x18\x63 \x01(\t\"b\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06IMPORT\x10\x01\x12\x11\n\rTABLE_SCHEMAS\x10\x02\x12\x15\n\x11SQL_BLOCK_SCHEMAS\x10\x03\x12\x0c\n\x08\x43OMPLETE\x10\x04\x12\t\n\x05\x45RROR\x10\x05\"9\n\x08SqlBlock\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\x12\x12\n\nconnection\x18\x03 \x01(\t\";\n\x0eSqlBlockSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\x12\x0e\n\x06schema\x18\x03 \x01(\t2\x9f\x02\n\x08\x43ompiler\x12T\n\x07\x43ompile\x12\".malloy.services.v1.CompileRequest\x1a#.malloy.services.v1.CompileResponse\"\x00\x12^\n\rCompileStream\x12\".malloy.services.v1.CompileRequest\x1a#.malloy.services.v1.CompilerRequest\"\x00(\x01\x30\x01\x12]\n\nThirdParty\x12%.malloy.services.v1.ThirdPartyRequest\x1a&.malloy.services.v1.ThirdPartyResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.v1.compiler_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_THIRDPARTYREQUEST']._serialized_start=50
  _globals['_THIRDPARTYREQUEST']._serialized_end=69
  _globals['_THIRDPARTYRESPONSE']._serialized_start=71
  _globals['_THIRDPARTYRESPONSE']._serialized_end=108
  _globals['_COMPILEREQUEST']._serialized_start=111
  _globals['_COMPILEREQUEST']._serialized_end=488
  _globals['_COMPILEREQUEST_TYPE']._serialized_start=411
  _globals['_COMPILEREQUEST_TYPE']._serialized_end=488
  _globals['_COMPILERESPONSE']._serialized_start=490
  _globals['_COMPILERESPONSE']._serialized_end=535
  _globals['_COMPILEDOCUMENT']._serialized_start=537
  _globals['_COMPILEDOCUMENT']._serialized_end=584
  _globals['_TABLESCHEMA']._serialized_start=586
  _globals['_TABLESCHEMA']._serialized_end=647
  _globals['_COMPILERREQUEST']._serialized_start=650
  _globals['_COMPILERREQUEST']._serialized_end=1029
  _globals['_COMPILERREQUEST_TYPE']._serialized_start=931
  _globals['_COMPILERREQUEST_TYPE']._serialized_end=1029
  _globals['_SQLBLOCK']._serialized_start=1031
  _globals['_SQLBLOCK']._serialized_end=1088
  _globals['_SQLBLOCKSCHEMA']._serialized_start=1090
  _globals['_SQLBLOCKSCHEMA']._serialized_end=1149
  _globals['_COMPILER']._serialized_start=1152
  _globals['_COMPILER']._serialized_end=1439
# @@protoc_insertion_point(module_scope)
