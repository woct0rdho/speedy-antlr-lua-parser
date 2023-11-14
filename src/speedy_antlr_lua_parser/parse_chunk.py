import antlr4

from . import sa_lua


class ErrorListener(sa_lua.SA_ErrorListener):
    def syntaxError(
        self,
        input_stream,
        offendingSymbol,
        char_index: int,
        line: int,
        column: int,
        msg: str,
    ):
        print("Syntax Error!")
        print("    input_stream:", repr(input_stream))
        print("    offendingSymbol:", offendingSymbol, type(offendingSymbol))
        print("    char_index:", char_index)
        print("    line:", line)
        print("    column:", column)
        print("    msg:", msg)


def parse_chunk(s: str):
    return sa_lua.parse(antlr4.InputStream(s), "chunk", ErrorListener())
