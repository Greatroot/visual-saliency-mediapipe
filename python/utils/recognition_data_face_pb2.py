# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: recognition_data_face.proto
# Protobuf Python Version: 5.28.2
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
    2,
    '',
    'recognition_data_face.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1brecognition_data_face.proto\"\xb4\x01\n\x0fRecognitionData\x12\x30\n\x05\x66\x61\x63\x65s\x18\x01 \x03(\x0b\x32!.NormalizedLandmarkListCollection\x12\x15\n\raugmentations\x18\x02 \x03(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\x12\x1b\n\x13\x63ontour_thicknesses\x18\x06 \x03(\x05\x12(\n\x0f\x66\x61\x63\x65Mesh_colors\x18\x07 \x03(\x0b\x32\x0f.FaceMeshColors\"\xa2\x01\n\x12NormalizedLandmark\x12\x0e\n\x01x\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x0e\n\x01y\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x0e\n\x01z\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x17\n\nvisibility\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x15\n\x08presence\x18\x05 \x01(\x02H\x04\x88\x01\x01\x42\x04\n\x02_xB\x04\n\x02_yB\x04\n\x02_zB\r\n\x0b_visibilityB\x0b\n\t_presence\"?\n\x16NormalizedLandmarkList\x12%\n\x08landmark\x18\x01 \x03(\x0b\x32\x13.NormalizedLandmark\"R\n NormalizedLandmarkListCollection\x12.\n\rlandmark_list\x18\x01 \x03(\x0b\x32\x17.NormalizedLandmarkList\"\x83\x03\n\x0e\x46\x61\x63\x65MeshColors\x12/\n\x1b\x66\x61\x63\x65Mesh_tesselation_colors\x18\x01 \x03(\x0b\x32\n.EdgeColor\x12+\n\x17\x66\x61\x63\x65Mesh_contour_colors\x18\x02 \x03(\x0b\x32\n.EdgeColor\x12-\n\x19\x66\x61\x63\x65Mesh_rightBrow_colors\x18\x03 \x03(\x0b\x32\n.EdgeColor\x12,\n\x18\x66\x61\x63\x65Mesh_leftBrow_colors\x18\x04 \x03(\x0b\x32\n.EdgeColor\x12,\n\x18\x66\x61\x63\x65Mesh_rightEye_colors\x18\x05 \x03(\x0b\x32\n.EdgeColor\x12+\n\x17\x66\x61\x63\x65Mesh_leftEye_colors\x18\x06 \x03(\x0b\x32\n.EdgeColor\x12-\n\x19\x66\x61\x63\x65Mesh_rightIris_colors\x18\x07 \x03(\x0b\x32\n.EdgeColor\x12,\n\x18\x66\x61\x63\x65Mesh_leftIris_colors\x18\x08 \x03(\x0b\x32\n.EdgeColor\"7\n\tEdgeColor\x12\t\n\x01r\x18\x01 \x01(\x05\x12\t\n\x01g\x18\x02 \x01(\x05\x12\t\n\x01\x62\x18\x03 \x01(\x05\x12\t\n\x01\x61\x18\x04 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recognition_data_face_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RECOGNITIONDATA']._serialized_start=32
  _globals['_RECOGNITIONDATA']._serialized_end=212
  _globals['_NORMALIZEDLANDMARK']._serialized_start=215
  _globals['_NORMALIZEDLANDMARK']._serialized_end=377
  _globals['_NORMALIZEDLANDMARKLIST']._serialized_start=379
  _globals['_NORMALIZEDLANDMARKLIST']._serialized_end=442
  _globals['_NORMALIZEDLANDMARKLISTCOLLECTION']._serialized_start=444
  _globals['_NORMALIZEDLANDMARKLISTCOLLECTION']._serialized_end=526
  _globals['_FACEMESHCOLORS']._serialized_start=529
  _globals['_FACEMESHCOLORS']._serialized_end=916
  _globals['_EDGECOLOR']._serialized_start=918
  _globals['_EDGECOLOR']._serialized_end=973
# @@protoc_insertion_point(module_scope)
