from hdwallet import HDWallet
from hdwallet.entropies import BIP39Entropy
from hdwallet.mnemonics import BIP39Mnemonic
from hdwallet.cryptocurrencies import Ethereum
from hdwallet.derivations import BIP44Derivation

import json

mnemonic_override = ""

entropy = BIP39Entropy(
    BIP39Entropy.generate(160)
    if mnemonic_override == "" else
    BIP39Mnemonic.decode(mnemonic_override)
)

derivation = BIP44Derivation(coin_type=Ethereum.COIN_TYPE)
wallet = HDWallet(cryptocurrency=Ethereum).from_entropy(entropy).from_derivation(derivation)

print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))
