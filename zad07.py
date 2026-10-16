measurements:list[tuple[int,str]] = [
(10, "temperatura w poniedzialek"),
(12, "temperatura we wtorek"),
(17, "temperatura w srode"),
(14, "temperatura w czwartek"),
(13, "temperatura w piatek")]

def _min(m:list[tuple[int,str]]) -> int:
    _minimum: float = float("inf")

    for tup in m:
        if tup[0] < _minimum:  # noqa: PLR1730
            _minimum = tup[0]
    return(int(_minimum))
def _max(m:list[tuple[int,str]]) -> int:
    _maximum: float = float("-inf")

    for tup in m:
        if tup[0] > _maximum:  # noqa: PLR1730
            _maximum = tup[0]
    return(int(_maximum))

print(f"Minimum is: {_min(measurements)}")
print(f"Maximum is: {_max(measurements)}")

