def analyze_activity(log_file):
    suspicious_keywords = ["encrypted", "locked", ".enc", ".crypt"]

    with open(log_file, "r") as file:
        logs = file.readlines()

    alerts = []

    for line in logs:
        for keyword in suspicious_keywords:
            if keyword in line.lower():
                alerts.append(line)

    if alerts:
        print("⚠️ Potential Ransomware Activity Detected:")
        for alert in alerts:
            print(alert)
    else:
        print("✅ No suspicious activity detected")


if __name__ == "__main__":
    analyze_activity("logs/activity_log.txt")
