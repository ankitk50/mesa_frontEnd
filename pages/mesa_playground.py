import streamlit as st
import altair as alt
import pandas as pd

st.title('Mesa Playground')
uploaded_file = st.file_uploader('Upload simulation result file (output/output_data.json)',type=['.json'])

plot_gen = st.button('Generate Plot')

if uploaded_file is not None and plot_gen:
    df = pd.read_json(uploaded_file)
    st.altair_chart(alt.Chart(df).mark_line(
    point=alt.OverlayMarkDef(color="red")
    ).encode(
        x='x',
        y='y'
    ),use_container_width=True)

    with st.expander('show raw data', expanded=False):
        st.table(df['y'])
if plot_gen and not uploaded_file:
    st.info('Upload file and the click generate plots')

