import flask
from flask import request
from flask import jsonify
from model_api import make_prediction, feature_names, get_features

app = flask.Flask(__name__)

@app.route("/")
def home():
    try:
        days = request.args.get('days', 0, type=str)
        patients = request.args.get('patients_day', 0, type = str)
        result = float(days)*float(patients)*5.34
    except:
        result = 0
    #as_json = json.dumps(fired_button)
    #button = json.loads(as_json)
    #print(button)
    #if button == "by_day":
    #    return jsonify(result = 5.48*30)
    #if button == "by_month":
    #    return jsonify(result = 5.48*30*31)
    #if button == "by_year":
    #    return jsonify(result = 5.48*30*365)
    #if button == "city":
    #    return jsonify(result = 5.48*360*365)
    return flask.render_template('home.html', result = result) #result = result, fired_button = fired_button)

@app.route('/background_process')
def background_process():
    try:
        lang = request.args.get('proglang', 0, type=str)
        return (jsonify(result = 'Wow'), lang)
        #if lang.lower() == 'python':
        #    return jsonify(result='You are wise')
        #else:
        #    return jsonify(result='Try again.')
    except Exception as e:
        return str(e)


@app.route("/predictor", methods=["POST", "GET"])
def predictor():
    feature_dict = get_features()
    if request.method == "POST":
        sex = request.form["sex"]
        age = request.form["age"]
        alert = request.form["alert"]
        injury = request.form["injury"]
        sbp = request.form["sbp"]
        dbp = request.form["dbp"]
        hr = request.form["hr"]
        rr = request.form["rr"]
        bt = request.form["bt"]
        pain = request.form["pain"]
        if sex == "male":
            feature_dict['sex'] = 1
        if alert == "no":
            feature_dict['not_alert'] = 1
        if injury == "yes":
            feature_dict['injury'] = 1
        if age == "old":
            feature_dict['old'] = 1
        if age == "mid_age":
            feature_dict['middle_age'] = 1
        if sbp == "norm":
            feature_dict['norm_sbp'] = 1
        if sbp == "high":
            feature_dict["high_sbp"] = 1
        if dbp == "norm":
            feature_dict['norm_dbp'] = 1
        if dbp == "high":
            feature_dict["high_dbp"] = 1
        if hr == "norm":
            feature_dict['norm_hr'] = 1
        if hr == "high":
            feature_dict["high_hr"] = 1
        if rr == "high":
            feature_dict["high_rr"] = 1
        if bt == "high":
            feature_dict["high_bt"] = 1
        if pain == "med":
            feature_dict["med_pain"] = 1
        if pain == "high":
            feature_dict["high_pain"] = 1
    predictions, pred = make_prediction(feature_dict)
    print(predictions)
    print(pred)
    return flask.render_template('predictor.html', prediction=predictions, pred = pred)

# @app.route("/test")
# def test():
#     return flask.render_template('test.html')
# # Start the server, continuously listen to requests.
# # We'll have a running web app!
#
# # For local development:
app.run(debug=True)

# For public web serving:
# app.run(host='0.0.0.0')
