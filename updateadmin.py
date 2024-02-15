import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from st_aggrid import AgGrid



def app():
    import streamlit as st

    df=pd.read_excel("letshego.xlsx")
    
    st.subheader("Automated Call Distribution Platform")
    
    df_data = df[df["Customer_Contacted"].isnull()]
    first_null_index = df[df["Customer_Contacted"].isnull()].index.min() 

# Check if there are any null values
    if  pd.notna(first_null_index):
        row_values = df.loc[first_null_index]
        option_form = st.form("Contact Customer")
        # Display row values in text boxes
        col1, col2, col3= option_form.columns((3))
        with col1:
           Customer_Name = st.text_input(label="Customer Name", value=row_values["Customer_Name"])
           Mobile = st.text_input(label="Mobile", value=str(row_values["Mobile"]))
           #Date_Contacted = st.text_input(label="Date Contacted", value=row_values["Date_Contacted"])
           Date_Contacted=st.text_input(label="Date Contacted",value=datetime.now().strftime("%d-%m-%y"))
    
        with col2:
           Account_no = st.text_input(label="Account no", value=str(row_values["Account_no"]))
           Campaign_Type= st.text_input(label="Campaign Type", value=str(row_values["Campaign_Type"]))
           Customer_Contacted = st.selectbox(label="Customer Contacted",
                                              options=["","Yes", "Customer not available"],
                                              index=0 if row_values["Customer_Contacted"] == "Yes" else 1)

        with col3:
           Customer_No = st.text_input(label="Customer No", value=str(row_values["Customer_No"]))
           Eligible_Amount= st.text_input(label="Eligible Amount", value=str(row_values["Eligible_Amount"]))
           Customer_Disposition = st.selectbox(label="Customer Disposition",
                                                options=["Customer Not available", "Not Interested", "Interested",
                                                         "Deal Closed", "Call Back"],
                                                index=0 if row_values["Customer_Disposition"] == "Customer Not available" else 1)

        col1, col2, col3, col4, col5,col6= option_form.columns((6)) 
        with col1:
           Tellisale_Agent = st.text_input(label="Tellisale Agent", value=row_values["Tellisale_Agent"])
        with col2:
           Country = st.text_input(label="Country", value=row_values["Country"])
        with col3:
           Date_Camp = st.text_input(label="Date Camp", value=row_values["Date_Camp"])
        with col4:
           Customer_Qualification = st.text_input(label="Cust Qualification", value=row_values["Customer_Qualification"])
        with col5:
           Topup_Winback = st.text_input(label="Topup Winback", value=row_values["Topup_Winback"])
        with col6:
           Cust_ID = st.text_input(label="Cust ID", value=str(row_values["Cust_ID"]))
           
        
        col1, col2, col3=option_form.columns((5,1,1))
        with col1:
           Agent_Feedback = st.text_input(label="Comments", value="", )

        with col2:
            update_button = option_form.form_submit_button(label="Update")

        with col3:
           next_button = option_form.form_submit_button(label="Next")


        if update_button:
            
            current_date = datetime.now().strftime("%d-%m-%y")
            Date_Contacted = current_date
            df.drop(first_null_index, inplace=True)

            # Creating updated data entry
            updated_prospect_data = pd.DataFrame([{
                "Tellisale_Agent": Tellisale_Agent,
                "Country": Country,
                "Account_no": Account_no,
                "Customer_No": Customer_No,
                "Mobile": Mobile,
                "Customer_Name": Customer_Name,
                "Cust_ID": Cust_ID,
                "Date_Camp": Date_Camp,
                "Customer_Qualification": Customer_Qualification,
                "Topup_Winback": Topup_Winback,
                "Customer_Contacted": Customer_Contacted,
                "Date_Contacted": Date_Contacted,
                "Customer_Disposition": Customer_Disposition,
                "Agent_Feedback": Agent_Feedback,
                "Campaign_Type": Campaign_Type,
                "Eligible_Amount": Eligible_Amount

            }])

            # Adding updated data to the DataFrame
            df = pd.concat([df, updated_prospect_data], ignore_index=True)
            df.to_excel("letshego.xlsx", index=False)
            st.success("Updated Customer Record!")
            
    else:
        st.info("No rows with null values in 'Customer_Contacted'.")
    if next_button:
     st.rerun()




    
