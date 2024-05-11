import streamlit as st

def app():
    
    st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    text-align: center;
}
.footer a {
    color: #333;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)
    st.markdown('<div class="footer"><a href="https://www.nclanarkshire.ac.uk">NCL HNC NextGen © 2024</a></div>', unsafe_allow_html=True)

    st.title("About Entertain.me")
    
    st.subheader("About Us 🎬📚🎵")
    st.write("""
    Welcome to Entertain.me - your ultimate destination for personalised recommendations and entertainment exploration!
    """)
    
    st.header("Our Mission 🚀")
    st.write("""
    At Entertain.me, our mission is simple yet powerful: to enhance your entertainment experience by providing you with tailored recommendations based on your preferences.
    """)
    
    st.subheader("Work in Progress 🛠️")
    st.write("""
    Currently, we have online film recommendations, but we are planning on expanding! Soon, you will be able to find book recommendations as well as music. Stay tuned for updates!
    """)
    
    st.header("How It Works 🤖")
    st.write("""
    We use advanced algorithms and machine learning techniques to analyze your preferences and recommend films that you're likely to love. Whether you're a fan of action-packed blockbusters, heartwarming dramas, or thought-provoking documentaries, our platform has something for everyone.
    """)
    
    st.subheader("Personalized Recommendations 💡")
    st.write("""
    By selecting your favorite genres, preferred IMDb ratings, and the number of recommendations you'd like to receive, Entertain.me curates a list of movies that align with your unique tastes. Our recommendation engine continuously learns from your interactions, ensuring that the suggestions become more accurate over time.
    """)
    
    st.subheader("Explore and Discover 🔍")
    st.write("""
    But Entertain.me is more than just a recommendation tool - it's a gateway to exploring the vast world of entertainment. Dive into movie details, read synopses, explore IMDb ratings, discover fascinating trivia about your favorite films, and even find stickers for your conversations. With Entertain.me, the journey of discovery never ends.
    """)
    
    st.header("Our Team 👩‍💻👨‍💼")
    st.write("""
    Entertain.me was created by a passionate team of enthusiasts, data scientists, and developers who share a common goal: to revolutionise the way people discover and enjoy their entertainment. With expertise in machine learning, data analytics, and user experience design, our team is dedicated to delivering an unparalleled entertainment experience to our users.
    """)

if __name__ == "__main__":
    app()
