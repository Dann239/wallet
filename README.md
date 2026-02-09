# Encrypt:

```
gpg --s2k-mode 3 --s2k-count 65011712 --s2k-digest-algo SHA512 --s2k-cipher-algo AES256 --symmetric --armor data.txt
```

# Draw as QR

```
qrencode -t utf8 < data.txt.asc
```
