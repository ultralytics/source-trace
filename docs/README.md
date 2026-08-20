<a href="https://www.ultralytics.com"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# Source Trace Docs

This directory is reserved for project documentation. The current repository does not include an MkDocs site or
`mkdocs.yml`; usage is documented in the root `README.md` and implemented in `source/run_repo.py`.

## Current Usage

To configure a comparison, update the constants near the top of `source/run_repo.py`:

- `SOURCE_REPO`: repository used as the source of candidate copied lines.
- `DEST_REPO`: repository compared against the source repository.
- `SUFFIXES`: file extensions included in the comparison.
- `IGNORE_START` and `IGNORE_LINES`: common lines ignored during matching.

After editing those values, run the script from the repository root:

```bash
python source/run_repo.py
```
