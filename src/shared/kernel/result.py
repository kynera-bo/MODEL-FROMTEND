"""
Result[T] — Pattern para operaciones asincronas.
Nunca lanzar excepciones esperadas; devolver Result.fail().
"""
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


@dataclass(frozen=True)
class Result(Generic[T]):
    _value: Optional[T] = None
    _error: Optional[str] = None

    @staticmethod
    def ok(value: T) -> "Result[T]":
        return Result(_value=value)

    @staticmethod
    def fail(error: str) -> "Result[T]":
        return Result(_error=error)

    @property
    def is_ok(self) -> bool:
        return self._error is None

    @property
    def is_fail(self) -> bool:
        return self._error is not None

    @property
    def value(self) -> T:
        if self._error:
            raise ValueError(f"Cannot get value from failed result: {self._error}")
        return self._value

    @property
    def error(self) -> str:
        if self._error is None:
            raise ValueError("Cannot get error from successful result")
        return self._error

    def map(self, func):
        if self.is_fail:
            return self
        return Result.ok(func(self._value))

    def __repr__(self):
        if self.is_ok:
            return f"Result.ok({self._value!r})"
        return f"Result.fail({self._error!r})"
