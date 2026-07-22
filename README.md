# 📊 Customer Churn Prediction using Machine Learning

## 📌 Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses. This project uses **Machine Learning** to predict whether a customer is likely to leave a service based on their demographic and service usage information.

The application provides:

* 🔍 Individual customer churn prediction
* 📂 Bulk prediction using CSV files
* 📈 Probability score indicating churn risk
* 🌐 Interactive web interface built with Streamlit

---

## 🚀 Features

* Predict customer churn in real time.
* Upload CSV files for bulk predictions.
* Displays churn probability.
* User-friendly Streamlit dashboard.
* Fast and lightweight ML inference.

---

## 🛠️ Tech Stack

| Technology   | Purpose                               |
| ------------ | ------------------------------------- |
| Python       | Programming Language                  |
| XGBoost      | Machine Learning Model                |
| Pandas       | Data Processing                       |
| NumPy        | Numerical Operations                  |
| Scikit-learn | Data Preprocessing & Train-Test Split |
| Streamlit    | Web Application                       |
| Pickle       | Model Serialization                   |

---

## 📂 Project Structure

```text
Customer-Churn-Prediction/
│
├── churn.csv               # Dataset
├── train.py                # Model training script
├── churn_model.pkl         # Trained ML model
├── front.py                # Streamlit application
├── requirements.txt        # Dependencies
└── README.md
```

---

## ⚙️ Machine Learning Workflow

1. Load customer churn dataset.
2. Remove unnecessary columns.
3. Handle missing values.
4. Encode categorical features.
5. Split dataset into training and testing sets.
6. Train an XGBoost Classifier.
7. Save the trained model.
8. Deploy the model using Streamlit.

The training script loads the dataset, preprocesses categorical and numerical features, trains an XGBoost classifier, and saves the trained model for deployment.

---

## 🖥️ Streamlit Application

The application provides two prediction modes:

### ✅ Individual Prediction

Users can enter:

* Customer tenure
* Monthly charges
* Contract type

The model predicts whether the customer is likely to churn and displays the churn probability.

### ✅ Bulk Prediction

Users can upload a CSV file containing multiple customer records for batch processing and preview the uploaded data through the dashboard.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
```

Navigate to the project folder:

```bash
cd customer-churn-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model (optional):

```bash
python train.py
```

Run the Streamlit application:

```bash
streamlit run front.py
```

---

## 📊 Dataset

The project uses a customer churn dataset containing information such as:

* Customer tenure
* Monthly charges
* Contract type
* Demographic information
* Service subscriptions
* Churn status (Target Variable)

---

## 📈 Model

**Algorithm Used**

* XGBoost Classifier

Why XGBoost?

* High prediction accuracy
* Handles mixed feature types effectively
* Fast training and inference
* Robust performance on structured/tabular datasets

---

## 📚 Requirements

```text
pandas
numpy
scikit-learn
xgboost
streamlit
```

The project dependencies include Pandas, NumPy, Scikit-learn, XGBoost, and Streamlit.

---

## 🎯 Future Improvements

* Improve feature engineering
* Hyperparameter tuning
* Interactive data visualizations
* Model performance metrics dashboard
* Docker deployment
* Cloud deployment (AWS/Azure/GCP)
* User authentication

---

## 👨‍💻 Author

**Yashwanth Dhadi**

* AI & Machine Learning Enthusiast
* Python Developer
* Passionate about Machine Learning, Data Science, and AI Applications

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
