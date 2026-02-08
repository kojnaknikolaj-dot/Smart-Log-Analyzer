🗄️ IoC Database Manager (Memory Edition)

📋 Project Overview

This project is a Python-based utility for managing Indicators of Compromise (IoCs). It simulates the core functionality of a Threat Intelligence Platform (TIP), allowing security analysts to maintain a local database of malicious IP addresses in system memory.

The goal of this project is to demonstrate proficiency in Data Structures (Lists of Dictionaries) and Conditional Logic.

🛠️ Key Technical Skills

In-Memory Data Management: Utilizing a list of dictionaries to represent complex objects.

Search & Filtering: Implementing search logic to match live log data against a threat database.

Duplicate Prevention: Logical checks to ensure data integrity by preventing redundant entries.

List Comprehensions: Using Pythonic ways to filter and remove data efficiently.

⚙️ Functionality

add_ioc(): Validates and inserts new threat actors into the database.

remove_ioc(): Efficiently clears outdated or whitelisted entries.

check_ip(): Provides instant lookups for SOC investigations.

show_stats(): Generates a high-level overview of the current threat landscape.

🏦 Use Case for Red Hat / Honeywell

In large environments, analysts often need to create "quick and dirty" scripts to track specific attack campaigns during an incident. This tool showcases the ability to build a structured, searchable system for tracking malicious activity without the overhead of a full SQL database.

🚀 Getting Started

Run the script to see the simulation of IoC management:

python ioc_manager.py


👨‍💻 Developer

Developed as part of a Python for SOC curriculum, focusing on automation for Czech banking (ČSOB/Spořitelna) and global tech leaders (Red Hat/Honeywell).