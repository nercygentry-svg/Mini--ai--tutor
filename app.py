import streamlit as st

st.set_page_config(page_title="Mini AI Tutor", layout="centered")

st.title("📘 Grade 6 AI Math Tutor")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.history = []

def tutor_response(user_answer, step):
    if step == 0:
        return "What is 1/2 + 1/2?"
    
    elif step == 1:
        if "1" in user_answer:
            return "Correct! Now try this: What is 1/4 + 1/4?"
        else:
            return "Not quite. Remember: 1/2 means one out of two equal parts. Try again: 1/2 + 1/2 = ?"
    
    elif step == 2:
        if "1/2" in user_answer or "0.5" in user_answer:
            return "Good! Now harder one: If you have 3/4 of a pizza and eat 1/4, how much is left?"
        else:
            return "Think of quarters of a pizza. Try again."
    
    else:
        return "Great progress! You are improving step by step."

if st.session_state.step == 0:
    st.write("👩‍🏫 Tutor: Let's start learning fractions step by step.")
    st.session_state.step = 1

user_input = st.text_input("Your answer:")

if st.button("Submit"):
    response = tutor_response(user_input, st.session_state.step)
    st.session_state.history.append((user_input, response))
    st.session_state.step += 1
    st.write("🧠 Tutor:", response)

st.write("---")
st.write("### Conversation History")
for u, r in st.session_state.history:
    st.write(f"👨 Student: {u}")
    st.write(f"🧠 Tutor: {r}")
