# =====================================================================
# 📋 PROJECT: Automated Cloud Firewall Rule Engine
# 💻 DEVELOPER: Mazen Ahmed (ZEMA222)
# =====================================================================

ALLOWED_PORTS = [433, 80, 22]
BLOCKED_COUNTRIES = ["INDIA", "ISRAEL", "USA", "IRAN"]
approved_connections = []
blocked_attempts = 0
total_data_gb = 0.0

print("=== 🛡️ Welcome to ZEMA Automated Cloud Firewall ===")
print("Paste your connection attempts below.")
print("Type 'exit' or press Enter without typing anything to generate the report.\n")

while True:
    user_input = input("Country port size: ").strip()
    
    if user_input.lower() == "exit" or not user_input:
        print("\n[+] Stop signal received. Analyzing gathered data...")
        break
        
    attempt = user_input.split()

    if len(attempt) < 3:
        print("❌ Invalid format! Please enter: [Country] [Port] [Size_MB]")
        continue

    country = attempt[0].upper()
    
    try:
        port = int(attempt[1])
    except ValueError:
        print(f"❌ Port tracking error: '{attempt[1]}' must be a valid integer port number!")
        continue
        
    try:
        size = float(attempt[2])
    except ValueError:
        print(f"❌ File size error: '{attempt[2]}' must be a valid number!")
        continue
    
    if country in BLOCKED_COUNTRIES:
        blocked_attempts += 1
        print("⚠️ Access Denied: Blocked Country Destination!")
        continue
        
    if port not in ALLOWED_PORTS:
        blocked_attempts += 1
        print("⚠️ Access Denied: Unauthorized Port Access!")
        continue
    if total_data_gb + (size / 1024) < 5:
        total_data_gb += (size / 1024)
    else:
        print("⚠️ Access Denied: MAX CAPACITY EXCEEDED!")
        blocked_attempts += 1
        continue  
    
    result = " -> ".join(attempt)
    approved_connections.append(result)
    print("✔ Connection approved and routed to cloud.")

# =====================================================================
# 3. FINAL SECURITY REPORT SUMMARY (Outside the execution engine loop)
# =====================================================================
print("\n" + "="*50)
print("             🛡️ CLOUD FIREWALL SUMMARY REPORT 🛡️             ")
print("="*50)
print(f"[-] Total Malicious/Unauthorized Blocks: {blocked_attempts}")
print(f"[-] Total Accumulated Cloud Traffic:     {round(total_data_gb, 4)} GB")
print(f"[-] Total Approved Infrastructure Links: {len(approved_connections)}")
print("-"*50)

print("📋 Approved Connection Registry:")
if approved_connections:
    for connection in approved_connections:
        print(f"  • {connection}")
else:
    print("  [!] Cloud infrastructure received zero approved traffic routes.")
    
print("="*50)
print("=== End of Cloud Security Session ===")