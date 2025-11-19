⚡ EV Range Predictor

A Machine Learning powered web application that predicts the driving range of Electric Vehicles (EVs) based on their specifications. This project also features an AI-powered Chatbot (using Google Gemini) to answer user queries about EV technology, battery health, and charging habits.

Developed by: Dhanush M Aradhyamath

Project: AICTE Internship

🚀 Features

🔋 ML-Based Range Prediction: Accurately estimates driving range using a trained Random Forest model.

🤖 AI Chatbot: Integrated with Google Gemini 2.5 Pro to answer EV-related questions.

📊 Interactive UI: User-friendly interface built with Streamlit, featuring sliders and visual metrics.

⚡ Efficiency Metrics: Calculates driving hours based on average speeds.

🛠️ Tech Stack

Python (Core Logic)

Streamlit (Frontend/UI)

Scikit-Learn (Machine Learning Model)

Google Generative AI (Gemini Chatbot)

Pandas & NumPy (Data Processing)

📂 Project Structure

EV-Range-Estimator-Project/
├── app.py # Main Streamlit application
├── ev_range_model.pkl # Trained Machine Learning Model
├── electric_vehicles_spec_2025.csv.csv # Dataset used for training
├── requirements.txt # Python dependencies
├── .env # API Keys (Not uploaded to GitHub)
├── .gitignore # Files to ignore (like .env)
└── README.md # Project Documentation

⚙️ Installation & Setup

Follow these steps to run the project locally:

1. Clone the Repository

git clone [https://github.com/Dhanush0426/EV-Range-Estimator-Project.git](https://github.com/Dhanush0426/EV-Range-Estimator-Project.git)
cd EV-Range-Estimator-Project

2. Install Dependencies

Make sure you have Python installed, then run:

pip install -r requirements.txt

3. Set up Environment Variables

Create a file named .env in the root folder and add your Google Gemini API key:

GEMINI_API_KEY=your_actual_api_key_here

4. Run the App

streamlit run app.py

🎯 How to Use

Range Predictor: Go to the "Range Predictor" tab, enter your EV's Battery Capacity (kWh), Efficiency (Wh/km), and Top Speed. Click Predict to see the estimated range.

Chatbot: Switch to the "Chatbot" tab and ask questions like "How can I improve my battery life?" or "Does fast charging hurt my battery?".

About: View project details and developer information.

⭐ Star this repository if you find it useful!
