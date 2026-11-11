# Python Network Scanner

A network scanner that finds active devices, uses multithreaded TCP port scanning, and creates detailed scan reports.

Created to help me learn python and some basic computer networking.

---

## Features

- **Network Discovery** — Uses ICMP ping to identify responding devices.
- **Port Scanning** — Detects open TCP ports using Python sockets.
- **Multithreading** — Uses concurrent threads to speed up port scanning.
- **Scan Options** — Choose between quick, standard, and custom port scans.
- **Input Validation** — Validates network addresses, subnet masks, and port ranges.
- **Scan Reports** — Automatically saves results to timestamped `.txt` files.

## Requirements

- Python 3
- Windows (uses Windows-specific ping commands)
- No additional Python packages required

## How to Use

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the scanner using:

   `py network_scanner.py`

4. Enter the network you want to scan, such as `192.168.1.0/24`.
5. Select your preferred scan type.
6. View your results in the terminal and the generated report file.

## Scan Options

| Scan Type | Description |
|---|---|
| Quick Scan | Scans 10 common TCP ports |
| Standard Scan | Scans TCP ports 1–100 |
| Custom Scan | Scans a user-defined port range |

## Example Output

```text
==================================================
             Starting Network Scan...
==================================================
127.0.0.1 | ONLINE | 15 ms
Port OPEN: 8000
        Open ports found: 1
        Scan duration: 2.0s
==================================================
Network scan completed.
Network: 127.0.0.1
Amount of reachable addresses: 1
Total Open Ports Found: 1
Total Scan Time: 2.02s
```

## Disclaimer

This tool is intended for educational purposes and authorized network testing only. Only scan devices and networks that are yours or you have permission to assess.
