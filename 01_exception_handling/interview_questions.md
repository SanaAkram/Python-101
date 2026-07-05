# Python Exception Handling Interview Questions

This document contains interview questions ranging from beginner to senior Python engineer level.

---

# Beginner Level

## 1. What is an exception?

An exception is an event that interrupts the normal execution of a program.

Python raises exceptions whenever an unexpected situation occurs during runtime.

Example:

```python
10 / 0
```

Raises

```
ZeroDivisionError
```

---

## 2. Why do we need exception handling?

Without exception handling, a program crashes whenever an unexpected error occurs.

Exception handling allows us to

- continue execution
- display meaningful messages
- log errors
- clean up resources

---

## 3. Difference between SyntaxError and Exception?

### SyntaxError

Occurs before the program starts.

Python cannot execute the program.

Example

```python
if True
    print("Hello")
```

---

### Exception

Occurs while the program is running.

Example

```python
10 / 0
```

---

## 4. What is the purpose of try?

The try block contains code that may raise an exception.

---

## 5. What is except?

The except block handles exceptions raised inside the try block.

---

## 6. What is else?

The else block executes only when the try block completes successfully without raising an exception.

---

## 7. What is finally?

The finally block always executes whether an exception occurs or not.

Typical use cases

- Closing files
- Closing database connections
- Releasing locks
- Closing sockets

---

## 8. Difference between else and finally?

### else

Runs only if NO exception occurs.

### finally

Always runs.

---

## 9. What happens if an exception is not handled?

The program terminates and Python prints a traceback.

---

## 10. What does raise do?

The raise statement manually raises an exception.

Example

```python
raise ValueError("Invalid age")
```

---

# Intermediate Level

## 11. Difference between raise and raise e?

### raise

Re-raises the current exception while preserving its traceback.

Preferred.

### raise e

Raises the exception object explicitly.

May alter how the traceback is presented.

---

## 12. Why is except Exception preferred over bare except?

Bare except catches

- KeyboardInterrupt
- SystemExit

which usually should not be swallowed.

Using

```python
except Exception:
```

avoids catching those system-level exceptions.

---

## 13. What is BaseException?

BaseException is the root of Python's exception hierarchy.

All built-in exceptions inherit from it.

---

## 14. Why doesn't next() return None when iteration ends?

Because None could be a valid value.

Instead Python raises

```
StopIteration
```

---

## 15. Can finally execute after return?

Yes.

Python executes the finally block before actually returning.

Example

```python
def test():
    try:
        return 10
    finally:
        print("Cleanup")
```

Output

```
Cleanup
10
```

---

## 16. Should we return inside finally?

No.

Returning inside finally suppresses previous returns and even exceptions.

Avoid it.

---

## 17. What are custom exceptions?

Custom exceptions are user-defined exception classes.

Example

```python
class InvalidAgeError(Exception):
    pass
```

---

## 18. Why create custom exceptions?

They make code easier to read and express business rules.

Example

```python
raise PaymentFailedError(...)
```

is more meaningful than

```python
raise Exception(...)
```

---

## 19. Can one except block catch multiple exceptions?

Yes.

```python
except (ValueError, TypeError):
    ...
```

---

## 20. What is exception propagation?

If an exception is not handled in the current function, Python propagates it up the call stack until a matching except block is found.

---

# Senior Level

## 21. Why should exceptions not be used for normal program flow?

Exceptions are expensive compared to normal conditional logic and make code harder to understand when overused.

---

## 22. Why is logging exceptions important?

Logging helps diagnose issues in production by preserving stack traces and contextual information.

---

## 23. What information does a traceback provide?

- Exception type
- Error message
- File name
- Line number
- Function call stack

---

## 24. When should you catch Exception?

Only when you can meaningfully handle unexpected application-level errors.

---

## 25. When should you avoid catching Exception?

When specific exception types are known and can be handled individually.

---

## 26. What is exception chaining?

Python allows one exception to be raised while preserving another as its cause using:

```python
raise NewException(...) from e
```

This keeps the original error available in the traceback.

---

## 27. What happens if an exception occurs inside finally?

The new exception replaces the previous one unless it is handled.

---

## 28. Is exception handling slow?

Handling exceptions has overhead. Exceptions should represent exceptional situations, not routine control flow.

---

## 29. How are exceptions used in FastAPI?

Examples include:

- Request validation
- Authentication failures
- Database errors
- External API failures
- File upload errors

---

## 30. How are exceptions used in AI systems?

Examples include:

- Model loading failures
- API timeouts
- Invalid prompts
- Vector database connection issues
- Embedding generation failures
- Rate limiting