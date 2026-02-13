# Resume_Parser
Resume Parser using Streamlit Framework

A Streamlit web app to parse resumes and classify them using KNN and SVM.

## Features
- Upload resume and parse details
- KNN model for classification
- Saves uploaded resumes locally (optional)

## Project Structure
- `app.py` : Main Streamlit app
- `details.py` : Resume parsing functions
- `model.joblib` : KNN model and SVM Model
- `dataset/` : Training data
- `requirements.txt` : Python dependencies

## How to Run
1. Install dependencies:  
   `pip install -r requirements.txt`
2. Run the app:  
   `streamlit run app.py`
