# Project 9: Python Website With Streamlit
import streamlit as st
import pandas as pd

# Required packages for this project:
# Install using: pip install streamlit pandas

# Set page config
st.set_page_config(page_title="Shop.CO.Pk ECom", layout="wide")

# Custom styling for a futuristic look
st.markdown(
    """
    <style>
    body {
        background-color:#f0f0f0;
        color: #00ffcc;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #00ffcc;
        color: black;
        border-radius: 10px;
        font-size: 18px;
    }
    .stTextInput>div>div>input {
        background-color: #222;
        color: #00ffcc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sample product data with different clothes images
products = pd.DataFrame({
    "Product": ["Cyberpunk Jacket", "Holographic Hoodie", "Neon Sneakers", "Techwear Pants", "LED Cap"],
    "Price": [199, 149, 99, 129, 59],
    "Image": [
        "https://example.com/cyberpunk_jacket.jpg",
        "https://example.com/holographic_hoodie.jpg",
        "https://example.com/neon_sneakers.jpg",
        "https://example.com/techwear_pants.jpg",
        "https://example.com/led_cap.jpg"
    ]
})

st.title("🚀 Futuristic eCommerce Store")
st.write("Bringing you the latest in futuristic fashion!")

# Display products in columns
cols = st.columns(len(products))

cart = []
for i, col in enumerate(cols):
    with col:
        st.image(products.loc[i, "Image"], width=150)
        st.subheader(products.loc[i, "Product"])
        st.write(f"💰 Price: ${products.loc[i, 'Price']}")
        if st.button(f"Add to Cart {i}"):
            cart.append(products.loc[i])
            st.success(f"{products.loc[i, 'Product']} added to cart!")

# Display cart and checkout option
if cart:
    st.sidebar.header("🛒 Your Cart")
    total_price = 0
    for item in cart:
        st.sidebar.write(f"✅ {item['Product']} - ${item['Price']}")
        total_price += item['Price']
    st.sidebar.write(f"**Total Price: ${total_price}**")
    
    if st.sidebar.button("Proceed to Checkout"):
        st.sidebar.success("Redirecting to payment...")
        payment_method = st.sidebar.radio("Choose Payment Method", ["Credit Card", "PayPal", "Cryptocurrency"])
        card_details = ""
        if payment_method == "Credit Card":
            card_details = st.sidebar.text_input("Enter Card Details")
        elif payment_method == "PayPal":
            card_details = st.sidebar.text_input("Enter PayPal Email")
        elif payment_method == "Cryptocurrency":
            card_details = st.sidebar.text_input("Enter Crypto Wallet Address")
        
        if st.sidebar.button("Confirm Payment"):
            st.sidebar.success("Payment Successful! Your order is on the way!")

# User authentication placeholder
st.sidebar.subheader("🔐 Login / Signup")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
if st.sidebar.button("Login"):
    st.sidebar.success(f"Welcome, {username}!")

st.sidebar.markdown("---")
st.sidebar.write("Powered by **Streamlit** 🚀")
