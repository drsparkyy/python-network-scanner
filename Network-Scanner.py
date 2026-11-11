# importing the required libraries
import socket
import ipaddress
import subprocess
import time
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from functools import partial





def get_local_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


def validIP(ip):
    try:
        ipaddress.ip_network(ip, strict =False)
        return True
    except ValueError:
        return False

def check_port(target_ip, port):
    
    try:
        sock = socket.create_connection((target_ip, port), timeout=1)
        sock.close()
        return port
    except (OSError):
        return None



print("Working directory:", os.getcwd())
def scan_ports(target_ip, ports):
    open_ports = []
    count = 0
    strTime = time.time()



    check_target = partial(check_port, target_ip)
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(check_target, ports)

        for result in results:
            if result is not None:
                open_ports.append(result)
                count += 1
                print("Port OPEN: " + str(result))

    
    
           
    endTime = time.time()
    scan_time = round(endTime - strTime, 2) 
    print("\tOpen ports found: " + str(count))
    print("\tScan duration: " + str(scan_time) + "s")

    return count, open_ports





def main():
    count = 0
    portsTot = 0
    devices = []
    hostname = socket.gethostname()
    IPaddress = get_local_ip()
    
    script_folder = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(script_folder, "scan_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt")
    print("Report will be saved to:", report_path)
    print("=" * 50)

    while True:
        network = input("Enter your network address with subnet mask (example: 192.168.1.0/24):")
        
        if not validIP(network):
            print("Invalid IP address. Please enter a valid IP address")
            continue


        net_obj = ipaddress.ip_network(network, strict=False)

        if net_obj.version != 4:
            print("Only IPv4 addresses are supported. Please enter a valid IPv4 network address")
            continue

    
        if net_obj.num_addresses > 256:
            print("The network is too large. Please enter a smaller network (example: 192.168.1.0/24)")
            continue

        

        if "/" not in network:
            print("Please include the subnet mask in CIDR notation")
            continue
        
        break
            

        

    print("\n=" * 10 + " Scan Options " + "=" * 10)
    print("1. Quick Scan (10 common ports)" + "\n2. Standard Scan (Ports 1-100)" + "\n3. Custom Scan" )
    choice = input("Enter your choice (1, 2, or 3): ")
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Please enter 1, 2, or 3: ")
    if choice == "1":
        ports = [21, 22, 23, 53, 80, 135, 139, 443, 445, 3389]
    elif choice == "2":
        ports = list(range(1, 101))
    else:
        strNum = input("Enter the starting number: ")
        endNum = input("Enter the ending number: ")
        if strNum.isdigit() and endNum.isdigit() and int(strNum) <= int(endNum) and int(strNum) >= 1 and int(endNum) <= 65535:
            ports = list(range(int(strNum), int(endNum) + 1))
        else:
            while not (strNum.isdigit() and endNum.isdigit() and int(strNum) <= int(endNum) and int(strNum) >= 1 and int(endNum) <= 65535):
                print("Invalid input. Please enter valid port numbers.")
                strNum = input("Enter the starting number: ")
                endNum = input("Enter the ending number: ")
            ports = list(range(int(strNum), int(endNum) + 1))








    print("=" * 50)
    cent = ("Starting Network Scan...").center(50)
    print(cent)
    print("=" * 50)
    totstrTime = time.time()
    for ip in net_obj.hosts():
        start_time = time.time()
        ret2 = subprocess.run(["ping", "-n", "1", str(ip)], capture_output=True, text=True)
        end_time = time.time()
        ms = round((end_time - start_time) * 1000)
        if "bytes=" in ret2.stdout:
            if str(ip) == IPaddress:
                print(str(ip) + " | ONLINE | " + " (your computer)" + " | " + str(ms) + " ms")
            else:
                print(str(ip) + " | ONLINE | " + str(ms) + " ms")
            portsFound, openports = scan_ports(str(ip), ports)
            count += 1
            portsTot += portsFound
            device = {str(ip): openports}
            devices.append(device)
        
    totendTime = time.time()
    totaltime = round(totendTime - totstrTime, 2)




    print ("=" * 50)
    print("Network scan completed.")
    print("Your computer name is: " + hostname)
    print("Your IP address is: " + IPaddress)
    print("Network: " + str(net_obj.network_address))
    print("Amount of addresses: " + str(net_obj.num_addresses))
    print("Amount of reachable addresses: " + str(count))
    print("Total Open Ports Found: " + str(portsTot))
    print("Total Scan Time: " + str(totaltime) + "s")

    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    with open(report_path, "w") as file:
        file.write("========== SCAN SUMMARY ==========\n")
        file.write("=" * 40 + "\n")
        file.write("Scan completed on: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for device in devices:
            for ip, open_ports in device.items():
                file.write("IP Address: " + ip + "\n")
                if open_ports:
                    file.write("\tOpen Ports: " + str(open_ports) + "\n")
                else:
                    file.write("\tNo open ports found.\n")
        file.write("=" * 40 + "\n")
        file.write("Network: " + str(net_obj.network_address) + "\n")
        file.write("Amount of reachable addresses: " + str(count) + "\n")
        file.write("Total Open Ports Found: " + str(portsTot) + "\n")
        file.write("Total Scan Time: " + str(totaltime) + "s\n")

    print("\nReport saved to:", os.path.abspath(report_path))

if __name__ == "__main__":
    main()