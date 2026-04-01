# 📊 ML-Driven Credit Risk Model

A **Machine Learning based Credit Risk Prediction System** that evaluates loan applicants and generates a **credit score and risk rating** using financial and behavioral features.

The model predicts the **probability of default**, converts it into a **credit score (300–900)**, and categorizes applicants into **Poor, Average, Good, or Excellent** credit ratings.

---


---

# 🧠 Project Overview

Financial institutions must assess the **risk of lending money** to applicants. This project builds a **Machine Learning credit scoring system** that:

- Predicts **loan default probability**
- Converts probability into a **credit score**
- Assigns a **credit rating category**
- Provides a **user-friendly Streamlit interface**

The system uses a trained **Logistic Regression model** with scaled financial features.

---

# 📌 Features

✔ Credit default probability prediction  
✔ Credit score generation (300–900 range)  
✔ Risk rating classification  
✔ Automated feature scaling  
✔ Streamlit interactive UI  
✔ Easy deployment using joblib model artifacts  

---

# 🏗 Project Architecture
User Input
│
▼
Streamlit App
│
▼
Feature Preparation
│
▼
MinMax Scaling
│
▼
Logistic Regression Model
│
▼
Default Probability
│
▼
Credit Score Calculation
│
▼
Risk Rating Classification


---

# ⚙️ Technologies Used

- Python  
- Streamlit  
- Scikit-learn  
- Pandas  
- NumPy  
- Joblib  

---

# 📂 Project Structure

---

# 🧮 Model Logic

The model predicts the **default probability** using a logistic regression equation:
P(default) = 1 / (1 + e^-(Wx + b))

Where:

- **W** = model coefficients  
- **x** = input features  
- **b** = intercept  

The **credit score** is calculated as:
Credit Score = 300 + (1 - P(default)) × 600

---

# 📊 Credit Score Rating

| Score Range | Rating |
|-------------|-------|
| 300 – 500 | Poor |
| 500 – 650 | Average |
| 650 – 750 | Good |
| 750 – 900 | Excellent |

---

# 📥 Installation

Clone the repository:
git clone https://github.com/ARCHANA201201/ML-Credit-Risk-Model.git

Install dependencies:
pip install -r requirements.txt

Run the Streamlit application:
streamlit run app.py

---

# 📊 Input Features

The model uses financial and behavioral features including:

- Age
- Income
- Loan Amount
- Loan Tenure
- Credit Utilization Ratio
- Delinquency Ratio
- Average Days Past Due
- Number of Open Accounts
- Residence Type
- Loan Purpose
- Loan Type

---

# 📈 Output

The system returns:

- Default Probability
- Credit Score (300–900)
- Credit Rating

Example output:
Default Probability: 0.12
Credit Score: 828
Rating: Excellent

---

# 🌐 Deployment

The application is deployed using **Streamlit Cloud**.



---



