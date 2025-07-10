import json
from models import MockConfig
from typing import Dict, Any
from jinja2 import Template

def match_dict(actual: Dict[str, Any], expected: Dict[str, Any]) -> bool:
    if not expected:
        return True
    return all(str(actual.get(k)) == str(v) for k, v in expected.items())

def match_request(incoming: Dict[str, Any], mock: MockConfig) -> bool:
    if incoming["method"].upper() != mock.method.upper():
        return False
    if incoming["path"] != mock.path:
        return False

    # Match query parameters
    if not match_dict(incoming["query"], mock.match.query or {}):
        return False

    # Match headers
    if not match_dict(incoming["headers"], mock.match.headers or {}):
        return False

    # Match body
    if mock.match.body:
        try:
            incoming_body = json.loads(incoming["body"])
        except Exception:
            return False
        if not match_dict(incoming_body, mock.match.body):
            return False

    return True

def render_template(template_str: str, context: Dict[str, Any]) -> str:
    try:
        template = Template(template_str)
        return template.render(**context)
    except Exception:
        return template_str
