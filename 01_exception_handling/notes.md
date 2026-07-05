# Exception Handling - Quick Notes

## What is an Exception?

An exception is an event that interrupts the normal execution of a program.

Example:

```python
10 / 0
```

Raises:

```
ZeroDivisionError
```

---

# Why Exception Handling?

- Prevent application crashes
- Handle unexpected situations gracefully
- Improve user experience
- Log errors
- Clean up resources

---

# Syntax

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

# try

Contains code that may raise an exception.

```python
try:
    number = 10 / 0
```

---

# except

Executes only if an exception occurs.

```python
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# else

Runs only if NO exception occurs.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    ...
else:
    print(result)
```

Use it for success logic.

---

# finally

Always executes.

Used for cleanup.

Examples:

- Close files
- Close database connections
- Release locks
- Close sockets

---

# raise

Raise an exception manually.

```python
raise ValueError("Invalid age")
```

---

# raise vs raise e

## raise

Re-raises the current exception.

Preferred.

Preserves traceback.

```python
raise
```

---

## raise e

Raises the exception object explicitly.

```python
raise e
```

Can modify how the traceback appears.

---

# Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass
```

Usage:

```python
raise InvalidAgeError("Age cannot be negative.")
```

---

# Exception Hierarchy

```
BaseException
│
├── KeyboardInterrupt
├── SystemExit
└── Exception
     ├── ValueError
     ├── TypeError
     ├── KeyError
     ├── IndexError
     ├── FileNotFoundError
     └── ...
```

---

# except vs except Exception

Avoid

```python
except:
```

Prefer

```python
except Exception:
```

Reason:

Bare except also catches

- KeyboardInterrupt
- SystemExit

---

# Best Practices

✅ Catch specific exceptions.

```python
except FileNotFoundError:
```

instead of

```python
except Exception:
```

when possible.

---

Never ignore exceptions.

Bad:

```python
except Exception:
    pass
```

---

Log exceptions.

---

Write meaningful error messages.

Bad:

```python
raise ValueError("Error")
```

Good:

```python
raise ValueError("Customer ID cannot be negative.")
```

---

# Common Exceptions

```
ValueError

TypeError

KeyError

IndexError

AttributeError

FileNotFoundError

ImportError

RuntimeError

ZeroDivisionError
```

---

# Interview Tips

Know the difference between:

- SyntaxError vs Exception
- raise vs raise e
- else vs finally
- Exception vs BaseException
- except vs except Exception

---

# AI Engineering Examples

- OpenAI API calls
- Reading PDFs
- Loading ML models
- Database connections
- File uploads
- HTTP requests
- Vector databases