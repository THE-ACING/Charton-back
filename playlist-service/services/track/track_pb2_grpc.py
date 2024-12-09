# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from services.track import track_pb2 as services_dot_track_dot_track__pb2

GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in services/track/track_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TrackStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTrack = channel.unary_unary(
                '/track.Track/CreateTrack',
                request_serializer=services_dot_track_dot_track__pb2.CreateTrackRequest.SerializeToString,
                response_deserializer=services_dot_track_dot_track__pb2.TrackResponse.FromString,
                _registered_method=True)
        self.GetTrack = channel.unary_unary(
                '/track.Track/GetTrack',
                request_serializer=services_dot_track_dot_track__pb2.TrackRequest.SerializeToString,
                response_deserializer=services_dot_track_dot_track__pb2.TrackResponse.FromString,
                _registered_method=True)
        self.GetTracks = channel.unary_unary(
                '/track.Track/GetTracks',
                request_serializer=services_dot_track_dot_track__pb2.TracksRequest.SerializeToString,
                response_deserializer=services_dot_track_dot_track__pb2.TracksResponse.FromString,
                _registered_method=True)
        self.SearchTracks = channel.unary_unary(
                '/track.Track/SearchTracks',
                request_serializer=services_dot_track_dot_track__pb2.SearchRequest.SerializeToString,
                response_deserializer=services_dot_track_dot_track__pb2.TracksResponse.FromString,
                _registered_method=True)
        self.CreateAuthor = channel.unary_unary(
                '/track.Track/CreateAuthor',
                request_serializer=services_dot_track_dot_track__pb2.CreateAuthorRequest.SerializeToString,
                response_deserializer=services_dot_track_dot_track__pb2.AuthorResponse.FromString,
                _registered_method=True)


class TrackServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTrack(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrack(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTracks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchTracks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAuthor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrackServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTrack': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTrack,
                    request_deserializer=services_dot_track_dot_track__pb2.CreateTrackRequest.FromString,
                    response_serializer=services_dot_track_dot_track__pb2.TrackResponse.SerializeToString,
            ),
            'GetTrack': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrack,
                    request_deserializer=services_dot_track_dot_track__pb2.TrackRequest.FromString,
                    response_serializer=services_dot_track_dot_track__pb2.TrackResponse.SerializeToString,
            ),
            'GetTracks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTracks,
                    request_deserializer=services_dot_track_dot_track__pb2.TracksRequest.FromString,
                    response_serializer=services_dot_track_dot_track__pb2.TracksResponse.SerializeToString,
            ),
            'SearchTracks': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchTracks,
                    request_deserializer=services_dot_track_dot_track__pb2.SearchRequest.FromString,
                    response_serializer=services_dot_track_dot_track__pb2.TracksResponse.SerializeToString,
            ),
            'CreateAuthor': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAuthor,
                    request_deserializer=services_dot_track_dot_track__pb2.CreateAuthorRequest.FromString,
                    response_serializer=services_dot_track_dot_track__pb2.AuthorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'track.Track', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('track.Track', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Track(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTrack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/track.Track/CreateTrack',
            services_dot_track_dot_track__pb2.CreateTrackRequest.SerializeToString,
            services_dot_track_dot_track__pb2.TrackResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTrack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/track.Track/GetTrack',
            services_dot_track_dot_track__pb2.TrackRequest.SerializeToString,
            services_dot_track_dot_track__pb2.TrackResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTracks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/track.Track/GetTracks',
            services_dot_track_dot_track__pb2.TracksRequest.SerializeToString,
            services_dot_track_dot_track__pb2.TracksResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SearchTracks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/track.Track/SearchTracks',
            services_dot_track_dot_track__pb2.SearchRequest.SerializeToString,
            services_dot_track_dot_track__pb2.TracksResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateAuthor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/track.Track/CreateAuthor',
            services_dot_track_dot_track__pb2.CreateAuthorRequest.SerializeToString,
            services_dot_track_dot_track__pb2.AuthorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
