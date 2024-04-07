from pathlib import Path

from git import Repo

from source import ROOT

SOURCE_REPO = "https://github.com/ultralytics/ultralytics"  # source repo
DEST_REPO = "https://github.com/ultralytics/yolov5"

SUFFIXES = (".py",)
IGNORE_START = ("import", "from", "try", "except", "with", "@pytest")
IGNORE_LINES = (
    '"""',
    "args:",
    "def main():",
    'if __name__ == "__main__":',
    "attributes:",
    "def __init__(",
    "@staticmethod",
    "return false",
    "return true",
    "return func(*args, **kwargs)",
    "def __init__(self):",
    "super().__init__()",
    "super().__init__(*args, **kwargs)",
    "model.eval()",
    "logger.info(",
    "logger.warning(",
    "parser.add_argument(",
    "def __len__(self):",
    "def __repr__(self):",
    "while true:",
    "parser = argparse.argumentparser()",
    "args = parser.parse_args()",
    "return model",
    "return output",
    "torch.cuda.empty_cache()",
    "return none",
    "def forward(self, x):",
    "@torch.no_grad()",
    "raise notimplementederror",
    ") -> np.ndarray:",
    ") -> torch.tensor:",
    "raise valueerror(",
    "if torch.cuda.is_available():",
    "cv2.destroyallwindows()",
)


def clone_repository(repo_url, clone_to):
    """Clone the repository from `repo_url` into the `clone_to` directory."""
    print(f"Cloning {repo_url} into {clone_to}")
    if not clone_to.exists():
        clone_to.mkdir(parents=True, exist_ok=True)
        Repo.clone_from(repo_url, clone_to)
    return clone_to


def extract_file_contents(repo_path):
    """Read all text-readable files in the local directory of a repository to extract their contents, ignoring binary
    files.
    """
    repo_path = Path(repo_path)
    contents = {}
    binary_extensions = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".bin", ".exe", ".dll", ".so", ".zip"}
    # Traverse through all files in the repository directory
    for file_path in repo_path.rglob("*"):
        if file_path.is_file() and file_path.suffix not in binary_extensions:
            try:
                with file_path.open("r", encoding="utf-8") as file:
                    contents[str(file_path.relative_to(repo_path))] = [line.strip().lower() for line in file]
            except UnicodeDecodeError:
                pass
    return contents


def compare_repos(repo_a_contents, repo_b_contents):
    """Compare contents of two repositories to find identical lines and report statistics for each repo."""
    # Calculate statistics for Repo A
    total_files_a = len(repo_a_contents)
    total_lines_a = sum(len(lines) for lines in repo_a_contents.values())
    print(f"{SOURCE_REPO}: {total_files_a} files, {total_lines_a} total lines of code")

    # Calculate statistics for Repo B
    total_files_b = len(repo_b_contents)
    total_lines_b = sum(len(lines) for lines in repo_b_contents.values())
    print(f"{DEST_REPO}: {total_files_b} files, {total_lines_b} total lines of code")

    # Perform comparison to find identical lines
    copied_lines = []
    for file_a, lines_a in repo_a_contents.items():
        for file_b, lines_b in repo_b_contents.items():
            if Path(file_a).suffix in SUFFIXES:
                common_lines = set(lines_a) & set(lines_b)
                if any(common_lines):
                    for line in common_lines:
                        if (
                            len(line) > 20
                            and not any(line.startswith(x) for x in IGNORE_START)
                            and not any(line == x for x in IGNORE_LINES)
                        ):
                            print(line)
                            copied_lines.append((file_a, file_b, line))

    return copied_lines


def calculate_statistics(copied_lines):
    """Calculate statistics based on the copied lines data, with debug outputs to trace values."""
    total_lines_copied = len(copied_lines)
    print(f"Debug: Total lines copied: {total_lines_copied}")
    files_a = {line[0] for line in copied_lines}
    files_b = {line[1] for line in copied_lines}
    return total_lines_copied, len(files_a), len(files_b)


def main(repo_a, repo_b, local_dir):
    """Main function to execute repository comparison."""
    path_a = clone_repository(repo_a, local_dir / Path(repo_a).parent.stem / Path(repo_a).stem)
    path_b = clone_repository(repo_b, local_dir / Path(repo_b).parent.stem / Path(repo_b).stem)
    repo_a_contents = extract_file_contents(path_a)
    repo_b_contents = extract_file_contents(path_b)
    copied_lines = compare_repos(repo_a_contents, repo_b_contents)
    stats = calculate_statistics(copied_lines)
    print("Comparison and statistics collection complete")
    return copied_lines, stats


if __name__ == "__main__":
    local_dir = ROOT / "github.com"
    copied_lines, stats = main(SOURCE_REPO, DEST_REPO, local_dir=local_dir)
