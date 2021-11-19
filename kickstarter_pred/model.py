import joblib

def predictor(df):
    model = joblib.load('kickstarter_pred/prediction_model.pkl')

    prediction = model.predict(df)[0]
    success_proba = model.predict_proba(df)[0][1]

    return prediction, success_proba