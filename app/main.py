import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Set page configuration
st.set_page_config(
    page_title="Finance: Credit Risk Modelling",
    page_icon="📊",
    layout="centered"
)

# Add a banner or header
st.markdown(
    """
    <div style="background-color: #4CAF50; padding: 5px; border-radius: 5px;">
        <h3 style="color: white; text-align: center;">Finance: Credit Risk Modelling</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Description
# st.markdown("""
# Analyze the credit risk of borrowers with our advanced modelling tool.
# Provide the required details, and we'll predict the default probability, credit score, and rating.
# """)

# Main form for inputs
with st.form("credit_risk_form"):
    st.header("Borrower Information")

    # Create rows for better grouping
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28, help="Borrower's age")
    with col2:
        income = st.number_input('Income (₹)', min_value=0, value=1200000, help="Annual income of the borrower")
    with col3:
        loan_amount = st.number_input('Loan Amount (₹)', min_value=0, value=2560000, help="Loan amount requested")

    # Display Loan to Income Ratio
    loan_to_income_ratio = loan_amount / income if income > 0 else 0
    st.markdown(f"**Loan to Income Ratio:** {loan_to_income_ratio:.2f}")

    # More borrower details
    col4, col5, col6 = st.columns(3)
    with col4:
        loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
    with col5:
        avg_dpd_per_delinquency = st.number_input('Avg Days Past Due (DPD)', min_value=0, value=20)
    with col6:
        delinquency_ratio = st.number_input(
            'Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30
        )

    col7, col8, col9 = st.columns(3)
    with col7:
        credit_utilization_ratio = st.number_input(
            'Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30
        )
    with col8:
        num_open_accounts = st.number_input(
            'Number of Open Loan Accounts', min_value=1, max_value=4, step=1, value=2
        )
    with col9:
        residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])

    col10, col11, col12 = st.columns(3)
    with col10:
        loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
    with col11:
        loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

    # Add a submit button
    submitted = st.form_submit_button("Calculate Risk")

# # Handle the form submission
# if submitted:
#     # Call the prediction function
#     probability, credit_score, rating = predict(
#         age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
#         delinquency_ratio, credit_utilization_ratio, num_open_accounts,
#         residence_type, loan_purpose, loan_type
#     )
#
#     # Display results
#     st.success("Risk Analysis Completed!")
#     st.write(f"### Default Probability: {probability:.2%}")
#     st.write(f"### Credit Score: {credit_score}")
#     st.write(f"### Rating: {rating}")
# Handle the form submission
if submitted:
    # Call the prediction function
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    # Display results
    st.success("Risk Analysis Completed!")
    st.write(f"### Default Probability: {probability:.2%}")
    st.write(f"### Credit Score: {credit_score}")

    # Color code the rating
    if rating.lower() == "poor":
        color = "red"
    elif rating.lower() == "average":
        color = "orange"
    elif rating.lower() == "good":
        color = "green"
    else:
        color = "green"  # Default color for unexpected ratings

    st.markdown(f"### Rating: <span style='color:{color}'>{rating}</span>", unsafe_allow_html=True)


