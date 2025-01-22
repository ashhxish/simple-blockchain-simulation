# Simple Blockchain Simulation

## Overview
This project demonstrates the basic principles of blockchain technology. It simulates a simple blockchain with blocks containing transactions, using SHA-256 hashing for block verification and a simple proof-of-work mechanism.

## Features
- Block structure with an index, timestamp, list of transactions, previous block's hash, and the current block's hash.
- Blockchain class to manage the chain, add new blocks, and validate the chain’s integrity.
- Basic proof-of-work mechanism to simulate computational effort in creating a block.
- Tamper detection: Modifying any block invalidates the blockchain.

## Installation

### Prerequisites
Ensure you have Python 3.6 or higher installed.

### Dependencies
To install the required dependencies, create a virtual environment and use the following:

```bash
pip install -r requirements.txt
