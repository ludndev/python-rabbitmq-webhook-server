import json
from dataclasses import dataclass, field, asdict
from typing import Dict, Any

@dataclass
class PayloadDto:
    event: str
    url: str
    body: Any
    headers: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict:
        return asdict(self)

    def to_json(self, sort_keys: bool = False, indent: None | int | str = None) -> str:
        return json.dumps(self.to_dict(), sort_keys=sort_keys, indent=indent)
