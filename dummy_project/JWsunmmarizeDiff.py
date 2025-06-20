import argparse
import re
import subprocess

def summarize_diff(diff):
    added = []
    removed = []
    modified = []

    lines = diff.split('\n')
    for line in lines:
        if line.startswith('+') and not line.startswith('+++'):
            added.append(line[1:])
        elif line.startswith('-') and not line.startswith('---'):
            removed.append(line[1:])
        elif line.startswith('@@'):
            modified.append(line)

    return {
        'added': added,
        'removed': removed,
        'modified': modified
    }

def main():
    # Run Git diff and save the output to a file in the current directory
    getDiff = subprocess.run(['git', 'diff'], capture_output=True, text=True)
    # Save the diff output to a file
    with open('configure.diff', 'w') as file:
        file.write(getDiff.stdout + '\n')

    summary = summarize_diff(getDiff.stdout)
    print(summary)

if __name__ == '__main__':
    main()

