import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(page_title="FINAL YEAR PROJECT")
import plotly.express as px

session_state = st.session_state
# session_state.cache = True
data = pd.read_excel(r"mult.xlsx")
x = list(data['Distance km'])
y = list(data['Loss dB'])

distance = x
attenuation = y 

st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
st.markdown("""""", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
    
                header{visibility:hidden;}
                .main {
                    margin-top: -10px;
                    padding-top:20px;
                    
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}

            </style>
            
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:#4267B2;">
    <a class="navbar-brand" href="#"  target="_blank"> OTDR REMOTE MONITOR</a>  
    </nav>
""",
    unsafe_allow_html=True,
)

# Create scatter plot with break location pinpointing
def plot_breakpoints():
    fig = go.Figure()

    # Simulated data for demonstration
    break_locations = []
    breaks = []
    for i in range(1, len(y)):
        if y[i] - y[i-1] > 5:
            breaks.append(x[i])
            break_locations.append((x[i], y[i]))
    for q in breaks:

        st.markdown(f"<span class='card note alert alert-warning' style='font-size:24px'>The break is predicted to be at a distance of {q} meters.</span>",unsafe_allow_html=True)

    # Scatter plot of data points
    fig.add_trace(go.Scatter(
        x=x, y=y,
        name='Distance',
        mode='lines+markers',
        marker=dict(color='purple', size=10)
    ))

    # Highlighting the break locations
    for loc in break_locations:
        fig.add_trace(go.Scatter(
            x=[loc[0]],
            y=[loc[1]],
            mode='markers',
            name='Break Location',
            marker=dict(color='red', size=15, symbol='triangle-up')
        ))

    # Configure layout and axes labels
    fig.update_layout(
        title="Distance(m) vs. Loss(Db)",
        xaxis_title="Distance (meters)",
        yaxis_title="Loss",
        legend=dict(x=1.2, y=0.95)
    )

    st.plotly_chart(fig, use_container_width=True)

# Call the function to generate the plot
plot_breakpoints()

# Create an expander for additional views
with st.expander("Other view"):
    # Include other views and visualizations here
    pass  # Placeholder for additional content

