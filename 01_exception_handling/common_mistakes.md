# Common Mistakes

These are mistakes I made while learning exception handling.

---

## Mistake #1

Using

```python
except:
```

instead of

```python
except Exception:
```

Reason:

Bare except catches KeyboardInterrupt and SystemExit.

---

## Mistake #2

Thinking raise creates an exception object.

Reality:

raise re-raises the current exception when used inside an except block.

---

## Mistake #3

Thinking raise e and raise are identical.

Reality:

raise preserves the current traceback.

raise e explicitly raises the exception object.

---

## Mistake #4

Thinking else runs after finally.

Reality:

Execution order

try

↓

except (if needed)

↓

else (only if no exception)

↓

finally

---

## Mistake #5

Thinking code after raise still executes.

Reality:

Execution immediately leaves the current block after raise.

---

## Mistake #6

Returning inside finally.

Reality:

It overrides previous returns and may suppress exceptions.

Avoid this pattern.

---

## Mistake #7

Ignoring exceptions.

```python
except Exception:
    pass
```

This hides bugs and makes debugging difficult.

---

## Lessons Learned

- Catch specific exceptions whenever possible.
- Use meaningful exception messages.
- Never ignore unexpected exceptions.
- Log errors in production.
- Use custom exceptions for business rules.