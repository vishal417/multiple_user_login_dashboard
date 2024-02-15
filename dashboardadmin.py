import streamlit as st
import pandas as pd
import numpy as np



def app():
    df=pd.read_excel("letshego.xlsx")

    st.subheader("Tele-Calling Dashboard")
    st.markdown('', unsafe_allow_html=False)
    col1, col2, col3, col4 = st.columns((4))
    with col1:
        # Create for Country
        Country = st.multiselect("Country", df["Country"].unique())
        if not Country:
            df2 = df.copy()
        else:
            df2 = df[df["Country"].isin(Country)]
    with col2:
        # Create for Country
        Customer_Qualification = st.multiselect("Customer Qualification", df["Customer_Qualification"].unique())
        if not Customer_Qualification:
            df3 = df2.copy()
        else:
            df3 = df2[df2["Customer_Qualification"].isin(Customer_Qualification)]
    with col3:
        # Create for Country
        Topup_Winback = st.multiselect("Topup/Winback", df["Topup_Winback"].unique())
        if not Topup_Winback:
            df4 = df3.copy()
        else:
            df4 = df3[df3["Topup_Winback"].isin(Topup_Winback)]

    with col4:
        # Create for Country
        Date_Camp = st.multiselect("Campaign Date", df["Date_Camp"].unique())
        if not Date_Camp:
            df5 = df4.copy()
        else:
            df5 = df4[df4["Date_Camp"].isin(Date_Camp)]


    if not Country and not Customer_Qualification and not Topup_Winback and not Date_Camp:
        filtered_df = df
    elif not Customer_Qualification and not Topup_Winback and not Date_Camp:
        filtered_df = df[df["Country"].isin(Country)]
    elif not Country and not Topup_Winback and not Date_Camp:
        filtered_df = df2[df2["Customer_Qualification"].isin(Customer_Qualification)]
    elif not Country and not Customer_Qualification and not Date_Camp:
        filtered_df = df3[df3["Topup_Winback"].isin(Topup_Winback)]
    elif not Country and not Customer_Qualification and not Topup_Winback:
        filtered_df = df4[df4["Date_Camp"].isin(Date_Camp)]
    elif Country and Customer_Qualification and Topup_Winback:
        filtered_df = df5[
            df["Country"].isin(Country)
            & df2["Customer_Qualification"].isin(Customer_Qualification)
            & df3["Topup_Winback"].isin(Topup_Winback)
        ]
    elif Country and Topup_Winback and Date_Camp:
        filtered_df = df5[
            df["Country"].isin(Country)
            & df3["Topup_Winback"].isin(Topup_Winback)
            & df4["Date_Camp"].isin(Date_Camp)
        ]
    elif Country and Customer_Qualification and Date_Camp:
        filtered_df = df5[
            df["Country"].isin(Country)
            & df2["Customer_Qualification"].isin(Customer_Qualification)
            & df4["Date_Camp"].isin(Date_Camp)
        ]
    elif Customer_Qualification and Topup_Winback and Date_Camp:
        filtered_df = df5[
            df2["Customer_Qualification"].isin(Customer_Qualification)
            & df3["Topup_Winback"].isin(Topup_Winback)
            & df4["Date_Camp"].isin(Date_Camp)
        ]
    elif Country and Customer_Qualification:
        filtered_df = df5[
            df["Country"].isin(Country) & df2["Customer_Qualification"].isin(Customer_Qualification)
        ]
    elif Country and Topup_Winback:
        filtered_df = df5[df["Country"].isin(Country) & df3["Topup_Winback"].isin(Topup_Winback)]
    elif Country and Date_Camp:
        filtered_df = df5[df["Country"].isin(Country) & df4["Date_Camp"].isin(Date_Camp)]
    elif Customer_Qualification and Topup_Winback:
        filtered_df = df5[
            df2["Customer_Qualification"].isin(Customer_Qualification) & df3["Topup_Winback"].isin(Topup_Winback)
        ]
    elif Customer_Qualification and Date_Camp:
        filtered_df = df5[
            df2["Customer_Qualification"].isin(Customer_Qualification) & df4["Date_Camp"].isin(Date_Camp)
        ]
    elif Topup_Winback and Date_Camp:
        filtered_df = df5[df3["Topup_Winback"].isin(Topup_Winback) & df4["Date_Camp"].isin(Date_Camp)]
    else:
        filtered_df = df5[
            df["Country"].isin(Country)
            & df3["Topup_Winback"].isin(Topup_Winback)
            & df4["Date_Camp"].isin(Date_Camp)
        ]

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns((9))

    with col1:
        total_customer_count = filtered_df["Customer_No"].nunique()
        st.markdown(f"<p style='font-size: small; font-weight: bold;'>Total number of Leads:</p>",
                    unsafe_allow_html=True)
        st.info(f"{total_customer_count}")

    with col2:
        # Count the occurrences of each unique value in "Customer_Contacted"
        contacted_counts = filtered_df["Customer_Contacted"].value_counts()

        # Get the count of "Yes" (if it exists, otherwise default to 0)
        yes_count = contacted_counts.get("Yes", 0)
        st.markdown(f"<p style='font-size: small; font-weight: bold;'>Contacted Customers </p>",
                    unsafe_allow_html=True)
        st.info(f"{yes_count}")

    with col3:
        # Count the occurrences of each unique value in "Customer_Contacted"
        null_count = filtered_df["Customer_Contacted"].isnull().sum()
        st.markdown(f"<p style='font-size: small; font-weight: bold;'>Not Contacted</p>",
                    unsafe_allow_html=True)
        st.info(f"{null_count}")

    with col4:
        if yes_count == 0 or len(filtered_df)==0:
            st.markdown(f"<p style='font-size: small; font-weight: bold;'> Contacted Customers%</p>",
                    unsafe_allow_html=True)
            st.info(f"{0}")
        else:
        # Count the occurrences of each unique value in "Customer_Contacted"
         percentage_contacted = round((yes_count / len(filtered_df)) * 100, 1)
         st.markdown(f"<p style='font-size: small; font-weight: bold;'> Contacted Customers%</p>",
                    unsafe_allow_html=True)
         st.info(f"{percentage_contacted}")

    with col5:
        # Count the occurrences of each unique value in "Customer_Disposition"
        disposition_counts = filtered_df["Customer_Disposition"].value_counts()

        # Get the count of "Call Back" (if it exists, otherwise default to 0)
        callback_count = disposition_counts.get("Call Back", 0)
        if callback_count == 0 or len(filtered_df)==0:
            st.markdown(f"<p style='font-size: small; font-weight: bold;'> Call Back Customer%</p>",
                    unsafe_allow_html=True)
            st.info(f"{0}")
        else:
        # Calculate the percentage of "Call Back" values and round to one decimal point
         percentage_callback = round((callback_count / len(filtered_df)) * 100, 1)
         st.markdown(f"<p style='font-size: small; font-weight: bold;'> Call Back Customer%</p>",
                    unsafe_allow_html=True)
         st.info(f"{percentage_callback}")


    with col6:
        # Count the occurrences of each unique value in "Customer_Disposition"
        disposition_counts = filtered_df["Customer_Disposition"].value_counts()

        # Get the count of "Call Back" (if it exists, otherwise default to 0)
        Customer_Not_available_count = disposition_counts.get("Customer Not available", 0)
        if Customer_Not_available_count == 0 or len(filtered_df)==0:
            st.markdown(f"<p style='font-size: small; font-weight: bold;'> Not Available%</p>",
                    unsafe_allow_html=True)
            st.info(f"{0}")
        else:
        # Calculate the percentage of "Call Back" values and round to one decimal point
            percentage_Customer_Not_available = round((Customer_Not_available_count / len(filtered_df)) * 100, 1)
            st.markdown(f"<p style='font-size: small; font-weight: bold;'>Not Available%</p>",
                        unsafe_allow_html=True)
            st.info(f"{percentage_Customer_Not_available}")

    with col7:
        # Count the occurrences of each unique value in "Customer_Disposition"
        disposition_counts = filtered_df["Customer_Disposition"].value_counts()

        # Get the count of "Call Back" (if it exists, otherwise default to 0)
        Deal_closed_count = disposition_counts.get("Deal Closed", 0)
        if Deal_closed_count == 0 or len(filtered_df)==0:
            st.markdown(f"<p style='font-size: small; font-weight: bold;'> Deal Closed%</p>",
                    unsafe_allow_html=True)
            st.info(f"{0}")
        else:

            # Calculate the percentage of "Call Back" values and round to one decimal point
            percentage_Deal_closed = round((Deal_closed_count / len(filtered_df)) * 100, 1)
            st.markdown(f"<p style='font-size: small; font-weight: bold;'> Deal Closed%</p>",
                        unsafe_allow_html=True)
            st.info(f"{percentage_Deal_closed}")

    with col8:
                # Count the occurrences of each unique value in "Customer_Disposition"
        disposition_counts = filtered_df["Customer_Disposition"].value_counts()

        # Get the count of "Call Back" (if it exists, otherwise default to 0)
        Interested_count = disposition_counts.get("Interested", 0)
        if Interested_count == 0 or len(filtered_df)==0:
            st.markdown(f"<p style='font-size: small; font-weight: bold;'> Interested Costomers%</p>",
                    unsafe_allow_html=True)
            st.info(f"{0}")
        else:
        # Calculate the percentage of "Call Back" values and round to one decimal point
            percentage_Interested = round((Interested_count / len(filtered_df)) * 100, 1)
            st.markdown(f"<p style='font-size: small; font-weight: bold;'> Interested Costomers%</p>",
                        unsafe_allow_html=True)
            st.info(f"{percentage_Interested}")

    with col9:
                # Count the occurrences of each unique value in "Customer_Disposition"
        disposition_counts = filtered_df["Customer_Disposition"].value_counts()

        # Get the count of "Call Back" (if it exists, otherwise default to 0)
        Not_Interested_count = disposition_counts.get("Not Interested", 0)
        if Not_Interested_count == 0 or len(filtered_df)==0:
            st.markdown(f"<p style='font-size: small; font-weight: bold;'> Not Interested%</p>",
                    unsafe_allow_html=True)
            st.info(f"{0}")
        else:
            # Calculate the percentage of "Call Back" values and round to one decimal point
            percentage_not_Interested = round((Not_Interested_count / len(filtered_df)) * 100, 1)
            st.markdown(f"<p style='font-size: small; font-weight: bold;'>Not Interested%</p>",
                        unsafe_allow_html=True)
            st.info(f"{percentage_not_Interested}")


    result_table = filtered_df.groupby('Tellisale_Agent').agg(
    TotalLeads=pd.NamedAgg(column='Tellisale_Agent', aggfunc='count'),
    CustomerContacted=pd.NamedAgg(column='Customer_Contacted', aggfunc=lambda x: (x == 'Yes').sum()),
    NotContacted=pd.NamedAgg(column='Customer_Contacted', aggfunc=lambda x: x.isna().sum()),
    CustomerNotAvailable=pd.NamedAgg(column='Customer_Contacted', aggfunc=lambda x: (x == 'Customer Not Available').sum()),
    ClosedDeal=pd.NamedAgg(column='Customer_Disposition', aggfunc=lambda x: (x == 'Deal Closed').sum()),
    CallBack=pd.NamedAgg(column='Customer_Disposition', aggfunc=lambda x: (x == 'Call Back').sum()),
    Interested=pd.NamedAgg(column='Customer_Disposition', aggfunc=lambda x: (x == 'Interested').sum()),
    NotInterested=pd.NamedAgg(column='Customer_Disposition', aggfunc=lambda x: (x == 'Not Interested').sum())
).reset_index()
    result_table['Contacted Percentage'] = result_table['CustomerContacted'] / result_table['TotalLeads'] * 100
    result_table['NotnContacted Percentage'] = result_table['NotContacted'] / result_table['TotalLeads'] * 100
    result_table['Customer Not Available percentage'] = result_table['CustomerNotAvailable'] / result_table['TotalLeads'] * 100
    result_table['Closed Deal Percentage'] = result_table['ClosedDeal'] / result_table['TotalLeads'] * 100
    result_table['CallBack Percentage'] = result_table['CallBack'] / result_table['TotalLeads'] * 100
    result_table['Interested Percentage'] = result_table['Interested'] / result_table['TotalLeads'] * 100
    result_table['NotInterested Percentage'] = result_table['NotInterested'] / result_table['TotalLeads'] * 100
    st.dataframe(result_table, height=300, width=1200, hide_index=True)


    Col1, Col2 = st.columns((2))
    with Col1:
        Customer_Disposition = st.multiselect("Customer Disposition", filtered_df["Customer_Disposition"].unique())
        if not Customer_Disposition:
           filtered_df = filtered_df.copy()
        else:
            filtered_df = filtered_df[filtered_df["Customer_Disposition"].isin(Customer_Disposition)]
    
    with Col2:
        feedback_counts = filtered_df['Agent_Feedback'].value_counts().reset_index().rename(columns={'index': 'Feedback', 'Agent_Feedback': 'Count'})
        st.dataframe(feedback_counts, height=200, width=1200,hide_index=True)

    

