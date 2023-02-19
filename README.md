<div align='center'>
    <h1>Sublime Text Manual Patch</h1>
    <br><img height="64" src="https://img.icons8.com/fluency/256/sublime-text.png"><br><br>

```
How to patch Sublime Text to Unlimited User License
```

</div>

# Install Sublime Text

## Windows

1. Download [Sublime Text](https://www.sublimetext.com/download_thanks?target=win-x64)
2. Open installer file
3. Select destination location, then click Next
4. You can add Sublime Text to explorer context menu, just check it then click Next
5. After installation succedded, click Finish

## Linux

**Apt**

The apt repository contains packages for both x86-64 and arm64.

1. Install the GPG key:
    ```
    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null
    ```

2. Select the channel to use:

    **Stable**
    ```
    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    ```

    **Dev**
    ```
    echo "deb https://download.sublimetext.com/ apt/dev/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    ```
3. Update apt sources and install Sublime Text:

    ```
    sudo apt-get update
    sudo apt-get install sublime-text
    ```

**Pacman**

1. Install the GPG key:
    ```
    curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg
    ```

2. Select the channel to use:

    **Stable x86_64**
    ```
    echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf
    ```

    **Dev x86_64**
    ```
    echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/dev/x86_64" | sudo tee -a /etc/pacman.conf
    ```

    **Stable aarch64**
    ```
    echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/aarch64" | sudo tee -a /etc/pacman.conf
    ```

    **Dev aarch64**
    ```
    echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/dev/aarch64" | sudo tee -a /etc/pacman.conf
    ```

3. Update pacman and install Sublime Text:
    ```
    sudo pacman -Syu sublime-text
    ```

**Yum**

1. Install the GPG key:
    ```
    sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
    ```

2. Select the channel to use:

    **Stable**
    ```
    sudo yum-config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
    ```

    **Dev**
    ```
    sudo yum-config-manager --add-repo https://download.sublimetext.com/rpm/dev/x86_64/sublime-text.repo
    ```
3. Update yum and install Sublime Text:

    ```
    sudo yum install sublime-text
    ```

**Dnf**

1. Install the GPG key:
    ```
    sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
    ```

2. Select the channel to use:

    **Stable**
    ```
    sudo dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
    ```

    **Dev**
    ```
    sudo dnf config-manager --add-repo https://download.sublimetext.com/rpm/dev/x86_64/sublime-text.repo
    ```
3. Update dnf and install Sublime Text:

    ```
    sudo dnf install sublime-text
    ```

**Zypper**

1. Install the GPG key:
    ```
    sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
    ```

2. Select the channel to use:

    **Stable**
    ```
    sudo zypper addrepo -g -f https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
    ```

    **Dev**
    ```
    sudo zypper addrepo -g -f https://download.sublimetext.com/rpm/dev/x86_64/sublime-text.repo
    ```
3. Update zypper and install Sublime Text:

    ```
    sudo zypper install sublime-text
    ```

## MacOS

1. Download [Sublime Text](https://www.sublimetext.com/download_thanks?target=mac)
2. Extract downloaded file
3. Drag Sublime Text.app into your Applications folder

# Patch Sublime Text

1. Go to [HexEd.it](https://hexed.it/)
2. Click Open file, then put executable file of Sublime Text

    **Windows**
    ```
    C:\Program Files\Sublime Text\sublime_text.exe
    ```

    **Linux**
    ```
    /opt/sublime_text/sublime_text
    ```

    **MacOS**
    ```
    /Applications/Sublime Text.app/Contents/MacOS/sublime_text
    ```

3. Search 80 78 05 00 0F 94 C1 in Search for
4. Click Find Next
5. Overwrite it to C6 40 05 01 48 85 C9 as Hexadecimal Values
6. After that click Save as, rename it to same as Sublime Text executable file
7. Backup old file, then move modified file to Sublime Text directory
