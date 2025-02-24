from hdwallet import HDWallet
from hdwallet.entropies import BIP39Entropy
from hdwallet.mnemonics import BIP39Mnemonic
from hdwallet.cryptocurrencies import Ethereum
from hdwallet.derivations import BIP44Derivation

import json

mnemonic_override = ""

if mnemonic_override == "":
    entropy = BIP39Entropy.generate(160)
else:
    entropy = BIP39Mnemonic.decode(mnemonic_override)

wallet = HDWallet(cryptocurrency=Ethereum).from_entropy(BIP39Entropy(entropy)).from_derivation(BIP44Derivation())

print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))
