import streamlit as st
import pickle


st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:16px !important;
}
</style>
""", unsafe_allow_html=True)

#useful variables
global loaded_model # declare a global variable to avoid unnecessary reloads
prediction_mapper={0:'Iris-Setosa',1:'Iris-Versicolour',2:'Iris-Virginica'}


st.title('IRIS Playground with Streamlit')
html_string = "<a href='https://en.wikipedia.org/wiki/Iris_flower_data_set' target='blank'>Know More About IRIS Data Set</a>"
st.markdown(html_string, unsafe_allow_html=True)

@st.cache_data
def load_model():
    try:
        loaded_model = pickle.load(open('./model/iris_model.sav', 'rb'))
        return loaded_model
    except Exception as e:
        return f"Exception Occured {str(e)}"

model_Load_state = st.text('Loading data...')
# loaded_model=load_model() # load the model here 
# model_Load_state.text("Model Loaded ! (using st.cache)")

@st.cache_data
def prediction(loaded_model,array_of_features):    
    if loaded_model:# only if the model is there        
        prediction_result=loaded_model.predict(array_of_features)
        try:
            species_type=prediction_mapper.get(prediction_result[0])
            return species_type
        except KeyError:
            species_type="Could Not Be Determined"
            return species_type

@st.cache_data
def load_model_and_predict(array_of_features):
    try:
        loaded_model = pickle.load(open('./model/iris_model.sav', 'rb'))
        prediction_result=loaded_model.predict(array_of_features)
        try:
            species_type=prediction_mapper.get(prediction_result[0])
            return species_type
        except KeyError:
            species_type="Could Not Be Determined"
            return species_type
    except Exception as e:
        return f"Exception Occured {str(e)}"

model_Load_state = st.text('Loading data...')
loaded_model=load_model() # load the model here 
model_Load_state.text("Model Loaded ! (using st.cache)")


st.container()
col1, col2 , col3 , col4 = st.columns(4)


sepallength=col1.number_input('Sepal Length')
sepalwidth=col2.number_input('Sepal Width')
petallength=col3.number_input('Petal Length')
petalwidth=col4.number_input('Petal Width')


result=st.button('Predict Species')

if result:
    model_Load_state = st.text('Predicting Species...')
    model_Load_state.text("Prediction Complete ! (using st.cache)")
    predicted_species=load_model_and_predict([[sepallength,sepalwidth,petallength,petalwidth]])      
    
    col5, col6 = st.columns(2)
    col5.subheader("Your Inputs")
    col5.write({
                "SepalLength":sepallength,
                "SepalWidth":sepalwidth,
                "PetalLength":petallength,
                "PetalWidth":petalwidth                
                })
    col6.subheader(f"Predicted Species : {predicted_species}")
    if predicted_species=='Iris-Setosa':
        col6.image('./img/setosa.jpeg')
    elif predicted_species=='Iris-Versicolour':
        col6.image('./img/versicolor.jpeg')
    elif predicted_species=='Iris-Virginica':
        col6.image('./img/virginica.jpeg')
    else:
        col6.write("Something went wrong. You may want to tweak your inputs")


    
    
    #Do something funny
    #st.balloons()   


    






