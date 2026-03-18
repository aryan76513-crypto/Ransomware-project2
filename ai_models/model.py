def detect_ransomware(file_content):
    if "encrypt" in file_content.lower():
        return True
    return False
