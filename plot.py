

def result():
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