import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from bokeh.models.widgets import Div
import webbrowser

NBA_WEB_APP = "https://alvarezmike-nba-streamlit-app-gmo44q.streamlitapp.com/"
NBA_WEB_APP_CODE = "https://github.com/alvarezmike/NBA-Streamlit"
TINDOG = "https://alvarezmike.github.io/TinDog-Advertisement/"
TINDOG_CODE = "https://github.com/alvarezmike/TinDog-Advertisement"

# For more emojis code https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Portfolio", page_icon=":computer:", layout="wide")


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# -- Load assets
lottie_coding = load_lottieur("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")
img_password_manager = Image.open("images/passwordmanager.png")

# -- header section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi, I am Michael :wave:")
        st.title("A Software Engineer")
        st.subheader("Turning ideas into well developed products is my calling")
        st.write("[See some of my codes >](https://github.com/alvarezmike)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding_1")

# -- What I Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            dgdggdgdgdgdgdgdgdg
            - sddgdgdggdgd
            - ddgdgdggdddhdhdhdh
            - dhdhhdhdhdhdhd
            - ahhaagagagag

            If this sounds interesting to you, coonsider subscribing shsushbbddbb
            """
        )
        st.write("[Youtube channel] > link here")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# -- Projects
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("NBA Data Web App")
        st.write("Web scrapes data and formats into a beautiful stats display web app where you "
                 "can select data based on year and teams as well as player roles. ")
        if st.button("See it live", key="nba_live"):
            webbrowser.open_new_tab(NBA_WEB_APP)
        if st.button("Code", key="nba_code"):
            webbrowser.open_new_tab(NBA_WEB_APP_CODE)
    with col2:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Github E-Mail Exposer")
        st.write("Expose all E-Mail addresses contributing to a given Github account.")
        if st.button('Enter App', key="gee_enter"):
            js = "window.open('https://github.com/ratherUsefulCode/github-email-exposer')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="gee_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/ratherUsefulCode/github-email-exposer')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col3:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Crypto Currency Watchlist")
        st.write("Django web application that shows some basic data of your favourite crypto currencies.")
        if st.button('Enter App', key="ccw_enter"):
            js = "window.open('https://crypto-watchlist-rather-to.herokuapp.com/')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="ccw_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/ratherUsefulCode/')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("QR Codes Reader and Generator")
        st.write("Create and/or read every QR code.")
        if st.button('Enter App', key="qrc_enter"):
            st.write('Web Application opens in new browser tab')
        if st.button('Github', key="qrc_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/ratherUsefulCode/github-email-exposer')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col5:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Advertisement Web Page")
        st.write("Tinder but for our four-legged friend's web")
        if st.button("See it live", key="tindog_live"):
            webbrowser.open_new_tab(TINDOG)
        if st.button("Code", key="tindog_code"):
            webbrowser.open_new_tab(TINDOG_CODE)
    with col6:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Portfolio Website made with Bootstrap")
        st.write("Portfolio Website made with HTML/Bootstrap.")
        if st.button('Enter App'):
            js = "window.open('https://rather.to')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
            st.write('Web Application opens in new browser tab')
        if st.button('Github', key="bpw_github"):
            js = "window.open('https://github.com/ratherUsefulCode/rather-to')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

# -- contact
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/kerer74@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()