import streamlit as st
from requester import request_image

st.title("AI Helper")


choice = st.sidebar.selectbox("Choose an option",("GPT3","DALL-E"))



if choice == "GPT3":
    st.subheader("Ask anything to GPT3")
    input_text = st.text_input("Input Text")

    if input_text is not None:
        if st.button("Generate Image"):
            
            st.image(input_text,caption="Text generated with GPT3")
            
elif choice == "DALL-E":
    st.subheader("Crate an image from your prompt DALL-E")
    input_text = st.text_input("Input Text")

    if input_text is not None:
        if st.button("Generate Image"):
            try:
                image = request_image(input_text)
                st.image(image,caption="Image generated with DALL-E")
            except Exception as e:
                st.error(f"Something went wrong \n {str(e)}")