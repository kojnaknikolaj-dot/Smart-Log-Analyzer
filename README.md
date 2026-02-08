🛡️ Smart Log Analyzer (Regex Edition)

📋 Project Overview

This project is a high-performance log parsing tool designed for SOC (Security Operations Center) environments. It demonstrates the ability to transform "raw" and "noisy" system logs into structured, actionable security intelligence using Python and Advanced Regular Expressions.

This tool is a key part of my security automation portfolio, aimed at roles in companies like Red Hat, Honeywell, and major Czech financial institutions (ČSOB, Česká spořitelna).

🛠️ Technical Deep Dive

The script implements several professional programming patterns:

Advanced Regex (Named Capture Groups): Instead of using index-based matching, the script uses (?P...) syntax. This makes the code highly maintainable and allows the use of .groupdict() for instant data structuring.

Dynamic Pattern Matching: Patterns for different log sources (SSH, Firewall) are stored in a dictionary, making it easy to add support for new log types (e.g., Nginx, Windows Events) without changing the core engine.

Security Logic & Classification:

Automated detection of failed login attempts and dropped connections.

Visual alerting: Uses [!] for potential threats (Failed, DROP) and [V] for legitimate traffic.

Data Integrity: Includes an "Unknown Format" handler to ensure that non-matching lines are flagged for review rather than silently ignored.

📊 Logic Example

Input Raw Log: Feb 07 12:10:12 firewall-ext filter: DROP connection from 185.220.101.5

Structured Extraction:

{
  "action": "DROP",
  "ip": "185.220.101.5",
  "user": "N/A"
}
🚀 Installation & Usage

Ensure you have Python 3.x installed.

Clone this repository.

Add your log data to the LOG_DUMP variable in log_analyzer.py.

Run the analyzer:

python python log_analyzer.py

📈 Portfolio Context

This is Project #2 in my SOC Automation track. While Project #1 focused on basic setup, this project proves my ability to handle unstructured data—one of the most frequent challenges in real-world security monitoring.
