import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        print(type(json.dumps(strs)))
        return json.dumps(strs)


    def decode(self, s: str) -> List[str]:
        print(type(json.loads(s)))
        return json.loads(s)
