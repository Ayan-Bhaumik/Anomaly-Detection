from keras.layers import Input, Dense, Dropout
from keras.models import Model

def build_autoencoder(config):
    input_dim = config['model']['input_dim']
    input_layer = Input(shape=(input_dim,))
    
    # Encoder
    x = input_layer
    for units in config['model']['encoder_layers']:
        x = Dense(units, activation=config['model']['activation'])(x)
        x = Dropout(config['model']['dropout_rate'])(x)
    
    # Decoder
    for units in config['model']['decoder_layers']:
        x = Dense(units, activation=config['model']['activation'])(x)
    
    output_layer = Dense(input_dim, activation='linear')(x)
    
    autoencoder = Model(input_layer, output_layer)
    autoencoder.compile(optimizer='adam', loss='mse')
    return autoencoder