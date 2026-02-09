apt update
apt install python3-pip qrencode -y
pip3 install qrcode[pil] hdwallet==3.3.0 --break-system-packages

wget https://github.com/MyEtherWallet/MyEtherWallet/releases/download/v6.9.26-hotfix.1/MyEtherWallet-v6.9.26-hotfix.1-Offline.zip
unzip MyEtherWallet-v6.9.26-hotfix.1-Offline.zip -d mew
