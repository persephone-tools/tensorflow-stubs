"""This is an example of how the reveal type tests should work.

This is useful for ensuring that the types are what we expect"""

foo = 1.3
bar = "baz"

reveal_type(foo)  # E: float
reveal_type(bar) # E: str
