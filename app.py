import streamlit as st
import seaborn as sns
import numpy as np 
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import re
import hashlib
import joblib
import os
#db
from database import * 
#from RandomForest import df2

from PIL import Image


#pickle_ran=open("random_class.pkl","rb")











#quality dictionary 
type_dict = {"L":0,"M":1,"H":2}
def type_dict_get(val,my_dict):
   for key,value in type_dict.items():
      if val==key:
         return value
      

# loding of model 
def load_model(model_file):
   loaded_model = joblib.load(open(os.path.join(model_file),"rb")) 
   return loaded_model     

def validate_password(password):
    return len(password) > 5

def validate_email(email):
    email_format = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(email_format, email))
 

image = Image.open('PREDICTIVE-MAINTENANCE.jpg')

st.image(image)

menu = ["Home","Login","SignUp"]
    
submenu=["Plot","Prediction"]

choice = st.sidebar.selectbox("Menu",menu)
if choice=="Home" :
        st.divider()
        st.title("What is Maintenance ? ")
        col24,col25=st.columns([2,1],gap="large")
        
        with col24:
         
         st.write("""Maintenance refers to the set of actions and processes undertaken to ensure the proper functioning, upkeep, and preservation of equipment, machinery, infrastructure, or any asset in various fields such as manufacturing, construction, transportation, and facilities management.

Maintenance activities are performed to prevent equipment deterioration, reduce the likelihood of breakdowns, extend the lifespan of assets, and ensure their optimal performance. Maintenance encompasses various tasks, including inspections, repairs, replacements, servicing, cleaning, and adjustments, aimed at preventing faults or failures that could lead to downtime, inefficiencies, or safety hazards.""")
        st.divider()
        
        with col25:
           
           st.write("""



""")
           st.image('what.png',width=230)

        st.title("Why Maintenance is Important ? ")
        col26,col27=st.columns([1,2]) 
        
        with col26:
           st.image('importnace.png')
        with col27:     
         
         st.write("""
1. **Reliability:** Maintenance ensures equipment operates reliably by minimizing unexpected breakdowns and malfunctions.
2. **Downtime Reduction:** Well-maintained equipment experiences fewer interruptions, contributing to increased productivity and consistent operations.
3. **Safety:** Maintenance identifies and mitigates potential safety risks associated with faulty equipment, fostering a secure and conducive work environment.
4. **Cost-Efficiency:** Effective maintenance practices lead to reduced repair costs and longer asset lifespans, resulting in substantial cost savings in the long run.
5. **Optimized Performance:** Regular upkeep enhances operational efficiency, leading to improved output quality and reduced energy consumption.
6. **Regulatory Compliance:** Adhering to maintenance standards ensures compliance with industry regulations, fostering a culture of safety and accountability.
7. **Asset Longevity:** Proper maintenance extends the lifespan of equipment, reducing the frequency of replacements and overall lifecycle costs.

Maintenance plays a pivotal role in ensuring equipment reliability, minimizing downtime, enhancing safety, saving costs, optimizing performance, ensuring compliance, and prolonging asset lifespan in various industries and sectors.""")
        st.divider()


        st.title("Predict and prevent")

        col7,col8=st.columns([3,1],gap="large")

        with col7:
         
         st.write("""
Predictive Analytics enables industrial companies to avoid costly unplanned downtime
in a no-code environment Predictive Analytics helps industrial users identify asset anomalies—weeks or
months before failure. It can forecast time to failure, so maintenance priorities can be set, and it
offers prescriptive advice, such as actions to remediate problems.By harnessing AI-driven insights, 
our platform identifies asset anomalies well in advance—detecting potential failures weeks or even 
months before they occur. This proactive approach enables businesses to forecast time to failure accurately, 
allowing for strategic maintenance planning. Additionally, our platform provides actionable insights and
prescriptive advice, suggesting specific actions to remediate potential issues.We understand the significance
of uninterrupted operations in the industrial sector. With our Predictive Analytics solutions, industrial 
users gain the ability to optimize their maintenance strategies. By leveraging our no-code environment,
companies can effortlessly access crucial insights and make informed decisions to enhance operational 
efficiency. Our platform's user-friendly interface ensures ease of use, empowering teams to take 
proactive steps towards maximizing asset performance and minimizing disruptions.
                      """)
         
        with col8:
           st.image('predictive_icon.png')

        st.divider()

        st.title("Different Types Of Maintainance")
        col9,col10,col11 = st.columns(3,gap="medium")

        with col9:
           st.subheader("Reactive Maintenance")
           st.image('reactive.jpg',width=300)
           st.write("Reactive maintenance refers to a corrective approach where equipment repairs or maintenance actions are carried out in response to failures or breakdowns. It involves fixing machinery or systems after they have malfunctioned, often resulting in unexpected downtime, higher repair costs, and potential production losses. While suitable for minor faults, relying solely on reactive maintenance can lead to inefficiencies and higher risks of equipment failure.")
        
        with col10:
           st.subheader('Preventive Maintenance')
           st.image('preventive.webp',width=300)
           st.write("Preventive maintenance is a proactive maintenance strategy focused on scheduled inspections, routine upkeep, and preemptive repairs to prevent equipment breakdowns or failures. It involves regularly servicing machinery based on predetermined schedules, usage patterns, or manufacturer recommendations. The goal is to identify and address potential issues before they lead to major failures, ensuring equipment reliability, enhancing safety, and reducing unexpected downtime and repair costs.")
           
        with col11:
           st.subheader('Predictive Maintenance')
           st.image('predective.jpg',width=300)
           st.write("Predictive maintenance involves using data-driven insights and advanced analytics to predict when equipment is likely to fail or require maintenance. By continuously monitoring and analyzing equipment conditions using sensors, IoT devices, and data analytics, predictive maintenance identifies patterns, anomalies, and potential failures before they occur. This proactive approach enables timely and targeted maintenance, minimizing downtime, optimizing resources, and extending the lifespan of machinery.")
              
        st.divider()
      
        st.header("Why We Choose Predictive Maintenance ?")
        col20,col21 = st.columns([1,2],gap="large")

        with col20:
           st.write("""
                    
                    
                      



                    
                    
                    """)
           st.image('Proactive-reactive-predictive.jpg')

        with col21:
           st.write("""

1. **Cost Efficiency:** Saves maintenance costs by targeting repairs only when necessary, optimizing resources.

2. **Minimized Downtime:** Reduces unplanned downtime by foreseeing and preventing equipment failures.

3. **Extended Equipment Life:** Early issue detection prevents major breakdowns, prolonging machinery lifespan.

4. **Efficient Planning:** Optimizes maintenance schedules based on real-time equipment data, enhancing efficiency.

5. **Enhanced Safety:** Proactive maintenance reduces risks from malfunctioning machinery, ensuring workplace safety.

6. **Data-Driven Insights:** Utilizes analytics and IoT for actionable insights, aiding informed decision-making.

7. **Competitive Edge:** Adoption of predictive maintenance offers a competitive advantage by ensuring reliability and innovation.

""")   

        st.divider()
        
        st.title("Predictive Maintenance Success Stories")
        st.subheader("Omron Automation")
        video_file = open('omron.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes) 
        st.write("""Whether dealing with legacy machinery or modern industrial equipment, proper maintenance remains crucial to maximize operational lifespan. Aging equipment often stands as a primary factor contributing to unplanned downtime, causing manufacturers to grapple with escalating maintenance costs. For companies facing these challenges, adopting a new maintenance strategy becomes imperative.

Traditional preventive maintenance methods typically rely on scheduled intervals, necessitating skilled personnel to execute time-consuming manual inspections and repairs. Despite these efforts, issues occurring between inspection dates might evade detection, leading to potential equipment failures and premature replacements. This approach often proves reactive rather than proactive in addressing critical equipment health.

In contrast, predictive maintenance presents a proactive strategy centered on the continuous assessment of equipment conditions. By harnessing a real-time monitoring system, this approach leverages cutting-edge technology such as IoT sensors and data analytics. Through this continuous evaluation, predictive maintenance aims to preemptively identify potential component failures. By predicting these issues before they manifest into critical problems, companies can significantly reduce instances of unplanned downtime and circumvent costly repairs.

The essence of predictive maintenance lies in its ability to transform maintenance practices from reactive and time-based to proactive and data-driven. It empowers businesses to shift from merely responding to breakdowns to foreseeing and mitigating potential failures before they disrupt operations. Consequently, this proactive approach not only increases operational efficiency but also extends the operational life of machinery, leading to substantial cost savings and improved productivity.""")
        

        st.subheader("C3 AI Reliability")
        video_file1 = open('C3reliablity.mp4', 'rb')
        video_bytes1 = video_file1.read()
        st.video(video_bytes1) 
        st.write("""C3 AI Reliability stands as a groundbreaking AI-powered predictive maintenance application, specifically designed to empower enterprises in enhancing asset uptime and operational productivity. This innovative application serves as a comprehensive solution that harmonizes operational data originating from diverse sources within an enterprise ecosystem.

At its core, C3 AI Reliability harnesses the power of cutting-edge technologies, integrating advanced machine learning, natural language processing (NLP), and generative AI techniques. This amalgamation of sophisticated technologies enables the system to delve deep into the operational data, identifying potential equipment risks well in advance.

One of the key strengths of C3 AI Reliability lies in its ability to distill complex data into digestible and actionable insights. Through the utilization of advanced analytics and NLP capabilities, the application translates intricate data patterns and anomalies into concise, easily understandable summaries. These insightful summaries offer a clear depiction of potential risks and crucial performance indicators.

Moreover, C3 AI Reliability goes beyond mere identification of risks by leveraging generative AI techniques to generate actionable recommendations. These recommendations are tailored to assist maintenance teams and operational staff in implementing preemptive measures. By providing prescriptive actions, the application aids in mitigating potential downtime scenarios and minimizing maintenance costs.""")



        st.subheader("Tetra-Pak")
        video_file2 = open('tetra-pak-predictive-maintenance.mp4', 'rb')
        video_bytes2 = video_file2.read()
        st.video(video_bytes2) 
        st.write("""Tetra Pak's visionary objective revolves around delivering an all-encompassing Predictive Maintenance offer, a holistic solution that encompasses not only the Separator but also critical additional components situated at our esteemed customers' sites.

Our commitment to reliability and operational excellence propels us to pioneer a paradigm shift in maintenance strategies. Tetra Pak aims to transcend the conventional and reactive maintenance approaches by proactively predicting potential failures before they manifest, thus revolutionizing the reliability landscape for our customers.

Through our robust Predictive Maintenance offering, we strive to elevate operational efficiency by preemptively identifying and addressing impending equipment failures. By leveraging advanced analytics, machine learning algorithms, and real-time data insights, Tetra Pak empowers its customers to optimize equipment uptime and performance.

The transformative power of our Predictive Maintenance solution lies in its ability to not only increase equipment uptime but also curtail waste generation and minimize unforeseen stoppages. By forecasting potential failures and implementing proactive maintenance measures, Tetra Pak mitigates the risks associated with unscheduled downtimes, ensuring uninterrupted operations and enhancing productivity.

This innovative Predictive Maintenance framework acts as a strategic shield against operational disruptions, reducing the likelihood of unscheduled stoppages, production losses, and associated financial impacts. Tetra Pak's commitment to predictive reliability underscores our dedication to providing unparalleled support and efficiency to our valued customers' operations.""")
     
        st.divider()

        st.title("Industry We are in :-")
        st.subheader("Manufacturing & Production Plants")

        st.divider()
        st.title("Why Predictive Maintenance is important in Manufacturing & Production Plants")
        col22,col23=st.columns([2,1],gap="large")
        with col22:
           st.write("""

1. **Reduced Downtime:** Predictive maintenance averts unexpected breakdowns by detecting issues early, allowing planned repairs and ensuring uninterrupted production schedules. It guarantees continuous operations, minimizing downtime-related losses.

2. **Optimized Performance:** Constant equipment monitoring maintains machinery at peak performance, bolstering overall productivity and operational efficiency.

3. **Cost Efficiency:** Proactive maintenance mitigates unnecessary repair expenses, cutting down maintenance costs, and avoiding premature replacements, leading to substantial savings.

4. **Extended Equipment Lifespan:** Timely issue detection prolongs machinery life, reducing the frequency of costly equipment replacements and ensuring assets perform optimally for longer periods.

5. **Enhanced Safety:** Anticipating and addressing potential failures ensures reliable machinery operations, mitigating risks of accidents or malfunctions, fostering a safer work environment.

6. **Improved Resource Planning:** Insights derived from predictive maintenance aid in precise resource allocation, facilitating better inventory management and streamlined operational planning, optimizing overall resource utilization.

In essence, predictive maintenance revolutionizes manufacturing and production plants, ensuring seamless operations, cost-effectiveness, and safety by proactively managing maintenance needs and optimizing equipment performance.""")


        with col23:
           st.write("""
                    
                    

                    
                    """)
           st.image('predictivemain.png')

        st.divider()

        st.title(" What is SMOTEomek ?")
        col32,col33=st.columns([1,2],gap="large")
        with col32:
           st.write("""
           
           
           
           
           
           
           
                    """)
           st.image('smotet.png')

        with col33:
           st.write("""SMOTE (Synthetic Minority Over-sampling Technique) and Tomek Links are two distinct techniques used in dealing with imbalanced datasets in machine learning. When combined, they form a hybrid method known as SMOTE-Tomek.

1. **SMOTE (Synthetic Minority Over-sampling Technique):** SMOTE is used to handle imbalanced datasets by oversampling the minority class. It works by generating synthetic samples for the minority class using interpolation between existing instances. By creating new synthetic instances, SMOTE helps balance the class distribution, which can improve the performance of machine learning models, especially in scenarios where one class is significantly underrepresented.

2. **Tomek Links:** Tomek Links are pairs of instances—one from the majority class and one from the minority class—that are close to each other but belong to different classes. These instances are considered ambiguous or noisy. The Tomek Links algorithm removes these pairs, thereby emphasizing the boundary between classes and potentially making the decision boundary clearer for classification algorithms.

3. **SMOTE-Tomek:** SMOTE-Tomek is a hybrid approach that combines the strengths of both SMOTE and Tomek Links. First, SMOTE generates synthetic samples for the minority class to balance the dataset. Then, Tomek Links are used to remove overlapping or ambiguous instances near the class boundaries. This combined method aims to enhance the quality of oversampling by addressing potential noisy or borderline cases created by SMOTE, ultimately improving the classifier's performance.

SMOTE-Tomek is especially useful in scenarios where there is a severe imbalance between classes in the dataset, helping to improve the generalization and robustness of machine learning models by balancing the data distribution and refining the class boundaries.""")   
        
        st.divider()
        
        st.title("About The Dataset")

        col30,col31 = st.columns([2,1],gap="large")
        with col30:
         st.write(""" The dataset consists of 10,000 data points stored as rows, each containing 14 features in columns:

1. **UID:** A unique identifier ranging from 1 to 10,000.
2. **ProductID:** Represents product quality variants labeled as L (low), M (medium), or H (high) with variant-specific serial numbers.
3. **Air Temperature [K]:** Generated via a random walk process, later normalized to a standard deviation of 2 K around 300 K.
4. **Process Temperature [K]:** Generated via a random walk process, normalized to a standard deviation of 1 K, and added to the air temperature plus 10 K.
5. **Rotational Speed [rpm]:** Calculated based on power of 2860 W, overlaid with normally distributed noise.
6. **Torque [Nm]:** Normally distributed torque values around 40 Nm with a standard deviation of 10 Nm and no negative values.
7. **Tool Wear [min]:** Tool wear duration affected by quality variants (H/M/L), adding 5/3/2 minutes respectively to the used tool in the process.
8. **Machine Failure Label:** Indicates if the machine failed in that particular data point for any of the specified failure modes.

Importantly, this dataset features two targets: 
1. **Failure or Not:** Binary classification indicating whether a failure occurred.
2. **Failure Type:** Classifies the type of failure that occurred.

""")
        st.divider()
        
        with col31:
           st.image('data.png')




elif choice == "Login":
        email = st.sidebar.text_input("Email")
        username = st.sidebar.text_input("Username")
        Password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            
          #  create_usertable()
            create_usertable()
            result = login_user(email,username,Password)
            #if Password == "12345":
            if result:
                st.success("Welcome {}".format(username))
                activity = st.selectbox("Activity",submenu)
                if activity=="Plot" :
                    st.header("Data Visualization")
            
                    #shocasing of database
                    with st.container(): 
                     df = pd.read_csv("predictive_maintenance.csv")
                     st.subheader("Database Used")
                     st.dataframe(df)

                    #total failure counts 
                    with st.container():
                     failure_counts=df['Failure Type'].value_counts()
                     st.subheader("Count of the different Failure Types are shown below : ")
                     st.write(failure_counts)


                    st.subheader("Different Relational Plots between the key variables.")
                    col1, col2, col3 = st.columns(3)

                    with col1:
                     st.text("""Plot between Air and Process temperature where
Hue is the Failure Type""")
                     plot_type = sns.relplot(x="Air temperature [K]", y="Process temperature [K]", hue="Failure Type",size="Failure Type", sizes=(120, 10),data=df)
                     st.pyplot(plot_type)

                    with col2:
                     st.text("""Plot between Rotational speed and Torque where 
Hue is the Failure Type""")
                     plot_type1 = sns.relplot(x="Torque [Nm]", y="Rotational speed [rpm]", hue="Failure Type",size="Failure Type", sizes=(100, 5),data=df)
                     st.pyplot(plot_type1)

                    with col3:
                      st.text("""Plot between Rotational Speed and Tool Wear where
Hue is the Failure Type""")
                      plot_type2 = sns.relplot(x="Tool wear [min]", y="Rotational speed [rpm]",hue="Failure Type", size="Failure Type",sizes=(80, 5),data=df)
                      st.pyplot(plot_type2)
                   
                    #heatmap
                    col4,col5=st.columns([3,1])
                    with col4:
                     img_wid=1000   
                     st.subheader("Correlation Heatmap")
                     fig, ax = plt.subplots(figsize=(img_wid/100, 15))
                     sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)

