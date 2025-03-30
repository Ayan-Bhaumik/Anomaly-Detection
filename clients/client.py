import flwr as fl
import numpy as np

class FLClient(fl.client.NumPyClient):
    def __init__(self, model, X_train, y_train):
        self.model = model
        self.X_train = X_train
        self.y_train = y_train
        
    def get_parameters(self, config):
        return self.model.get_weights()
    
    def fit(self, parameters, config):
        self.model.set_weights(parameters)
        normal_data = self.X_train[self.y_train == 0]  # Semi-supervised
        self.model.fit(
            normal_data, normal_data,
            epochs=config['local_epochs'],
            batch_size=config['batch_size'],
            verbose=0
        )
        return self.get_parameters(config), len(normal_data), {}
    
    def evaluate(self, parameters, config):
        self.model.set_weights(parameters)
        loss = self.model.evaluate(self.X_train, self.X_train, verbose=0)
        return loss, len(self.X_train), {"mse": loss}