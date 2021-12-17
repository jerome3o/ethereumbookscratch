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