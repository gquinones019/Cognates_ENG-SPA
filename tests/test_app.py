import subprocess
import json

BASE_URL = "http://127.0.0.1:5050"


def test_home():
    # This now returns HTML, so we just check if it loads
    cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", f"{BASE_URL}/"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    status_code = int(result.stdout)
    assert status_code == 200


def test_cognate_check_valid():
    cmd = ["curl", "-s", f"{BASE_URL}/cognate-check/?word=cable&lang=ENGLISH"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print("Invalid JSON:", result.stdout)
        raise e

    assert data.get("word") == "cable"
    assert data.get("lang") == "ENGLISH"
    assert "result_type" in data
    assert "message" in data


def test_cognate_check_missing_word():
    cmd = ["curl", "-s", "-w", "%{http_code}", f"{BASE_URL}/cognate-check/?lang=ENGLISH"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    response = result.stdout[:-3]
    status_code = int(result.stdout[-3:])

    data = json.loads(response)
    assert status_code == 400
    assert "error" in data


def test_cognate_check_invalid_lang():
    cmd = ["curl", "-s", "-w", "%{http_code}", f"{BASE_URL}/cognate-check/?word=house&lang=INVALID"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    response = result.stdout[:-3]
    status_code = int(result.stdout[-3:])

    data = json.loads(response)
    assert status_code == 400
    assert "error" in data


if __name__ == "__main__":
    test_home()
    test_cognate_check_valid()
    test_cognate_check_missing_word()
    test_cognate_check_invalid_lang()
