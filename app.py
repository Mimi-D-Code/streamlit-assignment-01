
import streamlit as st

# ── Ex 01: Page Title ────────────────────────────────────────
st.title("🎓 Grade Calculator")
st.subheader("Calculate your academic performance")
st.markdown("---")

# ── Ex 02: Instructions ─────────────────────────────────────
st.markdown("""
### 📋 How to use this calculator
- Enter your scores in the four subjects.
- Choose your grading scale.
- Click **Calculate Grade** to see your result.
""")

st.info("Please enter scores between 0 and 100.")

# ── Ex 03: Subject Scores ────────────────────────────────────
st.markdown("### 📚 Enter Subject Scores")

subject1 = st.number_input(
    "Subject 1",
    min_value=0,
    max_value=100,
    value=0
)

subject2 = st.number_input(
    "Subject 2",
    min_value=0,
    max_value=100,
    value=0
)

subject3 = st.number_input(
    "Subject 3",
    min_value=0,
    max_value=100,
    value=0
)

subject4 = st.number_input(
    "Subject 4",
    min_value=0,
    max_value=100,
    value=0
)

# ── Ex 04: Grading Scale Selector ────────────────────────────
st.markdown("### ⚙️ Choose Grading Scale")

scale = st.radio(
    "Select grading system:",
    ["Standard (A-F)", "Strict (A-F)"],
    horizontal=True
)

# ── Ex 05: Additional Widgets ────────────────────────────────
show_details = st.checkbox("Show detailed subject results")

student_name = st.text_input("Student Name (Optional)")

# ── Ex 06: Calculate Button ──────────────────────────────────
if st.button("Calculate Grade 🎯"):

    scores = [subject1, subject2, subject3, subject4]

    average = sum(scores) / len(scores)

    # Standard grading scale
    if scale == "Standard (A-F)":

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

    # Strict grading scale
    else:

        if average >= 95:
            grade = "A"
        elif average >= 85:
            grade = "B"
        elif average >= 75:
            grade = "C"
        elif average >= 65:
            grade = "D"
        else:
            grade = "F"

    # ── Display Results ──────────────────────────────────────
    st.markdown("---")
    st.markdown("### 📊 Your Results")

    if grade == "A":
        st.success(f"🏆 Excellent! Your Grade is {grade}")

    elif grade == "B":
        st.success(f"👏 Very Good! Your Grade is {grade}")

    elif grade == "C":
        st.info(f"👍 Good! Your Grade is {grade}")

    elif grade == "D":
        st.warning(f"⚠️ Your Grade is {grade}. You need improvement.")

    else:
        st.error(f"❌ Your Grade is {grade}. You did not pass.")

    st.metric("Average Score", f"{average:.2f}%")

    if student_name.strip():
        st.write(f"**Student Name:** {student_name}")

    # Display individual subject scores
    if show_details:
        st.markdown("#### Subject Details")

        for i, score in enumerate(scores, start=1):
            st.write(f"Subject {i}: {score}/100")

        st.write(f"**Total Score:** {sum(scores)}/400")

