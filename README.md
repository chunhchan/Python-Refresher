# Python Refresher: Echo + Fibonacci Decorators
This repository contains two Python scripts:

- `echo.py` simulates a fading mountain echo.
- `fib.py` computes Fibonacci numbers recursively using decorators (`lru_cache` and a custom `timer`) and generates a timing plot `fib.png`.

---

## 1) Echo (`echo.py`)

#### How to run
```bash
python echo.py

Example output
Yell something at a mountain: Hello
ooo
ooo
oo
o
.
```
## 2) Fib (`fib.py`)
#### How to run
```bash
python fib.py

Example output
Finished in 0.00000110s: f(1) -> 1
Finished in 0.00000090s: f(0) -> 0
Finished in 0.00058050s: f(2) -> 1 
Finished in 0.00075930s: f(3) -> 2 
Finished in 0.00082330s: f(4) -> 3
.
.
.
Finished in 0.01057200s: f(99) -> 218922995834555169026
Finished in 0.01077730s: f(100) -> 354224848179261915075
```
![alt text](image-1.png)
#### Explanation
```
The x-axis represents n in the Fibonacci calculation, and the y-axis represents execution time in seconds.
With lru_cache, each Fibonacci value is computed once and reused, resulting in a gradual increase in runtime instead of exponential growth.
```