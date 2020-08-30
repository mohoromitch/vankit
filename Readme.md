# Vankit

Vankit is a social media **van**ity tool**kit**. Social media vanity is a full time job. Let vanikit automate some of those toxic habits for you!

## Requirements

Developed using Python 3.8.3. There are only a handful of dependencies included in requirements.txt.

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

In the repository:

```bash
python3 ./vankit.py
```

The onscreen instructions will guide you through usage.

You can also type:

```bash
python3 ./vankit.py --help
```

For optional execution with supplied parameters.

## Meta

### What does this script support?

Currently the only thing it does is fetch some of your ig followers, and tells you in a pretty spartan way who you're following and isn't following you back, and vice versa.

It has the option to securely save your credentials though, which can save time when running a repetitive task like this. It uses keyring, which stores credentials in your system's credential store:


- macOS Keychain
- Freedesktop Secret Service supports many DE including GNOME (requires secretstorage)
- KDE4 & KDE5 KWallet (requires dbus)
- Windows Credential Locker

Source: [Keyring pypi project page.](https://pypi.org/project/keyring/)

### Why did I make this?

I mostly wanted to play with Python, so I grabbed a project from my running list of side project ideas and this one seemed easy.

### What's next?

I'm thinking of adding Twitter support soon. I think it would be useful to be able to delete tweets that are older than a particular date, and download them for personal archive purposes. The same could be extended to Reddit. I could also rework the current followback functionality 🤔.