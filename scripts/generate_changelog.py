# import sys
# import datetime

# def generate_changelog(diff_path):
#     with open(diff_path, 'r') as f:
#         diff = f.read()

#     modified = [line.split()[-1] for line in diff.splitlines() if line.startswith('+++ b/')]
#     today = datetime.datetime.today().strftime('%Y-%m-%d')

#     print("📝 Suggested Changelog Entry:")
#     print(f"- {today}: Updated logic in {', '.join(modified)}.")

# if __name__ == "__main__":
#     generate_changelog(sys.argv[1])


import os
import requests

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
REPO = os.environ['GITHUB_REPOSITORY']
PR_NUMBER = os.environ['PR_NUMBER']

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Step 1: Get PR title and body
pr_url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"
pr_resp = requests.get(pr_url, headers=headers)
pr_data = pr_resp.json()
pr_title = pr_data.get('title', '')
pr_body = pr_data.get('body', '')

# Step 2: Get list of files changed in this PR
files_url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}/files"
files_resp = requests.get(files_url, headers=headers)
changed_files = [f['filename'] for f in files_resp.json()]

# Step 3: Get the diff for each file
changelog_lines = []
for file in changed_files:
    # For demo: You could get the patch and parse "+" lines, but we'll just summarize file change
    filename = os.path.basename(file)
    if file.endswith('.py'):
        changelog_lines.append(f"Modified Python file: `{filename}`")
    elif file.endswith('.js'):
        changelog_lines.append(f"Modified JavaScript file: `{filename}`")
    elif file.endswith('.md'):
        changelog_lines.append(f"Updated documentation: `{filename}`")
    else:
        changelog_lines.append(f"Changed file: `{filename}`")

# Step 4: Compose Changelog message
body = (
    f"### 📝 **Changelog for PR #{PR_NUMBER}**\n"
    f"**PR Title:** {pr_title}\n\n"
    f"**Summary:** {pr_body}\n\n"
    f"**Structured Changelog:**\n"
    + "\n".join([f"- {line}" for line in changelog_lines])
)

# Step 5: Post comment to PR
comments_url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
comment_resp = requests.post(comments_url, headers=headers, json={"body": body})

print(body)