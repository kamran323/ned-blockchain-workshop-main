# Streamlit dApp for Ned Blockchain Workshop

This is a simple Streamlit application to interact with the Ethereum Sepolia Testnet smart contracts deployed in the Ned Blockchain Workshop project.

## Setup

1. Create a Python virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Update `app.py`:

- Replace `YOUR_INFURA_PROJECT_ID` with your Infura project ID or another Ethereum node provider URL.
- Replace `YOUR_CONTRACT_ADDRESS` with your deployed contract address.
- Paste your contract ABI JSON in the `contract_abi` variable.

## Running the app

Run the Streamlit app locally:

```bash
streamlit run app.py
```

## GitHub Deployment

To deploy this Streamlit app on GitHub:

1. Push this `streamlit_app` folder to your GitHub repository.

2. Use [Streamlit Community Cloud](https://streamlit.io/cloud) to deploy:

- Connect your GitHub repository.
- Select the `streamlit_app` folder as the app location.
- Set up any necessary secrets (e.g., Infura project ID) in the Streamlit Cloud settings.

3. Alternatively, set up GitHub Actions to deploy to a cloud provider of your choice.

## Notes

- This app connects to the Ethereum Sepolia Testnet.
- Ensure your smart contract is deployed and accessible.
- This is a basic example; extend it to add more dApp features as needed.
