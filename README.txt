🤖 Multi-Agent Research Assistant
AI-Powered Research & Comparison Tool using Groq + Streamlit

An intelligent AI research assistant that generates clear, structured, and downloadable research reports for any analytical or comparison-based query.
Built using Streamlit and Groq LLM for high-speed, reliable inference with zero rate-limit issues.

🚀 Live Demo

🔗 Deployed App:

https://<your-app-name>.streamlit.app

🧠 Key Features

🔍 Accepts open-ended research & comparison queries

⚡ Powered by Groq LLM (ultra-fast inference)

📝 Produces professional, well-structured reports

Headings & subheadings

Comparative analysis

Pros & Cons

Final verdict

📄 Export research as:

Markdown (.md)

PDF (.pdf)

⬇️ One-click PDF download

🌐 Deployed globally using Streamlit Cloud

🔐 Secure API key handling via Streamlit Secrets

🛠️ Tech Stack
Technology	Role
Python	Core logic
Streamlit	Frontend UI
Groq API	Large Language Model
FPDF	PDF generation
GitHub	Version control
Streamlit Cloud	Deployment
📁 Project Structure
agent/
│── app.py               # Main Streamlit app
│── requirements.txt     # Dependencies
│── .gitignore           # Ignored files
│── reports/             # Generated reports
│── README.md            # Documentation

⚙️ Installation & Local Setup
1️⃣ Clone Repository
git clone https://github.com/sravan-jetangula/<repo-name>.git
cd <repo-name>

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Groq API Key
setx GROQ_API_KEY "your_groq_api_key"


Restart the terminal after setting the key.

5️⃣ Run the App
streamlit run app.py

🌍 Deployment (Streamlit Cloud)

Push the project to GitHub

Go to 👉 https://streamlit.io/cloud

Click New App

Select:

Repository

Branch

app.py

Add Secrets:

GROQ_API_KEY = "your_groq_api_key"


Deploy 🎉

🧪 Example Queries

Compare Dell and ASUS laptops

Python vs Java for Data Science

AWS vs Azure vs GCP

iOS vs Android security comparison

Machine Learning vs Deep Learning

📄 Sample Output

✔ Clear research format
✔ Technical accuracy
✔ Professional tone
✔ Exportable PDF
✔ Recruiter-ready presentation

🔒 Security & Best Practices

API keys managed via environment variables

No hard-coded secrets

.gitignore used for sensitive files

Production-ready deployment setup

🎯 Use Cases

Academic research

Technical comparisons

Business analysis

Product evaluation

Interview preparation

AI demo projects

🚧 Future Enhancements

🧠 Multi-agent workflow (CrewAI integration)

📥 DOCX export

📊 Auto-generated tables & charts

🗂 Research history

🔐 User authentication

🌐 Custom domain support

👨‍💻 Author

Sravan Jetangula
🎓 B.Tech – Artificial Intelligence & Machine Learning
💡 Data Analytics | AI | Machine Learning | Python

🔗 GitHub: https://github.com/sravan-jetangula

⭐ Support

If you find this project useful:

⭐ Star the repository

🔁 Share with others

💬 Feedback is welcome!

🔥 Recruiter Note

This project demonstrates:

LLM integration

API handling

Cloud deployment

Secure key management

Clean UI & documentation