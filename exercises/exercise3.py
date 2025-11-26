"""
This exercise simulates processing webhook events from an external system,
such as Workday, Salesforce, Stripe, or NetSuite.

It tests:
- Event sorting
- Deduplication logic
- Validation
- Error reporting
- Normalization
- Real-life integration patterns

----------------------------------------------------------------
REQUIREMENTS
----------------------------------------------------------------

You are given a list of event objects:

{
    "event_id": <int>,
    "type": <string | missing>,
    "timestamp": <int>,
    "payload": <object | missing>
}

IMPLEMENT process_events() WITH THE FOLLOWING RULES:

1. SORTING:
   - Sort all events by ascending timestamp BEFORE processing.

2. DEDUPLICATION:
   - Only keep the *earliest* event for each unique event_id.
   - Later events with same event_id must be ignored.

3. VALIDATION:
   - If payload is missing:
        Add to invalidEvents:
            {
                "event_id": <id>,
                "reason": "Missing payload"
            }
        DO NOT include in validEvents.

   - If type is missing:
        Set type = "unknown"
        Still consider it valid.

4. OUTPUT FORMAT:
   Return an object:
   {
       "validEvents": [
           {
               "event_id": <id>,
               "type": <string>,
               "timestamp": <int>,
               "payload": <dict>
           },
           ...
       ],
       "invalidEvents": [
           { "event_id": <id>, "reason": "Missing payload" },
           ...
       ]
   }

5. DO NOT MODIFY THE TEST FILE.
   Your implementation MUST satisfy all test cases.

IMPLEMENT process_events() TO PASS THE TESTS.
===============================================================
"""

def process_events(events: list):
    raise NotImplementedError("Exercise 3 not implemented yet.")
