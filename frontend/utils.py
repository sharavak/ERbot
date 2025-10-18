import base64
import urllib.parse
import sys;
import base64;
import zlib;

def mermaid_to_encoded_string(mermaid_diagram_definition: str):
    diagram_bytes = mermaid_diagram_definition.encode("utf-8")
    base64_bytes = base64.b64encode(diagram_bytes)
    base64_string = base64_bytes.decode("utf-8")
    encoded_string = urllib.parse.quote(base64_string)
    return encoded_string

    try:
        bytes_data = mermaid_diagram_definition.encode('utf-8')
        compressed_data = zlib.compress(bytes_data, 9)
        encoded_string = base64.urlsafe_b64encode(compressed_data).decode('utf-8') 
        return encoded_string
    except:
        ''
        