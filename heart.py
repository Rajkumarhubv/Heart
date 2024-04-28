import streamlit as st 
import pandas as pd 
import plotly.graph_objects as go 

st.title("Stroke Prediction Dashboard") 
st.markdown("The dashboard will help a researcher to get to know")
st.sidebar.title("Select Visual Charts") 
st.sidebar.markdown("Select the Charts/Plots accordingly:") 

uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())  # Display the uploaded data

    chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                        ('Line Chart', 'Bar Chart', 'Bubble Chart')) 

    st.sidebar.checkbox("Show Analysis by Smoking Status", True, key = 1) 
    selected_status = st.sidebar.selectbox('Select Smoking Status', 
                                           options = ['Formerly_Smoked', 'Smoked', 'Never_Smoked', 'Unknown']) 

    fig = go.Figure() 

    if chart_visual == 'Line Chart' or chart_visual == 'Bar Chart': 
        for status in ['Formerly_Smoked', 'Smoked', 'Never_Smoked', 'Unknown']:
            if selected_status == status: 
                fig.add_trace(go.Scatter(x=data['Country'], y=data[status], mode='lines', name=status))
            elif chart_visual == 'Bar Chart':
                fig.add_trace(go.Bar(x=data['Country'], y=data[status], name=status)) 

    elif chart_visual == 'Bubble Chart': 
        for status in ['Formerly_Smoked', 'Smoked', 'Never_Smoked', 'Unknown']:
            if selected_status == status: 
                fig.add_trace(go.Scatter(x=data['Country'], y=data[status], mode='markers', marker_size=[40, 60, 80, 60, 40, 50,40,20,50,40,30,20], name=status)) 

    fig.update_layout(title=f'{chart_visual} for {selected_status}', xaxis_title='Country', yaxis_title='Value')
    st.plotly_chart(fig, use_container_width=True) 
else:
    st.write("Please upload a CSV file.")
