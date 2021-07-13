#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# 

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import message_pb2 as message__pb2
from . import metric_service_pb2 as metric__service__pb2


class MetricServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registerMetricMeta = channel.unary_unary(
                '/ai_flow.MetricService/registerMetricMeta',
                request_serializer=metric__service__pb2.MetricMetaRequest.SerializeToString,
                response_deserializer=metric__service__pb2.MetricMetaResponse.FromString,
                )
        self.updateMetricMeta = channel.unary_unary(
                '/ai_flow.MetricService/updateMetricMeta',
                request_serializer=metric__service__pb2.MetricMetaRequest.SerializeToString,
                response_deserializer=metric__service__pb2.MetricMetaResponse.FromString,
                )
        self.deleteMetricMeta = channel.unary_unary(
                '/ai_flow.MetricService/deleteMetricMeta',
                request_serializer=metric__service__pb2.MetricNameRequest.SerializeToString,
                response_deserializer=message__pb2.Response.FromString,
                )
        self.getMetricMeta = channel.unary_unary(
                '/ai_flow.MetricService/getMetricMeta',
                request_serializer=metric__service__pb2.MetricNameRequest.SerializeToString,
                response_deserializer=metric__service__pb2.MetricMetaResponse.FromString,
                )
        self.listDatasetMetricMetas = channel.unary_unary(
                '/ai_flow.MetricService/listDatasetMetricMetas',
                request_serializer=metric__service__pb2.ListDatasetMetricMetasRequest.SerializeToString,
                response_deserializer=metric__service__pb2.ListMetricMetasResponse.FromString,
                )
        self.listModelMetricMetas = channel.unary_unary(
                '/ai_flow.MetricService/listModelMetricMetas',
                request_serializer=metric__service__pb2.ListModelMetricMetasRequest.SerializeToString,
                response_deserializer=metric__service__pb2.ListMetricMetasResponse.FromString,
                )
        self.registerMetricSummary = channel.unary_unary(
                '/ai_flow.MetricService/registerMetricSummary',
                request_serializer=metric__service__pb2.MetricSummaryRequest.SerializeToString,
                response_deserializer=metric__service__pb2.MetricSummaryResponse.FromString,
                )
        self.updateMetricSummary = channel.unary_unary(
                '/ai_flow.MetricService/updateMetricSummary',
                request_serializer=metric__service__pb2.MetricSummaryRequest.SerializeToString,
                response_deserializer=metric__service__pb2.MetricSummaryResponse.FromString,
                )
        self.deleteMetricSummary = channel.unary_unary(
                '/ai_flow.MetricService/deleteMetricSummary',
                request_serializer=metric__service__pb2.UuidRequest.SerializeToString,
                response_deserializer=message__pb2.Response.FromString,
                )
        self.getMetricSummary = channel.unary_unary(
                '/ai_flow.MetricService/getMetricSummary',
                request_serializer=metric__service__pb2.UuidRequest.SerializeToString,
                response_deserializer=metric__service__pb2.MetricSummaryResponse.FromString,
                )
        self.listMetricSummaries = channel.unary_unary(
                '/ai_flow.MetricService/listMetricSummaries',
                request_serializer=metric__service__pb2.ListMetricSummariesRequest.SerializeToString,
                response_deserializer=metric__service__pb2.ListMetricSummariesResponse.FromString,
                )


class MetricServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def registerMetricMeta(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateMetricMeta(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteMetricMeta(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMetricMeta(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listDatasetMetricMetas(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listModelMetricMetas(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registerMetricSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateMetricSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteMetricSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMetricSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listMetricSummaries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetricServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'registerMetricMeta': grpc.unary_unary_rpc_method_handler(
                    servicer.registerMetricMeta,
                    request_deserializer=metric__service__pb2.MetricMetaRequest.FromString,
                    response_serializer=metric__service__pb2.MetricMetaResponse.SerializeToString,
            ),
            'updateMetricMeta': grpc.unary_unary_rpc_method_handler(
                    servicer.updateMetricMeta,
                    request_deserializer=metric__service__pb2.MetricMetaRequest.FromString,
                    response_serializer=metric__service__pb2.MetricMetaResponse.SerializeToString,
            ),
            'deleteMetricMeta': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteMetricMeta,
                    request_deserializer=metric__service__pb2.MetricNameRequest.FromString,
                    response_serializer=message__pb2.Response.SerializeToString,
            ),
            'getMetricMeta': grpc.unary_unary_rpc_method_handler(
                    servicer.getMetricMeta,
                    request_deserializer=metric__service__pb2.MetricNameRequest.FromString,
                    response_serializer=metric__service__pb2.MetricMetaResponse.SerializeToString,
            ),
            'listDatasetMetricMetas': grpc.unary_unary_rpc_method_handler(
                    servicer.listDatasetMetricMetas,
                    request_deserializer=metric__service__pb2.ListDatasetMetricMetasRequest.FromString,
                    response_serializer=metric__service__pb2.ListMetricMetasResponse.SerializeToString,
            ),
            'listModelMetricMetas': grpc.unary_unary_rpc_method_handler(
                    servicer.listModelMetricMetas,
                    request_deserializer=metric__service__pb2.ListModelMetricMetasRequest.FromString,
                    response_serializer=metric__service__pb2.ListMetricMetasResponse.SerializeToString,
            ),
            'registerMetricSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.registerMetricSummary,
                    request_deserializer=metric__service__pb2.MetricSummaryRequest.FromString,
                    response_serializer=metric__service__pb2.MetricSummaryResponse.SerializeToString,
            ),
            'updateMetricSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.updateMetricSummary,
                    request_deserializer=metric__service__pb2.MetricSummaryRequest.FromString,
                    response_serializer=metric__service__pb2.MetricSummaryResponse.SerializeToString,
            ),
            'deleteMetricSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteMetricSummary,
                    request_deserializer=metric__service__pb2.UuidRequest.FromString,
                    response_serializer=message__pb2.Response.SerializeToString,
            ),
            'getMetricSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.getMetricSummary,
                    request_deserializer=metric__service__pb2.UuidRequest.FromString,
                    response_serializer=metric__service__pb2.MetricSummaryResponse.SerializeToString,
            ),
            'listMetricSummaries': grpc.unary_unary_rpc_method_handler(
                    servicer.listMetricSummaries,
                    request_deserializer=metric__service__pb2.ListMetricSummariesRequest.FromString,
                    response_serializer=metric__service__pb2.ListMetricSummariesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ai_flow.MetricService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MetricService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def registerMetricMeta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/registerMetricMeta',
            metric__service__pb2.MetricMetaRequest.SerializeToString,
            metric__service__pb2.MetricMetaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateMetricMeta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/updateMetricMeta',
            metric__service__pb2.MetricMetaRequest.SerializeToString,
            metric__service__pb2.MetricMetaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteMetricMeta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/deleteMetricMeta',
            metric__service__pb2.MetricNameRequest.SerializeToString,
            message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMetricMeta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/getMetricMeta',
            metric__service__pb2.MetricNameRequest.SerializeToString,
            metric__service__pb2.MetricMetaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listDatasetMetricMetas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/listDatasetMetricMetas',
            metric__service__pb2.ListDatasetMetricMetasRequest.SerializeToString,
            metric__service__pb2.ListMetricMetasResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listModelMetricMetas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/listModelMetricMetas',
            metric__service__pb2.ListModelMetricMetasRequest.SerializeToString,
            metric__service__pb2.ListMetricMetasResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def registerMetricSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/registerMetricSummary',
            metric__service__pb2.MetricSummaryRequest.SerializeToString,
            metric__service__pb2.MetricSummaryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateMetricSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/updateMetricSummary',
            metric__service__pb2.MetricSummaryRequest.SerializeToString,
            metric__service__pb2.MetricSummaryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteMetricSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/deleteMetricSummary',
            metric__service__pb2.UuidRequest.SerializeToString,
            message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMetricSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/getMetricSummary',
            metric__service__pb2.UuidRequest.SerializeToString,
            metric__service__pb2.MetricSummaryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listMetricSummaries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.MetricService/listMetricSummaries',
            metric__service__pb2.ListMetricSummariesRequest.SerializeToString,
            metric__service__pb2.ListMetricSummariesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
