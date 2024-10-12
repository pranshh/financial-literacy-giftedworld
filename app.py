import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from tempfile import NamedTemporaryFile

st.set_page_config(page_title="Financial Literacy || Gifted World",
                    page_icon="GW_logo.webp")

st.title("Financial Literacy || Gifted World Sep-Oct 2024")
st.header("Mentor: Meeta Kabra, TA: Pranshu Jaiswal")

week1 = pd.read_csv("Week 1.csv")
week2 = pd.read_csv("Week 2.csv")
week3 = pd.read_csv("Week 3.csv")
week4 = pd.read_csv("Week 4.csv")
certificates = pd.read_excel("Certificates.xlsx", sheet_name=None)

week = st.selectbox(
    "Choose week for its statistics",
    ("Week 1", "Week 2", "Week 3", "Week 4"),
    index=None,
    placeholder="Select Week...",
)

if week == "Week 1":
    with st.container(border=True):
        st.header("Week 1")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="No of participants in Mentor Hour", value=32)
            st.metric(label="No of optional questions", value=11)

        with col2:
            st.metric(label="No of participants in TA Hour", value=20)
            st.metric(label="No of submissions", value=len(week1))

        with col3:
            st.metric(label="Total marks", value=28)


        st.subheader("Week 1 Marks Distribution")
        data1 = week1["Score"]
        data1_1 = week1["Number of Optional Attempted"]

        fig1, (ax1, ax1_1) = plt.subplots(2, 1, figsize=(6, 8))

        ax1.hist(data1, bins=20, edgecolor='black')
        ax1.set_xlabel("Marks", fontsize=10)
        ax1.set_ylabel("Frequency", fontsize=10)
        ax1.set_title("Marks Distribution", fontsize=12)
        ax1.tick_params(axis='both', which='major', labelsize=8)

        ax1_1.hist(data1_1, bins=30, edgecolor='black')
        ax1_1.set_xlabel("Number of Optional Questions Attempted", fontsize=10)
        ax1_1.set_ylabel("Frequency", fontsize=10)
        ax1_1.set_title("Distribution of Optional Questions Attempted", fontsize=12)
        ax1_1.tick_params(axis='both', which='major', labelsize=8)

        plt.tight_layout()
        st.pyplot(fig1)

        st.subheader("Statistics")
        col1, col2 = st.columns(2)

        with col1:
            st.write("Marks")
            st.write(f"Mean: {data1.mean():.2f}")
            st.write(f"Median: {data1.median():.2f}")
            st.write(f"Standard Deviation: {data1.std():.2f}")

        with col2:
            st.write("Optional Questions")
            st.write(f"Mean: {data1_1.mean():.2f}")
            st.write(f"Median: {data1_1.median():.2f}")
            st.write(f"Mode: {data1_1.mode().values[0]}")

if week == "Week 2":
    with st.container():
        st.header("Week 2")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="No of participants in Mentor Hour", value=26, delta=-6, delta_color="normal")
            st.metric(label="No of optional questions", value=7, delta=-4, delta_color="normal")

        with col2:
            st.metric(label="No of participants in TA Hour", value=12, delta=-8, delta_color="normal")
            st.metric(label="No of submissions", value=len(week2), delta=-4, delta_color="normal")

        with col3:
            st.metric(label="Total marks", value=23, delta=-11, delta_color="normal")

        st.subheader("Week 2 Marks Distribution")
        data2 = week2["Score"]
        data2_1 = week2["Number of Optional Attempted"]

        fig2, (ax2, ax2_1) = plt.subplots(2, 1, figsize=(6, 8))

        ax2.hist(data2, bins=20, edgecolor='black')
        ax2.set_xlabel("Marks", fontsize=10)
        ax2.set_ylabel("Frequency", fontsize=10)
        ax2.set_title("Marks Distribution", fontsize=12)
        ax2.tick_params(axis='both', which='major', labelsize=8)

        ax2_1.hist(data2_1, bins=30, edgecolor='black')
        ax2_1.set_xlabel("Number of Optional Questions Attempted", fontsize=10)
        ax2_1.set_ylabel("Frequency", fontsize=10)
        ax2_1.set_title("Distribution of Optional Questions Attempted", fontsize=12)
        ax2_1.tick_params(axis='both', which='major', labelsize=8)

        plt.tight_layout()
        st.pyplot(fig2)

        st.subheader("Statistics")
        col1, col2 = st.columns(2)

        with col1:
            st.write("Marks")
            st.write(f"Mean: {data2.mean():.2f}")
            st.write(f"Median: {data2.median():.2f}")
            st.write(f"Standard Deviation: {data2.std():.2f}")

        with col2:
            st.write("Optional Questions")
            st.write(f"Mean: {data2_1.mean():.2f}")
            st.write(f"Median: {data2_1.median():.2f}")
            st.write(f"Mode: {data2_1.mode().values[0]}")

