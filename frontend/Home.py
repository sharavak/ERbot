import streamlit as st
st.set_page_config(page_title="ERBot - Home", layout="wide",page_icon='https://cdn-icons-png.flaticon.com/64/11629/11629055.png')

st.title("ERBot - Smart ER Diagram & Text Generator")
st.subheader("Generate, visualize, and download Entity-Relationship diagrams with explanations")
st.markdown("---")



col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ER Diagram Generator")
    st.write("Automatically creates ER diagrams from your text input.")

with col2:
    st.markdown("### Chat & Explain")
    st.write("Get detailed explanations along with generated diagrams.")

with col3:
    st.markdown("### Download & Share")
    st.write("Export ER diagrams as PNG/JPG and share.")

st.markdown("---")
st.markdown("## Get Started")
st.markdown("Go to the **Chatbot Page** from the sidebar to start generating ER diagrams.")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .css-1d391kg {  /* sidebar background */
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)
