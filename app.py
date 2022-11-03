import pickle
from flask import Flask, jsonify

# function to predict result
def model_prediction(usr_txt):
    result = {}
    with open('parameters.pickle', "rb") as f:
        Le, cv = pickle.load(f)
    with open('classifier.pickle', "rb") as m:
        clf = pickle.load(m)
    cv_text = cv.transform([usr_txt]).toarray()
    pred_res = clf.predict(cv_text)
    result['pred_label'] = Le.inverse_transform(pred_res)[0]
    result['confidence'] = {'ham':clf.predict_proba(cv_text)[0][0],'spam':clf.predict_proba(cv_text)[0][1]}
    result['input_text'] = usr_txt
    return jsonify(pred_label= Le.inverse_transform(pred_res)[0],
                   confidence= {'ham':clf.predict_proba(cv_text)[0][0],'spam':clf.predict_proba(cv_text)[0][1]},
                   input_text= usr_txt)

# flask implementation
app = Flask(__name__)
@app.route("/")

def home():
     return '''Created & Distributed by Pykit: https://pykit.org/ OR https://ai-marketplace.pykit.org/'''
    
@app.route("/smsPredict/<string:txt>")
def smsPredict(txt):
    userText = txt
    return model_prediction(userText)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)