# 🚀 Federated IoT Anomaly Detection
### Privacy-Preserving Threat Detection for IoT Networks using Federated Learning

<div align="center">
  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange)](https://www.tensorflow.org/)
[![Flower](https://img.shields.io/badge/Flower%20FL-1.4.0-yellowgreen)](https://flower.dev/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE)

</div>

## 👨‍💻 Developer
### **Ayan Bhaumik**  
<div align="center">
  
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://ayanbhaumik.in/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayan-bhaumik/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:connect@ayanbhaumik.in)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ayan-Bhaumik)
  
</div>

## 🌟 Key Features
- **Federated Learning Framework** - Train across distributed devices without data centralization
- **Autoencoder Architecture** - Deep neural networks for anomaly detection
- **UNSW-NB15 Dataset** - Real-world IoT network traffic with attack patterns
- **Privacy-Preserving** - Only shares model updates, never raw data
- **Modular Design** - Easily extensible components


## 🛠️ Installation
```bash

# Clone repository
git clone https://github.com/Ayan-Bhaumik/Anomaly-Detection.git
cd federated-iot-anomaly-detection

# Install dependencies

pip install -r requirements.txt
📂 Project Structure
Copy
├── configs/
│   └── config.yaml            # All configuration parameters
├── clients/                   # Client implementations
│   └── client.py              
├── server/                    # Server implementation
│   └── server.py             
├── utils/                     # Core functionality
│   ├── data_loader.py        # Data processing
│   └── model.py              # Neural network architecture
├── data/                      # Dataset storage
├── models/                    # Trained model weights
├── main.py                    # Entry point
└── requirements.txt           # Dependency list
⚙️ Configuration
Edit configs/config.yaml to customize:

yaml
Copy
model:
  encoder_layers: [128, 64, 32]  # Neural network architecture
  decoder_layers: [64, 128]
  
training:
  epochs: 10                    # Training parameters
  batch_size: 64

federation:
  num_clients: 3                # Number of IoT devices
  num_rounds: 10                # FL training rounds
🏃‍♂️ Running the System

# Start the federated learning process

python main.py
📊 Performance Metrics
Metric	Score
Accuracy	92.4%
F1-Score	0.91
Precision	0.93
Recall	0.89
Training Time	42 min
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

📬 Contact
For questions or collaborations:
Email connect@ayanbhaumik.in / mrayanbhaumik@gmail.com
LinkedIn https://www.linkedin.com/in/ayan-bhaumik/