# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

Source-Trace (`source-trace`, AGPL-3.0) is an internal Ultralytics tool that clones two Git repositories and reports lines of code that appear in both, to surface potential cross-repository code duplication. It is run from a checkout rather than installed from PyPI.

## Core Principles (CRITICAL)

**Less is more. The simplest solution is the best solution.** The action hierarchy for every change: **Delete > Replace > Add**.

1. **Solve at the owner**: Put behavior in the code path that owns or observes it. For fixes, never guard a symptom with a staleness check, initialization flag, skip-first-call branch, or `try/except` around broken logic; relocate the trigger and delete the wrong path. For features, extend the existing owner rather than creating a parallel abstraction.
2. **Search and reuse first**: Search the whole repository before creating a feature, component, helper, workflow, or utility. Reuse or adapt what exists, consolidate in-scope duplication in the shared owner, and delete duplicate paths. Three similar lines beat a helper nobody else calls.
3. **Delete and modify existing code before creating new code**: Bugfixes are net-negative by default unless deletion and relocation are demonstrably impossible. A new file must first prove it cannot fit cleanly in an existing owner.
4. **Keep scope minimal**: Implement only the simplest complete solution. Avoid impossible-state handling, speculative flags, compatibility shims, policy scaffolding, and unrelated cleanup. Tests are out of scope by default — rely on existing coverage and focused validation; only an uncovered, high-risk regression path justifies minimal new test code.
5. **Ship zero-regression, production-ready changes**: Understand what you remove instead of retaining broken code as insurance. Remove unused imports, functions, types, files, and comments; run relevant cleanup checks; and thoroughly debug and validate the changed owner. Do not break existing features or workflows unless the PR intentionally removes them with evidence.

**Review gate:** for every addition, the reviewer decides whether deleting or changing existing code would have fixed the problem instead — if it would, that is a blocking finding. A missing or thin PR description is never itself a finding.

NEVER push to `main`. NEVER force push. Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Review the full diff in-session against the Core Principles, performance, and the review gate above, then batch the fixes into one commit and push. After each round of bot or human commits, pull and resume the same reviewer on `<last-reviewed-sha>..HEAD` plus anything that delta could have invalidated. Repeat until the local head matches the live head.
3. Hand off or merge only on a clean final pass: one cold full-diff review returning LGTM with no findings, on a head that is still live at merge time.
4. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never reset or revert commits you did not author.
5. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

## Commands

```bash
# Editable install (only dependency: gitpython)
uv pip install -e .

# Run a comparison — edit the constants at the top of source/run_repo.py first
python source/run_repo.py
```

- There is no test suite and no test CI. The only workflows are `format.yml` (Ultralytics Actions autoformat, labels, PR summaries) and `cla.yml`; neither runs the tool.
- A run clones both repositories in full into `github.com/<org>/<repo>` under the repository root and reuses that directory on later runs, so delete it to force a fresh clone.

## Architecture

Everything lives in `source/run_repo.py`; `source/__init__.py` only exposes `__version__` and `ROOT`. The tool is configured by editing module-level constants rather than by CLI flags: `SOURCE_REPO`, `DEST_REPO`, `SUFFIXES`, `IGNORE_START`, and `IGNORE_LINES`.

The pipeline is four functions called in order by `main(repo_a, repo_b, local_dir)`:

- `clone_repository()` clones a repository URL into `local_dir/<org>/<repo>`, skipping the clone when the directory already exists.
- `extract_file_contents()` reads every non-binary file in a clone and returns `{relative_path: [stripped_lowercased_lines]}`, skipping files that fail to decode as UTF-8.
- `compare_repos()` intersects the line sets of each source/destination file pair whose source suffix is in `SUFFIXES`, keeping only lines longer than 20 characters that do not start with an `IGNORE_START` prefix and do not exactly match an `IGNORE_LINES` entry. It returns `(source_file, dest_file, line)` tuples.
- `calculate_statistics()` reduces those tuples to the duplicated-line count and the number of distinct files on each side.

Matching is line-level and set-based, so it detects identical lines rather than moved blocks, and it reports each distinct line once per file pair regardless of how often it repeats. No Git history is read: authorship and commit dates are not collected.

## Conventions

- Every Python file starts with `# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license` — Ultralytics Actions adds headers automatically; don't add or revert them manually.
- Google-style docstrings and Ruff formatting at line length 120 (`[tool.ruff]` in pyproject.toml), applied automatically by `format.yml` on PRs.
- `docs/` holds a plain README describing usage; there is no MkDocs site or `mkdocs.yml`, so keep usage docs in `README.md` and `docs/README.md` in sync with the constants in `source/run_repo.py`.
- There is no release workflow and the package is not on PyPI; leave `__version__` in `source/__init__.py` alone.
