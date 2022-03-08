import json
import json.scanner


class Decoder(json.JSONDecoder):

    def __init__(
        self,
        *,
        object_hook=None,
        parse_float=None,
        parse_int=None,
        parse_constant=None,
        strict=True,
        object_pairs_hook=None,
    ):
        super().__init__(
            object_hook=object_hook,
            parse_float=parse_float,
            parse_int=parse_int,
            parse_constant=parse_constant,
            strict=strict,
            object_pairs_hook=object_pairs_hook,
        )

        _parse_string = self.parse_string

        def parse_string(*args, **kwargs):
            s, end = _parse_string(*args, **kwargs)
            return s.encode('latin-1').decode(), end

        self.parse_string = parse_string

        self.scan_once = json.scanner.py_make_scanner(self)


def loads(s):
    return json.loads(s, cls=Decoder)
