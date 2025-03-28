<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🛠 Ultralytics Source Trace

Welcome to the `ultralytics/source-trace` repository! This specialized tool from [Ultralytics](https://www.ultralytics.com/) is designed to analyze and report potential [code duplication](https://en.wikipedia.org/wiki/Duplicate_code) between different [Git](https://git-scm.com/) repositories. Building upon the standard Ultralytics [Python](https://www.python.org/) project template, `source-trace` focuses specifically on enhancing code integrity and tracking. It empowers developers by identifying code segments that might be copied across repositories, offering detailed insights into the source, destination, and associated [metadata](https://en.wikipedia.org/wiki/Metadata) for each instance of duplication.

[![Ultralytics Actions](https://github.com/ultralytics/source-trace/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/source-trace/actions/workflows/format.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

## ✨ Features

- **Detailed Comparison**: Generates comprehensive reports highlighting lines of code from one repository found within another.
- **Comprehensive Statistics**: Provides valuable [metrics](https://www.ultralytics.com/glossary/accuracy) detailing the extent of code duplication, broken down by file and author.
- **Metadata Tracking**: Captures essential metadata for each duplication instance, including the author and commit date.

## 🚀 Getting Started

To begin using `source-trace` for your analysis:

1.  **Clone the Repository**: Use [Git clone](https://git-scm.com/docs/git-clone) to copy `source-trace` to your local machine or server.
    ```bash
    git clone https://github.com/ultralytics/source-trace.git
    cd source-trace
    ```
2.  **Install Dependencies**: Install the required [Python packages](https://pypi.org/) using [pip](https://pip.pypa.io/en/stable/). We recommend using a [virtual environment](https://docs.python.org/3/tutorial/venv.html).
    ```bash
    pip install -e .
    ```
3.  **Set Up Your Analysis**: Consult the documentation within the `docs/` directory for guidance on configuring your comparison parameters.
4.  **Run the Tool**: Execute the analysis scripts located in the `source/` directory to start the code duplication check.

## 💡 Contribute

Ultralytics thrives on community collaboration, and we deeply appreciate your contributions! Please review our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) for detailed information on how you can get involved. We also encourage you to share your feedback through our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A heartfelt thank you 🙏 goes out to all our contributors!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

## 📄 License

Ultralytics offers two licensing options to accommodate diverse needs:

- **AGPL-3.0 License**: This [OSI-approved](https://opensource.org/license/agpl-v3) open-source license is ideal for students, enthusiasts, and researchers who value open collaboration and knowledge sharing. See the [LICENSE](LICENSE) file for details.
- **Enterprise License**: Designed for commercial use, this license permits seamless integration of Ultralytics software and AI models into commercial products and services, bypassing the open-source requirements of AGPL-3.0. For enterprise solutions, please contact us via [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📮 Contact

For bug reports or feature suggestions related to `source-trace`, please raise an issue on [GitHub Issues](https://github.com/ultralytics/source-trace/issues). You're also welcome to join our [Discord](https://discord.com/invite/ultralytics) community for discussions, questions, and support!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
