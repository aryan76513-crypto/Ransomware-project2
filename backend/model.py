def detect(file_name):
    # Simple logic (demo purpose)
    if ".exe" in file_name or "encrypt" in file_name:
        return "⚠️ Ransomware Detected"
    else:
        return "✅ Safe File"