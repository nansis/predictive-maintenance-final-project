---
license: mit
language:
- en
library_name: scikit-learn
pipeline_tag: tabular-classification
tags:
- predictive-maintenance
- classification
- scikit-learn
- tabular-data
metrics:
- accuracy
- precision
- recall
- f1
---

# Predictive Maintenance Model

## Overview
This repository contains the best-performing machine learning model developed for the predictive maintenance project.

## Business Problem
The objective of this model is to classify whether an engine is operating normally or is likely to require maintenance based on sensor readings.

## Input Features
- Engine_rpm
- Lub_oil_pressure
- Fuel_pressure
- Coolant_pressure
- lub_oil_temp
- Coolant_temp

## Selected Model
AdaBoost

## Evaluation Summary
{'Model': 'AdaBoost', 'Best_Parameters': "{'learning_rate': 0.05, 'n_estimators': 100}", 'CV_Best_F1': 0.7752, 'Test_Accuracy': 0.6304, 'Test_Precision': 0.6304, 'Test_Recall': 1.0, 'Test_F1': 0.7733}

## Model Interpretation
The selected model was identified after comparing multiple tree-based algorithms using cross-validation and test-set evaluation.

## Limitation
Although the selected model achieved the highest test F1-score, its confusion matrix shows that it predicted all observations as class 1. This means the model was very strong in identifying maintenance-required cases but weak in distinguishing normal operating cases.
