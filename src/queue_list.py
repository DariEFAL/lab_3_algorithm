class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x: int) -> None:
        """Добавляет элемент в конец очереди"""
        self.queue.append(x)

    def dequeue(self) -> int:
        """Удаляет и возвращает первый элемент очереди"""
        if self.is_empty():
            raise IndexError("Пустая очередь")

        return self.queue.pop(0)

    def front(self) -> int:
        """Возвращает первый элемент очереди без удаления"""
        if self.is_empty():
            raise IndexError("Пустая очередь")

        return self.queue[0]

    def is_empty(self) -> bool:
        """Проверяет на пустоту"""
        return len(self.queue) == 0

    def __len__(self) -> int:
        """Возвращает количество элементов в очереди"""
        return len(self.queue)
