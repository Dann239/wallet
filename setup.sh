apt update
apt install python3-pip qrencode -y
pip3 install qrcode[pil] hdwallet==3.3.0 --break-system-packages

# pin because of https://github.com/MyEtherWallet/MyEtherWallet/issues/5253
wget https://github.com/MyEtherWallet/MyEtherWallet/releases/download/v6.9.25-hotfix.4/MyEtherWallet-v6.9.25-hotfix.4-Offline.zip
