import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.title("Iris prediction App")
st.markdown("""
# *This App predicts the iris flower type*
""")

st.sidebar.header('User Input Parameters')


def UserInputfeatures():
    sepal_length = st.sidebar.slider('Sepal length', 4.2, 7.7, 5.2)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.5)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.3)

    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_width,
        "petal_width": petal_width
    }

    features = pd.DataFrame(data, index=[0])
    return features


df = UserInputfeatures()

st.subheader("""User Input Parameters""")
st.write(df)

iris = datasets.load_iris()

x= iris.data
y= iris.target

clf = RandomForestClassifier()
clf.fit(x,y)
prediction = clf.predict(df)
prediction_prob = clf.predict_proba(df)

st.subheader("""
Class labels and their corresponding index
""")

st.write(iris.target_names)

st.subheader('prediction')
st.write(iris.target_names[prediction])
# st.write(prediction)

st.subheader('Prediction probability')
st.write(prediction_prob)