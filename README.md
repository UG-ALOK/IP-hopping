# ⚡ Advanced Enterprise-Grade IP-Hop & Proxy Rotation Utility

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Linux-green.svg)](https://github.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Advanced IP-Hop** is a high-performance, lightweight command-line interface (CLI) utility architected specifically for Termux and Linux-based environments. It automates real-time, verified proxy extraction, strict background validation, live geolocated routing, and continuous IP swapping without leaving persistent storage traces.

---

## 🚀 Key Architectural Features

* **Zero Persistent Storage Footprint**: Operates entirely in volatile memory (RAM). No sensitive proxy lists, historical logs, or cache files are written to internal storage or SD card directories.
* **Strict Socket Pre-Filtering**: Before any swap occurs, raw proxy pools fetched from trusted upstream repositories undergo rigorous socket-level connectivity tests. Dead or lagging nodes are purged instantly.
* **Live Geolocation & ISP Intelligence**: Integrated directly with high-accuracy geolocation APIs to extract real-time metadata for every active circuit, including Country, Region Code, City, and Internet Service Provider (ISP).
* **Structured UI Box Rendering**: Eliminates cluttered terminal outputs by wrapping every successful circuit rotation inside an isolated, color-coded ANSI box structure for pristine legibility.
* **Smart Anti-Repetition Logic**: Incorporates an internal tracking stack that caches recently utilized nodes to prevent redundant, consecutive loops over the same IP address.
* **Interactive Session Suspension**: Fully supports graceful interrupt handling (`Ctrl+C`). Pressing interrupt pauses the rotation sequence instantly, holding the current terminal state intact for forensic logging or screenshot capture.
* **Global Command Wrapper Integration**: The automated installation shell script establishes global system shortcuts (`ip hop` / `ip-hop`), allowing execution from any directory path without manual Python interpreter declarations.

---

## 🛠️ System Requirements & Dependencies

* **Interpreter**: Python 3.8 or higher.
* **Environment**: Android Termux (with core utilities) or standard GNU/Linux distributions (Ubuntu, Debian, Kali Linux, Arch).
* **Network**: Active internet connection required for upstream proxy harvesting and geolocation lookups.

---

## 📦 Automated Installation Guide

To deploy the utility globally across your terminal environment, execute the following commands in your shell:

# Clone the repository
```bash
git clone https://github.com/UG-ALOK/IP-hopping.git
```
# Navigate to the project director
```bash
cd IP-hopping
```
# Grant execution permissions to the installer script
```bash
chmod +x install.sh
```
# Execute the deployment script
```bash
./install.sh
```
Alternatively, the hyphenated alias is also natively supported
* Run 2
```bash
ip-hop
```
Interactive Menu Operations:
• [1] ⚡ IP Hopping: Initializes upstream list harvesting, executes strict socket checks, displays a live progress bar, and starts real-time rotating circuits accompanied by formatted metadata boxes.
• [2] Exit Utility: Terminates runtime processes cleanly and restores default shell states.

🛑 Execution Control & Interruption
During active hopping phases, you may halt the loop at any designated moment by issuing a standard keyboard interrupt signal:
• Command: Press Ctrl + C
• Behavior: The script catches the exception gracefully, suppresses traceback dumps, freezes the terminal frame at the current rotation block, and prompts you to review data before returning to the primary menu interface.

⚙️ Technical Blueprint & Workflow
• Harvesting Stage: Fetches raw, unfiltered proxy nodes from continuously maintained public GitHub data pools.
• Sanitization & Validation: Parses text matrices, validates IPv4 syntax patterns, and runs low-latency socket connection handshakes.
• Circuit Selection: Selects verified live nodes while cross-referencing internal history filters to ensure absolute variance.
• Verification & Geolocation: Renders an animated progress sequence, routes validation queries, resolves target endpoints, and prints structured terminal boxes.
```bash
📄 Legal Disclaimer & Liability Notice
Ug-alok 
This software is developed strictly for educational and ethical network research purposes. 
The developer and author are not responsible for any misuse, damage, or illegal activities. 
If any illegal or unauthorized action occurs, it is entirely the user's sole responsibility. 
The developer assumes zero liability under any circumstances. 
Users must operate this tool strictly at their own risk.
```
