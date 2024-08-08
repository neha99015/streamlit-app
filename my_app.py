import streamlit as st

st.write("Hell world: Getting Bore,Hello Brother!!")
st.title("Disply Title use st.title()")
st.write("To write text use st.write()")
st.header("I am header to write header use st.header()")
st.subheader("I am subheader To write subheader use st.subheader()")
st.text("Hey I am simple text to write simple text use st.text()")
# To creat hyperlink
st.markdown("[streamlit](https://streamlit.io/)")
st.markdown("[streamlit CheatSheet](https://cheat-Sheet.streamlit.app/)")
st.success("Success!")
st.info("information")
st.warning("This is a warning")
st.error("This is an error!")


from PIL import Image
img=Image.open("smj.jpg")
st.image(img,width=300,caption="satymev jayte")

video_file =open("vid.mp4","rb")
video_bytes =video_file.read()
st.video(video_bytes)

st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")

audio_file = open("song.mp3","rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes,format="audio/mp3")

st.button("play")

st.header("Button Widgets")

if st.button("play1"):
    st.text("Hellow World")
    
    
if st.button("play2"):
    st.text("Enjoy Music")
    st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")
    
if st.checkbox("checkbox"):
    st.text("checkbox selected")
    
    
    