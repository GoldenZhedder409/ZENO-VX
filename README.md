<p align="center">
<img src="https://img.shields.io/badge/Version-Extreme_Edition-red?style=for-the-badge" alt="Version">
<img src="https://img.shields.io/badge/Language-Python_3-blue?style=for-the-badge" alt="Python">
<img src="https://img.shields.io/badge/Purpose-Security_Research-green?style=for-the-badge" alt="Purpose">
<img src="https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge" alt="License">
</p>

---

### What is this? 
🛡️ ZENO VX - Multi-Vector Network Stress Tester
ZENO VX is an advanced network performance and stress-testing framework written in Python. It is designed for security researchers and system administrators to evaluate the resilience of network infrastructures against various high-concurrency traffic patterns.

---

### Disclaimer ⚠️
> [!WARNING]
> LEGAL DISCLAIMER: This tool is for Educational Purposes Only. Unauthorized use against third-party systems is illegal and may result in criminal charges. The author and distributor assume no liability for misuse of this software.
> 
🚀 Key Features
 * Multi-Vector Attack Simulation: Supports TCP, UDP, HTTP, and SYN flooding techniques.
 * Slowloris Module: Specifically designed to exhaust server connection pools by keeping HTTP headers open.
 * High Concurrency: Utilizes ThreadPoolExecutor for managing 1000+ simultaneous threads.
 * IP Header Spoofing: Simulates traffic from randomized origins using X-Forwarded-For and custom headers.
 * Optimized Payloads: Dynamic generation of variable-sized packets (up to 65KB for UDP) to test bandwidth limits.
 * Real-time Analytics: Provides live feedback on total packets sent and transmission rates per second.

---

### Attack method 💢
📊 Attack Vectors Explained
| Vector | Method | Target Layer |
|---|---|---|
| TCP Flood | Sends large chunks of random data via established TCP connections. | Layer 4 |
| UDP Flood | Floods ports with massive datagram bursts to saturate bandwidth. | Layer 4 |
| HTTP Flood | Rapid GET requests with randomized User-Agents and Keep-Alive headers. | Layer 7 |
| SYN Flood | Rapidly opens and closes connections to exhaust the TCP stack. | Layer 4 |
| Slowloris | Holds many connections open simultaneously by sending partial headers. | Layer 7 |
🛠️ Installation & Usage

---

### requirement 📋
Prerequisites
 * Python 3.8 or higher.
 * Root/Administrator privileges (required for optimized socket performance).
 * Linux (Ubuntu/Debian recommended) or Windows.

---

### How to run? 🚀
Running the Tool
 * Clone or save the script as zeno_vx.py.
 * Execute with root privileges:
   sudo python3 zeno_vx.py
 * Command Line Arguments:
   python3 zeno_vx.py --target 192.168.1.1 --port 80 --threads 1500
