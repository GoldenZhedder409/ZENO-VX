ZENO VX - Advanced DDoS Tool 🔥

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=500&color=6A5ACD&center=true&vCenter=true&random=false&width=435&lines=ZENO+VX;Advanced+DDoS+Tool;Multi-Vector+Attack;Security+Research" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/license-MIT-red?style=for-the-badge&logo=opensourceinitiative&logoColor=white" />
  <img src="https://img.shields.io/badge/platform-Linux%20%7C%20Ubuntu-orange?style=for-the-badge&logo=linux&logoColor=white" />
  <img src="https://img.shields.io/badge/status-stable-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/code-size/GolDer409/zeno-vx?style=for-the-badge&logo=github&label=Code%20Size" />
  <img src="https://img.shields.io/github/stars/GolDer409/zeno-vx?style=for-the-badge&logo=github&logoColor=white&color=yellow" />
  <img src="https://img.shields.io/github/forks/GolDer409/zeno-vx?style=for-the-badge&logo=github&logoColor=white&color=blue" />
  <img src="https://img.shields.io/github/issues/GolDer409/zeno-vx?style=for-the-badge&logo=github&logoColor=white&color=red" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/contributions-welcome-orange?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/maintained-yes-green?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge&logo=git&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/GolDer409/zeno-vx?style=for-the-badge&logo=github&label=Last%20Update" />
  <img src="https://img.shields.io/github/release/GolDer409/zeno-vx?style=for-the-badge&logo=github&label=Latest%20Release" />
  <img src="https://img.shields.io/github/downloads/GolDer409/zeno-vx/total?style=for-the-badge&logo=github&label=Downloads" />
</p>

---

## 🔥 Overview

**ZENO VX** is a cutting-edge multi-vector DDoS attack simulation tool that combines 5 different attack methodologies for comprehensive security testing. Built with performance optimization and low detection in mind.

```python
# Quick Start
sudo python3 zeno_vx.py --target example.com --port 80 --threads 2000

⚠️ LEGAL DISCLAIMER: This tool is for educational and security testing purposes only. Unauthorized use against systems you don't own is illegal. The author is not responsible for any misuse.

📋 Overview

ZENO VX is a multi-vector DDoS attack simulation tool that combines multiple attack methodologies for security testing and research purposes. Built with performance optimization and low detection in mind.

🚀 Features

Attack Vector Description Status
TCP Flood Raw TCP packet flooding ✅
UDP Flood High-volume UDP traffic ✅
HTTP Flood Layer 7 application attacks ✅
SYN Flood Half-open connection attacks ✅
Slowloris Connection holding attacks ✅

⚙️ Technical Specifications

```
Threads      : 1000+ concurrent
Timeout      : 3 seconds
Buffer Size  : 65,535 bytes
Delay        : 0.0001s (configurable)
Packet Rate  : 10,000+ packets/second
```

🛠️ Installation

```bash
# Clone repository
git clone https://github.com/yourusername/zeno-vx.git

# Navigate to directory
cd zeno-vx

# Make executable
chmod +x zeno_vx.py

# Run with root privileges
sudo python3 zeno_vx.py
```

📖 Usage Examples

```bash
# Basic usage
sudo python3 zeno_vx.py

# Advanced with parameters
sudo python3 zeno_vx.py --target 192.168.1.100 --port 443 --threads 2000

# Help menu
python3 zeno_vx.py --help
```

Parameters

Argument Description Default
--target Target IP or domain User input
--port Target port number 80
--threads Number of threads 1000

🏗️ Architecture

```
┌─────────────────────────────────────┐
│         ZENO VX Core Engine         │
├─────────────────────────────────────┤
│  ┌──────┐  ┌──────┐  ┌──────────┐  │
│  │ TCP  │  │ UDP  │  │   HTTP   │  │
│  └──────┘  └──────┘  └──────────┘  │
│  ┌──────┐  ┌───────────────┐       │
│  │ SYN  │  │   Slowloris   │       │
│  └──────┘  └───────────────┘       │
└─────────────────────────────────────┘
         ↓        ↓        ↓
    ThreadPoolExecutor (1000+ threads)
         ↓        ↓        ↓
    Socket Layer (Optimized)
```

⚡ Performance Metrics

```
Attack Type    | Packets/sec | Success Rate
---------------|-------------|-------------
TCP Flood      | 2,500+      | 95%
UDP Flood      | 10,000+     | 98%
HTTP Flood     | 1,000+      | 90%
SYN Flood      | 15,000+     | 85%
Slowloris      | N/A (conn)  | 100 conns/sec
```

🔧 Requirements

· OS: Linux/Ubuntu (optimized)
· Python: 3.6 or higher
· Privileges: Root/sudo required
· Network: Stable internet connection

📦 Dependencies

```python
# All built-in modules - no external dependencies!
- os
- socket
- threading
- random
- time
- sys
- signal
- concurrent.futures
- argparse
```

🚦 How It Works

1. Target Resolution - Resolves domain to IP
2. Multi-threading - 1000+ concurrent threads
3. Socket Optimization - TCP_NODELAY, SO_REUSEADDR
4. Payload Generation - Dynamic size randomization
5. IP Spoofing - X-Forwarded-For header manipulation
6. Statistics - Real-time packet counting

📊 Attack Vectors Explained

TCP Flood

Raw TCP packets with random payload (512-2048 bytes)

UDP Flood

High-volume UDP traffic with large payloads (1KB-65KB)

HTTP Flood

Layer 7 attacks with:

· Random user agents
· Spoofed IP headers
· Keep-alive connections
· Cache bypass

SYN Flood

Rapid connect/disconnect with non-blocking sockets

Slowloris

Hold connections open by sending partial headers

⚠️ Important Notes

· Requires root for optimal socket performance
· Ubuntu/Linux optimized (not for Windows)
· Educational purposes only
· Test only on authorized systems
· Rate limiting may apply based on network

📈 Future Updates

· IPv6 support
· Proxy rotation
· DNS amplification
· NTP reflection
· Web interface
· Distributed mode

📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author

Rifqi Asy-Syakur

· Group: HDN Cyber Forces
· Protocol: ZENO Protocol
· Role: Front Man

📞 Contact & Support

· GitHub: @yourusername
· Report Issues: Issues Page

---

🌟 Star History

https://api.star-history.com/svg?repos=yourusername/zeno-vx&type=Date

---

Made with 🔥 for security research
