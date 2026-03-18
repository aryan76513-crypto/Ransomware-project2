from model import detect_ransomware

sample = "User files are being encrypted..."
print("Ransomware Detected:", detect_ransomware(sample))
