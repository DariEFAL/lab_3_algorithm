class Stack:
    def __init__(self):
        self.stack: list[tuple[int | float | str, int | float | str]] = []

    def push(self, x: int | float | str) -> None:
        """Добавляет элемент в конец стека"""
        if self.is_empty():
            mn_now = x
        else:
            mn_now = min(self.stack[-1][1], x)

        self.stack.append((x, mn_now))

    def pop(self) -> int | float | str:
        """Удаляет и возвращает последний элемент стека"""
        if self.is_empty():
            raise IndexError("Пустой стек")

        return self.stack.pop()[0]

    def peek(self) -> int | float | str:
        """Возвращает последний элемент стека без удаления"""
        if self.is_empty():
            raise IndexError("Пустой стек")

        return self.stack[-1][0]

    def is_empty(self) -> bool:
        """Проверяет на пустоту"""
        return len(self.stack) == 0

    def __len__(self) -> int:
        """Возвращает количество элементов в стеке"""
        return len(self.stack)

    def min(self) -> int | float | str:
        """Возвращает минимальный элемент в стеке"""
        if self.is_empty():
            raise ValueError("Пустой стек")

        return self.stack[-1][1]
