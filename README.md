## Features

- **Protocol Identification**: Logs the type of protocol used (e.g., ICMP, TCP, UDP).
- **IP Address Logging**: Records both sender and target IP addresses.
- **File Output**: Appends packet details to `file.txt` for persistent storage.
- **Real-time Monitoring**: Displays packet details in real-time on the console.

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/rihadroshan/packetsniffer.git
   cd packetsniffer
   ```

3. Install the required Python package (Scapy):
   ```
   pip install scapy
   ```

4. Run the program:

   - **On Linux**:
     ```
     sudo python3 packetsniffer.py
     ```

   - **On Windows**:
     ```
     python3 packetsniffer.py
     ```

5. It will start capturing and logging packet details. Check the console output and `file.txt` for logged data.

## Example

Here’s an example of the output you might see:

```
Protocol: TCP
Sender IP address: 192.168.1.5
Target IP address: 192.168.1.10
--------------------------------------------------
```

## Notes

- On Linux, you might need to use `sudo` to run the script with sufficient permissions for packet sniffing.
- On Windows, administrative privileges may be required to capture packets.
- The script appends data to `file.txt`, so ensure you have write permissions for the directory where the script is executed.
