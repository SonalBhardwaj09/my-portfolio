import streamlit as st
import matplotlib.pyplot as plt

def calculate_loan(principal, rate, time, loan_type):
    try:
        principal = float(principal)
        rate = float(rate) / 100.0
        time = float(time)

        if loan_type == "Home Loan":
            total_amount = principal * (1 + rate) ** time
            interest = total_amount - principal
        elif loan_type == "Personal Loan":
            interest = (principal * rate * time) / 100
            total_amount = principal + interest
        elif loan_type == "Car Loan":
            interest = (principal * rate * time) / 100
            total_amount = principal + interest

        # Calculate monthly payment (EMI) for both simple and compound interest
        num_payments = time * 12  # Assuming monthly payments
        monthly_payment_simple = total_amount / num_payments
        monthly_payment_compound = total_amount * rate / 12 / (1 - (1 + rate / 12) ** (-num_payments))

        return total_amount, interest, monthly_payment_simple, monthly_payment_compound
    except ValueError:
        return None, None, None, None

st.title("Loan Calculator")

# Sidebar
st.sidebar.title("Input Parameters")
principal = st.sidebar.text_input("Principal (₹)", "100000")
rate = st.sidebar.slider("Annual Interest Rate (%)", 0.1, 50.0, 10.0)
time = st.sidebar.slider("Time (years)", 1, 30, 10)
loan_type = st.sidebar.radio("Loan Type", ["Home Loan", "Personal Loan", "Car Loan"])

# Calculate loan
total_amount, interest, monthly_payment_simple, monthly_payment_compound = calculate_loan(principal, rate, time, loan_type)

# Display result
st.write(f"### Total amount after interest: ₹{total_amount:.2f}" if total_amount else "")
st.write(f"### Interest: ₹{interest:.2f}" if interest else "")

# Monthly payment analysis
if monthly_payment_simple and monthly_payment_compound:
    st.write("#### Monthly Payment (EMI) Analysis:")
    st.write(f"- Monthly Payment (Simple Interest): ₹{monthly_payment_simple:.2f}")
    st.write(f"- Monthly Payment (Compound Interest): ₹{monthly_payment_compound:.2f}")

# Plot pie chart
if total_amount and interest:
    labels = ['Principal', 'Interest']
    sizes = [principal, interest]
    colors = ['#ff9999', '#66b3ff']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Loan Breakdown')
    st.pyplot(fig)
