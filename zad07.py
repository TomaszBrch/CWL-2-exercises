measurements:list[tuple[int,str]] = [
(9, "temperatura w poniedzialek"),
(10, "temperatura we wtorek"),
(13, "temperatura w srode"),
(12, "temperatura w czwartek"),
(10, "temperatura w piatek"),
(7, "temperatura w sobote"),
(8,"temperatura w niedziele")]

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
def mean(m:list[tuple[int,str]])->float:
    
    _sum = 0

    for tup in m:
        _sum += tup[0]

    _mean: float = _sum / len(m)

    return(_mean)


print(f"Minimum is: {_min(m=measurements)}")
print(f"Maximum is: {_max(m=measurements)}")
print(f"Mean is: {mean(m=measurements)}")

descending_sort: list[tuple[int, str]] = sorted(measurements, key=lambda meas: meas[0], reverse=True)


_avg: float = mean(measurements)



above_average_sort: list[tuple[int, str]] = sorted([m for m in measurements if m[0] > _avg],
key=lambda x:x[0])

print(above_average_sort)