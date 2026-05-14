# 💰 साधारण ब्याज Calculator

A Nepali Streamlit app for calculating Simple Interest (साधारण ब्याज).

---

# 📦 Files Included

- app.py
- requirements.txt
- README.md

---

# ▶️ Run Locally

## 1. Install Requirements

```bash
pip install -r requirements.txt
```

## 2. Start Streamlit App

```bash
streamlit run app.py
```

---

# ☁️ Deploy Online

## Option 1: Streamlit Community Cloud

1. Upload project to GitHub
2. Open:

https://share.streamlit.io/

3. Connect GitHub repository
4. Select:
   - Branch: main
   - File: app.py
5. Click Deploy

---

## Option 2: Render

1. Open:

https://render.com/

2. Create New Web Service
3. Connect GitHub repository
4. Use:

Build Command:
```bash
pip install -r requirements.txt
```

Start Command:
```bash
streamlit run app.py --server.port 10000 --server.address 0.0.0.0
```

---

# 🧮 Formula Used

Simple Interest Formula:

SI = (P × R × T) / 100

Where:

- P = Principal
- R = Rate
- T = Time

---

# ❤️ Built Using

- Python
- Streamlit
