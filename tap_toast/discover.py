import os
import singer
from tap_toast.streams import Stream
import re
from tap_toast.utils import get_abs_path


def discover_streams(client):
    streams = []

    for f in os.listdir(get_abs_path(f'metadatas/')):
        m = re.match(r'([a-zA-Z_]+)\.json', f)
        if m is not None:
            s = Stream(m.group(1), client)
            schema = singer.resolve_schema_references(s.load_schema())
            metadata = s.load_metadata()
            streams.append({'stream': s.name, 'stream_alias': s.postman_item, 'tap_stream_id': s.name, 'schema': schema, 'metadata': metadata})
    return streams
