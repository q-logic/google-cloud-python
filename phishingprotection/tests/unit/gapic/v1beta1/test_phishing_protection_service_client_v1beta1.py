# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pytest

from google.cloud import phishingprotection_v1beta1
from google.cloud.phishingprotection_v1beta1.proto import phishingprotection_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestPhishingProtectionServiceClient(object):
    def test_report_phishing(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = phishingprotection_pb2.ReportPhishingResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = phishingprotection_v1beta1.PhishingProtectionServiceClient()

        # Setup Request
        parent = client.project_path("[PROJECT]")
        uri = "uri116076"

        response = client.report_phishing(parent, uri)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = phishingprotection_pb2.ReportPhishingRequest(
            parent=parent, uri=uri
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_report_phishing_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = phishingprotection_v1beta1.PhishingProtectionServiceClient()

        # Setup request
        parent = client.project_path("[PROJECT]")
        uri = "uri116076"

        with pytest.raises(CustomException):
            client.report_phishing(parent, uri)
