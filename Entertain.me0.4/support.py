import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.buy_me_a_coffee import button

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

    st.title("Welcome to Our Support Page! 🌟")
    st.write("We're excited to offer you the opportunity to support our community through Ko-fi and Buy Me a Coffee ☕. Your support keeps our community thriving and allows us to continually improve our services. 🚀")

    st.subheader("Subscription Options: 🎁")

    st.subheader("Bro Bronze Tier - £3 per month 💰")
    st.write("Join the Bro Bronze Tier and earn the respect of your peers! With this tier, you'll be able to change your nickname on the server and receive stickers from other servers. Plus, you'll receive the exclusive medal of your respected tier, available only to subscribers. 🥉")

    st.subheader("Admirer Silver Tier - £7 per month 💎")
    st.write("Upgrade to the Admirer Silver Tier to unlock everything from the previous tier and more! Gain the ability to create public branches and enjoy access to our music bot. And of course, you'll receive the exclusive medal of your respected tier. 🎵")

    st.subheader("Patron Gold Tier - £10 per month 🏅")
    st.write("Elevate yourself to the prestigious Patron Gold Tier and enjoy all the perks from the previous tiers, plus the ability to mention everyone and all roles. Don't forget, you'll also receive the exclusive medal of your respected tier. 🌟")

    st.subheader("Investor Platinum Tier - £20 per month 💼")
    st.write("With the Investor Platinum Tier, you'll get access to everything offered in the previous tiers and more! Enjoy the sound bar, moderator rights, and the option to send voice messages. And as always, receive the exclusive medal of your respected tier. 🔊")

    st.subheader("Venture Capitalist Diamond Tier - £100 per month 💎💎")
    st.write("Reach the peak with the Venture Capitalist Diamond Tier. In addition to all the benefits from previous tiers, you'll receive extra moderator rights and the ability to create events. And of course, you'll proudly display the exclusive medal of your respected tier. 🌟🔨")

    st.write("Join now and start enjoying the exclusive perks and benefits of each tier! 🚀")

    st.subheader("How to Subscribe: 📝")
    st.write("Visit our Ko-fi page.")
    st.write("Choose your preferred subscription tier.")
    st.write("Enjoy the exclusive benefits and know that you're helping support our community's growth. 🌱")

    st.subheader("Subscription Availability: 🌐")
    st.write("Please note that all subscriptions are currently available only on Ko-fi. However, we're working on making them available on Buy Me a Coffee soon. In the meantime, if Buy Me a Coffee is your preferred platform, you can still support us by making a one-time donation. If you want to receive Discord benefits, simply donate the amount of the tier you want and send us a message through the contact form with your order number. 💌")

    st.write("Thank you for considering supporting us! Your contributions make a significant difference in our journey. If you have any questions or need assistance, feel free to reach out. 🙌")

    components.iframe(
        src='https://ko-fi.com/entertainme/?hidefeed=true&widget=true&embed=true&preview=true',
        width=None,
        height=1000,
        scrolling=False
    )
    button(username="entertain.me", floating=True, width=221)

if __name__ == "__main__":
    app()
