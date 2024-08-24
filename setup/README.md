# Setup Commmand List for Windows

- Created : 2024/08/24
- Machine : Initialized Windows11

# Install PowerShell 7.x

- [Winget を使用して PowerShell をインストールする (推奨)](https://learn.microsoft.com/ja-jp/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4#winget)

- Check PowerShell Version

```sh
$PSVersionTable.PSVersion
Major  Minor  Build  Revision
-----  -----  -----  --------
5      1      22621  3958
```

- Check Available PowerShell
  
```sh
winget search Microsoft.PowerShell
Name               Id                           Version   Source
-----------------------------------------------------------------
PowerShell         Microsoft.PowerShell         7.4.4.0   winget
PowerShell Preview Microsoft.PowerShell.Preview 7.5.0.3   winget
```

- Install New PowerShell

```sh
winget install --id Microsoft.Powershell --source winget
```

- Check Installed PowerShell

```sh
winget list | Select-String "PowerShell"

PowerShell 7-x64                   Microsoft.PowerShell                7.4.
5.0
```

- Switch Default Terminal from old PowerShell to new PowerShell
- Check PowerShell Version Again

```sh
$PSVersionTable.PSVersion

Major  Minor  Patch  PreReleaseLabel BuildLabel
-----  -----  -----  --------------- ----------
7      4      5
```

# Install WSL2

- [WSL を使用して Windows に Linux をインストールする方法](https://learn.microsoft.com/ja-jp/windows/wsl/install)

- Install WSL2

```sh
wsl --install
```

- Reboot PC
- Open Ubuntu
- Register user name and password

# Upgrade apt repositories (Maybe Optional)

```sh
sudo apt update
sudo apt upgrade
```

## Optional

- Close Ubuntu
- Open Ubuntu in Terminal
- Install WSL Extension in VSCode

# Check Git Version

```sh
git --version
git version 2.34.1
```

# Install VSCode in WSL2

```sh
code
Installing VS Code Server for Linux x64 (fee1edb8d6d72a0ddff41e5f71a671c23ed924b9)
Downloading: 100%
Unpacking: 100%
Unpacked 1754 files and folders to /home/aoba/.vscode-server/bin/fee1edb8d6d72a0ddff41e5f71a671c23ed924b9.
Looking for compatibility check script at /home/aoba/.vscode-server/bin/fee1edb8d6d72a0ddff41e5f71a671c23ed924b9/bin/helpers/check-requirements.sh
Running compatibility check script
Compatibility check successful (0)
```

# Install pyenv

- Install required apt packages

```sh
sudo apt update
sudo apt install build-essential libffi-dev libssl-dev zlib1g-dev liblzma-dev libbz2-dev \
  libreadline-dev libsqlite3-dev libopencv-dev tk-dev git
```

- Clone pyenv from GitHub

```sh
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

- Configure Path (bashrc)

```sh
echo '' >> ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
source ~/.bashrc
```

- Check pyenv version

```sh
pyenv -v
pyenv 2.4.10
```

# Install Python via pyenv

- Check available Python versions 3.12.x

```sh
pyenv install --list | grep '^  3.12'
  3.12.0
  3.12-dev
  3.12.1
  3.12.2
  3.12.3
  3.12.4
  3.12.5
```

- Install Python 3.12.5

```sh
pyenv install 3.12.5
Downloading Python-3.12.5.tar.xz...
-> https://www.python.org/ftp/python/3.12.5/Python-3.12.5.tar.xz
Installing Python-3.12.5...
Installed Python-3.12.5 to /home/aoba/.pyenv/versions/3.12.5
```

- Check current environment

```sh
pyenv versions
* system (set by /home/aoba/.pyenv/version)
  3.12.5
```

- Switch environment from system to 3.12.5

```sh
pyenv global 3.12.5
```

- Check current environment again

```sh
pyenv versions
  system
* 3.12.5 (set by /home/aoba/.pyenv/version)
```

- Check Python version

```sh
python -V
Python 3.12.5
```

# Create Project

- Create Repository on GitHub
- Create Personal Access Token in GitHub
- Clone it

```sh
git clone  git clone https://github.com/xxxxxxx/ProblemSolvingProgrammingSample.git
Cloning into 'ProblemSolvingProgrammingSample'...
warning: You appear to have cloned an empty repository.
```

- Open project

```sh
code ProblemSolvingProgrammingSample/
```

- Add gitignore

```sh
~/ProblemSolvingProgrammingSample: touch .gitignore
```

- Ignore file list

```text
    venv/
    .venv
    *.pyc
    .idea
    .vscode
    *.mo
    *.pot
    *.log
    result/*
    .DS_Store
    parameters.json
    .python-version
```

- Download nut_ppp.zip

[SampleProject](https://suitc-my.sharepoint.com/:f:/g/personal/kwatabe_mail_saitama-u_ac_jp/EvJkjZXiYs9Arh0yXf7RH1ABNLqa_nhQ7RqRY31Oa1md4w?e=aGa5Gh)

```sh
~/ProblemSolvingProgrammingSample: ls
nut_ppp.zip
```

- unzip it

```sh
sudo apt update
sudo apt instal unzip
~/ProblemSolvingProgrammingSample: unzip nut_ppp.zip
```

- move files 

```sh
~/ProblemSolvingProgrammingSample: mv nut_ppp/* .
```

# Setup Python environment

- Create virtual environment (venv)

```sh
~/ProblemSolvingProgrammingSample: python -m venv venv 
```

- Activate venv

```sh
~/ProblemSolvingProgrammingSample: source venv/bin/activate
(venv) ~/ProblemSolvingProgrammingSample: python -V
Python 3.12.5
```

# Push Project to GitHub

- Commit changes

```sh
(venv) ~/ProblemSolvingProgrammingSample: git add .
(venv) ~/ProblemSolvingProgrammingSample: git config --global user.email "aobaiwaki@gmail.com"
(venv) ~/ProblemSolvingProgrammingSample: git config --global user.name "AobaIwaki123"
(venv) ~/ProblemSolvingProgrammingSample: git commit -m "first commit"
```

- Push it

```sh
(venv) ~/ProblemSolvingProgrammingSample: git push origin main
Username for 'https://github.com': AobaIwaki123
Password for 'https://AobaIwaki123@github.com': {PersonalAccessToken}
```
