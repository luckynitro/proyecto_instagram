try:
    from pathlib import Path
except ImportError:
    # Para versiones de Python anteriores a la 3.4
    from pathlib2 import Path

from web3 import Web3

# Conectar a un nodo Ethereum (puede ser tu nodo local o Infura)
infura_url = "https://mainnet.infura.io/v3/b113bca31edd4ba08e64c966e5ef3743"
w3 = Web3(Web3.HTTPProvider(infura_url))

# Dirección del propietario del contrato y su clave privada
owner_address = "0x4Bf8a105452A55d4266f5213700aeb20c68061C9"
private_key = "bc8963f6f6c7cef80d969c4275a6da515590e32d5e57549c8c05eac1406e41af"

# Cargar el contrato compilado
contract_path = Path("output/ContentMonetization")
contract_abi_path = contract_path.with_suffix(".abi")
contract_bin_path = contract_path.with_suffix(".bin")

with contract_abi_path.open() as f:
    contract_abi = f.read()

with contract_bin_path.open() as f:
    contract_bin = f.read()

# Resto del código...

