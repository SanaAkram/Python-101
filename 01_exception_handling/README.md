# Chapter 01 — Exception Handling

> "Good developers write code that works. Great developers write code that continues to work even when things go wrong."

---

# Learning Objectives

After completing this chapter, you should be able to:

- Understand what exceptions are and why they exist.
- Differentiate between syntax errors and runtime exceptions.
- Handle exceptions using `try`, `except`, `else`, and `finally`.
- Raise exceptions using `raise`.
- Create custom exceptions.
- Understand Python's exception hierarchy.
- Write production-ready exception handling code.
- Apply exception handling in AI, backend, and FastAPI applications.
- Answer common Python interview questions related to exceptions.

---

# Table of Contents

1. What is an Exception?
2. Why Exception Handling?
3. Syntax Errors vs Runtime Errors
4. Exception Hierarchy
5. try
6. except
7. else
8. finally
9. raise
10. Custom Exceptions
11. Best Practices
12. Common Mistakes
13. Production Examples
14. AI Engineering Use Cases
15. Interview Questions
16. Summary

---

# What is an Exception?

An exception is an event that interrupts the normal execution of a program.

Example:

```python
print(10 / 0)
```

Output

```
ZeroDivisionError: division by zero
```

Instead of crashing silently, Python raises an exception describing the problem.

---

# Why Exception Handling?

Imagine an AI chatbot.

User uploads:

```
resume.pdf
```

Works perfectly.

Now imagine another user uploads:

```
corrupted_resume.pdf
```

Without exception handling:

- The application crashes.
- User receives a 500 Internal Server Error.
- Logs become difficult to analyze.
- Other users may be affected.

With proper exception handling:

- The error is logged.
- The user receives a meaningful message.
- The application continues running.

This is why exception handling is essential in production software.

---

# Syntax Error vs Runtime Error

## Syntax Error

Occurs before the program starts executing.

Example:

```python
if True
    print("Hello")
```

Output

```
SyntaxError
```

Python cannot even start executing the program.

---

## Runtime Error (Exception)

Occurs while the program is running.

Example

```python
10 / 0
```

Output

```
ZeroDivisionError
```

The program starts successfully but encounters an unexpected situation.

---

# Exception Hierarchy

Python exceptions inherit from the built-in `BaseException`.

```
BaseException
│
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
│
└── Exception
     │
     ├── ArithmeticError
     │     ├── ZeroDivisionError
     │     ├── OverflowError
     │     └── FloatingPointError
     │
     ├── LookupError
     │     ├── IndexError
     │     └── KeyError
     │
     ├── TypeError
     ├── ValueError
     ├── AttributeError
     ├── FileNotFoundError
     ├── ImportError
     ├── RuntimeError
     └── ...
```

### Why is this important?

During our lessons we discussed why we generally write:

```python
except Exception:
```

instead of:

```python
except:
```

Reason:

`except:` catches everything, including:

- KeyboardInterrupt
- SystemExit

These exceptions are usually meant to stop the program and should not be swallowed accidentally.

---

# try

The `try` block contains code that may raise an exception.

Example

```python
try:
    number = 10 / 0
```

Python executes the code normally until an exception occurs.

---

# except

The `except` block executes only if an exception occurs inside the `try` block.

Example

```python
try:
    number = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output

```
Cannot divide by zero.
```

---

# Catching Multiple Exceptions

```python
try:
    value = int(input())

except ValueError:
    print("Invalid number.")

except KeyboardInterrupt:
    print("Cancelled by user.")
```

You can also catch multiple exceptions together.

```python
except (ValueError, TypeError):
    print("Invalid input.")
```

---

# else

The `else` block executes **only if no exception occurs**.

Example

```python
try:
    number = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Everything executed successfully.")
```

Output

```
Everything executed successfully.
```

Use `else` for code that should only run when the `try` block succeeds.

---

# finally

The `finally` block executes whether an exception occurs or not.

Example

```python
try:
    file = open("data.txt")

finally:
    file.close()
```

Even if an exception occurs, the file is closed.

Common use cases:

- Closing files
- Closing database connections
- Closing network sockets
- Releasing locks
- Cleaning temporary files

---

# raise

The `raise` statement is used to manually raise an exception.

Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Output

```
ValueError: Age cannot be negative.
```

---

# raise vs raise e

Suppose:

```python
try:
    ...
except Exception as e:
```

### `raise`

Re-raises the current exception while preserving its original traceback.

```python
raise
```

Preferred when you simply want the exception to continue propagating.

---

### `raise e`

Raises the exception object explicitly.

```python
raise e
```

This may alter how the traceback is presented and is generally less preferred unless you have a specific reason.

---

# Custom Exceptions

Python allows us to create our own exception types.

Example

```python
class InvalidAgeError(Exception):
    pass
```

Usage

```python
age = -5

if age < 0:
    raise InvalidAgeError("Age cannot be negative.")
```

Custom exceptions make code more readable and expressive.

---

# Best Practices

✅ Catch only the exceptions you expect.

```python
except FileNotFoundError:
```

is better than

```python
except Exception:
```

when you know the likely failure.

---

Never write

```python
except:
    pass
```

unless you have a very good reason.

Ignoring exceptions hides bugs.

---

Always log exceptions in production systems.

---

Prefer meaningful exception messages.

Bad

```python
raise ValueError("Error")
```

Good

```python
raise ValueError("Customer ID must be a positive integer.")
```

---

Use custom exceptions for business logic.

---

# Common Mistakes

## Mistake 1

Using

```python
except:
```

instead of

```python
except Exception:
```

---

## Mistake 2

Ignoring exceptions.

```python
except Exception:
    pass
```

---

## Mistake 3

Using exceptions for normal program flow.

Exceptions should represent exceptional situations.

---

## Mistake 4

Returning from inside `finally`.

Doing so can suppress exceptions and make debugging difficult.

---

# AI Engineering Use Cases

Exception handling is everywhere in AI systems.

Examples:

- Calling OpenAI APIs
- Loading machine learning models
- Reading datasets
- Processing uploaded documents
- Connecting to vector databases
- Calling external REST APIs
- Streaming LLM responses
- Handling timeout errors
- Retrying failed requests

Example:

```python
try:
    response = client.responses.create(...)

except TimeoutError:
    logger.error("OpenAI request timed out.")
```

---

# Interview Questions

- What is an exception?
- Difference between syntax errors and runtime errors?
- Difference between `except:` and `except Exception:`?
- Difference between `raise` and `raise e`?
- When should `finally` be used?
- When should `else` be used?
- What are custom exceptions?
- Why should exceptions be logged?
- What happens if an exception is not handled?
- Can `finally` execute after `return`?

---

# Key Takeaways

- Exceptions interrupt normal program execution.
- `try` contains risky code.
- `except` handles exceptions.
- `else` executes only if no exception occurs.
- `finally` always executes.
- `raise` manually raises exceptions.
- Prefer `except Exception:` over bare `except:`.
- Create custom exceptions for business logic.
- Exception handling is a critical skill for backend and AI engineers.

---

# Next Chapter

In the next chapter, we explore one of Python's most misunderstood topics:

**Iterables & Iterators**

Understanding this chapter is essential before learning generators, asynchronous programming, and Python internals.