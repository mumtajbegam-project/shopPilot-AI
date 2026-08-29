import streamlit as st
import json
import re

st.set_page_config(
    page_title="ShopPilot AI",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ ShopPilot AI")
st.subheader("Your AI-Powered Shopping Assistant")

st.write(
    "Tell me what you are looking for, and I will recommend products based on your needs."
)

user_query = st.text_input(
    "What are you looking for?",
    placeholder="Example: I need a laptop under 60000 for coding"
)

if user_query:

    with open("data/products.json", "r") as file:
        products = json.load(file)

    # Find budget from user query
    numbers = re.findall(r'\d+', user_query.replace(",", ""))

    budget = None

    if numbers:
        budget = int(numbers[0])

    # Filter products based on budget
    recommended_products = products

    if budget:
        recommended_products = [
            product for product in products
            if product["price"] <= budget
        ]

    st.success("AI has analyzed your shopping requirement!")

    if budget:
        st.write(f"💰 Your budget: ₹{budget:,}")

    st.subheader("🤖 Recommended Products")

    if recommended_products:

        # Sort by rating
        recommended_products = sorted(
            recommended_products,
            key=lambda x: x["rating"],
            reverse=True
        )

        for index, product in enumerate(recommended_products):

            if index == 0:
                st.success("🏆 Best Recommendation")

            st.write(f"### {product['name']}")
            st.write(f"💰 Price: ₹{product['price']:,}")
            st.write(f"⭐ Rating: {product['rating']}")
            st.write(
                "Features: " + ", ".join(product["features"])
            )

            if "coding" in user_query.lower():
                st.info(
                    f"Why recommended: {product['name']} is suitable for coding based on its specifications and rating."
                )

            st.divider()

    else:
        st.warning(
            "Sorry! No products were found within your budget."
        )