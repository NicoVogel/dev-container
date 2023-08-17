# Dev Container Setup for Simplified Onboarding

Welcome to the `dev-container` repository!
This project is geared towards simplifying the onboarding process for new team members, ensuring a consistent development environment across different operating systems. 
It utilizes the power of Dev Containers with Visual Studio Code.

[![VSCode Dev Containers](https://img.shields.io/badge/VSCode-Dev%20Containers-blue)](https://code.visualstudio.com/docs/devcontainers/containers)

## Features

- Utilizes `pnpm` for enhanced performance.
- Incorporates `playwright` for end-to-end testing.
- Supports "docker in docker" via socket mount, allowing Docker within the development environment.
- Compatible with Linux, Windows (via WSL2 or Docker Volume), and Mac.

## Quick Start

1. Ensure you have [Git](https://git-scm.com/) and [Docker](https://www.docker.com/) installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/NicoVogel/dev-container.git
   ```
3. Open the project in Visual Studio Code.
4. Rename the directory `template` to `.devconainer`
5. Make sure the extension `Dev Containers` is installed (`ms-vscode-remote.remote-containers`)
6. Use the VS Code command `Dev Containers: Reopen in Container`.

## Customization

This template can be tailored to meet your project's specific requirements. For detailed instructions on customization, refer to the [blog post](https://dev.to/nicovogel/onboarding-new-team-members-simplified-with-dev-containers-5gag).

## Feedback & Contributions

Feel free to open issues if you encounter any problems or have suggestions. Contributions via pull requests are also welcomed!

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[MIT](./LICENSE)
