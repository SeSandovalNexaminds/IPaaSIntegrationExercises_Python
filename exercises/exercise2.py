
"""
Exercise 2 – Retry Logic + Idempotency (Medium)
(incomplete on purpose)
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
