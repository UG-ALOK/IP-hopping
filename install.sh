#!/bin/bash

if [ ! -f "main.py" ]; then
    echo "[!] Error: main.py not found in current directory!"
    exit 1
fi

if [ -d "/data/data/com.termux" ]; then
    BIN_PATH="/data/data/com.termux/files/usr/bin"
else
    BIN_PATH="/usr/local/bin"
fi

cat << 'EOF' > "$BIN_PATH/ip hop"
#!/bin/bash
python3 "$(pwd)/main.py" "$@"
EOF

cat << 'EOF' > "$BIN_PATH/ip-hop"
#!/bin/bash
python3 "$(pwd)/main.py" "$@"
EOF

chmod +x "$BIN_PATH/ip hop"
chmod +x "$BIN_PATH/ip-hop"
chmod +x "main.py"

echo "[✔] Installation Completed Successfully!"
echo "[+] Now you can simply type 'ip hop' from anywhere in your terminal to run the utility."
