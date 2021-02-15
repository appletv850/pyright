# This sample tests basic parsing of match statements as
# described in PEP 634.

from typing import Any

value_obj: Any = 4


match (1, ):
    case a1, b1 if True:
        pass

    case (a2, b2):
        pass

    case [a3, b3]:
        pass

    case () | []:
        pass

    # This should generate an error because of a missing pattern.
    case :
        pass

    case (a4):
        pass

    case (a5,):
        pass

    case [a6,]:
        pass

    case a7 as b7, c7 as d7 if True:
        pass

    case (a8, b8, ) as c8 if 1 == 3:
        pass

    case a9, *b8:
        pass

    # This should generate an error because multiple star
    # patterns in a sequence are not allowed.
    case *a10, *b10:
        pass

    # This should generate an error because star
    # patterns cannot be used with "as".
    case *a11 as b11, b12:
        pass

    case value_obj.a, value_obj.b:
        pass

    case a12 | b12 | c12, d12 | e12 as f12:
        pass

    # This should generate an error because star
    # patterns can't be used with |.
    case a13 | *b13 | c13:
        pass

    case *a14, b14:
        pass

    case (a20, (b20,), [c20, *d20]) as e20:
        pass

    case 3 | -3:
        pass

    case 3.2 - 2.1j | -3.2 + 2.1j | 3j:
        pass

    # This should generate an error because the grammar
    # indicates that imaginary number must come second.
    case 2j + 4:
        pass

    # This should generate an error because the grammar
    # indicates that imaginary number must come second.
    case - 2j + 4:
        pass

    case "hi" """hi""" | r"hi" r"""hi""":
        pass

    # This should generate an error because f-strings are
    # not allowed.
    case "hi" f"""hi""":
        pass

    # This should generate an error.
    case {}:
        pass

    case {"a": 3, -3 + 4j: a30, value_obj.a: b30, **c30}:
        pass

    # This should generate an error because only one ** expression
    # can be used.
    case {"a": 3, **a31, "b": -3j, **b31}:
        pass

    # This should generate an error because ** cannot be used with
    # wildcard "_".
    case {"a": 3, **_, "b": -3}:
        pass

    case (3 as x) as y:
        pass

    case int():
        pass

    case int(1, a40, value_obj.b as b40, c40=3|-2 + 5j|"hi" as d40, y=[e40, f40] as g40,):
        pass
  
    # This should generate an error because positional arguments
    # cannot appear after keyword arguments.
    case str(1, a41, x=3, value_obj.b as b41, c41=3, y=[d41, e41] as f41):
        pass
  
