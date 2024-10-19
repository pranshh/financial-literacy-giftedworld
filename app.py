import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Financial Literacy || Gifted World",
                    page_icon="GW_logo.webp")

st.title("Financial Literacy || Gifted World Sep-Oct 2024")
st.header("Mentor: Meeta Kabra, TA: Pranshu Jaiswal")

week1 = pd.read_csv("Week 1.csv")
week2 = pd.read_csv("Week 2.csv")
week3 = pd.read_csv("Week 3.csv")
week4 = pd.read_csv("Week 4.csv")
certificates = pd.read_excel("Certificates.xlsx", sheet_name=None)

week = st.multiselect(
    "Choose week(s) for statistics",
    ["Week 1", "Week 2", "Week 3", "Week 4"],
    ["Week 1", "Week 2", "Week 3", "Week 4"]
)

def display_week_stats(week_name, week_data, prev_week_data=None):
    with st.container(border=True):
        st.header(week_name)

        col1, col2, col3 = st.columns(3)
        with col1:
            mentor_hour = {"Week 1": 32, "Week 2": 26, "Week 3": 23, "Week 4": 20}[week_name]
            optional_questions = {"Week 1": 11, "Week 2": 7, "Week 3": 5, "Week 4": 8}[week_name]
            st.metric(label="No of participants in Mentor Hour", value=mentor_hour)
            st.metric(label="No of optional questions", value=optional_questions)

        with col2:
            ta_hour = {"Week 1": 20, "Week 2": 12, "Week 3": 10, "Week 4": 8}[week_name]
            st.metric(label="No of participants in TA Hour", value=ta_hour)
            st.metric(label="No of submissions", value=len(week_data))

        with col3:
            total_marks = {"Week 1": 28, "Week 2": 23, "Week 3": 19, "Week 4": 29}[week_name]
            st.metric(label="Total marks", value=total_marks)

        st.subheader(f"{week_name} Marks Distribution")
        data = week_data["Score"]
        data_optional = week_data["Number of Optional Attempted"]

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

        ax1.hist(data, bins=20, edgecolor='black')
        ax1.set_xlabel("Marks", fontsize=10)
        ax1.set_ylabel("Frequency", fontsize=10)
        ax1.set_title("Marks Distribution", fontsize=12)
        ax1.tick_params(axis='both', which='major', labelsize=8)

        ax2.hist(data_optional, bins=30, edgecolor='black')
        ax2.set_xlabel("Number of Optional Questions Attempted", fontsize=10)
        ax2.set_ylabel("Frequency", fontsize=10)
        ax2.set_title("Distribution of Optional Questions Attempted", fontsize=12)
        ax2.tick_params(axis='both', which='major', labelsize=8)

        plt.tight_layout()
        st.pyplot(fig)

        st.subheader("Statistics")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(label="Mean Score", value=f"{data.mean():.2f}")
            st.metric(label="Mean Optional Questions", value=f"{data_optional.mean():.2f}")

        with col2:
            st.metric(label="Median Score", value=f"{data.median():.2f}")
            st.metric(label="Median Optional Questions", value=f"{data_optional.median():.2f}")

        with col3:
            st.metric(label="Score Std Dev", value=f"{data.std():.2f}")
            st.metric(label="Mode Optional Questions", value=f"{data_optional.mode().values[0]}")


if week:
    for selected_week in week:
        if selected_week == "Week 1":
            display_week_stats("Week 1", week1)
        elif selected_week == "Week 2":
            display_week_stats("Week 2", week2, week1)
        elif selected_week == "Week 3":
            display_week_stats("Week 3", week3, week2)
        elif selected_week == "Week 4":
            display_week_stats("Week 4", week4, week3)
else:
    st.write("Please select at least one week to display statistics.")

with st.container(border=True):
    st.subheader("Submissions")
    st.write("Number of active students:", 30)

    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine='xlsxwriter', engine_kwargs={'options': {'strings_to_numbers': True}}) as writer:
        for sheet_name, df in certificates.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    buffer.seek(0)

    st.download_button(
        label='📥 Download Certificates Data',
        data=buffer,
        file_name='Certificate List.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    labels = 'Certificate of Outstanding Performance', 'Certificate of Excellence', 'Certificate of Completion', 'No Certificate'
    sizes = [17, 3, 3, 7]
    explode = (0, 0, 0, 0.1)

    def autopct_format(pct, allvals):
        absolute = int(pct/100.*sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    fig5, ax5 = plt.subplots()
    ax5.pie(sizes, explode=explode, labels=labels, autopct=lambda pct: autopct_format(pct, sizes),
            shadow=True, startangle=90)
    ax5.axis('equal')

    ax5.set_title("Certificates Distribution") 
    st.pyplot(fig5)
