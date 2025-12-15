import typer
from typing import Optional, List

from src.fibo_factorial import factorial, factorial_recursive, fibo, fibo_recursive
from src.sorted import heap_sort, quick_sort, radix_sort, bubble_sort, bucket_sort, counting_sort


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
                  """)

@app.command("factorial")
def cmd_factorial(n: int, recursive: bool = False) -> None:
    """Вызов функций факториала"""
    try:
        if recursive:
            typer.echo(factorial_recursive(n))
        else:
            typer.echo(factorial(n))
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")

@app.command("fibo")
def cmd_fibo(n: int, recursive: bool = False) -> None:
    """Вызов функций фибоначи"""
    try:
        if recursive:
            typer.echo(fibo_recursive(n))
        else:
            typer.echo(fibo(n))
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")

@app.command("sort_heap")
def cmd_heap_sort(n: Optional[List[str]] = typer.Argument(None)) -> None:
    """Вызов sort_heap"""
    if n is None:
        n = []
    n = list(map(int, n))
    try:
        typer.echo(heap_sort(n))
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")

@app.command("sort_quick")
def cmd_quick_sort(n: Optional[List[str]] = typer.Argument(None)) -> None:
    """Вызов sort_quick"""
    if n is None:
        n = []
    n = list(map(int, n))
    try:
        typer.echo(quick_sort(n))
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")

@app.command("sort_radix")
def cmd_radix_sort(n: Optional[List[str]] = typer.Argument(None), base: int = 10) -> None:
    """Вызов sort_radix"""
    if n is None:
        n = []
    n = list(map(int, n))
    try:
        typer.echo(radix_sort(n, base))
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")

@app.command("sort_bubble")
def cmd_bubble_sort(n: Optional[List[int]] = typer.Argument(None)) -> None:
    """Вызов sort_bubble"""
    if n is None:
        n = []
    n = list(map(int, n))
    try:
        typer.echo(bubble_sort(n))
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")

@app.command("sort_bucket")
def cmd_bucket_sort(n: Optional[List[float]] = typer.Argument(None), buckets: int | None = None) -> None:
    """Вызов sort_bucket"""
    if n is None:
        n = []
    n = list(map(float, n))
    try:
        typer.echo(bucket_sort(n, buckets))
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")

@app.command("sort_counting")
def cmd_сounting_sort(n: Optional[List[int]] = typer.Argument(None)) -> None:
    """Вызов sort_counting"""
    if n is None:
        n = []
    n = list(map(int, n))
    try:
        typer.echo(counting_sort(n))
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")
