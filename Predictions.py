import streamlit as st 
type_dict = {"L":0,"M":1,"H":2}
def type_dict_get(val,my_dict):
   for key,value in type_dict.items():
      if val==key:
         return value




st.title("Predective Analytics")    
st.subheader("1.) Machine Type/Quality (L = Low, M = Medium and H = High qualities)")
type = st.radio("choose according to your machine quality :- ",tuple(type_dict.keys())) 
st.subheader("2.) Air Temprature (in Kelvin)")
st.info("The maximum and the minimum values of air temprature in the dataset are 304.40, 295.30")
air_temp = st.number_input("Enter the Air Temprature :-")
st.subheader("3.) Process Temprature (in Kelvin)")
st.info("The maximum and the minimum values of Process temprature in the dataset are 313.80, 305.70 ")
process_temp = st.number_input("Enter the Process Temprature :-")
st.subheader("4.) Rotational speed (in rotations per miniute (rpm))")
st.info("The maximum and the minimum values of Rotational speed in the dataset are 2886.00, 1168.00. ")
rotation = st.number_input("Enter the Rotational speed :-")
st.subheader("5.)Torque  (in Newton per meter(Nm))")
st.info("The maximum and the minimum values of Torque in the dataset are 76.600, 35.469573. ")
torque = st.number_input("Enter Torque:-")
st.subheader("6.)Tool wear  (in miniutes (min))")
st.info("The maximum and the minimum values of Tool wear in the dataset are 253.00, 0.00. ")
tool_wear = st.number_input("Enter Tool wear:-")
                    
feature_list = [type_dict_get(type,type_dict),air_temp,process_temp,rotation,torque,tool_wear]
st.write(feature_list)
pretty_result = {"type":type,"Air Temprature":air_temp,"Process Temprature":process_temp,"Rotational Speed":rotation,"Torque":torque,"Tool Wear":tool_wear}
st.json(pretty_result)
single_data = np.array(feature_list).reshape(1,-1)
model_choice = st.selectbox("Select Model",["Random Forest","LightGBM","XGBClassifier","Catboost","OneVsRestClassifier","OneVsOneClassifier"])