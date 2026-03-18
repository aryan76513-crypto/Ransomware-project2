from ai_models.model import detect_ransomware

def test_detect_ransomware():
    assert detect_ransomware("encrypt files") == True
    assert detect_ransomware("normal text") == False

