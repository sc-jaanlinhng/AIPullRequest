import re
from collections import Counter
import sys

def parse_git_log(file_path):
    with open(file_path) as f:
        log = f.read()

    file_authors = {}
    commits = log.strip().split('commit ')
    for commit in commits:
        author = re.search(r'Author: (.+?) <', commit)
        if not author:
            continue
        author = author.group(1)
        files = re.findall(r'\n    ([^\n]+\.py)', commit)
        for file in files:
            file_authors.setdefault(file.strip(), []).append(author)

    return file_authors

def suggest_reviewers(diff_path, git_log_path):
    with open(diff_path) as f:
        diff = f.read()

    changed_files = [line.split()[-1].replace('b/', '') for line in diff.splitlines() if line.startswith('+++ b/')]

    file_authors = parse_git_log(git_log_path)
    reviewers = []

    for file in changed_files:
        reviewers += file_authors.get(file, [])

    top_reviewers = Counter(reviewers).most_common(3)
    print("👥 Suggested Reviewers:")
    for name, count in top_reviewers:
        print(f" - {name} (worked on {count} related changes)")

if __name__ == "__main__":
    suggest_reviewers(sys.argv[1], 'data/git_log_sample.txt')
