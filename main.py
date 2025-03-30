import os
from utils.data_loader import load_config, load_and_preprocess_data
from utils.model import build_autoencoder
from server.server import run_server
from clients.client import FLClient
import numpy as np
import flwr as fl

def main():
    
    config = load_config()
    
   
    X_train, X_test, y_train, y_test = load_and_preprocess_data(config)
    config['model']['input_dim'] = X_train.shape[1]
    
    # Build model
    model = build_autoencoder(config)
    
    # Start server in a separate process
    if os.fork() == 0:
        run_server(model, X_test, y_test, config)
    else:
        # Start clients
        client_data = np.array_split(X_train, config['federation']['num_clients'])
        for i, data in enumerate(client_data):
            if os.fork() == 0:
                client = FLClient(
                    build_autoencoder(config),
                    data,
                    y_train[i*len(data):(i+1)*len(data)]
                )
                fl.client.start_numpy_client(
                    server_address=config['federation']['server_address'],
                    client=client
                )
                exit()

if __name__ == "__main__":
    main()