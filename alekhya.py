import streamlit as st
 
# App Configuration
st.set_page_config(page_title="TradeX - Smart Barter & UPI Exchange", layout="wide")
 
# Sidebar Navigation
st.sidebar.title("📲 TradeX Menu")
menu = st.sidebar.radio("Navigate", ["Home", "List an Item", "Browse Trades", "My Trades", "Wallet"])
 
# Helper Function
def display_item_card(item):
    st.markdown(f"""
    ### {item['title']}
    **Category:** {item['category']}  
    **Offered:** {item['have']}  
    **Wants:** {item['want']}  
    **Estimated Value:** ₹{item['value']}  
    """)
    if st.button(f"💬 Propose Trade with {item['title']}", key=item['title']):
        st.info("This would initiate a chat/trade negotiation in a full app.")
 
# Sample Listings
sample_items = [
    {"title": "Yamaha Guitar", "category": "Instruments", "have": "Guitar", "want": "DSLR Camera", "value": 3000},
    {"title": "Python Tutoring", "category": "Services", "have": "Python Lessons", "want": "Tablet / ₹", "value": 2000},
    {"title": "Bluetooth Speaker", "category": "Electronics", "have": "Speaker", "want": "Books / ₹", "value": 1000},
]
 
# Pages
if menu == "Home":
    st.title("📦 Welcome to TradeX")
    st.subheader("Trade. Exchange. Pay Smart.")
    st.write("TradeX lets you barter goods and services with others, or fill trade gaps using UPI.")
    st.image("https://cdn.pixabay.com/photo/2016/01/19/17/44/trade-1143731_960_720.jpg", width=600)
    st.markdown("**Quick Actions:**")
    st.button("➕ List an Item")
    st.button("🔍 Browse Trades")
    st.button("💼 Go to Wallet")
 
elif menu == "List an Item":
    st.title("➕ List an Item or Service")
    title = st.text_input("Title (e.g., Guitar for Camera)")
    category = st.selectbox("Category", ["Electronics", "Books", "Services", "Instruments", "Others"])
    have = st.text_input("What are you offering?")
    want = st.text_input("What do you want in return?")
    value = st.number_input("Estimated Value (in ₹)", min_value=0, step=100)
    image = st.file_uploader("Upload an image (optional)", type=["jpg", "png", "jpeg"])
    if st.button("List Now"):
        st.success(f"Your item '{title}' has been listed!")
        st.info("In a full app, this would save to the database.")
 
elif menu == "Browse Trades":
    st.title("🔍 Browse Listings")
    for item in sample_items:
        display_item_card(item)
 
elif menu == "My Trades":
    st.title("💼 My Trades")
    st.info("This section will show your active, pending, and completed trades.")
    st.warning("You don't have any active trades yet.")
 
elif menu == "Wallet":
    st.title("💰 UPI Wallet")
    st.write("In a full version, you'd link your UPI apps like Google Pay or PhonePe.")
    st.info("You can use UPI to settle partial trades, delivery, or service charges.")
    st.button("🔗 Link UPI Account")
    st.metric("Trade Tokens", 0)
    st.metric("Total ₹ Saved via Trades", 0)