Potato Disease Classification
Overview
This project aims to classify potato plant images into different categories of diseases, such as Early Blight, Late Blight, and Healthy plants. The classification is performed using a Convolutional Neural Network (CNN) model trained on a dataset of potato plant images. The model is then deployed as a web application using Flask, allowing users to upload images and get predictions on the disease status of the potato plants.

Table of Contents
Installation

Usage

Model Training

Dataset

Web Application

Contributing

License

Installation
To run this project locally, follow these steps:

Clone the repository:

bash
Copy
git clone https://github.com/ravivarmanr26/potato_disease_classification.git
cd potato_disease_classification
Set up a virtual environment:

bash
Copy
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy
pip install -r requirements.txt
Usage
To start the web application, run the following command:

bash
Copy
python app.py
Once the application is running, open your web browser and navigate to http://127.0.0.1:5000/ to access the Potato Disease Classification web interface. You can upload images of potato plants and get predictions on whether the plant is healthy or affected by Early Blight or Late Blight.

Model Training
The model used in this project is a Convolutional Neural Network (CNN) trained on a dataset of potato plant images. The training script can be found in the train.py file. To train the model from scratch, follow these steps:

Prepare the dataset:

Ensure that the dataset is organized in the following structure:

Copy
dataset/
├── Early_Blight/
├── Late_Blight/
├── Healthy/
Train the model:

bash
Copy
python train.py --data_dir dataset/ --model_dir models/
This will train the model and save the best model weights in the models/ directory.

Dataset
The dataset used for training the model consists of images of potato plants categorized into three classes:

Early Blight: Images of potato plants affected by Early Blight disease.

Late Blight: Images of potato plants affected by Late Blight disease.

Healthy: Images of healthy potato plants.

The dataset can be downloaded from Kaggle or any other source that provides similar images.

Web Application
The web application is built using Flask, a lightweight web framework for Python. The app.py file contains the code for the Flask application, which allows users to upload images and get predictions from the trained model.

The application has a simple interface where users can:

Upload an image of a potato plant.

Click the "Predict" button to get the disease classification.

Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
