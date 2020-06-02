# Triage to AI

The objective of this project is to predict whether a patients will be admitted to the hospital or not based on vitals taken upon entering the ER. 

**Dataset:**

- Data comes from a [Korean Triage Study](https://figshare.com/articles/Triage_accuracy_and_causes_of_mistriage_using_the_Korean_Triage_and_Acuity_Scale/9779267/1)

**Notebooks:**

- cleaning_eda: Going through each feature in the study, filling in nulls, and visualizing distributions <br/>
- features: Feature engineering by binning some categoricals and transforming features with skewed distributions <br/>
- models: Exprimenting with different classification models and assessing them using Fbeta score

**Write Up:**

I published a blog detailing this project to Towards Data Science. It can be found [here](https://towardsdatascience.com/triage-to-ai-a-machine-learning-approach-to-hospital-admissions-classification-7d3a8d5df631)

**Conclusions:**

Logistic regression represents the best predictions keeping in mind simplicity and interpretability. An app was deployed to allow for real-time prediction [here](https://hospital-admissions-predictor.herokuapp.com/)

- website: Scripts for building and deploying heroku app and pickled model are stored here