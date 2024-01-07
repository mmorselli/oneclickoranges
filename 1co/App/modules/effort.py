import os
import base64
import math
import time
from dotenv import load_dotenv
from algosdk.v2client import algod, indexer
from algosdk import encoding
import customtkinter

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'Configs', '.env')
load_dotenv(dotenv_path)


# Fetch configuration from environment variables
ALGOD_ADDRESS = os.getenv("ALGOD_MAINNET_SERVER") + ":" + os.getenv("ALGOD_MAINNET_PORT")
ALGOD_TOKEN = os.getenv("ALGOD_MAINNET_TOKEN")
INDEXER_ADDRESS = "https://mainnet-idx.algonode.cloud"  # Algonode indexer address
APPLICATION_ID = int(os.getenv("APP_MAINNET"))

# Initialize Algod and Indexer clients
algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)
indexer_client = indexer.IndexerClient("", INDEXER_ADDRESS)

def calculate_recent_effort_per_ora():
    try:
        # Get application data
        app_data = algod_client.application_info(APPLICATION_ID)
        state = app_data['params']['global-state']

        # Extract miner reward from state and scale it to ALGOs (6 decimal places)
        miner_reward = next((d['value']['uint'] for d in state if base64.b64decode(d['key']) == b'miner_reward'), 0) / math.pow(10, 6)

        # Calculate the application address
        app_address = encoding.encode_address(encoding.checksum(b'appID' + APPLICATION_ID.to_bytes(8, 'big')))

        # Search for transactions
        response = indexer_client.search_transactions(address=app_address, address_role="sender")

        # Get only the last 10 transactions
        recent_transactions = response['transactions'][10:]

        # Calculate costs
        costs = []
        for tx in recent_transactions:
            if 'logs' in tx and len(tx['logs']) > 0:
                try:
                    log = tx['logs'][0]
                    address = base64.b64decode(log)[:32]
                    if address != b'\x00' * 32:
                        # Scale cost to ALGOs (6 decimal places)
                        cost = int.from_bytes(base64.b64decode(log)[32:], 'big', signed=False) / math.pow(10, 6)
                        costs.append(cost)
                except Exception:
                    continue
            else:
                continue

        if costs:
            # Calculate average cost
            average_cost = sum(costs) / len(costs)
            # Adjust the calculation by multiplying by 100
            recent_effort_per_ora = (average_cost / miner_reward) * 100
        else:
            recent_effort_per_ora = 0

        # Format to 6 decimal places
        return "{:.6f}".format(recent_effort_per_ora)

    except Exception as e:
        # Handle any exceptions that may occur during the execution
        print(f"An error occurred: {str(e)}")
        return None
    
def PrintEffort(text_widget):    
    while True:
        recent_effort_per_ora = calculate_recent_effort_per_ora()
        if recent_effort_per_ora is not None:
            # print(f"Recent Effort per ORA: {recent_effort_per_ora} ALGO")
            text_widget.insert(customtkinter.END, f"Recent Effort per ORA: {recent_effort_per_ora} ALGO\n")
        time.sleep(5)  # Sleep for 15 seconds

# Main Execution
# if __name__ == "__main__":
#     PrintEffort()
