import yaml
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_config(config_path="configs/config.yaml"):
    with open(config_path) as f:
        return yaml.safe_load(f)

def load_and_preprocess_data(config):
    try:
        # Load dataset
        df = pd.read_csv(config['dataset']['url'])
        
        # Select features and label
        features = config['dataset']['features']
        label = config['dataset']['label']
        df = df[features + [label]]
        
        # Convert categorical columns to dummy variables
        categorical_cols = ['proto', 'service', 'state']
        df = pd.get_dummies(df, columns=[col for col in categorical_cols if col in df.columns])
        
        # Separate features and labels
        X = df.drop(columns=[label]).values
        y = df[label].values
        
        # Normalize features
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        
        # Split into train and test sets
        return train_test_split(
            X, y,
            test_size=config['training']['test_size'],
            random_state=config['training']['random_state']
        )
    except Exception as e:
        print(f"Data loading error: {e}")
        return None, None, None, None