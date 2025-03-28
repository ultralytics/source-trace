<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# Documentation Directory (`docs/`)

Welcome to the `docs/` directory! This folder contains all the documentation for the project. We use [MkDocs](https://www.mkdocs.org/), a fast and simple [static site generator](https://en.wikipedia.org/wiki/Static_site_generator), to build and manage our documentation site. Our aim is to provide clear, accurate, and accessible documentation for all users.

## 📂 Overview

- **MkDocs Configuration**: The primary configuration file for our documentation site is `mkdocs.yml`. This file defines the site's structure, navigation, theme, and various build settings. You can learn more about configuring MkDocs in their [user guide](https://www.mkdocs.org/user-guide/configuration/).
- **Documentation Files**: All documentation content is written using [Markdown](https://www.markdownguide.org/basic-syntax/), a lightweight markup language with plain text formatting syntax. These `.md` files are located within this `docs/` directory and its subdirectories.
- **Structure**: The organization of Markdown files and the navigation menu displayed on the documentation site are defined in the `mkdocs.yml` file. This ensures a logical and user-friendly layout, similar to the main [Ultralytics Docs site](https://docs.ultralytics.com/).

## 🚀 Getting Started

To view, edit, or build the documentation locally, follow these steps:

1.  **Install MkDocs**: Ensure you have MkDocs and the necessary themes or extensions installed in your Python environment. If you haven't already, follow the official [MkDocs installation guide](https://www.mkdocs.org/user-guide/installation/). Key packages typically include `mkdocs` and `mkdocs-material`. You can find the [MkDocs Material theme documentation here](https://squidfunk.github.io/mkdocs-material/getting-started/).
2.  **Preview Documentation**: Open your terminal, navigate to the project's root directory (the one containing the `mkdocs.yml` file), and run the command `mkdocs serve`. This command starts a local development server, allowing you to preview the documentation site in your web browser, usually at `http://127.0.0.1:8000`. The site automatically updates when you save changes to documentation files or the configuration. See the [`mkdocs serve` documentation](https://www.mkdocs.org/user-guide/cli/#mkdocs-serve) for more details.
3.  **Build Documentation**: To generate the static HTML site (for example, for deployment), run the command `mkdocs build`. This process compiles the Markdown files into HTML and outputs them to the `site/` directory by default. More information is available in the [`mkdocs build` documentation](https://www.mkdocs.org/user-guide/cli/#mkdocs-build).

## ✨ Contributing

High-quality documentation is vital for the project's success. We welcome and encourage contributions to keep the documentation accurate, comprehensive, and up-to-date.

- Please adhere to the guidelines outlined in the main [Ultralytics Contribution Guide](https://docs.ultralytics.com/help/contributing/).
- If you discover errors, areas needing improvement, or missing information, please open an issue or submit a pull request on GitHub. Check out our blog post for helpful [tips on contributing to Ultralytics open-source projects](https://www.ultralytics.com/blog/tips-to-start-contributing-to-ultralytics-open-source-projects).

Your contributions help make our documentation better for the entire community!
