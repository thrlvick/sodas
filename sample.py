#resource allllocation
import sys
import socket
from concurrent.futures import ThreadPoolExecutor

#system contoller
class NetworkEngine:
    def __init__(self, target_ip: str, total_threads: int = 50):
        # State Allocation 
        self.target = target_ip
        self.threads = total_threads
        self.open_ports = []

#parameter
    def probe_port(self, port: int) -> None: #class define
        """
        Executes a raw TCP socket connection parameter over a defined argument.
        """
        # AF_INET = IPv4 protocol path | SOCK_STREAM = Connection-oriented TCP layer
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Set a tight timeout window so threads don't hang in infinite loops
            sock.settimeout(1.0)
            
            # Connect_ex returns a clean integer status code instead of throwing a messy crash
            status_code = sock.connect_ex((self.target, port))
            
            # Status Code 0 means the TCP handshake completed cleanly (Port is Open)
            if status_code == 0:
                print(f"[+] Operational Node Identified: Port {port} OPEN")
                self.open_ports.append(port)
#concurrent engine
    def orchestrate_deployment(self, target_ports: list) -> list:
        """
        Spins up high-speed concurrent execution threads over the target matrix.
        """
        print(f"[*] Deploying {self.threads} hardware threads against {self.target}...")
        
        # Opens an elite asynchronous execution pool
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            # map passes the 'probe_port' parameters across the 'target_ports' arguments
            executor.map(self.probe_port, target_ports)
            
        return sorted(self.open_ports)
#starter
if __name__ == "__main__":
    # Production check: Enforce parameter arguments from the terminal entry point
    if len(sys.argv) < 2:
        print("[!] Execution aborted. Usage: python file.py <target_ip>")
        sys.exit(1)
        
    runtime_target = sys.argv[1]
    scan_matrix = [21, 22, 53, 80, 443, 8080]  # Standard critical service ports
    
    # Instantiate -> Execute Pipeline (engine parameters earlier )
    scanner = NetworkEngine(target_ip=runtime_target, total_threads=10)
    results = scanner.orchestrate_deployment(scan_matrix)
    
    print(f"\n[=] Final Architecture Telemetry: Discovered Ports -> {results}")