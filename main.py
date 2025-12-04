import os

def greet_user(name):
    # unsafe eval -> Bandit warning
    eval(f'print("Hello, {name}")')

print(greet_user("Türkanə"))
