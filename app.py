import streamlit as st
from groq import Groq
from fpdf import FPDF
import os

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    layout="wide"
)

st.title("🤖 Multi-Agent Research Assistant")
st.caption("Powered by Groq LLM (Fast • Reliable • No Rate Limits)")

# ---------------- GROQ CLIENT ----------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- INPUT ----------------
query = st.text_input(
    "Enter your research question:",
    placeholder="Compare Dell and ASUS laptops"
)

# ---------------- HELPERS ----------------
def clean_text(text: str) -> str:
    return (
        text.replace("—", "-")
            .replace("–", "-")
            .replace("’", "'")
            .replace("“", '"')
            .replace("”", '"')
            .replace("•", "-")
    )

def generate_response(user_query: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ CURRENT SUPPORTED MODEL
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional technology research analyst. "
                    "Provide clear, structured, and detailed comparisons using headings, "
                    "bullet points, pros/cons, and a concise final verdict. "
                    "Avoid markdown tables."
                ),
            },
            {"role": "user", "content": user_query},
        ],
        temperature=0.3,
        max_tokens=1200,
    )
    return response.choices[0].message.content

def safe_pdf_write(pdf, text):
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            pdf.ln(4)
            continue
        pdf.multi_cell(180, 8, line)

# ---------------- RUN BUTTON ----------------
if st.button("Run Research"):
    if not query.strip():
        st.warning("Please enter a research question.")
    else:
        with st.spinner("Analyzing with Groq LLM..."):
            result = generate_response(query)

        st.success("Research Completed!")

        # ---------------- DISPLAY ----------------
        st.subheader("📄 Generated Report")
        st.markdown(result)

        # ---------------- SAVE FILES ----------------
        os.makedirs("reports", exist_ok=True)

        # Save markdown
        md_path = "reports/output.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(result)

        # ---------------- PDF GENERATION (CRASH-SAFE) ----------------
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        cleaned_result = clean_text(result)
        safe_pdf_write(pdf, cleaned_result)

        pdf_path = "reports/output.pdf"
        pdf.output(pdf_path)

        # ---------------- DOWNLOAD BUTTON ----------------
        with open(pdf_path, "rb") as file:
            st.download_button(
                label="⬇️ Download PDF Report",
                data=file,
                file_name="research_report.pdf",
                mime="application/pdf"
            )