if week == "Week 3":
    with st.container():
        st.header("Week 3")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="No of participants in Mentor Hour", value=23, delta=-3, delta_color="normal")
            st.metric(label="No of optional questions", value=5, delta=-2, delta_color="normal")

        with col2:
            st.metric(label="No of participants in TA Hour", value=10, delta=-2, delta_color="normal")
            st.metric(label="No of submissions", value=len(week3), delta=-2, delta_color="normal")

        with col3:
            st.metric(label="Total marks", value=19, delta=-4, delta_color="normal")

        st.subheader("Week 3 Marks Distribution")
        data3 = week3["Score"]
        data3_1 = week3["Number of Optional Attempted"]

        fig3, (ax3, ax3_1) = plt.subplots(2, 1, figsize=(6, 8))

        ax3.hist(data3, bins=20, edgecolor='black')
        ax3.set_xlabel("Marks", fontsize=10)
        ax3.set_ylabel("Frequency", fontsize=10)
        ax3.set_title("Marks Distribution", fontsize=12)
        ax3.tick_params(axis='both', which='major', labelsize=8)

        ax3_1.hist(data3_1, bins=30, edgecolor='black')
        ax3_1.set_xlabel("Number of Optional Questions Attempted", fontsize=10)
        ax3_1.set_ylabel("Frequency", fontsize=10)
        ax3_1.set_title("Distribution of Optional Questions Attempted", fontsize=12)
        ax3_1.tick_params(axis='both', which='major', labelsize=8)

        plt.tight_layout()
        st.pyplot(fig3)

        st.subheader("Statistics")
        col1, col2 = st.columns(2)

        with col1:
            st.write("Marks")
            st.write(f"Mean: {data3.mean():.2f}")
            st.write(f"Median: {data3.median():.2f}")
            st.write(f"Standard Deviation: {data3.std():.2f}")

        with col2:
            st.write("Optional Questions")
            st.write(f"Mean: {data3_1.mean():.2f}")
            st.write(f"Median: {data3_1.median():.2f}")
            st.write(f"Mode: {data3_1.mode().values[0]}")

if week == "Week 4":
    with st.container():
        st.header("Week 4")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="No of participants in Mentor Hour", value=20, delta=-3, delta_color="normal")
            st.metric(label="No of optional questions", value=8, delta=3, delta_color="normal")

        with col2:
            st.metric(label="No of participants in TA Hour", value=8, delta=-2, delta_color="normal")
            st.metric(label="No of submissions", value=len(week3), delta=-1, delta_color="normal")

        with col3:
            st.metric(label="Total marks", value=29, delta=10, delta_color="normal")


        st.subheader("Week 4 Marks Distribution")
        data4 = week4["Score"]
        data4_1 = week4["Number of Optional Attempted"]

        fig4, (ax4, ax4_1) = plt.subplots(2, 1, figsize=(6, 8))

        ax4.hist(data4, bins=20, edgecolor='black')
        ax4.set_xlabel("Marks", fontsize=10)
        ax4.set_ylabel("Frequency", fontsize=10)
        ax4.set_title("Marks Distribution", fontsize=12)
        ax4.tick_params(axis='both', which='major', labelsize=8)

        ax4_1.hist(data4_1, bins=30, edgecolor='black')
        ax4_1.set_xlabel("Number of Optional Questions Attempted", fontsize=10)
        ax4_1.set_ylabel("Frequency", fontsize=10)
        ax4_1.set_title("Distribution of Optional Questions Attempted", fontsize=12)
        ax4_1.tick_params(axis='both', which='major', labelsize=8)

        plt.tight_layout()
        st.pyplot(fig4)

        st.subheader("Statistics")
        col1, col2 = st.columns(2)

        with col1:
            st.write("Marks")
            st.write(f"Mean: {data4.mean():.2f}")
            st.write(f"Median: {data4.median():.2f}")
            st.write(f"Standard Deviation: {data4.std():.2f}")

        with col2:
            st.write("Optional Questions")
            st.write(f"Mean: {data4_1.mean():.2f}")
            st.write(f"Median: {data4_1.median():.2f}")
            st.write(f"Mode: {data4_1.mode().values[0]}")

with st.container(border=True):
    st.subheader("Submissions")
    st.write("Number of active students:", 30)

    with NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        with pd.ExcelWriter(tmp.name, engine='xlsxwriter') as writer:
            for sheet_name, df in certificates.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)

        tmp.close()

    st.download_button(label='📥 Download Certificates Data',
                    data=open(tmp.name, 'rb').read(),
                    file_name='Certificates.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    os.remove(tmp.name)

    labels = 'Certificate of Outstanding Performance', 'Certificate of Excellence', 'Certificate of Completion', 'No Certificate'
    sizes = [12, 3, 5, 10]
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
