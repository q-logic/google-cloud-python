# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/model.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1.proto import (
    translation_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_translation__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/model.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\032com.google.cloud.automl.v1P\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoML\\V1\352\002\031Google::Cloud::AutoML::V1"
    ),
    serialized_pb=_b(
        '\n(google/cloud/automl_v1/proto/model.proto\x12\x16google.cloud.automl.v1\x1a.google/cloud/automl_v1/proto/translation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto"\x91\x04\n\x05Model\x12V\n\x1atranslation_model_metadata\x18\x0f \x01(\x0b\x32\x30.google.cloud.automl.v1.TranslationModelMetadataH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x12\n\ndataset_id\x18\x03 \x01(\t\x12/\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x10\x64\x65ployment_state\x18\x08 \x01(\x0e\x32-.google.cloud.automl.v1.Model.DeploymentState\x12\x39\n\x06labels\x18" \x03(\x0b\x32).google.cloud.automl.v1.Model.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"Q\n\x0f\x44\x65ploymentState\x12 \n\x1c\x44\x45PLOYMENT_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44\x45PLOYED\x10\x01\x12\x0e\n\nUNDEPLOYED\x10\x02\x42\x10\n\x0emodel_metadataB\xaa\x01\n\x1a\x63om.google.cloud.automl.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoML\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3'
    ),
    dependencies=[
        google_dot_cloud_dot_automl__v1_dot_proto_dot_translation__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_MODEL_DEPLOYMENTSTATE = _descriptor.EnumDescriptor(
    name="DeploymentState",
    full_name="google.cloud.automl.v1.Model.DeploymentState",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="DEPLOYMENT_STATE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="DEPLOYED", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="UNDEPLOYED", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=610,
    serialized_end=691,
)
_sym_db.RegisterEnumDescriptor(_MODEL_DEPLOYMENTSTATE)


_MODEL_LABELSENTRY = _descriptor.Descriptor(
    name="LabelsEntry",
    full_name="google.cloud.automl.v1.Model.LabelsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1.Model.LabelsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1.Model.LabelsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=563,
    serialized_end=608,
)

_MODEL = _descriptor.Descriptor(
    name="Model",
    full_name="google.cloud.automl.v1.Model",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="translation_model_metadata",
            full_name="google.cloud.automl.v1.Model.translation_model_metadata",
            index=0,
            number=15,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1.Model.name",
            index=1,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.automl.v1.Model.display_name",
            index=2,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dataset_id",
            full_name="google.cloud.automl.v1.Model.dataset_id",
            index=3,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.automl.v1.Model.create_time",
            index=4,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update_time",
            full_name="google.cloud.automl.v1.Model.update_time",
            index=5,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="deployment_state",
            full_name="google.cloud.automl.v1.Model.deployment_state",
            index=6,
            number=8,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="labels",
            full_name="google.cloud.automl.v1.Model.labels",
            index=7,
            number=34,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_MODEL_LABELSENTRY],
    enum_types=[_MODEL_DEPLOYMENTSTATE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="model_metadata",
            full_name="google.cloud.automl.v1.Model.model_metadata",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=180,
    serialized_end=709,
)

_MODEL_LABELSENTRY.containing_type = _MODEL
_MODEL.fields_by_name[
    "translation_model_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_translation__pb2._TRANSLATIONMODELMETADATA
)
_MODEL.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MODEL.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MODEL.fields_by_name["deployment_state"].enum_type = _MODEL_DEPLOYMENTSTATE
_MODEL.fields_by_name["labels"].message_type = _MODEL_LABELSENTRY
_MODEL_DEPLOYMENTSTATE.containing_type = _MODEL
_MODEL.oneofs_by_name["model_metadata"].fields.append(
    _MODEL.fields_by_name["translation_model_metadata"]
)
_MODEL.fields_by_name[
    "translation_model_metadata"
].containing_oneof = _MODEL.oneofs_by_name["model_metadata"]
DESCRIPTOR.message_types_by_name["Model"] = _MODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Model = _reflection.GeneratedProtocolMessageType(
    "Model",
    (_message.Message,),
    dict(
        LabelsEntry=_reflection.GeneratedProtocolMessageType(
            "LabelsEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_MODEL_LABELSENTRY,
                __module__="google.cloud.automl_v1.proto.model_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.Model.LabelsEntry)
            ),
        ),
        DESCRIPTOR=_MODEL,
        __module__="google.cloud.automl_v1.proto.model_pb2",
        __doc__="""API proto representing a trained machine learning model.
  
  
  Attributes:
      model_metadata:
          Required. The model metadata that is specific to the problem
          type. Must match the metadata type of the dataset used to
          train the model.
      translation_model_metadata:
          Metadata for translation models.
      name:
          Output only. Resource name of the model. Format: ``projects/{p
          roject_id}/locations/{location_id}/models/{model_id}``
      display_name:
          Required. The name of the model to show in the interface. The
          name can be up to 32 characters long and can consist only of
          ASCII Latin letters A-Z and a-z, underscores (\_), and ASCII
          digits 0-9. It must start with a letter.
      dataset_id:
          Required. The resource ID of the dataset used to create the
          model. The dataset must come from the same ancestor project
          and location.
      create_time:
          Output only. Timestamp when the model training finished and
          can be used for prediction.
      update_time:
          Output only. Timestamp when this model was last updated.
      deployment_state:
          Output only. Deployment state of the model. A model can only
          serve prediction requests after it gets deployed.
      labels:
          Optional. The labels with user-defined metadata to organize
          your model.  Label keys and values can be no longer than 64
          characters (Unicode codepoints), can only contain lowercase
          letters, numeric characters, underscores and dashes.
          International characters are allowed. Label values are
          optional. Label keys must start with a letter.  See
          https://goo.gl/xmQnxf for more information on and examples of
          labels.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.Model)
    ),
)
_sym_db.RegisterMessage(Model)
_sym_db.RegisterMessage(Model.LabelsEntry)


DESCRIPTOR._options = None
_MODEL_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
