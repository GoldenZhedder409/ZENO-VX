ZENO VX - Advanced DDoS Tool 🔥


https://img.shields.io/badge/python-3.6%2B-blue
https://img.shields.io/badge/license-MIT-red
https://img.shields.io/badge/platform-Linux%20%7C%20Ubuntu-orange
https://img.shields.io/badge/status-stable-brightgreen
https://img.shields.io/github/languages/code-size/GolDer409/zeno-vx
https://img.shields.io/github/stars/GolDer409/zeno-vx?style=social


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
