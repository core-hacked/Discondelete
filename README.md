[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Latest Stable][releaselateststable-shield]][releaselateststable-url]




<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/core-hacked/">
    <img src="logo.png" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">Discondelete</h3>

  <p align="center">
    Discondelete, is a Discord self-bot to delete dm's or purge all messages from a guild. <br/>
    <code>Named by combining the words "discord", "anaconda", and "delete".</code>
    <br />
    <a href="https://github.com/core-hacked/Discondelete/issues">Report Bug</a>
    ·
    <a href="https://github.com/core-hacked/Discondelete/issues">Request Feature</a>
    <br/>
    <br/>
  </p>
</p>



<!-- TABLE OF CONTENTS -->

<details open>
  <summary><h2>Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Python Tested Version][python397test-shield]][releaselateststable-url]

### Built With

* [Python](https://www.python.org/)
* [Discord.py-self](https://github.com/dolfies/discord.py-self)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

<br/>

# How to get user token
1. Open Discord
2. Press `CTRL+SHIFT+I` to open the Developer Console
3. Copy and paste the code below into the console to automatically copy your user token to the clipboard.
```js
window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    if (!req.c) {
      console.error('req.c is undefined or null');
      return;
    }

    for (const m of Object.keys(req.c)
      .map(x => req.c[x].exports)
      .filter(x => x)) {
      if (m.default && m.default.getToken !== undefined) {
        return copy(m.default.getToken());
      }
      if (m.getToken !== undefined) {
        return copy(m.getToken());
      }
    }
  },
]);
console.log('%cWorked!', 'font-size: 50px');
console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
```

### Installation on Linux

<!-- Linux / Debian-based install -->
<details>
<summary> 
Debian-based distros (using <code>APT</code>)
</summary>

### Prerequisites

* Python
  ```sh
  sudo apt install python3
  ```
* Discord.py
  ```sh
  python3 -m pip install -U discord.py
  ```
* GIT
  ```sh
  sudo apt install git
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/core-hacked/Discondelete.git
   ```
2. Run the file with python
   ```sh
   python3 main.py
   ```
</details>
<br/>

<!-- Linux | Fedora/Red Hat (DNF) -->
<details>
<summary> 
Fedora / Red Hat (using <code>DNF</code>)
</summary>

### Prerequisites

* Python
  ```sh
  sudo dnf install python3
  ```
* Discord.py
  ```sh
  python3 -m pip install -U discord.py-self
  ```
* Git
  ```sh
  sudo dnf install git-all
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/core-hacked/Discondelete.git
   ```
2. Run the file with python
   ```sh
   python3 main.py
   ```
</details>
<br/>

<!-- Linux | Arch (Pacman) -->
<details>
<summary> 
Archlinux (using <code>PacMan</code>)
</summary>

### Prerequisites

* Python
  ```sh
  sudo pacman -S python
  ```
* Discord.py
  ```sh
  python3 -m pip install -U discord.py-self
  ```
* Git
  ```sh
  sudo pacman -S git
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/core-hacked/Discondelete.git
   ```
2. Run the file with python
   ```sh
   python3 main.py
   ```
</details>
<br/>

### Installation on Windows

<!-- Windows / Installers -->
<details>
<summary>
Windows (using provided installers)
</summary>
<br/>

1. Go to [python.org](https://www.python.org/downloads/) and download the latest version of Python (or 3.9.7).
2. Follow the installation wizard and install Python.
3. Go to [git-scm.com](https://git-scm.com/download/win), then download the installer (32-bit or 64-bit). 
4. follow the installation wizard and install Git.
5. Open command-prompt or PowerShell and install Discord.py using PIP. 
```bat
python3 -m pip install -U discord.py-self
```
6. Clone the repo using git.
```bat
git clone https://github.com/core-hacked/Discondelete.git
```
7. Change directory to the repo and run the file.
```bat
cd Discondelete
python3 main.py
```
</details>
<br/>

<!-- Windows / winget -->
<details>
<summary> 
Windows (using <code>WinGet</code>)
</summary>

### Prerequisites

* WinGet <br/>
  https://docs.microsoft.com/en-us/windows/package-manager/winget/
  <br/>

  > ⚠️ The winget command line tool is only supported on Windows 10 1709 (build 16299) or later at this time.
* Python
  ```powershell
  winget install -e --id Python.Python.3
  ```
* Discord.py
  ```powershell
  python3 -m pip install -U discord.py-self
  ```
* Git
  ```powershell
  winget install -e --id Git.Git
  ```

### Installation
1. Clone the repo
   ```bat
   git clone https://github.com/core-hacked/Discondelete.git
   ```
2. Run the file with python
   ```bat
   python3 main.py
   ```
</details>
<br/>

### Installation on MacOS

<!-- MacOS | Brew -->
<details>
<summary>
MacOS (using <code>Brew</code>)
</summary>

### Prerequisites

* [Brew](https://brew.sh/)
  ```sh
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
* Python
  ```sh
  brew install python
  ```
* Discord.py
  ```sh
  python3 -m pip install -U discord.py-self
  ```
* Git
  ```sh
  brew install git
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/core-hacked/Discondelete.git
   ```
2. Run the file with python
   ```sh
   python3 main.py
   ```
</details>
<br/>

> I also highly recommend using [Anaconda](https://www.anaconda.com/)

<br/>

## Usage
1. Running the file and passing it a token via the prompt
  ```sh
  python3 main.py
  ```
  ```sh
  # Results in 4 prompts for the token, a prefix, a heartbeat timeout and the server purge prefix
  ```
  Then in discord type your prefix or the default ``#DEL`` or ``#PS`` to purge messages from an entire server

2. Running the file with arguments
  ```sh
  python3 main.py *followed by arguments*
  ```
  ```sh
  # arguments: 
  # -t or --token [token] | Specify a token
  # -p or --prefix [prefix] | Specify a prefix (for double word prefix' or ones with special char's use quotes)
  # -b or --heartbeat [int] | Specify the heartbeat timeout 
  # -s or --serverpurge [prefix] | Specify a prefix for a server purge or leave blank for default
  # -o or --output | Specify if you want to output deleted messages in the console
  # -h or --help | to view this in the terminal/console
  ```
  Then in discord type your prefix or the default ``#DEL`` or ``#PS`` to purge messages from an entire server
  You can also purge a set of messages in a server by adding a number after your prefix.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/core-hacked/Discondelete/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be... learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

This repository is distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

[info@corehacked.com](mailto:info@corehacked.com)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/core-hacked/Discondelete.svg?colorA=1e1e28&colorB=E38C8F&style=for-the-badge&logo=starship%20style=for-the-badge
[contributors-url]: https://github.com/core-hacked/Discondelete/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/core-hacked/Discondelete.svg?colorA=1e1e28&colorB=A4B9EF&style=for-the-badge&logo=starship%20style=for-the-badge
[forks-url]: https://github.com/core-hacked/Discondelete/network/members
[stars-shield]: https://img.shields.io/github/stars/core-hacked/Discondelete.svg?colorA=1e1e28&colorB=EBDDAA&style=for-the-badge&logo=starship%20style=for-the-badge
[stars-url]: https://github.com/core-hacked/Discondelete/stargazers
[issues-shield]: https://img.shields.io/github/issues/core-hacked/Discondelete.svg?colorA=1e1e28&colorB=B1E3AD&style=for-the-badge&logo=starship%20style=for-the-badge
[issues-url]: https://github.com/core-hacked/Discondelete/issues
[license-shield]: https://img.shields.io/github/license/core-hacked/Discondelete.svg?colorA=1e1e28&colorB=F9C096&style=for-the-badge&logo=starship%20style=for-the-badge
[license-url]: https://github.com/core-hacked/Discondelete/blob/master/LICENSE
[python397test-shield]: https://img.shields.io/badge/Python%203.9.7-Working-green?colorA=1e1e28&colorB=B1E3AD&style=for-the-badge&logo=starship%20style=for-the-badge
[releaselateststable-shield]: https://img.shields.io/badge/Release-Stable%3A%20v1.3.0-blue?colorA=1e1e28&colorB=A4B9EF&style=for-the-badge&logo=starship%20style=for-the-badge
[releaselateststable-url]: https://github.com/core-hacked/Discondelete/releases/latest
