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

    with st.container():
        st.header(":mailbox_with_mail: Let us know what you think")
        st.write("Please take a moment to share your thoughts and suggestions with us. Whether you seek information, have questions, or encounter a technical issue, we value your feedback and inquiries and are committed to ensuring a seamless experience.💬🔍🛠️")

        # Define the emoji URLs
        normal_logo_url = "https://cdn3.emoji.gg/emojis/2372-discord-clyde-dark.png"
        hover_logo_url = "https://cdn3.emoji.gg/emojis/8721-discord-clyde-dark-gif.gif"
        
        st.markdown(
        """
        <style>
        .logo-button {
            background-image: url('"""+ normal_logo_url +"""');
            background-size: cover;
            width: 30px;
            height: 30px;
            border: none;
            cursor: pointer;
            transition: background-image 0.3s ease-in-out;
            display: inline-block; /* Ensure button dimensions match image dimensions */
        }
        .logo-button:hover {
            background-image: url('"""+ hover_logo_url +"""');
        }
        .purple-text {
            color: purple;
            font-weight: bold;
        }
        .linkedin-link {
            color: blue;
        }
        </style>
        """,
        unsafe_allow_html=True
        )
        
        st.markdown(
        """
        <div style="display: flex; align-items: center;">
            <p>Whether you're here with questions or just for some fun, our <span class="purple-text">Discord </span> community offers the perfect space to connect with like-minded individuals, so feel free to join our channel on <span class="purple-text">Discord </span> !
                <a href="https://discord.gg/J3KQu5kfNZ" target="_blank">
                    <button class="logo-button"></button>
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
        )
        
        st.markdown(
        """
        <p>P.S. Interested in joining our team? Leave us a message on <a href="https://www.linkedin.com/in/entertain-me-905aa1304" class="linkedin-link" target="_blank">LinkedIn</a>. We're actively on the lookout for talented individuals! 💼
        </p>
        """,
        unsafe_allow_html=True
        )

        st.markdown(
        """
        <p>You can also apply directly through our <a href="https://docs.google.com/forms/d/e/1FAIpQLSdBsXiachwHM928L25VDd2Lh7TWRY7sYPKxU3afwzdNEHfEbA/viewform?usp=sf_link" target="_blank">Google Form</a>. 📝
        </p>
        """,
        unsafe_allow_html=True
        )
        
    def contact1():
        contact_form = """
            <form action="https://formsubmit.co/entertain.me.contact@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here"></textarea>
                <button type="submit">Send</button>
            </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

        # Apply Local CSS Styles
        st.markdown(
            """
            <style>
            input[type=text], input[type=email], textarea {
                width: 100%;
                padding: 12px;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
                margin-top: 6px;
                margin-bottom: 16px;
                resize: vertical;
            }
            button[type=submit] {
                background-color: #91A774; 
                color: white;
                padding: 16px 24px; 
                border: none;
                border-radius: 4px;
                cursor: pointer;
                width: 150px;
            }
            button[type=submit]:hover {
                background-color: #B4CD96;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Redirect user to home page after submitting the form
        if st.query_params.get('submit') == 'true':
            st.experimental_set_query_params()
            st.experimental_rerun()
            st.experimental_set_query_params(submit=None)

        # Check if form is submitted
        if st.query_params.get('submit') == 'true':
            st.success("Thank you for your message! You will be redirected to the home page shortly.")

    # Call the contact1() function to display the contact form
    contact1()

# Call the app function to run the Streamlit app
if __name__ == "__main__":
    app()
