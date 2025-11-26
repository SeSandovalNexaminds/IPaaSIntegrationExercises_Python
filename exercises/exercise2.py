"""
This exercise simulates calling an unreliable external API and requires:
- Retry logic
- Handling temporary failures
- Global idempotency (avoiding duplicates)
- Error handling
- Real-world integration concepts

----------------------------------------------------------------
REQUIREMENTS
----------------------------------------------------------------

The provided function call_external_api() behaves like this:

- First call  → raises Exception("Temporary API failure")
- Second call → raises Exception("Temporary API failure")
- Third call  → returns a valid object:
      {
          "id": 42,
          "value": "sample",
          "timestamp": <milliseconds>
      }
- Fourth+ calls ALSO return this same object (same ID = 42)

You must implement call_with_retry().

1. RETRY LOGIC (3 TOTAL ATTEMPTS):
   - Try to call call_external_api()
   - If it fails, retry
   - If all 3 attempts fail:
        return {
            "success": False,
            "error": "API failed after 3 attempts"
        }

2. IDEMPOTENCY (CRITICAL):
   - If an ID has already been returned in ANY PREVIOUS successful call:
        return {
            "success": True,
            "data": None,
            "message": "Duplicate ignored"
        }

3. SUCCESS CASE:
   If a new ID is returned:
        return {
            "success": True,
            "data": <returned_object>
        }

4. You MUST track seen IDs globally (e.g., a global set).

5. Tests rely on the ability to reset global state via reset_state().

IMPLEMENT call_with_retry().
DO NOT MODIFY TEST FILES.
===============================================================
"""

import time

_counter = 0
_seen_ids = set()

def call_external_api():
    global _counter
    _counter += 1

    if _counter < 3:
        raise Exception("Temporary API failure")

    return {"id": 42, "value": "sample", "timestamp": int(time.time() * 1000)}

def call_with_retry():
    raise NotImplementedError("Exercise 2 not implemented yet.")

def reset_state():
    global _counter, _seen_ids
    _counter = 0
    _seen_ids = set()
