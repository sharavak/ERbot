import base64
import urllib.parse
import base64;

def mermaid_to_encoded_string(mermaid_diagram_definition: str):
    diagram_bytes = mermaid_diagram_definition.encode("utf-8")
    base64_bytes = base64.b64encode(diagram_bytes)
    base64_string = base64_bytes.decode("utf-8")
    encoded_string = urllib.parse.quote(base64_string)
    return encoded_string