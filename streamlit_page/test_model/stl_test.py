import streamlit as st
# import numpy as np
import os
# import glob
# import configargparse
from few_tensorf.dataLoader.__init__ import *
from few_tensorf.opt import *
from streamlit_page.test_model.stl_rendering import *
from streamlit_page.test_model.stl_mesh_extract import *
from streamlit_page.test_model.stl_comparison import *


def test_model():
    st.title('Testing model')

    rendering_tab, mesh_extract_tab, comparison_tab = st.tabs(["Rendering", "Mesh extract", "Comparison"])

    log_dir = os.path.join('few_tensorf','log')
    os.makedirs(log_dir, exist_ok=True)
    
    with rendering_tab:
        rendering(log_dir)
    
    with mesh_extract_tab:
        mesh_extract(log_dir)
            
    with comparison_tab:
        comparison(log_dir)

