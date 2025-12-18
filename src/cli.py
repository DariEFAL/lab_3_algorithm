import typer
from typing import Optional, List

from fibo_factorial import factorial, factorial_recursive, fibo, fibo_recursive
from sorted import heap_sort, quick_sort, radix_sort, bubble_sort, bucket_sort, counting_sort
from stack_list import Stack
from queue_list import Queue

app = typer.Typer(help="""
                  Есть такие команды: \n
                  python src/main.py fibo \n
                  python src/main.py factorial \n
                  python src/main.py sort_heap -- \n
                  python src/main.py sort_quick -- \n
                  python src/main.py sort_radix -- \n
                  python src/main.py sort_bubble -- \n
                  python src/main.py sort_bucket -- \n
                  python src/main.py sort_counting --
                  python src/main.py queue
                  python src/main.py stack
                  """)

@app.command("factorial")
def cmd_factorial(n: int, recursive: bool = False) -> None:
    """Вызов функций факториала"""
    if recursive:
        typer.echo(factorial_recursive(n))
    else:
        typer.echo(factorial(n))

@app.command("fibo")
def cmd_fibo(n: int, recursive: bool = False) -> None:
    """Вызов функций фибоначи"""
    if recursive:
        typer.echo(fibo_recursive(n))
    else:
        typer.echo(fibo(n))

@app.command("sort_heap")
def cmd_heap_sort(n: Optional[List[str]] = typer.Argument(None)) -> None:
    """Вызов sort_heap"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(heap_sort(n))

@app.command("sort_quick")
def cmd_quick_sort(n: Optional[List[str]] = typer.Argument(None)) -> None:
    """Вызов sort_quick"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(quick_sort(n))

@app.command("sort_radix")
def cmd_radix_sort(base: int = 10, n: Optional[List[str]] = typer.Argument(None)) -> None:
    """Вызов sort_radix"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(radix_sort(n, base))

@app.command("sort_bubble")
def cmd_bubble_sort(n: Optional[List[int]] = typer.Argument(None)) -> None:
    """Вызов sort_bubble"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(bubble_sort(n))

@app.command("sort_bucket")
def cmd_bucket_sort(buckets: int | None = None, n: Optional[List[float]] = typer.Argument(None)) -> None:
    """Вызов sort_bucket"""
    if n is None:
        n = []
    n = list(map(float, n))
    typer.echo(bucket_sort(n, buckets))


@app.command("sort_counting")
def cmd_сounting_sort(n: Optional[List[int]] = typer.Argument(None)) -> None:
    """Вызов sort_counting"""
    if n is None:
        n = []
    n = list(map(int, n))
    typer.echo(counting_sort(n))

@app.command("stack")
def cmd_сounting_sort(n: Optional[List[int]] = typer.Argument(None)) -> None:
    """Вызов режима стека"""
    stack = Stack()


@app.command("stack")
def cmd_stack() -> None:
    """Интерактивный режим работы со стеком"""
    st = Stack()

    typer.echo("=== Интерактивный режим стека ===")
    typer.echo("Доступные команды:")
    typer.echo("  push - добавить элемент")
    typer.echo("  pop - удалить и получить последний элемент")
    typer.echo("  peek - посмотреть последний элемент")
    typer.echo("  min - получить минимальный элемент")
    typer.echo("  size - размер стека")
    typer.echo("  empty - проверка на пустоту")
    typer.echo("  exit - выход")
    typer.echo("================================")

    while True:
        try:
            user_input = typer.prompt("stack>").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                typer.echo("Выход из режима стека")
                break

            elif command == "push":
                if len(parts) != 2:
                    typer.echo("Неправильный ввод")
                    continue
                value = parts[1]

                try:
                    if int(value) == float(value):
                        value = int(value)
                    else:
                        value = float(value)
                except Exception:
                    pass

                st.push(value)

            elif command == "pop":
                typer.echo(st.pop())

            elif command == "peek":
                value = st.peek()
                typer.echo(f"Последний элемент: {value}")

            elif command == "empty":
                value = st.is_empty()
                typer.echo(f"Проверка на пустоту: {value}")

            elif command == "min":
                value = st.min()
                typer.echo(f"Минимальный элемент: {value}")

            elif command == "size":
                typer.echo(f"Размер стека: {st.__len__()}")

            else:
                typer.echo(f"Неизвестная команда: {command}")

        except ValueError as e:
            typer.echo(f"ValueError: {e}")
        except IndexError as e:
            typer.echo(f"IndexError: {e}")
        except Exception as e:
            typer.echo(f"Неожиданная ошибка: {e}")


@app.command("queue")
def cmd_queue() -> None:
    """Интерактивный режим работы с очередью"""
    qu = Queue()

    typer.echo("=== Интерактивный режим очереди ===")
    typer.echo("Доступные команды:")
    typer.echo("  enqueue - Добавляет элемент в конец очереди")
    typer.echo("  dequeue - Удаляет и возвращает первый элемент очереди")
    typer.echo("  front - Возвращает первый элемент очереди без удаления")
    typer.echo("  size - размер стека")
    typer.echo("  empty - проверка на пустоту")
    typer.echo("  exit - выход")
    typer.echo("================================")

    while True:
        try:
            user_input = typer.prompt("queue>").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                typer.echo("Выход из режима очереди")
                break

            elif command == "enqueue":
                if len(parts) != 2:
                    raise ValueError("Неправильный ввод")

                value = parts[1]

                try:
                    if int(value) == float(value):
                        value = int(value)
                    else:
                        value = float(value)
                except Exception:
                    pass

                qu.enqueue(value)

            elif command == "dequeue":
                typer.echo(qu.dequeue())

            elif command == "front":
                typer.echo(qu.front())

            elif command == "size":
                typer.echo(f"Размер стека: {qu.__len__()}")

            elif command == "empty":
                typer.echo(f"Проверка на пустоту: {qu.is_empty()}")

            else:
                typer.echo(f"Неизвестная команда: {command}")

        except ValueError as e:
            typer.echo(f"ValueError: {e}")
        except IndexError as e:
            typer.echo(f"IndexError: {e}")
        except Exception as e:
            typer.echo(f"Неожиданная ошибка: {e}")
