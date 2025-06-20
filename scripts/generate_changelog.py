import sys
import datetime

def generate_changelog(diff_path):
    with open(diff_path, 'r') as f:
        diff = f.read()

    modified = [line.split()[-1] for line in diff.splitlines() if line.startswith('+++ b/')]
    today = datetime.datetime.today().strftime('%Y-%m-%d')

    print("📝 Suggested Changelog Entry:")
    print(f"- {today}: Updated logic in {', '.join(modified)}.")

if __name__ == "__main__":
    generate_changelog(sys.argv[1])