# =====================================================================
# 📋 PROJECT: Network Security Log Analyzer & Report Generator
# 💻 DEVELOPER: Mazen Ahmed (ZEMA222)
# =====================================================================

# 1. Global Variables Configuration (Preserving data scope outside the loop)
attacks_counter = 0
invalid_logs = 0
safe_logs = []

print("=== 🛡️ Welcome to ZEMA Network Security Log Analyzer 🛡️ ===")
print("Paste your raw firewall logs below.")
print("Type 'exit' or press Enter without typing anything to generate the report.\n")

# 2. Continuous Engine (The Infinite Loop Engine)
while True:
    # Capture input and clean unexpected leading/trailing whitespaces immediately
    user_input = input("Log entry: ").strip()
    
    # Exit Conditions
    if user_input.lower() == "exit" or not user_input:
        print("\n[+] Stop signal received. Analyzing gathered data...")
        break
        
    # Split the raw string into an actionable list based on whitespaces
    Logs = user_input.split()

    # Structural Validation: Ensure all 3 required segments exist
    if len(Logs) < 3:
        print("❌ Invalid log format! Please enter: [IP] [STATUS] [PORT]")
        invalid_logs += 1
        continue
        
    # Data Extraction & Case Normalization
    ip = Logs[0]
    status = Logs[1].upper()

    # Defensive Coding Wall (Try-Except) to safely convert Port in-place
    try:
        port = int(Logs[2])
    except ValueError:
        print(f"❌ Port tracking error: '{Logs[2]}' must be a valid integer port number!")
        invalid_logs += 1
        continue
    
    # Security Filtering & Threat Analysis
    if status == "MALICIOUS" or status == "ATTACK":
        print(f"⚠️ SECURITY ALERT: Threat blocked from IP {ip} trying to access Port {port}!")
        attacks_counter += 1
    else:
        print("✔ Log analyzed successfully. Connection is clean.")
        
        # In-place anonymous list creation combined with .join() for memory efficiency
        clean_line = " | ".join([ip, f"PORT:{port}", "STATUS:CLEAN"])
        
        # Commit the formatted entry to the clean traffic log database
        safe_logs.append(clean_line)

# =====================================================================
# 3. Final Security Report Summary - Outside the while loop scope
# =====================================================================
print("\n" + "="*50)
print("             🛡️ FINAL SECURITY SUMMARY REPORT 🛡️             ")
print("="*50)
print(f"[-] Total Malicious Threats Blocked: {attacks_counter}")
print(f"[-] Total Malformed Logs Skipped:    {invalid_logs}")
print(f"[-] Total Clean Connections Logged:  {len(safe_logs)}")
print("-"*50)

print("📋 Clean Traffic Database (Filtered Logs):")
if safe_logs:
    # Iterate and print out the secure database traffic line by line
    for log in safe_logs:
        print(f"  • {log}")
else:
    print("  [!] No clean logs recorded during this session.")
    
print("="*50)
print("=== End of Security Analysis Session ===")