# python-network-scanner
Python based network scanner that finds active devices, uses multithreaded TCP port scanning, and generates detailed scan reports.


Created to help me learn Python programming and networking fundamentals.


**Features**

  Network Discovery: Uses ICMP ping to identify responding devices.

  Port Scanning: Detects open TCP ports using Python sockets.

  Multithreading: Uses concurrent threads to speed up port scanning.

  Scan Options: Choose between quick, standard, or custom port scans.

  Input Validation: Checks IP addresses, subnet masks, and port ranges.

  Scan Reports: Automatically saves scan results to timestamped .txt files.


**Requirements**

  Python 3

  Windows (uses Windows ping commands)

  No additional Python packages required


**How to Use**

  Download or clone this repository.

  Open a terminal in the project folder.

  Run the scanner:

  py network_scanner.py

  Enter the network you want to scan (example: 192.168.1.0/24).

  Select a scan type.

  View the results in the terminal and the automatically generated report.


**Example Output**

  Starting Network Scan...

  127.0.0.1 | ONLINE
  Port OPEN: 8000

  Network scan completed.
  Amount of reachable addresses: 1
  Total Open Ports Found: 1
  Total Scan Time: 2.02s



--------------------------------------------------------------------
This project is intended for educational purposes only. Only scan networks and devices that are yours and have permission to test.
