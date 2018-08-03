"""This is an example of how the fail type tests should work.

These tests are all expected failures with the appropriate mypy messages."""

foo = {} #type: dict
bar = int(foo) #E: No overload variant of "int" matches argument type "Dict[Any, Any]"
