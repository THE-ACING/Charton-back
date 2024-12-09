# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: playlist.proto
# Protobuf Python Version: 5.28.1
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
    1,
    '',
    'playlist.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eplaylist.proto\x12\x08playlist\"\x1d\n\x0fPlaylistRequest\x12\n\n\x02id\x18\x01 \x01(\t\"L\n\x15\x43reatePlaylistRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x16\n\tthumbnail\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0c\n\n_thumbnail\"g\n\x15UpdatePlaylistRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\x05title\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tthumbnail\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_titleB\x0c\n\n_thumbnail\"@\n\x10PlaylistResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tthumbnail\x18\x04 \x01(\t\"B\n\x19\x41\x64\x64TrackToPlaylistRequest\x12\x13\n\x0bplaylist_id\x18\x01 \x01(\t\x12\x10\n\x08track_id\x18\x02 \x01(\t\"1\n\x10PlaylistsRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\"B\n\x11PlaylistsResponse\x12-\n\tplaylists\x18\x01 \x03(\x0b\x32\x1a.playlist.PlaylistResponse2\xc1\x04\n\x08Playlist\x12\x46\n\x0bGetPlaylist\x12\x19.playlist.PlaylistRequest\x1a\x1a.playlist.PlaylistResponse\"\x00\x12O\n\x0e\x43reatePlaylist\x12\x1f.playlist.CreatePlaylistRequest\x1a\x1a.playlist.PlaylistResponse\"\x00\x12O\n\x0eUpdatePlaylist\x12\x1f.playlist.UpdatePlaylistRequest\x1a\x1a.playlist.PlaylistResponse\"\x00\x12I\n\x0eRemovePlaylist\x12\x19.playlist.PlaylistRequest\x1a\x1a.playlist.PlaylistResponse\"\x00\x12W\n\x12\x41\x64\x64TrackToPlaylist\x12#.playlist.AddTrackToPlaylistRequest\x1a\x1a.playlist.PlaylistResponse\"\x00\x12\\\n\x17RemoveTrackFromPlaylist\x12#.playlist.AddTrackToPlaylistRequest\x1a\x1a.playlist.PlaylistResponse\"\x00\x12I\n\x0cGetPlaylists\x12\x1a.playlist.PlaylistsRequest\x1a\x1b.playlist.PlaylistsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'playlist_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PLAYLISTREQUEST']._serialized_start=28
  _globals['_PLAYLISTREQUEST']._serialized_end=57
  _globals['_CREATEPLAYLISTREQUEST']._serialized_start=59
  _globals['_CREATEPLAYLISTREQUEST']._serialized_end=135
  _globals['_UPDATEPLAYLISTREQUEST']._serialized_start=137
  _globals['_UPDATEPLAYLISTREQUEST']._serialized_end=240
  _globals['_PLAYLISTRESPONSE']._serialized_start=242
  _globals['_PLAYLISTRESPONSE']._serialized_end=306
  _globals['_ADDTRACKTOPLAYLISTREQUEST']._serialized_start=308
  _globals['_ADDTRACKTOPLAYLISTREQUEST']._serialized_end=374
  _globals['_PLAYLISTSREQUEST']._serialized_start=376
  _globals['_PLAYLISTSREQUEST']._serialized_end=425
  _globals['_PLAYLISTSRESPONSE']._serialized_start=427
  _globals['_PLAYLISTSRESPONSE']._serialized_end=493
  _globals['_PLAYLIST']._serialized_start=496
  _globals['_PLAYLIST']._serialized_end=1073
# @@protoc_insertion_point(module_scope)
