## Cat vs Dog Image Classifier using CNN

## Project Overview

This project implements a Convolutional Neural Network (CNN) using TensorFlow and Keras to classify images as either Cats or Dogs.

The model was trained on the Microsoft PetImages dataset containing thousands of labeled cat and dog images.

## Features

* Image classification using CNN
* TensorFlow/Keras implementation
* Dataset loading from directories
* Image preprocessing and normalization
* Training and validation split
* Model saving and loading
* Prediction on custom images

## Dataset

Dataset Used:

Microsoft PetImages Dataset

Classes:

* Cat
* Dog

Total Images:

Approximately 25,000 images

## CNN Architecture

Input Shape:

128 × 128 × 3

Architecture:

* Conv2D (32 filters)
* MaxPooling2D
* Conv2D (64 filters)
* MaxPooling2D
* Flatten
* Dense (64 units)
* Dense (1 unit, Sigmoid)

## Training Results

Training Accuracy: ~92%

Validation Accuracy: ~76%

Observations:

* Model successfully learns features from cat and dog images.
* Some overfitting was observed.
* Future improvements include:

  * Data Augmentation
  * Dropout Layers
  * Transfer Learning (MobileNetV2)

## Installation

```bash
pip install -r requirements.txt
```

## Training

```bash
python train.py
```

## Prediction

```bash
python predict.py
```

## Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib

## Future Improvements

* Transfer Learning
* Better Generalization
* Hyperparameter Tuning
* Model Deployment

## Author

Noman Ayub
AI & Data Science Student
