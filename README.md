# House Price Prediction

This repository contains a machine learning project to predict house prices based on various features. The dataset is preprocessed and analyzed to build a predictive model using Linear Regression.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Evaluation Metrics](#evaluation-metrics)
- [Repository Structure](#repository-structure)

## Introduction

The objective of this project is to create a machine learning model that predicts the sale price of houses. The dataset used contains multiple features describing various aspects of houses.

## Features

Key features used in this project include:
- Numeric features related to house size, condition, and location.
- Categorical features (converted to one-hot encoded variables).

Dropped features:
- `PID`, `Street`, `Alley`, `Utilities`, `Condition_2`, `Roof_Matl`, `Heating`, `Pool_QC`, `Misc_Feature`, `Longitude`, `Latitude`

## Requirements

Before running the project, install the dependencies using the following command:


pip install -r requirements.txt
Usage
Clone this repository:

bash
Copy code
git clone https://github.com/Ahmed-J646/House-Price-Prediction.git
cd House-Price-Prediction
Ensure the dataset (train.csv) is present in the root directory.

Run the script to preprocess data, train the model, and evaluate its performance:


python main.py
Evaluation Metrics
Mean Squared Error (MSE): Measures the average squared difference between actual and predicted prices.
Mean Absolute Error (MAE): Measures the average absolute difference between actual and predicted prices.
R² Score: Indicates the goodness of fit of the model.
Repository Structure
plaintext
Copy code
House-Price-Prediction/
│
├── train.csv                # Dataset (to be placed in the root directory)
├── main.py                  # Main script for training and evaluation
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
└── backend.py               # For Backend Operations
└── frontend.py              # For Frontend Operations

License:
This project is open source and available under the MIT License.
