import sys

def summarize_diff(diff_path):
    with open(diff_path, 'r') as f:
        diff = f.read()

    files_changed = set()
    additions = deletions = 0
    for line in diff.splitlines():
        if line.startswith('+++ b/') or line.startswith('--- a/'):
            path = line.split()[-1].replace('a/', '').replace('b/', '')
            files_changed.add(path)
        elif line.startswith('+') and not line.startswith('+++'):
            additions += 1
        elif line.startswith('-') and not line.startswith('---'):
            deletions += 1

    print("🔍 PR Summary:")
    print(f"Files changed: {len(files_changed)}")
    print(f"Lines added: {additions}")
    print(f"Lines removed: {deletions}")
    print("Changed files:")
    for file in files_changed:
        print(f" - {file}")

if __name__ == "__main__":
    summarize_diff(sys.argv[1])
