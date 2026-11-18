
import streamlit as st
import pandas as pd
import os

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI College Admission Assistant",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# 2. CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #F5F7FF,
        #EEF2FF,
        #F8FAFF
    );
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

h1, h2, h3 {
    color: #172554;
    font-weight: 800;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #101B3C,
        #25245C
    );
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.stButton > button {
    background: linear-gradient(
        90deg,
        #4F46E5,
        #7C3AED
    );
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 20px;
    font-weight: bold;
}

.stButton > button:hover {
    background: #3730A3;
    color: white;
}

[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #E0E7FF;
    box-shadow: 0 4px 12px rgba(30,41,100,0.05);
}

.stTextInput input,
.stNumberInput input {
    border-radius: 10px;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. COLLEGE DATABASE FUNCTION
# ==========================================

def load_colleges():

    if os.path.exists("colleges.csv"):

        df = pd.read_csv("colleges.csv")

        required_columns = [
            "college_name",
            "course",
            "location",
            "fees",
            "minimum_percentage"
        ]

        if all(col in df.columns for col in required_columns):
            return df

        st.error("Your colleges.csv file has incorrect column names.")
        st.stop()

    else:

        st.error(
            "colleges.csv not found! "
            "Please keep it in the same folder as app.py."
        )

        st.stop()


# ==========================================
# 4. SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("🎓 Admission Assistant")

st.sidebar.write("Your Smart College Guide")

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "College Search",
        "Eligibility Checker",
        "AI Chatbot",
        "College Recommendations"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Your future starts with the right college!"
)


# ==========================================
# 5. HOME PAGE
# ==========================================

