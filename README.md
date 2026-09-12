<div align="center">

# 🤖 AI Automation Lab

### Autonomous agents that actually *do* the work not just talk about it.

![n8n](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Status](https://img.shields.io/badge/status-experimental-orange?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

</div>

---

## ⚡ What is this?

A collection of **AI-powered automation workflows** built with n8n focused on agentic research, web intelligence, and AI-assisted decision-making.

These aren't copy-pasted templates. They started as experiments and evolved into full-blown **autonomous systems** that research, analyze, crawl, and decide while you grab a coffee. ☕

> 💡 Instead of using AI to just *generate text*, these workflows give agents an actual **job to do**.

---

## 🚀 Projects

### 🕵️ 1. AI Research War Room
*Multiple AI agents walk into a research topic. One report walks out.*

A multi-agent workflow that investigates a topic from every angle and consolidates it into one clean report.

| Agent | Role |
|---|---|
| 🔬 Technical | Deep-dives the tech |
| 📈 Market | Industry & competitive landscape |
| 🧐 Critical | Fact-checks & pressure-tests findings |
| 🧠 Synthesis | Combines everything into the final report |

---

### 💼 2. Autonomous Job Hunter & Resume Matcher
*Stop guessing if you're a fit. Let the agent do the math.*

Feeds a job posting + your profile into an AI pipeline that:
- ✅ Extracts job requirements
- 🎯 Calculates a match score
- 🔍 Flags matching & missing skills
- 📊 Highlights experience gaps
- ✍️ Suggests resume tweaks
- 🗣️ Preps you for the interview
- 🚦 Verdict: **APPLY** / **CONSIDER** / **SKIP**

---

### 🏢 3. AI Company Intelligence Agent
*Know the company before they know you.*

Points an AI agent at a company's public web presence and returns a full intel report:

`Overview` · `Products` · `AI/Tech Stack` · `Target Customers` · `Hiring Signals` · `Competitors` · `Key Pages` · `Takeaways`

Perfect for interview prep, cold outreach, or just nosy research. 👀

---

### 🕸️ 4. Autonomous AI Crawler
*Point it at the web. Get structured data back.*

An n8n-based crawler that discovers, extracts, and cleans web content on autopilot:

`Crawl` → `Extract HTML` → `Convert to Markdown` → `Dedupe` → `Filter` → `Structure`

Adaptable architecture — plug it into any research or extraction use case.

---

## 🛠️ Tech Stack

<div align="left">

`n8n` • `AI Agents` • `OpenAI` • `Tavily` • `HTTP APIs` • `Web Crawling` • `Structured JSON` • `JavaScript` • `Workflow Automation`

</div>

---

## 🏗️ Architecture

```
                    ┌─────────────────────┐
                    │      n8n Trigger     │  ⚡
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Research / Input   │  📥
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      AI Agents       │  🧠
                    │  Research            │
                    │  Analysis            │
                    │  Intelligence        │
                    │  Decision Making     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Tools / Web / APIs  │  🔧
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Structured Output   │  📦
                    └─────────────────────┘
```

---

## 🎯 Why This Repo Exists

Most "AI projects" stop at generating text. These don't.

Every workflow here is built to:

🔎 Research something → 🕸️ Crawl information → ⚖️ Compare evidence → 🧮 Analyze requirements → 🚦 Make decisions → 📦 Ship structured output

---

## 🏁 Getting Started

1. 📦 Install or run [n8n](https://n8n.io/)
2. 🍴 Clone this repository
3. 📥 Import the `.json` workflow you want into n8n
4. 🔑 Configure your API credentials
5. ⚙️ Update workflow inputs for your use case
6. ▶️ Run it manually — or wire it to a trigger and let it fly

---

## 📁 Repository Structure

```
AI-Automation-Lab/
│
├── AI_Research_War_Room_n8n.json
├── Autonomous_Job_Hunter_Resume_Matcher_n8n.json
├── AI_Company_Intelligence_Agent_n8n.json
├── Autonomous_AI_Crawler.json
│
└── README.md
```

---

## ⚠️ Disclaimer


 Don't let the robots make your life choices for you.  We are more than that .

---

<div align="center">

## 👤 Author

**Amirtha Ganesh R**

*Data Science | Machine Learning | Generative AI | MLOps*

⭐ **If this repo helped you, consider dropping a star!** ⭐

</div>
