**ARPDetective**

ARPDetective is a Python script designed to scan your local network and discover active IP addresses along with their associated MAC addresses. Ideal for network administrators, and security professionals, this tool helps in network management, troubleshooting, and security assessments.

### Features

- **Scan Local Network**: Identify active IP addresses and their corresponding MAC addresses on your network.
- **Simple Command-Line Interface**: Easy to use with straightforward command-line options.
- **Customizable Scanning Range**: Specify individual IP addresses or entire network ranges.
- **Fast and Efficient**: Uses ARP protocol for quick and accurate results.

### Technologies Used

- **Python 3**: The scripting language used for developing the tool.
- **Scapy**: A powerful Python library for network packet manipulation and analysis.

### Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/secusavvy/ARPDetective.git
   cd ARPDetective
   ```

2. **Run the Script**:

   ```bash
   python arpd.py -i <ipaddress>
   ```

   - Replace `<ipaddress>` with the IP address or network range you want to scan (e.g., 192.168.1.1/24).

### Example

```bash
python arpd.py -i 192.168.1.1/24
```

This command will scan the 192.168.1.1/24 network range and display active IP addresses and their MAC addresses.

### How It Works

1. The script sends ARP requests to the specified IP range or address.
2. It collects and processes ARP replies to determine which devices are active.
3. Displays the results with IP addresses and corresponding MAC addresses.

### Disclaimer

**The author of this script is not responsible for any misuse or damages caused by using this script. Use it at your own risk.**

*Happy hacking responsibly!*
