import joblib;

model_t = joblib.load('./model.joblib')
X_test = ...
Y_test = ...

y_pred_t = model_t.predict(X_test)