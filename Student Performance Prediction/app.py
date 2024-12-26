# Note : this is .py file not .ipynb 
import streamlit as st #to download write %pip or pip install streamlit  
import joblib # to download write %pip or pip install joblib 

# Header of the Webapp
st.header("Student Performance Prediction")

#loading the saved model and storing it in model variable
model=joblib.load("Saved_model.joblib")

# Our predict Function
def predict(avg_marks):
    if ((avg_marks>100) | (avg_marks<0)):
        st.error("Plz Enter Between 0-100")
        return None # return none if value is invalid
    else:
        result=model.predict([[avg_marks]])
        return result #return prediction if value is valid

# st.num_input to get input in num and storing that num in input_score variable
input_score=st.number_input("Enter Average score",min_value=0.0,max_value=101.0) 

#st.button to get button click and storing that button click in button variable
if st.button("predict"): # if clicked then this if condition runs
    result=predict(input_score)
    if result is not None:
        if result == 0:
            # st.success gives a green display on web app with this statement that looks good we can also use st.write instead of this
            st.success("The predicted grade is: A") 
        elif result == 1:
            st.success("The predicted grade is: B")
        elif result == 2:
            st.success("The predicted grade is:C")
        elif result == 3:
            st.success("The predicted grade is:D")
        elif result == 4:
            st.success("The predicted grade is:E")
        else:
            st.success("The predicted grade is:F")
    else:
        st.error("No value to predict") # st.error gives a red display along the text writen in braces
else:
    st.write("Please enter your score") # using st.write gives a simple display