# Save the figure to a temporary file
                     fig.savefig('heatmap.png')

# Display the saved figure in the Streamlit app
                    st.image('heatmap.png', width=1000, output_format='PNG', channels='BGR')
                    
                    st.subheader("Area Chart")
                    if st.checkbox("Click here if you want to built a area chart among features."):
                       all_columns = df.columns.to_list()
                       feat_choices = st.multiselect("Choose a feature : ",all_columns)
                       new_df = df[feat_choices]
                       st.area_chart(new_df)


                  

                elif activity=="Prediction":
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
                    if st.button("Predict"):
                      if model_choice=="Random Forest" :
                       loaded_model=load_model('RandomForest.py')
                       prediction = loaded_model.predict(single_data)
                       st.write(prediction)
                    #Model of ml

                    
            else:
             st.warning("Incorrect Username OR Password !!! ")  
             st.info("""Please singup if you havent. 
                     OR 
                     Check weather your username and password are correct.""")
             








elif choice == "SignUp":
     New_email = st.sidebar.text_input("Email")
     New_Username=st.sidebar.text_input("Username")
     New_Password=st.sidebar.text_input("Password",type='password')
     
     Confirm_Password=st.sidebar.text_input("Confirm Password",type='password')
     if New_Password==Confirm_Password:
          st.success("Pasword Matched")
     else:
         st.warning("Password no the same, re-enter the password")

     if st.button("Submit"):
         create_usertable()

         if not validate_password(New_Password):
            st.error('Password should be more than 5 characters')
            if not validate_email(New_email):
              st.error('Enter a valid email address')
                   
         else:
              
              if singup(New_email,New_Username,New_Password):
          
                add_userdata(New_email,New_Username,New_Password)
                st.success("You have successfully created a new account")  
                st.info("Login to get Started")
  
              else:
               st.info("Account Alredy exsists.") 