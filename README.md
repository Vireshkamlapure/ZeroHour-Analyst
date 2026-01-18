# ⏱️ ZeroHour Analyst

### Your Personal Data Science Mentor & Strategist

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://zerohour-analyst.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Gemini AI](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**ZeroHour Analyst** is an AI-powered tool designed for Data Science students and professionals. Unlike standard code generators that do the homework for you, this tool acts as a **Senior Mentor**. It analyzes your dataset's structure (metadata) and provides a strategic, theoretical roadmap to solve your specific problem.

## 🚀 Live Demo
**Try it here:** [https://zerohour-analyst.streamlit.app](https://zerohour-analyst-frshgnxjcwvjipgdlcbbzp.streamlit.app)

*(Note: If the app is asleep, click "Wake App" and wait a moment for it to boot up.)*

---

## 🧠 Key Features

* **Hybrid Analysis Engine:** Combines the strategic thinking of a "Senior Data Scientist" with the educational clarity of a "Professor."
* **Privacy-First Architecture:** Never sends your actual dataset rows to the AI. It only extracts and analyzes **metadata** (column names, types, and statistics), ensuring data privacy and speed.
* **Large Dataset Support:** capable of handling massive CSV/Excel files that would typically crash a browser-based analysis tool.
* **Critical Thinking Challenges:** Instead of giving copy-paste code, it generates specific logical hypotheses to test, encouraging students to write their own implementation.
* **Auto-Model Switching:** Automatically detects and switches between available Gemini models (`2.0-flash`, `2.0-flash-lite`, `1.5-flash`) for maximum reliability.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **AI Engine:** [Google Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/)
* **Data Processing:** Pandas, OpenPyXL
* **Deployment:** Streamlit Community Cloud

---

## 💻 Installation (Run Locally)

If you want to run this on your own machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Vireshkamlapure/ZeroHour-Analyst.git](https://github.com/Vireshkamlapure/ZeroHour-Analyst.git)
    cd ZeroHour-Analyst
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up API Keys**
    Create a file named `.streamlit/secrets.toml` in the root directory and add your Google Gemini API key:
    ```toml
    [general]
    gemini_api_key = "YOUR_AIza_KEY_HERE"
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/Vireshkamlapure/ZeroHour-Analyst/issues).

---

## 👤 Author

**Viresh Kamlapure**

* **GitHub:** [@Vireshkamlapure](https://github.com/Vireshkamlapure)
* **LinkedIn:** [viresh-kamlapure](https://www.linkedin.com/in/viresh-kamlapure-02102004v/)

---

*Developed with ❤️ for the Data Science Community.*
