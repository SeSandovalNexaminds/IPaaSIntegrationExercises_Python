"""
You are given a Workday-style employee object (a Python dict) and must
transform it into a Salesforce-style object.

This exercise tests:
- Data validation
- Data transformation
- Date parsing
- Error handling
- Normalization (string cleaning)
- iPaaS-style mapping logic (Workday → Salesforce)

----------------------------------------------------------------
REQUIREMENTS
----------------------------------------------------------------

INPUT FORMAT (example):
{
    "id": 318,
    "email": "john@example.com",
    "department": "Sales",
    "start_date": "2025-01-01",
    "phone": None
}

1. REQUIRED FIELDS:
   - id
   - email
   - department
   - start_date

   If ANY are missing:
      return {
          "success": False,
          "error": "Missing required fields",
          "input": <original_object>
      }

2. DATE CONVERSION:
   Input:  "YYYY-MM-DD"
   Output: "M/D/YYYY"

   If invalid date:
      return {
          "success": False,
          "error": "Invalid date",
          "input": <original_object>
      }

3. PHONE HANDLING:
   - If phone is None → "N/A"
   - Else keep original value

4. DEPARTMENT:
   - Trim leading/trailing whitespace

5. SUCCESS OUTPUT FORMAT:
   {
       "success": True,
       "data": {
           "employeeId": <id>,
           "contact": {
               "emailAddress": <email>,
               "phoneNumber": <phone or 'N/A'>
           },
           "metadata": {
               "group": <trimmed department>,
               "startDate": <converted date>
           }
       }
   }

IMPLEMENT transform_workday_to_salesforce() TO MAKE THE TESTS PASS.
DO NOT MODIFY TEST FILES.
===============================================================
"""

def transform_workday_to_salesforce(data: dict):
    raise NotImplementedError("Exercise 1 not implemented yet.")
