# Exception Handling Cheat Sheet

## Basic Structure

```python
try:
    ...
except Exception:
    ...
else:
    ...
finally:
    ...
```

---

## try

Contains risky code.

---

## except

Runs only when an exception occurs.

---

## else

Runs only if NO exception occurs.

---

## finally

Always executes.

Perfect for cleanup.

---

## raise

```python
raise ValueError("Invalid value")
```

---

## Custom Exception

```python
class InvalidAgeError(Exception):
    pass
```

---

## Catch Multiple Exceptions

```python
except (TypeError, ValueError):
    ...
```

---

## Exception Hierarchy

```
BaseException
│
├── KeyboardInterrupt
├── SystemExit
└── Exception
```

---

## Don't Do This

```python
except:
    pass
```

---

## Do This

```python
except Exception as e:
    logger.exception(e)
```

---

## Common Exceptions

| Exception | Meaning |
|-----------|---------|
| ValueError | Correct type, wrong value |
| TypeError | Wrong data type |
| KeyError | Dictionary key missing |
| IndexError | Invalid index |
| AttributeError | Attribute doesn't exist |
| ZeroDivisionError | Division by zero |
| FileNotFoundError | File missing |
| ImportError | Import failed |

---

## Difference

### else

Runs when NO exception occurs.

### finally

Runs EVERY time.

---

## raise vs raise e

### raise

- Re-raises current exception
- Preserves traceback
- Preferred

### raise e

- Raises exception object
- May modify traceback

---

## Interview Questions

✔ What is an exception?

✔ Difference between SyntaxError and Exception?

✔ Why use finally?

✔ Why use else?

✔ Difference between raise and raise e?

✔ Why avoid bare except?

✔ What is a custom exception?

✔ Can finally execute after return?

Answer: **Yes.**

---

## Production Best Practices

- Catch specific exceptions.
- Never silently ignore exceptions.
- Log every unexpected exception.
- Use custom exceptions for business logic.
- Always clean up resources.

---

## One-line Summary

```
try      -> Risky code

except   -> Handle errors

else     -> Runs if no error

finally  -> Always runs

raise    -> Raise an exception manually
```