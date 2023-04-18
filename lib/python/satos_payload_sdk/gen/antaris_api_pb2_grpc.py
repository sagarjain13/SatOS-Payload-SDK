# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from satos_payload_sdk.gen import antaris_api_pb2 as satos__payload__sdk_dot_gen_dot_antaris__api__pb2


class AntarisapiApplicationCallbackStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PA_StartSequence = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_StartSequence',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.StartSequenceParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PA_ShutdownApp = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ShutdownApp',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ShutdownParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PA_ProcessHealthCheck = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessHealthCheck',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.HealthCheckParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PA_ProcessResponseRegister = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessResponseRegister',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespRegisterParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PA_ProcessResponseGetCurrentLocation = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessResponseGetCurrentLocation',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespGetCurrentLocationParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PA_ProcessResponseStageFileDownload = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessResponseStageFileDownload',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespStageFileDownloadParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PA_ProcessResponsePayloadPowerControl = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessResponsePayloadPowerControl',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespPayloadPowerControlParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )


class AntarisapiApplicationCallbackServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PA_StartSequence(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PA_ShutdownApp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PA_ProcessHealthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PA_ProcessResponseRegister(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PA_ProcessResponseGetCurrentLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PA_ProcessResponseStageFileDownload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PA_ProcessResponsePayloadPowerControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AntarisapiApplicationCallbackServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PA_StartSequence': grpc.unary_unary_rpc_method_handler(
                    servicer.PA_StartSequence,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.StartSequenceParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PA_ShutdownApp': grpc.unary_unary_rpc_method_handler(
                    servicer.PA_ShutdownApp,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ShutdownParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PA_ProcessHealthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.PA_ProcessHealthCheck,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.HealthCheckParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PA_ProcessResponseRegister': grpc.unary_unary_rpc_method_handler(
                    servicer.PA_ProcessResponseRegister,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespRegisterParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PA_ProcessResponseGetCurrentLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.PA_ProcessResponseGetCurrentLocation,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespGetCurrentLocationParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PA_ProcessResponseStageFileDownload': grpc.unary_unary_rpc_method_handler(
                    servicer.PA_ProcessResponseStageFileDownload,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespStageFileDownloadParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PA_ProcessResponsePayloadPowerControl': grpc.unary_unary_rpc_method_handler(
                    servicer.PA_ProcessResponsePayloadPowerControl,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespPayloadPowerControlParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'antaris_api_peer_to_peer.AntarisapiApplicationCallback', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AntarisapiApplicationCallback(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PA_StartSequence(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_StartSequence',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.StartSequenceParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PA_ShutdownApp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ShutdownApp',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ShutdownParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PA_ProcessHealthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessHealthCheck',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.HealthCheckParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PA_ProcessResponseRegister(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessResponseRegister',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespRegisterParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PA_ProcessResponseGetCurrentLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessResponseGetCurrentLocation',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespGetCurrentLocationParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PA_ProcessResponseStageFileDownload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessResponseStageFileDownload',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespStageFileDownloadParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PA_ProcessResponsePayloadPowerControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiApplicationCallback/PA_ProcessResponsePayloadPowerControl',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespPayloadPowerControlParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AntarisapiPayloadControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PC_register = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_register',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqRegisterParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PC_get_current_location = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_get_current_location',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqGetCurrentLocationParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PC_stage_file_download = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_stage_file_download',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqStageFileDownloadParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PC_sequence_done = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_sequence_done',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.CmdSequenceDoneParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PC_payload_power_control = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_payload_power_control',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqPayloadPowerControlParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PC_response_health_check = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_response_health_check',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespHealthCheckParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )
        self.PC_response_shutdown = channel.unary_unary(
                '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_response_shutdown',
                request_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespShutdownParams.SerializeToString,
                response_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
                )


class AntarisapiPayloadControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PC_register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PC_get_current_location(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PC_stage_file_download(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PC_sequence_done(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PC_payload_power_control(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PC_response_health_check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PC_response_shutdown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AntarisapiPayloadControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PC_register': grpc.unary_unary_rpc_method_handler(
                    servicer.PC_register,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqRegisterParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PC_get_current_location': grpc.unary_unary_rpc_method_handler(
                    servicer.PC_get_current_location,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqGetCurrentLocationParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PC_stage_file_download': grpc.unary_unary_rpc_method_handler(
                    servicer.PC_stage_file_download,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqStageFileDownloadParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PC_sequence_done': grpc.unary_unary_rpc_method_handler(
                    servicer.PC_sequence_done,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.CmdSequenceDoneParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PC_payload_power_control': grpc.unary_unary_rpc_method_handler(
                    servicer.PC_payload_power_control,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqPayloadPowerControlParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PC_response_health_check': grpc.unary_unary_rpc_method_handler(
                    servicer.PC_response_health_check,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespHealthCheckParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
            'PC_response_shutdown': grpc.unary_unary_rpc_method_handler(
                    servicer.PC_response_shutdown,
                    request_deserializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespShutdownParams.FromString,
                    response_serializer=satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'antaris_api_peer_to_peer.AntarisapiPayloadController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AntarisapiPayloadController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PC_register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_register',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqRegisterParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PC_get_current_location(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_get_current_location',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqGetCurrentLocationParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PC_stage_file_download(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_stage_file_download',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqStageFileDownloadParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PC_sequence_done(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_sequence_done',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.CmdSequenceDoneParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PC_payload_power_control(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_payload_power_control',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.ReqPayloadPowerControlParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PC_response_health_check(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_response_health_check',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespHealthCheckParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PC_response_shutdown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/antaris_api_peer_to_peer.AntarisapiPayloadController/PC_response_shutdown',
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.RespShutdownParams.SerializeToString,
            satos__payload__sdk_dot_gen_dot_antaris__api__pb2.AntarisReturnType.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
