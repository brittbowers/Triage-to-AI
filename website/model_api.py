import pickle
import numpy as np


with open("model.pkl", "rb") as read_file:
    lr_model = pickle.load(read_file)

feature_names = lr_model.feature_names

def get_features():
    feature_dict = dict((feature,0) for feature in lr_model.feature_names)
    return feature_dict
def make_prediction(feature_dict):
    """
    Input:
    feature_dict: a dictionary of the form {"feature_name": "value"}

    Function makes sure the features are fed to the model in the same order the
    model expects them.

    Output:
    Returns (x_inputs, probs) where
      x_inputs: a list of feature values in the order they appear in the model
      probs: a list of dictionaries with keys 'name', 'prob'
    """
    x_input = [
        float(feature_dict[name]) for name in lr_model.feature_names
    ]

    pred_probs = lr_model.predict_proba([x_input]).flat

    # 'name' refers to the feature target name
    predictions = [{'name': lr_model.target_names[index], 'prob': pred_probs[index]}
             for index in np.argsort(pred_probs)[::-1]]
    pred = ''
    if predictions[0]['name'] == 'Admitted':
        if predictions[0]['prob'] > predictions[1]['prob']:
            pred = 'Admitted'
    if predictions[0]['name'] == 'Not Admitted':
        if predictions[0]['prob'] > predictions[1]['prob']:
            pred = 'Not Admitted'

    return (predictions, pred)

# This section checks that the prediction code runs properly
# To run, type "python predictor_api.py" in the terminal.
#
# The if __name__='__main__' section ensures this code only runs
# when running this file; it doesn't run when importing
if __name__ == '__main__':
    from pprint import pprint
    print("Checking to see what setting all params to 0 predicts")
    features = {f: '0' for f in feature_names}
    print('Features are')
    pprint(features)

    predictions, pred = make_prediction(features)
    print(f'Input values: {x_input}')
    print('Output probabilities')
    pprint(probs)
