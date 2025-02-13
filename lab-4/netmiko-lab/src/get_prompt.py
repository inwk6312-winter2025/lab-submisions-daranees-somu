from netmiko import Netmiko

# List of devices to connect to
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.107",  # R1 Mgmt Interface
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.108",  # R2 Mgmt Interface
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.109",  # R3 Mgmt Interface
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    # Add other devices here similarly
]

# Loop through all devices in the list
for device in devices:
    try:
        # Establish connection to device
        net_connect = Netmiko(**device)

        # Print default prompt
        print(f"Connecting to {device['ip']}...")
        print(f"Default prompt for {device['ip']}: {net_connect.find_prompt()}")

        # Send disable command and print prompt
        net_connect.send_command_timing("disable")
        print(f"Disable command for {device['ip']}: {net_connect.find_prompt()}")

        # Send enable command and print prompt
        net_connect.enable()
        print(f"Enable command for {device['ip']}: {net_connect.find_prompt()}")

        # Close the connection
        net_connect.disconnect()
        print("-" * 40)  # Divider for clarity between devices

    except Exception as e:
        print(f"Failed to connect to {device['ip']} due to: {e}")
