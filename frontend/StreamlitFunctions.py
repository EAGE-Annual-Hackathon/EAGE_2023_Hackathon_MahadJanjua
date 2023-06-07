import streamlit as st
import streamlit_toggle as tog
from PIL import Image
import base64
from htbuilder import HtmlElement, div, hr, p, styles
from htbuilder.units import percent, px
import os
import pathlib
from frontend.streamlit_state_handling import *


#--------------------------------------------------------------------
# Streamlit Functions Module
#--------------------------------------------------------------------


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def add_bg_from_local(background_image):
    with open(background_image, "rb") as background_image:
        encoded_string = base64.b64encode(background_image.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def add_image_and_title(logo_image):

    col1, mid, col2 = st.columns([1,1,0.33])
    image = Image.open(logo_image)
    with col1:
        st.title('GeoExplorer - Smart Search Engine')
        st.markdown("### Developers: \n\n **[Mahad Nadeem Janjua](mahad-nadeem.janjua@wintershalldea.com)** \n\n **[Durra Handri Saputera](durra.handri@gmail.com)** \n\n **[Stallone Teng](stallone.tht@gmail.com)** ")
    with col2:
        st.image(image, width=200)


def footer_layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="grey",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(0.5)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def call_footer():
    myargs = [
        "The <em>GeoExplorer - Smart Search Engine</em> Tool is a product developed at the EAGE Annual Conference Hackathon Event. The developers own the Intellectual Property Rights."
    ]
    footer_layout(*myargs)


def initialize_app_states():
    """
    Initialize session states
    """
    
    state = st.session_state
    state = set_all_states(state)

    return state


def initializing_sidebar_for_status_info():  
    """
    Initializing sidebar for streamlit app page 
    """

    image_path = os.path.join(str(pathlib.Path(__file__).parent.resolve()),"../app_images", "wdb.png")

    image = Image.open(image_path)
    with st.sidebar:
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.title("  ")
        with col2:
            st.image(image) 
        with col3:
            st.write("")
        st.write("")
        status = st.empty()

    return status


def st_layout_pipeline(background_image, logo_image, style_css):
    """
    Pipeline for definition of the streamlit app layout
    """
    
    st.set_page_config(layout="wide")
    local_css(style_css)
    add_bg_from_local(background_image)
    add_image_and_title(logo_image)
    state = initialize_app_states()
    status = initializing_sidebar_for_status_info()
    call_footer()

    return state, status
