# Frontend UI for Mesa

Steps to run:

- (From a virtual environment) Install all requirements using: `pip install -r requirements.txt`
- From the project folder run: `streamlit run app.py`

The app will automatically open in your local browser. Here is a preview of the app: 

## StremLit Example interface
The interface allows selection of a model, and other parameters for the simulation.

![Main Interface](/data/inteface_boltmann.png?)

Run simulation button runs the simulations and shows the following plot(s).
### Agent Grid after the simulation
![Agent Grid](data/grid.png?raw=true)

### Gini Value over Sim-Ticks (using Plotly)
![Agent Grid](data/gini.png?raw=true)

### Gini Value over Sim-Ticks (using Altair)
![Agent Grid](data/altair_line.png?raw=true)

### Load output of a compelted simulation (using Mesa Playground)
Browse *ouput/output_data.json* to regenerate all the plots w/o running the simulation.

![Agent Grid](data/playground.png?raw=true)

## Panel Jupyter Notebook Example
The Panel interface allows selection of a model, and other parameters for the simulation inside a Jupyter notebook. Checkout the notebook **Panel_Mesa_Example.ipynb** for more information.

![Agent Grid](data/PanelJupyter.png?raw=true)

