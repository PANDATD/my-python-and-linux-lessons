#!/bin/usr/python3.10


def demo() -> None:
    global x
    x = 10
    print(f"Value Of X Inside The Funcation: {x}")
    y = 20
    print(f"Value Of Y Inside The Funcation: {y}")
    return None


demo()

print(
    f"Value Of X Outside The Funcation: {x}"
)  # This will Work Beacuse of we declare global x .
# print(f"Value Of Y OutSide The Funcation: {y}") This will Not Work
