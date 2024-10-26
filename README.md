📊 Business Intelligence for Attrition Prediction and HR Dashboard Development

Project Overview
This project uses Business Intelligence (BI) techniques to analyze employee data for predicting attrition and visualizing insights through an interactive HR dashboard. With this tool, HR teams can proactively monitor employee satisfaction, performance, and turnover trends, enhancing retention strategies.


📑 Table of Contents
1)🔍 Introduction
2)🎯 Project Objectives
3)📁 Project Structure
4)⚙️ Installation
5)🚀 Usage
6)📈 Results
7)🛠️ Technologies Used
8)👥 Contributors



1)🔍 Introduction
Employee attrition impacts organizational productivity and morale. By analyzing key indicators, this project provides data insights to help HR teams reduce turnover and improve employee engagement.

2)🎯 Project Objectives
🔮 Predict Employee Attrition: Identify employees at risk of leaving based on performance, satisfaction, and more.
📊 Develop an HR Dashboard: Visualize metrics such as turnover rates, satisfaction, and performance.
📉 Descriptive Analytics: Aggregate employee data to reveal trends.
📡 Real-Time Insights: Offer actionable data for enhancing engagement and retention.

3)📁 Project Structure
php
Copy code
├── README.md
├── app.py                  # Flask application for prediction
├── attrition_predictor.ipynb  # Jupyter notebook for data preprocessing and model training
├── static/
│   └── images/             # Contains images for the dashboard UI
├── templates/
│   └── form.html           # HTML form for input and prediction
├── attrition_model.pkl     # Trained model for predicting attrition
└── dataset.csv             # Dataset used for training and testing


4)⚙️ Installation
a)📥 Clone the repository:
git clone https://github.com/yourusername/AttritionPredictionBI.git
cd AttritionPredictionBI

b)📦 Install required packages:
pip install -r requirements.txt

c)▶️ Run the Flask Application:
python app.py

d)📊 Access the Dashboard: Open Power BI and connect to the dataset to view the HR dashboard.


5)🚀 Usage
📂 Data Input: Upload employee data via the form on the web app or directly to Power BI.
🔍 Prediction: Enter employee details to predict attrition risk.
📊 Dashboard View: Use the Power BI dashboard to filter and view key metrics like department performance and satisfaction scores.


6)📈 Results
The project successfully provides:
🌐 A web interface for predicting employee attrition.
📊 An interactive Power BI dashboard with real-time insights.
📉 Visualizations to monitor turnover rates, employee satisfaction, and performance metrics.

7)🛠️ Technologies Used
🐍 Python for backend and machine learning.
🌐 Flask for web development.
📊 Power BI for dashboard visualization.
📓 Jupyter Notebook for data preprocessing and model training.

8)👥 Contributors
🧑‍💻 Utkarsha Late

