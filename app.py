import streamlit as st
from money_model import *
import numpy as np
import matplotlib.pyplot as plt
import time
import plotly.express as px
st.title('Mesa StreamLit Interface')

col1,col2,col3  = st.columns(3)
model = st.selectbox('Select Model',['Boltzman Wealth Model'])
num_ticks = st.slider('Select number of Simulation Runs',min_value=1,max_value=100,value=50)
num_agents= st.slider('Select number of Agents',min_value=1,max_value=100,value=50)
height = st.slider('Select Grid Height',min_value=10,max_value=100,step=10,value=15)
width = st.slider('Select Grid Width',min_value=10,max_value=100,step=10,value=20)
model = MoneyModel(num_agents, height, width)


status_text = st.empty()
if st.button('Run Simulation'):
    tick = time.time()
    for i in range(num_ticks):
        model.step()
    tock = time.time()
    st.success('Simulation completed in {:.2f} secs'.format(tock-tick))
    agent_counts = np.zeros((model.grid.width, model.grid.height))
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        agent_count = len(cell_content)
        agent_counts[x][y] = agent_count

    st.subheader('Agent Grid')
    fig = px.imshow(agent_counts,labels={'color':'Agent Count'})
    st.plotly_chart(fig)
    st.subheader('Gini value over sim ticks')
    chart = st.line_chart(model.datacollector.model_vars['Gini'])


