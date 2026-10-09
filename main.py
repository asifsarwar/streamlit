import streamlit as st

st.write('Welcome to AI ML & DL class')

st.write('This is a simple streamlit app for demonstrating ML and DL concepts')

st.title('This is a title')

st.header('This is a header')

st.subheader('This is a subheader')

st.text('This is a text')

st.markdown('This is a markdown')

st.info("Information")

st.success('Success')

st.warning('Warning')

st.write(2)

st.text(2)

st.image(r'C:\Users\Asif Sarwar\Downloads\beach.jpg')

st.video(r'https://youtu.be/hP48QCkiQVI?si=aiAey1q6i3m8QatF')

age = st.number_input('Enter age:', min_value=10, max_value= 100)

if(st.button('Calculate')):
    st.success(age)

hobbies = st.multiselect("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write('You selected', len(hobbies), hobbies,'hobbies')

st.checkbox('Show/Hide', False)

st.radio('Select Gender', ['Male', 'Female'])