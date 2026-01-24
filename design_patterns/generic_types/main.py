from typing import TypeVar, Any

T = TypeVar("T")


def sort(items: list[T]) -> list[T]:
    return sorted(items)


a = sort([5, 3, 1, 4, 2])
b = sort(["apple", "orange", "banana"])


def any_sort(items: list[Any]) -> list[Any]:
    return sorted(items)


a = any_sort([5, 3, 1, 4, 2])
b = any_sort(["apple", "orange", "banana"])

# Using TypeVar provides better type checking and clarity compared to using Any.
