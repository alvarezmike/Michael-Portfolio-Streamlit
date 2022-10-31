import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import webbrowser
from pathlib import Path

# LINKS PROJECTS
NBA_WEB_APP = "https://alvarezmike-nba-streamlit-app-gmo44q.streamlitapp.com/"
NBA_WEB_APP_CODE = "https://github.com/alvarezmike/NBA-Streamlit"
STOCK_STREAMLIT = "https://alvarezmike-stock-streamlit-app-dscgjt.streamlitapp.com/"
STOCK_CODE = "https://github.com/alvarezmike/Stock-Streamlit"
TINDOG = "https://alvarezmike.github.io/TinDog-Advertisement/"
TINDOG_CODE = "https://github.com/alvarezmike/TinDog-Advertisement"
CRUD_VIDEO = "https://github.com/alvarezmike/CRUDApp/blob/main/README.md"
CRUD_CODE = "https://github.com/alvarezmike/CRUDApp"
PASSWORD_MANAGER_VIDEO = "https://github.com/alvarezmike/100daysOfPython/blob/main/Day30/Day30.md"
PASSWORD_MANAGER_CODE = "https://github.com/alvarezmike/100daysOfPython/tree/main/Day30/improved-password-manager"


# Path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir/"Michael Alvarez Resume.pdf"

# Load PDF
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# For more emojis code https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Michael-Portfolio", page_icon=":computer:", layout="wide")


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
lottie_coding = load_lottieur("https://assets2.lottiefiles.com/packages/lf20_l4fgppor.json")
img_password_manager = Image.open("images/passwordmanager.png")

# -- header section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Hi, I am Michael :wave:")
        st.title("A Software Engineer")
        st.subheader("Turning ideas into well developed products is my calling")
        st.write("[Visit my Github](https://github.com/alvarezmike)")
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding_1")



# -- Projects
with st.container():
    st.write("---")
    st.subheader("Portfolio")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("NBA Data Web App")
        st.write("Web scrapes data and formats into a beautiful stats display web app where you "
                 "can select data based on year and teams as well as player roles. ")
        st.markdown(f'''
                    <a href={NBA_WEB_APP}><button style="background-color:#04AA6D; color:white;border:none;border-radius:4px;">See it live</button></a>
                    ''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <a href={NBA_WEB_APP_CODE}><button style="background-color:greenyellow; color:black;border:none;border-radius:4px;">View Code</button></a>
                    ''',
                    unsafe_allow_html=True)
    with col2:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Stock Price Web App")
        st.write("Retrieves company information as well as the stock price data.")
        st.markdown(f'''
                    <a href={STOCK_STREAMLIT}><button style="background-color:#04AA6D; color:white;border:none;border-radius:4px;">See it live</button></a>
                    ''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <a href={STOCK_CODE}><button style="background-color:greenyellow; color:black;border:none;border-radius:4px;">View Code</button></a>
                    ''',
                    unsafe_allow_html=True)
    with col3:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Password Manager")
        st.write("Tkinter GUI App that manages all your passwords.")
        st.markdown(f'''
                    <a href={PASSWORD_MANAGER_VIDEO}><button style="background-color:#04AA6D; color:white;border:none;border-radius:4px;">Video Demo</button></a>
                    ''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <a href={PASSWORD_MANAGER_CODE}><button style="background-color:greenyellow; color:black;border:none;border-radius:4px;">View Code</button></a>
                        ''',
                    unsafe_allow_html=True)


with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Data Entry Desktop App")
        st.write("Tkinter GUI with MySQL database connection.")
        st.markdown(f'''
                    <a href={CRUD_VIDEO}><button style="background-color:#04AA6D; color:white;border:none;border-radius:4px;">Video Demo</button></a>
                    ''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <a href={CRUD_CODE}><button style="background-color:greenyellow; color:black;border:none;border-radius:4px;">View Code</button></a>
                    ''',
                    unsafe_allow_html=True)
    with col5:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Advertisement Web Page")
        st.write("Tinder but for our four-legged friend's web.")
        st.markdown(f'''
                    <a href={TINDOG}><button style="background-color:#04AA6D; color:white;border:none;border-radius:4px;">See it live</button></a>
                    ''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <a href={TINDOG_CODE}><button style="background-color:greenyellow; color:black;border:none;border-radius:4px;">View Code</button></a>
                    ''',
                    unsafe_allow_html=True)
    with col6:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Responsive Portfolio Website ")
        st.write("Portfolio Website made with HTML/CSS/JS.")
        st.markdown(f'''
        <a href={"https://alvarezmike.github.io/Responsive-Portfolio/"}><button style="background-color:#04AA6D; color:white;border:none;border-radius:4px;">See it live</button></a>
        ''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                <a href={"https://github.com/alvarezmike/Responsive-Portfolio"}><button style="background-color:greenyellow; color:black;border:none;border-radius:4px;">View Code</button></a>
                ''',
                    unsafe_allow_html=True)

# -- contact
with st.container():
    st.write("---")
    st.subheader("Get in touch with me")

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