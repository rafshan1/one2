import streamlit as st
import webbrowser

def main():
    st.image("f.gif")
    st.write('''Explore a comprehensive collection of GPT models gathered in one convenient application. 
             Compare various iterations of cutting-edge AI technology effortlessly. Uncover the perfect model to suit your specific needs with ease and efficiency.
     Seamlessly navigate through the realm of GPT advancements for enhanced productivity and innovation.''')
    
    
    st.sidebar.title('Available Models')
    command = st.sidebar.selectbox('Select a model', ['Chatgpt', 'Copilot', 'Gemeni', 'Claude', 'Perplexcity'])
    
    if command == 'Chatgpt🤖':
        webbrowser.open("https://chat.openai.com/")
    elif command == 'Copilot🤖':
        webbrowser.open('https://copilot.microsoft.com/?form=WSBSH2&cvid=7e40ac4d8a62473081fcc8c9ded8a2de&nclid=0A88352DD13E603FE110D7B1EADB85D0&ts=1708793898138&nclidts=1708793898&tsms=138&wlsso=1&wlexpsignin=1&wlexpsignin=1')
    elif command == 'Gemeni🤖':
        webbrowser.open("https://gemini.google.com/app")
    elif command == 'Claude🤖':
        webbrowser.open("https://claude.ai/login?returnTo=%2F")
    elif command == 'Perplexcity🤖':
        webbrowser.open('https://www.perplexity.ai/')
    
    
    else:
        st.stop()

if __name__ == "__main__":
    main()