if menu == "Home":

    # HERO SECTION
    st.markdown("""
    <style>
    .hero-box {
        background: linear-gradient(120deg, #101B3C, #4338CA, #7C3AED);
        padding: 40px;
        border-radius: 20px;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="hero-box">
            <h4 style="color:#C7D2FE;">
                YOUR FUTURE STARTS HERE
            </h4>
            <h1 style="color:white;">
                Discover Your Dream College 🎓
            </h1>
            <p style="color:#E0E7FF;font-size:17px;">
                Your intelligent companion for college admissions.
                Explore colleges, check eligibility and discover
                the right academic opportunities with AI.
            </p>
            <h4 style="color:white;">
                ✨ Smart Admissions. Smarter Future.
            </h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # DASHBOARD
    st.header("📊 Your Admission Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Platform Tools", "04")
    c2.metric("AI Assistant", "Active")
    c3.metric("College Search", "Explore")
    c4.metric("Eligibility", "Check")

    st.divider()

    # SERVICES
    st.header("🚀 Explore Our Services")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("🏫 College Search")
            st.write("Explore colleges and available courses.")

        with st.container(border=True):
            st.subheader("📋 Eligibility Checker")
            st.write("Check your academic eligibility.")

    with col2:
        with st.container(border=True):
            st.subheader("🤖 AI Chatbot")
            st.write("Get answers to admission questions.")

        with st.container(border=True):
            st.subheader("🎯 College Recommendations")
            st.write("Discover colleges matching your marks.")

    st.divider()

    # HOW IT WORKS
    st.header("🧭 How It Works")

    s1, s2, s3, s4 = st.columns(4)

    s1.write("### 01")
    s1.write("👨‍🎓 Student Details")

    s2.write("### 02")
    s2.write("🔍 College Search")

    s3.write("### 03")
    s3.write("📊 Check Eligibility")

    s4.write("### 04")
    s4.write("🤖 AI Guidance")

    st.success("Your future starts with the right college! 🎓")


# ==========================================
# 6. COLLEGE SEARCH
# ==========================================

elif menu == "College Search":

    st.header("🏫 College Search")

    df = load_colleges()

    st.write("Find colleges based on your preferred course.")

    courses = ["All Courses"] + sorted(
        df["course"].dropna().unique().tolist()
    )

    course = st.selectbox(
        "Select Course",
        courses
    )

    location = st.selectbox(
        "Select Location",
        ["All Locations"] + sorted(
            df["location"].dropna().unique().tolist()
        )
    )

    results = df.copy()

    if course != "All Courses":
        results = results[results["course"] == course]

    if location != "All Locations":
        results = results[results["location"] == location]

    st.subheader("Available Colleges")

    st.success(f"Found {len(results)} colleges.")

    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# 7. ELIGIBILITY CHECKER
# ==========================================

elif menu == "Eligibility Checker":

    st.header("🎓 Student Eligibility Checker")

    st.write(
        "Enter your academic details to check "
        "matching college eligibility."
    )

    student_name = st.text_input("Enter Student Name")

    percentage = st.number_input(
        "Enter 12th Standard Percentage",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=0.5
    )

    df = load_colleges()

    courses = sorted(df["course"].dropna().unique().tolist())

    course = st.selectbox(
        "Select Preferred Course",
        courses,
        key="eligibility_course"
    )

    if st.button("Check My Eligibility"):

        if not student_name.strip():

            st.warning("Please enter your name.")

        else:

            course_data = df[
                df["course"] == course
            ]

            eligible = course_data[
                course_data["minimum_percentage"] <= percentage
            ]

            st.subheader("Eligibility Results")

            if not eligible.empty:

                st.success(
                    f"Congratulations {student_name}! "
                    "You meet the sample eligibility criteria."
                )

                st.dataframe(
                    eligible,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.error(
                    "No matching colleges found. "
                    "Try another course or improve your marks."
                )

    st.caption(
        "Note: This is a demonstration. Actual admission "
        "eligibility depends on official college rules."
    )


# ==========================================
# 8. AI CHATBOT
# ==========================================

elif menu == "AI Chatbot":

    st.header("🤖 AI College Admission Assistant")

    st.write(
        "Hello! Ask me about admissions, courses, fees "
        "and required documents."
    )

    def get_response(question):

        q = question.lower()

        if any(word in q for word in ["hello", "hi", "hey"]):

            return (
                "Hello! 👋 Welcome to your College Admission "
                "Assistant. How can I help you today?"
            )

        elif "document" in q or "certificate" in q:

            return (
                "Common admission documents include:\n"
                "1. 10th marksheet\n"
                "2. 12th marksheet\n"
                "3. Transfer certificate\n"
                "4. ID proof\n"
                "5. Passport-size photographs\n"
                "6. Category certificate, if applicable."
            )

        elif "admission" in q or "apply" in q:

            return (
                "To apply for college admission:\n"
                "1. Visit the official college website.\n"
                "2. Check admission eligibility.\n"
                "3. Complete the application form.\n"
                "4. Upload required documents.\n"
                "5. Pay the application fee, if applicable.\n"
                "6. Track your application status."
            )

        elif "fee" in q or "fees" in q:

            return (
                "College fees depend on the institution "
                "and course. Please check the official "
                "college website for updated fee details."
            )

        elif "eligibility" in q or "percentage" in q:

            return (
                "Eligibility depends on your course, marks "
                "and college admission rules. Use our "
                "Eligibility Checker to explore matching colleges."
            )

        elif "course" in q or "courses" in q:

            return (
                "Popular courses include B.Tech CSE, "
                "B.Tech ECE, BCA and BBA. Course availability "
                "depends on the college."
            )

        elif "college" in q:

            return (
                "Use our College Search feature to explore "
                "colleges based on your preferred course and location."
            )

        elif "scholarship" in q:

            return (
                "Scholarships may be available based on merit, "
                "income, category and government schemes. "
                "Check official scholarship portals and college websites."
            )

        else:

            return (
                "I can help with admission procedures, "
                "documents, fees, courses, scholarships "
                "and eligibility. Please ask another question."
            )

    # CHAT HISTORY

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    question = st.chat_input(
        "Ask your admission question..."
    )

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        answer = get_response(question)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        with st.chat_message("assistant"):
            st.write(answer)

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# ==========================================
# 9. COLLEGE RECOMMENDATIONS
# ==========================================

elif menu == "College Recommendations":

    st.header("🎯 Personalized College Recommendations")

    st.write(
        "Find colleges based on your marks, "
        "preferred course and location."
    )

    df = load_colleges()

    percentage = st.number_input(
        "Enter your 12th percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        key="recommendation_percentage"
    )

    courses = sorted(
        df["course"].dropna().unique().tolist()
    )

    course = st.selectbox(
        "Choose your preferred course",
        courses,
        key="recommendation_course"
    )

    locations = ["All Locations"] + sorted(
        df["location"].dropna().unique().tolist()
    )

    location = st.selectbox(
        "Choose your preferred location",
        locations,
        key="recommendation_location"
    )

    if st.button("Find My Colleges"):

        results = df[
            (df["course"] == course) &
            (df["minimum_percentage"] <= percentage)
        ]

        if location != "All Locations":

            results = results[
                results["location"] == location
            ]

        st.subheader("Your Recommended Colleges")

        if not results.empty:

            st.success(
                f"We found {len(results)} matching colleges!"
            )

            for index, college in results.iterrows():

                with st.container(border=True):

                    st.subheader(
                        "🏫 " + str(college["college_name"])
                    )

                    st.write(
                        "📚 Course:",
                        college["course"]
                    )

                    st.write(
                        "📍 Location:",
                        college["location"]
                    )

                    st.write(
                        "💰 Fees: ₹",
                        format(int(college["fees"]), ",")
                    )

                    st.write(
                        "📊 Minimum Percentage:",
                        str(college["minimum_percentage"]) + "%"
                    )

        else:

            st.warning(
                "No matching colleges found. "
                "Try changing your preferences."
            )

    st.caption(
        "Recommendations use sample data. Always verify "
        "official admission criteria and fees."
    )


# ==========================================
# 10. FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#64748B;">
        🎓 AI-Powered College Admission Assistant
        <br>
        Your Smart Guide to College Admissions
    </div>
    """,
    unsafe_allow_html=True
)
