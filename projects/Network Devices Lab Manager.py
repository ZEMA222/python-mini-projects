lab_devices = [
    {
        "id" : 101,
        "type" : "Router" ,
        "status" : "online" ,
            "Network" : {
                "ip" : "192.168.1.1" ,
                "subnetmask" : "255.255.255.0"
            }
    },
    {
        "id" : 102,
        "type" : "PC" ,
        "status" : "online" ,
            "Network" : {
                "ip" : "192.168.1.5" ,
                "subnetmask" : "255.255.255.0"
            }
    },
    {
        "id" : 103,
        "type" : "Server" ,
        "status" : "online" ,
            "Network" : {
                "ip" : "192.168.1.7" ,
                "subnetmask" : "255.255.255.0"
            }
    }
]

choice = None 
while choice != 4:
    print("\n=== Lab Network Manager ===")
    print("1- View All Devices")
    print("2- Search Device by IP")
    print("3- Change Device Status")
    print("4- Exit")

    try:
        choice = int(input("Choose an action: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    match choice:
        case 1:
            print("\n--- Current Lab Devices ---")
            for device in lab_devices:
                print(f"Device ID: {device['id']} | Type: {device['type']} | IP: {device['Network']['ip']} | Status: {device['status']}")
                
        case 2:
            get_ip = input("Enter the ip for the Device you are looking for: ").strip()
            found = False
            
            for device in lab_devices:
                if device["Network"]["ip"] == get_ip:
                    print(f"\n✔ Found Device! ID: {device['id']} | Type: {device['type']} | Status: {device['status']}")
                    found = True
                    break 

            if not found:
                print("❌ This IP doesn't exist in the lab.")

        case 3:
            try:
                device_id = int(input("Please Enter the device ID: "))
            except ValueError:
                print("Please enter a valid number!")
                continue 
            
            
            id_found = False
            for device in lab_devices:
                if device["id"] == device_id:
                    new_status = input(f"Enter new status for device {device_id} (online/offline): ").strip()
                    device["status"] = new_status
                    print(f"✔ Device {device_id} status updated successfully to '{new_status}'!")
                    id_found = True
                    break
            
            if not id_found:
                print("❌ This Device ID doesn't exist.")
                
        case 4:
            print("Exiting Program... Goodbye!")
            
        case _:
            print("Invalid choice, try again.")