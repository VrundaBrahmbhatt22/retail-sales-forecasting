# 🛍️ Retail Sales Forecasting with XGBoost + Streamlit

This project predicts weekly Walmart sales using machine learning techniques. It covers the full data science pipeline: data preprocessing, feature engineering, model building with XGBoost, evaluation, and a Streamlit-based web app for real-time forecasting. The final model achieved **98.46% R² score** on the test set.

---

## 📌 Problem Statement

Walmart wants to forecast sales for each store and department to optimize inventory and improve profitability. This project uses historical sales and economic data to build a predictive model capable of estimating future weekly sales.

---

## 📊 Features of This Project

- ✅ End-to-end Data Science workflow
- 💡 Feature engineering (lag variables, rolling averages, markdowns, etc.)
- 🧠 Model trained using XGBoost with hyperparameter tuning
- 🧪 Evaluated using R², MAE, and RMSE
- 🌐 Interactive Streamlit app for predictions
- 📦 Model saved and loaded using Pickle
- 🔄 Clean codebase, modular structure, virtual environment support

---

## 🧪 Model Performance

| Metric    | Value   |
|-----------|---------|
| R² Score  | 98.46%  |
| MAE       | 1321.16 |
| RMSE      | 2707.77 |

---

## 📁 Project Structure

retail-sales-forecasting/
├── app.py # Streamlit app script
├── model/
│ └── xgb_sales_model.pkl # Trained XGBoost model
├── notebooks/ # Jupyter notebooks (EDA, training, evaluation)
├── data/ # Raw datasets (optional)
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md # Project overview and usage

yaml
Copy
Edit

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/VrundaBrahmbhatt22/retail-sales-forecasting.git
cd retail-sales-forecasting
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate        # Windows
# OR
source venv/bin/activate     # macOS/Linux
3. Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Streamlit app
bash
Copy
Edit
streamlit run app.py
📥 Input Features
Store Number

Department Number

Store Type (A/B/C)

Store Size

IsHoliday

Temperature

Fuel Price

CPI

Unemployment Rate

MarkDown1–5

Lag1 (previous week’s sales)

Rolling Average (past 4 weeks)

Year, Month, Week

📚 Dataset Source
Walmart Sales Forecasting Dataset
Used from Kaggle or public academic source (2010–2012 data)

👩‍💻 Author
Vrunda Brahmbhatt
📧 Email: yourname@email.com
🌐 GitHub: VrundaBrahmbhatt22
🔗 LinkedIn: Your LinkedIn Profile

📌 License
This project is open source and free to use under the MIT License.

yaml
Copy
Edit

---

### ✅ Final Step

1. Paste this cleaned version into your `README.md`
2. Save it
3. Push it:

```bash
git add README.md
git commit -m "Fix README formatting and structure"
git push