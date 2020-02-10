from web3 import Web3
import web3
import json
from solc import compile_standard
provider='/home/joydeep/projects/ethereum/data/geth.ipc'

myprovider=Web3.IPCProvider(provider)

#from web3.auto import w3


w3 = Web3(myprovider)
w3.eth.defaultAccount = w3.eth.accounts[0]
print(w3.eth.accounts)

def gas_price_strategy(w3,transaction_params=None):
     return w3.toWei(0.0000000001, 'wei')

#w3.geth.miner.setGasPrice(1)
w3.eth.setGasPriceStrategy(gas_price_strategy)
print(w3.geth.personal.unlockAccount('0x77F0a7a52005C6EaB67cd4F3E16c315998AebF30', 'joydeep'))
#print(w3.eth.generateGasPrice())
'''
compiled_sol = compile_standard({
    "language": "Solidity",
     "sources": {
        "joydeep.sol": {
             "content": ''''''
                 pragma solidity 0.6.2;

                 contract joydeep {
                 int public value;

                  constructor() public {
                     value = 100;
                  }

                  function setvalue(int newvalue) public {
                     value = newvalue ;              }

                   function greet() view public returns (int ) {
                      return value;                }
                 }
               ''''''
                        }
     },
    "settings":
         {
             "outputSelection": {
                "*": {
                    "*": [
                         "metadata", "evm.bytecode"
                         , "evm.bytecode.sourceMap"
                     ]
                 }
             }
         }
 })

bytecode=compiled_sol['contracts']['joydeep.sol']['joydeep']['evm']['bytecode']['object']
abi=json.loads(compiled_sol['contracts']['joydeep.sol']['joydeep']['metadata'])['output']['abi']


joydeep=w3.eth.contract(abi=abi,bytecode=bytecode)
#tx_hash=joydeep.constructor().estimateGas()
'''
#tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

#print(tx_hash)

tx=w3.eth.sendTransaction({'to': '0x2A5C850121bd9D137e7a1eE38BdAB898354ca5b0', 'from': w3.eth.coinbase, 'value': 0})

tx_receipt=
print(tx)