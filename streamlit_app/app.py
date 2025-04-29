import streamlit as st
from web3 import Web3

# Connect to Ethereum node (e.g., Infura or local node)
INFURA_URL = "https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

st.title("Ned Blockchain Workshop - Streamlit dApp")

if w3.isConnected():
    st.success("Connected to Ethereum Sepolia Testnet")
else:
    st.error("Failed to connect to Ethereum Sepolia Testnet")

# Example: Display latest block number
latest_block = w3.eth.block_number
st.write(f"Latest Block Number: {latest_block}")

# Add your contract address and ABI here
contract_address = "YOUR_CONTRACT_ADDRESS"
contract_abi = []  # Paste your contract ABI JSON here

if contract_address and contract_abi:
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    st.write("Contract loaded successfully")
    # Add interaction with contract here
else:
    st.warning("Please set your contract address and ABI in the app.py file.")
