# AI Automation Lab

A collection of AI-powered automation workflows built with **n8n**, focused on practical agentic workflows, research automation, web intelligence, and AI-assisted decision making.

These projects started as experiments with n8n workflows and evolved into customized automation systems rather than simply importing templates.

---

## Projects

### 1. AI Research War Room
A multi-agent research workflow that investigates a topic from different perspectives and produces a consolidated research report.

The workflow uses specialized AI agents for:
- Technical research
- Industry and market research
- Critical analysis and fact-checking
- Final synthesis

The goal is to simulate a research team where multiple agents investigate independently before a lead agent combines their findings.

### 2. Autonomous Job Hunter & Resume Matcher
An AI-powered job analysis workflow that evaluates a job posting against a candidate profile.

It:
- Extracts job requirements
- Compares required skills with the candidate profile
- Calculates a match score
- Identifies matching and missing skills
- Highlights experience gaps
- Suggests resume improvements
- Generates interview preparation points
- Recommends **APPLY**, **CONSIDER**, or **SKIP**

The goal is to turn a job description into an actionable application strategy.

### 3. AI Company Intelligence Agent
An AI research agent designed to investigate a company using its website and publicly available pages.

It analyzes:
- Company overview
- Products and services
- AI and technology
- Target customers
- Careers and hiring information
- Competitors and alternatives
- Important company pages
- Research takeaways

The workflow is useful for company research, interview preparation, and understanding organizations before applying or reaching out.

### 4. Autonomous AI Crawler
An n8n-based web crawling workflow that automatically discovers and processes information from websites.

The workflow handles:
- Web page crawling
- HTML extraction
- Markdown conversion
- URL processing
- Duplicate removal
- Content filtering
- Structured information extraction

The crawler architecture can be adapted for different research and information-extraction use cases.

---

## Tech Stack

- n8n
- AI Agents
- OpenAI
- Tavily
- HTTP APIs
- Web Crawling
- Structured JSON Outputs
- JavaScript
- Workflow Automation

---

## Architecture

```
                    ┌─────────────────────┐
                    │      n8n Trigger     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Research / Input   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      AI Agents       │
                    │                      │
                    │  Research            │
                    │  Analysis            │
                    │  Intelligence        │
                    │  Decision Making     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Tools / Web / APIs  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Structured Output   │
                    └─────────────────────┘
```

---

## Why This Repository?

The purpose of this repository is to experiment with what can be built when **workflow automation + AI agents + external tools** are combined.

Instead of using AI only to generate text, these workflows focus on giving agents a job to perform:

- Research something
- Crawl information
- Compare evidence
- Analyze requirements
- Make decisions
- Produce structured outputs

---

## Getting Started

1. Install or run [n8n](https://n8n.io/).
2. Clone this repository.
3. Import the required `.json` workflow into n8n.
4. Configure the required API credentials.
5. Update the workflow inputs for your use case.
6. Execute the workflow manually or connect it to a trigger.

---

## Repository Structure

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

## Author

**Amirtha Ganesh R**
Data Science | Machine Learning | Generative AI | MLOps
