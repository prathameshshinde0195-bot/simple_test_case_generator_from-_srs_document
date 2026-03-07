PROMPT = """
You are a senior QA automation engineer.

From the SRS below generate exhaustive software testcases.

Categories required:

Functional
Negative
Boundary
Edge cases
Security
Performance
Integration
API
UI

Return structured JSON.

SRS:

{context}
"""