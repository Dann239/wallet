from hdwallet import HDWallet
from hdwallet.entropies import BIP39Entropy
from hdwallet.mnemonics import BIP39Mnemonic
from hdwallet.cryptocurrencies import Ethereum, Bitcoin
from hdwallet.derivations import BIP44Derivation

import qrcode

import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--qr', action='store_true')
parser.add_argument('--btc', action='store_true')
qr = parser.parse_args().qr
assert isinstance(qr, bool)
btc = parser.parse_args().btc
assert isinstance(btc, bool)

mnemonic_override = input()

if mnemonic_override != "":
    known_words = set(BIP39Mnemonic.get_words_list_by_language('english'))
    unrecognized_words = set(mnemonic_override.split()) - known_words
    assert len(unrecognized_words) == 0, unrecognized_words

entropy = BIP39Entropy(
    BIP39Entropy.generate(160)
    if mnemonic_override == "" else
    BIP39Mnemonic.decode(mnemonic_override)
)

coin = Bitcoin if btc else Ethereum
derivation = BIP44Derivation(coin_type=coin.COIN_TYPE)
wallet = HDWallet(cryptocurrency=coin).from_entropy(entropy).from_derivation(derivation)

print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))

if qr:
    input("Press Enter to generate a QR code")
    qr = qrcode.QRCode()
    qr.add_data(wallet.address())
    os.system("clear")
    qr.print_ascii()
