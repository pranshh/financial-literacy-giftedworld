import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Financial Literacy || Gifted World",
                    page_icon="GW_logo.webp")

st.title("Financial Literacy || Gifted World Sep-Oct 2024")
st.header("Mentor: Meeta Kabra, TA: Pranshu Jaiswal")

week1 = pd.read_csv("Week 1.csv")
week2 = pd.read_csv("Week 2.csv")
week3 = pd.read_csv("Week 3.csv")
week4 = pd.read_csv("Week 4.csv")
certificates = pd.read_csv("Certificates.csv")

week = st.selectbox(
    "Choose week for its statistics",
    ("Week 1", "Week 2", "Week 3"),
    index=None,
    placeholder="Select Week...",
)

if week == "Week 1":
    with st.container():
        st.header("Week 1")

        st.write("Number of participants in Mentor Hour:", 32)
        st.write("Number of participants in TA Hour:", 20)
        
        st.write("Number of submissions:", len(week1))
        st.write("Total Marks:", 34)

        st.subheader("Week 1 Marks Distribution")
        data1 = week1["Score"]

        fig1, ax1 = plt.subplots(figsize=(3, 2))
        ax1.hist(data1, bins = 20)
        ax1.set_xlabel("Marks Distribution", fontsize = 7)
        ax1.tick_params(axis='both', which='major', labelsize=7)
        plt.tight_layout()
        ax1.set_ylabel("Frequency", fontsize = 7)

        st.pyplot(fig1, use_container_width=False)

if week == "Week 2":
    with st.container():
        st.header("Week 2")

        st.write("Number of participants in Mentor Hour:", 26)
        st.write("Number of participants in TA Hour:", 12)
        
        st.write("Number of submissions:", len(week2))
        st.write("Total Marks:", 23)

        st.subheader("Week 2 Marks Distribution")
        data2 = week2["Score"]

        fig2, ax2 = plt.subplots(figsize=(3, 2))
        ax2.hist(data2, bins = 20)
        ax2.set_xlabel("Marks Distribution", fontsize = 7)
        ax2.tick_params(axis='both', which='major', labelsize=7)
        plt.tight_layout()
        ax2.set_ylabel("Frequency", fontsize = 7)

        st.pyplot(fig2, use_container_width=False)

if week == "Week 3":
    with st.container():
        st.header("Week 3")

        st.write("Number of participants in Mentor Hour:", 23)
        st.write("Number of participants in TA Hour:", 10)
        
        st.write("Number of submissions:", len(week3))
        st.write("Total Marks:", 19)

        st.subheader("Week 3 Marks Distribution")
        data3 = week3["Score"]

        fig3, ax3 = plt.subplots(figsize=(3, 2))
        ax3.hist(data3, bins = 20)
        ax3.set_xlabel("Marks Distribution", fontsize = 7)
        ax3.tick_params(axis='both', which='major', labelsize=7)
        plt.tight_layout()
        ax3.set_ylabel("Frequency", fontsize = 7)

        st.pyplot(fig3, use_container_width=False)

if week == "Week 4":
    with st.container():
        st.header("Week 4")

        st.write("Number of participants in Mentor Hour:", 20)
        st.write("Number of participants in TA Hour:", 8)
        
        st.write("Number of submissions:", len(week4))
        st.write("Total Marks:", 29)

        st.subheader("Week 4 Marks Distribution")
        data4 = week4["Score"]

        fig4, ax4 = plt.subplots(figsize=(3, 2))
        ax4.hist(data4, bins = 20)
        ax4.set_xlabel("Marks Distribution", fontsize = 7)
        ax4.tick_params(axis='both', which='major', labelsize=7)
        plt.tight_layout()
        ax4.set_ylabel("Frequency", fontsize = 7)

        st.pyplot(fig4, use_container_width=False)

with st.container():
    st.table(certificates)