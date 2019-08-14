# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.automl_v1beta1.proto import (
    prediction_service_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_prediction__service__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class PredictionServiceStub(object):
    """AutoML Prediction API.

  On any input that is documented to expect a string parameter in
  snake_case or kebab-case, either of those cases is accepted.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.Predict = channel.unary_unary(
            "/google.cloud.automl.v1beta1.PredictionService/Predict",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_prediction__service__pb2.PredictRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_prediction__service__pb2.PredictResponse.FromString,
        )
        self.BatchPredict = channel.unary_unary(
            "/google.cloud.automl.v1beta1.PredictionService/BatchPredict",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_prediction__service__pb2.BatchPredictRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class PredictionServiceServicer(object):
    """AutoML Prediction API.

  On any input that is documented to expect a string parameter in
  snake_case or kebab-case, either of those cases is accepted.
  """

    def Predict(self, request, context):
        """Perform an online prediction. The prediction result will be directly
    returned in the response.
    Available for following ML problems, and their expected request payloads:
    * Image Classification - Image in .JPEG, .GIF or .PNG format, image_bytes
    up to 30MB.
    * Image Object Detection - Image in .JPEG, .GIF or .PNG format, image_bytes
    up to 30MB.
    * Text Classification - TextSnippet, content up to 60,000 characters,
    UTF-8 encoded.
    * Text Extraction - TextSnippet, content up to 30,000 characters,
    UTF-8 NFC encoded.
    * Translation - TextSnippet, content up to 25,000 characters, UTF-8
    encoded.
    * Tables - Row, with column values matching the columns of the model,
    up to 5MB. Not available for FORECASTING

    [prediction_type][google.cloud.automl.v1beta1.TablesModelMetadata.prediction_type].
    * Text Sentiment - TextSnippet, content up 500 characters, UTF-8
    encoded.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchPredict(self, request, context):
        """Perform a batch prediction. Unlike the online [Predict][google.cloud.automl.v1beta1.PredictionService.Predict], batch
    prediction result won't be immediately available in the response. Instead,
    a long running operation object is returned. User can poll the operation
    result via [GetOperation][google.longrunning.Operations.GetOperation]
    method. Once the operation is done, [BatchPredictResult][google.cloud.automl.v1beta1.BatchPredictResult] is returned in
    the [response][google.longrunning.Operation.response] field.
    Available for following ML problems:
    * Image Classification
    * Image Object Detection
    * Video Classification
    * Video Object Tracking * Text Extraction
    * Tables
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PredictionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Predict": grpc.unary_unary_rpc_method_handler(
            servicer.Predict,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_prediction__service__pb2.PredictRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_prediction__service__pb2.PredictResponse.SerializeToString,
        ),
        "BatchPredict": grpc.unary_unary_rpc_method_handler(
            servicer.BatchPredict,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_prediction__service__pb2.BatchPredictRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.automl.v1beta1.PredictionService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
