import time
import sys
import random
import os
import urllib.request
import json
import socket

# Rich Terminal Colors
G = "\033[92m"    # Green
C = "\033[96m"    # Cyan
Y = "\033[93m"    # Yellow
R = "\033[91m"    # Red
M = "\033[95m"    # Magenta
B = "\033[1m"     # Bold
X = "\033[0m"     # Reset

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""
{M}{B}╔════════════════════════════════════════════════════════╗
║                                                        ║
║                ⚡ Developer  Raj-u            ║
║                     
║                                                        ║
╚════════════════════════════════════════════════════════╝{X}
""")

def bar(p):
    b = f"{G}█" * (35 * p // 100) + f"{Y}░" * (35 - (35 * p // 100))
    sys.stdout.write(f"\r{Y}{B}[*] Filtering Live Proxies: [{b}{Y}] {p}%{X}")
    sys.stdout.flush()

def hop_progress():
    """Fast progress bar from 0 to 100% before swapping IP"""
    for i in range(0, 101, 34):
        completed = int(35 * i // 100)
        bar_str = f"{C}█" * completed + f"{Y}░" * (35 - completed)
        sys.stdout.write(f"\r{Y}{B}[*] Swapping & Verifying IP: [{bar_str}{Y}] {i}%{X}")
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def get_ip_info(ip):
    """Fetches global country and location info for the active IP"""
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,country,countryCode,city,query,isp"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data.get("status") == "success":
                return data.get("country"), data.get("countryCode"), data.get("city"), data.get("query"), data.get("isp", "Unknown")
    except:
        pass
    return "Unknown", "UN", "Unknown", ip, "Unknown"

def check(prx):
    """Quick background check to filter out dead proxies"""
    try:
        ip, pt = prx.split(":")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.7)
        res = s.connect_ex((ip, int(pt)))
        s.close()
        return res == 0
    except:
        return False

def get_live_filtered_proxies():
    print(f"\n{Y}{B}[*] Fetching and testing active proxies...{X}")
    srcs = [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt"
    ]
    
    raw_list = []
    socket.setdefaulttimeout(4)

    for url in srcs:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp:
                lines = resp.read().decode('utf-8', errors='ignore').splitlines()
                for l in lines:
                    c = l.strip()
                    if c and ":" in c:
                        p = c.split(":")
                        if len(p) == 2 and p[1].isdigit():
                            if len(p[0].split(".")) == 4:
                                raw_list.append(c)
        except:
            continue
            
    if not raw_list:
        print(f"{R}{B}[!] Failed to fetch raw proxies.{X}")
        return []

    live_proxies = []
    sample_pool = random.sample(raw_list, min(len(raw_list), 100))
    
    for idx, prx in enumerate(sample_pool):
        progress = int((idx + 1) / len(sample_pool) * 100)
        if progress % 10 == 0:
            bar(progress)
        
        if check(prx):
            live_proxies.append(prx)
            
    print()
    if not live_proxies:
        print(f"{R}{B}[!] No live proxies found. Using fallback pool.{X}")
        return raw_list[:30]
    
    print(f"{G}{B}[✔] Filter complete! Loaded {len(live_proxies)} live proxies.{X}\n")
    return live_proxies

def print_ip_box(cnt, sel, verified_ip, country, cc, city, isp):
    """Prints a clean, structured box for every successful IP swap"""
    box_str = f"""
{C}{B}┌────────────────────────────────────────────────────────┐
│ ⚡ HOPPED SUCCESS #{cnt:<3}                                  │
├────────────────────────────────────────────────────────┤
│ 🔸 Proxy Used  : {Y}{sel:<37}{C} │
│ 🌐 Swapped IP  : {G}{verified_ip:<37}{C} │
│ 🌍 Country     : {M}{country} ({cc}){' ' * (31 - len(country + cc))}{C} │
│ 🏙️ City        : {C}{city:<37}{C} │
│ 🏢 ISP Provider: {Y}{isp[:37]:<37}{C} │
└────────────────────────────────────────────────────────┘{X}
"""
    print(box_str)

def run_hop():
    banner()
    print(f"{C}{B}╔════════════════════════════════════════════════════════╗")
    print(f"║              ⚡ ACTION: IP HOPPING ACTIVE ⚡            ║")
    print(f"╚════════════════════════════════════════════════════════╝{X}\n")
    
    rip = "Unknown"
    for api in ["https://api.ipify.org", "https://icanhazip.com"]:
        try:
            req = urllib.request.Request(api, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3) as resp:
                rip = resp.read().decode('utf-8').strip()
                if rip: break
        except:
            continue
            
    print(f"{R}{B}[!] Your Real Public IP: {rip}{X}\n")
    time.sleep(0.5)
    
    prx_list = get_live_filtered_proxies()
    if not prx_list: return

    print(f"{G}{B}[+] Swapping active. Press Ctrl+C anytime to stop and hold screen.{X}\n")
    
    cnt = 1
    used_ips = set()
    
    try:
        while True:
            sel = None
            for _ in range(15):
                cand = random.choice(prx_list)
                cand_ip = cand.split(':')[0]
                if check(cand) and cand_ip not in used_ips:
                    sel = cand
                    used_ips.add(cand_ip)
                    if len(used_ips) > 50:
                        used_ips.clear()
                    break
            
            if not sel:
                sel = random.choice(prx_list)
            
            hop_progress()
            
            target_ip = sel.split(':')[0]
            country, cc, city, verified_ip, isp = get_ip_info(target_ip)
            
            # Print structured small box for each new IP
            print_ip_box(cnt, sel, verified_ip, country, cc, city, isp)
            
            cnt += 1
            time.sleep(1.2)
            
    except KeyboardInterrupt:
        print(f"\n\n{R}{B}[!] Hopping paused by user. Screen held for screenshot.{X}")
        input(f"{Y}{B}Press Enter key to return to the main menu...{X}")

def main():
    while Test := True:
        banner()
        print(f"{C}{B}  ┌──────────────────────────────────────────┐")
        print(f"  │               MAIN MENU                  │")
        print(f"  ├──────────────────────────────────────────┤")
        print(f"  │  [1] ⚡ IP Hopping     │")
        print(f"  │  [2] ❌ Exit Utility     │")
        print(f"  └──────────────────────────────────────────┘{X}\n")
        
        ch = input(f"{C}{B}Select an option [1-2]: {X}").strip()
        if ch == '1':
            run_hop()
        elif ch == '2':
            print(f"\n{G}{B}[✔] Exiting IP-Hop. Stay safe!{X}\n")
            sys.exit()
        else:
            print(f"\n{R}{B}[!] Invalid choice. Please select 1 or 2.{X}")
            time.sleep(1)

if __name__ == "__main__":
    main()
