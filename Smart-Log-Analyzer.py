import re

LOG_DUMP = """
Feb 07 12:00:01 web-srv-01 sshd[112]: Failed password for root from 192.168.1.105 port 22 ssh2
Feb 07 12:05:33 db-srv-prod auth[443]: Accepted password for admin from 10.0.0.42 port 54332
Feb 07 12:10:12 firewall-ext filter: DROP connection from 185.220.101.5 to 172.16.0.5
Feb 07 12:15:00 web-srv-01 sshd[112]: Failed password for guest from 192.168.1.200 port 22 ssh2
"""

def analyze_logs(raw_text):
    """
    Parses multi-line logs using regex to extract usernames, IP addresses, and actions.
    """
    print("=== SOC LOG ANALYSIS REPORT ===")
    print(f"Analyzing {len(raw_text.splitlines()) - 1} events...\n")

    
    patterns = {
        "ssh_auth": r"(?P<action>Failed|Accepted) password for (?P<user>\w+) from (?P<ip>[\d.]+)",
        "firewall": r"(?P<action>DROP) connection from (?P<ip>[\d.]+)"
    }

    found_threats = 0

    for line in raw_text.strip().splitlines():
        matched = False
        
        # Check against available patterns
        for key, pattern in patterns.items():
            match = re.search(pattern, line)
            
            if match:
                data = match.groupdict()
                action = data.get("action", "UNKNOWN")
                user = data.get("user", "N/A")
                ip = data.get("ip")

                # Visual verdict based on action
                status_icon = "[!]" if action in ["Failed", "DROP"] else "[V]"
                print(f"{status_icon} {action:8} | User: {user:10} | Source IP: {ip}")
                
                if action in ["Failed", "DROP"]:
                    found_threats += 1
                
                matched = True
                break
        
        if not matched:
            print(f"[-] SKIPPED  | Unknown format: {line[:40]}...")

    print("\n" + "="*40)
    print(f"Analysis Complete. Threats detected: {found_threats}")
    print("="*40)

if __name__ == "__main__":
    analyze_logs(LOG_DUMP)