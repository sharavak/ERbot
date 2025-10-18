import streamlit as st
st.set_page_config(page_title="ER diagram AI",page_icon='https://cdn-icons-png.flaticon.com/64/11629/11629055.png')
st.title("ER Diagrams")

er_code=[]
for i in st.session_state.chat_history:
    for j in i:
        if j=='er_code' and i[j].strip():
         er_code.append(i[j])
       
if not er_code:
    st.info("No ER diagrams yet. Go to Chat first.")

else:
    with st.spinner("Fetching diagrams..."):
        for i in range(0, len(er_code), 2):  
            cols = st.columns(2)
            for j, er in enumerate(er_code[i:i+2]):
                with cols[j]:
                    st.subheader(f"Diagram {i+j+1}")
                    st.image(er)
                    st.download_button(
                        f"⬇️ Download PNG {i+j+1}",
                        data=er,
                        file_name=f"er_diagram_{i+j+1}.png",
                        mime="image/png"
                    )