import requests
from prompt_template import PROMPT
import json

API_KEY = "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"

URL = "https://api.groq.com/openai/v1/chat/completions"

# Mock test cases generator (for testing without API key)
def generate_mock_testcases(context):
    """Generate sample test cases for demo purposes"""
    return json.dumps({
        "Functional": [
            "TC001: Verify user can upload a valid PDF file",
            "TC002: Verify system extracts text from PDF correctly",
            "TC003: Verify test cases are generated from extracted text",
            "TC004: Verify output files are created in JSON format",
            "TC005: Verify output files are created in PDF format"
        ],
        "Negative": [
            "TC101: Verify system rejects invalid file formats",
            "TC102: Verify system handles corrupted PDF files gracefully",
            "TC103: Verify system rejects empty PDF files",
            "TC104: Verify system handles large file uploads",
            "TC105: Verify error messages are user-friendly"
        ],
        "Boundary": [
            "TC201: Verify system handles minimum text content (1 character)",
            "TC202: Verify system handles maximum text content (10000 characters)",
            "TC203: Verify system handles PDFs with special characters",
            "TC204: Verify system handles PDFs with different encodings"
        ],
        "Security": [
            "TC301: Verify API requires authentication",
            "TC302: Verify uploaded files are not accessible to other users",
            "TC303: Verify sensitive data in PDFs is handled securely",
            "TC304: Verify CORS is properly configured"
        ],
        "Performance": [
            "TC401: Verify response time < 5 seconds for normal files",
            "TC402: Verify system handles concurrent requests",
            "TC403: Verify memory usage is optimized"
        ],
        "Integration": [
            "TC501: Verify PDF reader integration works correctly",
            "TC502: Verify vector database integration works correctly",
            "TC503: Verify LLM integration returns valid responses"
        ]
    }, indent=2)

def generate_testcases(context):
    """Generate test cases using Groq API or mock data"""
    
    # For demo/testing, uncomment line below to use mock data:
    return generate_mock_testcases(context)
    
    prompt = PROMPT.format(context=context)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        response_json = response.json()
        
        if "choices" not in response_json:
            error_msg = response_json.get("error", {}).get("message", "Unknown API error")
            raise ValueError(f"API Response Error: {error_msg}")
        
        return response_json["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        raise ValueError(f"API Request Failed: {str(e)} - SOLUTION: Use mock data for testing by uncommenting line in llm.py")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Invalid API Response Format: {str(e)}")