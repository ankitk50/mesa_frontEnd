import streamlit as st
from money_model import *
import numpy as np
import matplotlib.pyplot as plt
import time
import plotly.express as px
import altair as alt
import pandas as pd
import yaml
import json
st.title('Mesa StreamLit Interface')

model = st.selectbox('Select Model',['Boltzman Wealth Model'])
num_ticks = st.slider('Select number of Simulation Runs',min_value=1,max_value=100,value=50)
num_agents= st.slider('Select number of Agents',min_value=1,max_value=100,value=50)
height = st.slider('Select Grid Height',min_value=10,max_value=100,step=10,value=15)
width = st.slider('Select Grid Width',min_value=10,max_value=100,step=10,value=20)
model = MoneyModel(num_agents, height, width)


col1,col2,col3  = st.columns(3)
status_text = st.empty()
with col1:
    run = st.button('Run Simulation')
with col2:
    save = st.checkbox('Save output')


if run :
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
    st.subheader('Gini value over sim ticks (Plotly)')
    chart = st.line_chart(model.datacollector.model_vars['Gini'])

    st.subheader('Gini value over sim ticks (Altair)')
    gini_values = model.datacollector.model_vars['Gini']
    index_x= [i+1 for i in range(len(gini_values))]
    # if st.checkbox('Show Raw Gini data'):
    df = pd.DataFrame({'y':gini_values,'x':index_x})
    st.altair_chart(alt.Chart(df).mark_line(
    point=alt.OverlayMarkDef(color="red")
    ).encode(
        x='x',
        y='y'
    ),use_container_width=True)
    with st.expander('show raw data', expanded=False):
        st.table(df['y'])

    # yaml_dump_dict= {'agent_count':agent_counts.tolist(), 'gini':gini_values}
    json_dump_dict= {'x':index_x,'y':gini_values}
    if save:
        with open('output/output_data.json', 'w') as fp:
            json.dump(json_dump_dict, fp)



