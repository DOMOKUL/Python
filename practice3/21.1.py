def from_string_to_list(string: str, container):
    [container.append(int(x)) for x in string.split(" ")]
    return container
a = [1, 2, 3]
from_string_to_list("1 3 99 52", a)
print(*a)