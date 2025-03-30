import flwr as fl
from typing import Dict, Tuple, Optional
import numpy as np
from sklearn.metrics import accuracy_score, f1_score

def get_evaluation_fn(model, X_test, y_test):
    def evaluate(weights):
        model.set_weights(weights)
        reconstructions = model.predict(X_test, verbose=0)
        mse = np.mean(np.power(X_test - reconstructions, 2), axis=1)
        threshold = np.quantile(mse, 0.95)
        y_pred = (mse > threshold).astype(int)
        
        return float("inf"), {
            "accuracy": accuracy_score(y_test, y_pred),
            "f1": f1_score(y_test, y_pred),
            "threshold": threshold
        }
    return evaluate

def run_server(model, X_test, y_test, config):
    strategy = fl.server.strategy.FedAvg(
        evaluate_fn=get_evaluation_fn(model, X_test, y_test),
        fraction_fit=1.0,
        fraction_evaluate=0.5,
        min_available_clients=config['federation']['num_clients']
    )
    
    fl.server.start_server(
        server_address=config['federation']['server_address'],
        strategy=strategy,
        config=fl.server.ServerConfig(
            num_rounds=config['federation']['num_rounds']
        )
    )