# Ultralytics YOLO 🚀, AGPL-3.0 license


from collections import defaultdict
from pathlib import Path

from git import Repo

# Constants for repository URLs and the local directory
SOURCE_REPO = 'https://github.com/ultralytics/ultralytics'  # source repo that code may come from
DEST_REPO = 'https://github.com/lancedb/lancedb'
LOCAL_DIRECTORY = 'repos'


def clone_repository(repo_url, clone_to):
    """Clone the repository from `repo_url` into the `clone_to` directory."""
    return Repo.clone_from(repo_url, clone_to)


def extract_file_contents(repo_path):
    """Extract file contents and commit history from the specified repository."""
    repo = Repo(repo_path)
    contents = defaultdict(list)
    for commit in repo.iter_commits():
        for file in commit.stats.files:
            contents[file].append((commit.hexsha, commit.author.name, commit.committed_datetime))
    return contents


def compare_repos(repo_a_contents, repo_b_contents):
    """Compare contents of two repositories and identify identical lines."""
    copied_lines = []
    for file_a, data_a in repo_a_contents.items():
        for file_b, data_b in repo_b_contents.items():
            if file_a == file_b:  # Simple filename match; extend this as needed
                lines_a = set(data_a)
                lines_b = set(data_b)
                common_lines = lines_a.intersection(lines_b)
                for line in common_lines:
                    copied_lines.append((file_a, line[0], file_b, line[0], line[1], line[2]))
    return copied_lines


def calculate_statistics(copied_lines):
    """Calculate statistics based on the copied lines data."""
    total_lines_copied = len(copied_lines)
    files_a = {line[0] for line in copied_lines}
    files_b = {line[2] for line in copied_lines}
    authors = defaultdict(int)
    for line in copied_lines:
        authors[line[4]] += 1
    return total_lines_copied, len(files_a), len(files_b), authors


def main(repo_a_url, repo_b_url, local_dir):
    """Main function to execute repository comparison."""
    path_a = clone_repository(repo_a_url, Path(local_dir) / Path(repo_a_url).stem)
    path_b = clone_repository(repo_b_url, Path(local_dir) / Path(repo_b_url).stem)
    repo_a_contents = extract_file_contents(path_a)
    repo_b_contents = extract_file_contents(path_b)
    copied_lines = compare_repos(repo_a_contents, repo_b_contents)
    stats = calculate_statistics(copied_lines)
    return copied_lines, stats


if __name__ == '__main__':
    # Execute the main function using defined constants
    copied_lines, stats = main(SOURCE_REPO, DEST_REPO, LOCAL_DIRECTORY)
    print("Copied Lines:", copied_lines)
    print("Statistics:", stats)
