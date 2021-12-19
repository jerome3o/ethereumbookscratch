# Chapter 7: Smart Contracts and Solidity

## Compiling using `solc`


```console
07:34 $ solc --optimize --bin chapter_7_smart_contracts/faucet/faucet_1.sol 

======= chapter_7_smart_contracts/faucet/faucet_1.sol:Faucet =======
Binary:
608060405234801561001057600080fd5b5060da8061001f6000396000f3fe60806040526004361060205760003560e01c80632e1a7d4d14602b57600080fd5b36602657005b600080fd5b348015603657600080fd5b5060466042366004608c565b6048565b005b67016345785d8a0000811115605c57600080fd5b604051339082156108fc029083906000818181858888f193505050501580156088573d6000803e3d6000fd5b5050565b600060208284031215609d57600080fd5b503591905056fea26469706673582212209f79e53b1620930b0d0cadcce7a93bbb9b0a158609c79ca1863bf5e74a68e65664736f6c634300080a0033
```

## Inspect ABI

```console
07:37 $ solc --abi chapter_7_smart_contracts/faucet/faucet_1.sol 

======= chapter_7_smart_contracts/faucet/faucet_1.sol:Faucet =======
Contract JSON ABI
[{"inputs":[{"internalType":"uint256","name":"withdraw_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]
```

## Truffle

### Setup

```console
npm install -g truffle

mkdir faucet
cd faucet
truffle init
npm init
npm install dotenv truffle-wallet-provider ethereumjs-wallet

# Add engines field to package.json (tip: npm -v, and node -v)

rm truffle.js

```

In `truffle-config.js`, uncomment the the localnode development network:

```js
    development: {
      host: "127.0.0.1", // Localhost (default: none)
      port: 8545, // Standard Ethereum port (default: none)
      network_id: "*", // Any network (default: none)
    },
```

#### Setting up contracts

Put your contract into `./contracts/` and run `truffle compile`

Make a new migration based off the existing:

```sh
sed 's/Migrations/Faucet/g' migrations/1_initial_migration.js > migrations/2_deploy_contracts.js
```

### Ganache

```
npm install -g ganache-cli

# Run with:
ganache-cli --networkId=3 --port="8545" --verbose --gasLimit=8000000 --gasPrice=4000000000
```

This should be running in a different terminal before running truffle, unless you have a local node running

### Migrating

```console
truffle migration --network development
```

## Playing around with the truffle console

Attach to the local node

```console
truffle console --network development
```

```js
// Getting a reference to the deployed faucet contract
Faucet.deployed().then(f => {FaucetDeployed = f})

// Sending eth to the Faucet
FaucetDeployed.send(web3.utils.toWei("1", "ether")).then(res => {console.log(res.logs[0].event, res.logs[0].args)})

// Deposit Result {
//   '0': '0x0E256759C4db963922B919B4C3F5B2A5f4e373Dc',
//   '1': BN {
//     negative: 0,
//     words: [ 56885248, 2993385, 222, <1 empty item> ],
//     length: 3,
//     red: null
//   },
//   __length__: 2,
//   from: '0x0E256759C4db963922B919B4C3F5B2A5f4e373Dc',
//   amount: BN {
//     negative: 0,
//     words: [ 56885248, 2993385, 222, <1 empty item> ],
//     length: 3,
//     red: null
//   }
// }

FaucetDeployed.withdraw(web3.utils.toWei("0.1", "ether")).then(res => {console.log(res.logs[0].event, res.logs[0].args)})

// Withdrawal Result {
//   '0': '0x0E256759C4db963922B919B4C3F5B2A5f4e373Dc',
//   '1': BN {
//     negative: 0,
//     words: [ 25821184, 13721111, 22, <1 empty item> ],
//     length: 3,
//     red: null
//   },
//   __length__: 2,
//   to: '0x0E256759C4db963922B919B4C3F5B2A5f4e373Dc',
//   amount: BN {
//     negative: 0,
//     words: [ 25821184, 13721111, 22, <1 empty item> ],
//     length: 3,
//     red: null
//   }
// }

```

