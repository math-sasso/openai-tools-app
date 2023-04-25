import streamlit as st


st.title("AI Image Generatorion App")


choice = st.sidebar.selectbox("Choose an option",("GPT3","DALL-E"))
st.subheader("Crate an image using Stable Diffusion")


if choice == "GPT3":
    input_text = st.text_input("Input Text")

    if input_text is not None:
        if st.button("Generate Image"):
            
            st.image(input_text,caption="Text generated with GPT3")
            
elif choice == "DALL-E":
    input_text = st.text_input("Input Text")

    if input_text is not None:
        if st.button("Generate Image"):
            
            st.image(input_text,caption="Image generated with DALL-E")