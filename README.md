# 🧠 Smart Merge Request Assistant

This project demonstrates the use of AI tools to assist with managing pull requests (PRs), including:

- ✅ Automatic PR summarization  
- 📦 Changelog generation  
- 👥 Reviewer suggestions based on Git history

---

## 📁 Project Structure

AI-PULLREQUEST/
├── dummy_project/ # Simple Python project
│ ├── main.py
│ └── utils.py
├── pr_samples/ # Sample PR diffs
│ └── pr_001.diff # Example
├── scripts/ # AI/logic scripts
│ 
└── README.md

---

## 🚀 How to Run

### 1. Initial Requirement

- Python


## to run
python scripts/suggest_reviewers.py pr_diffs/pr1.diff 
python scripts/summarize_diff.py pr_diffs/pr1.diff 
python scripts/generate_changelog.py pr_diffs/pr1.diff 