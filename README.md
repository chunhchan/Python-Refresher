# Python Refresher: Echo + Fibonacci Decorators

This repository contains two Python scripts:

- `echo.py` simulates a fading mountain echo.
- `fib.py` computes Fibonacci numbers recursively using decorators (`lru_cache` and a custom `timer`) and generates a timing plot `fib.png`.

---

## 1) Echo (`echo.py`)

### How to run
```bash
python echo.py
Example output

2) Fibonacci + Decorators (fib.py)
How to run
python fib.py
Example output

Fibonacci Timing Plot


Explanation
The x-axis represents n in the Fibonacci calculation, and the y-axis represents execution time in seconds.
With lru_cache, each Fibonacci value is computed once and reused, resulting in a gradual increase in runtime instead of exponential growth.

Final checklist
echo.py and fib.py run without errors

fib.png exists in the repository root

images/echo_output.png exists

images/fib_output.png exists


---



1. **Save the file** (`Ctrl + S`)
2. Open terminal and run:

```bash
git add README.md
git commit -m "Finalize README"
git push
Refresh your GitHub repo:

You should see images rendered

You should see the plot

No weird formatting