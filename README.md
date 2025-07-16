<p align="center">
  <img src="https://img.shields.io/pypi/v/nglstrike?color=blue&label=PyPI&logo=pypi&style=flat-square">
  <img src="https://img.shields.io/pypi/dm/nglstrike?color=orange&label=Downloads&logo=python&style=flat-square">
  <img src="https://img.shields.io/github/license/mallikmusaddiq1/nglstrike?style=flat-square&color=green">
  <img src="https://img.shields.io/github/stars/mallikmusaddiq1/nglstrike?style=flat-square&label=Stars&color=yellow">
  <img src="https://img.shields.io/github/last-commit/mallikmusaddiq1/nglstrike?style=flat-square&color=purple">
  <img src="https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F%20in%20Python-blue?style=flat-square">
</p>

# nglstrike

Anonymous Auto-Sender for NGL — because sometimes, kindness needs a little automation.

## 📌 Overview

`nglstrike` is a professional-grade command-line tool that automates the process of sending anonymous messages via [ngl.link](https://ngl.link). Built for thoughtful experimentation and personal use, it supports single-message repetition or bulk message delivery from `.txt` files — with built-in delay, dry-run simulation, offensive word filtering, and message shuffling.

---

## ✨ Features

* ✅ **Send anonymous messages to any NGL username**
* 📄 **Load messages from a `.txt` file**
* ⏱️ **Custom interval delay between messages**
* 🔁 **Single message repeat or random pick from message pool**
* 🔄 **Shuffle mode (no message repeats until exhausted)**
* 🧪 **Dry-run mode** to preview message flow before actually sending
* 🚫 **Built-in offensive language filter**
* 🔍 **Common argument mistake detection**
* 📈 **Clean logging + ETA predictions**
* 📋 **Auto-generated summary after run**

---

## 🚀 Installation

### Option 1 - Clone the repo:

```bash
git clone https://github.com/mallikmusaddiq1/nglstrike.git
cd nglstrike
```

Make it executable:

```bash
chmod +x nglstrike.py
```

Run with Python 3:

```bash
nglstrike.py [options]
```

### Option 2: Pip installation.

```bash
pip install nglstrike
```

---

## 🧠 Usage Examples

### Send a single message repeatedly:

```bash
nglstrike.py -u your_username -m "Stay strong!"
```

### Send multiple messages from a file:

```bash
nglstrike.py -u your_username -m-path messages.txt --limit 10 -i 30
```

### Preview sending order (no actual messages):

```bash
nglstrike.py -u your_username -m-path messages.txt --dry-run --limit 5
```

### Shuffle messages (each sent only once):

```bash
nglstrike.py -u your_username -m-path messages.txt --shuffle
```

---

## 📁 Format for `messages.txt`

Plaintext file with one message per line. Example:

```
You're amazing.
Keep going — you're close.
Someone out there believes in you.
The best is yet to come.
```

---

## ⚙️ Arguments

| Argument                    | Description                                       |
| --------------------------- | ------------------------------------------------- |
| `-u`, `--username`          | **(Required)** Your NGL username (no link)        |
| `-m`, `--message`           | Send a single repeated message                    |
| `-m-path`, `--message-path` | Path to `.txt` file with multiple messages        |
| `-i`, `--interval`          | Delay between messages in seconds (default: `60`) |
| `--limit`                   | Stop after sending `N` messages                   |
| `--dry-run`                 | Preview messages instead of sending               |
| `--shuffle`                 | Send each message only once in random order       |
| `-v`, `--version`           | Show version and legal info                       |
| `-h`, `--help`              | Show help message                                 |

---

## 🧼 Offensive Word Filter

Before sending, `nglstrike` checks each message for offensive content using a predefined blacklist of strictly abusive terms. If **all messages** are flagged as offensive, the tool exits.

Use responsibly.

---

## 🛑 Legal & Ethical Notice

```
This tool is intended strictly for educational and personal experimentation.
Do NOT use this tool to spam, harass, or disturb anyone.
Misuse may violate NGL's Terms of Service.
You alone are responsible for your actions.
```

Keep digital spaces kind, safe, and human.

---

## 👤 Author

**Mallik Mohammed Musaddiq**  
GitHub: [@mallikmusaddiq1](https://github.com/mallikmusaddiq1)  
Email: [mallikmusaddiq1@gmail.com](mailto:mallikmusaddiq1@gmail.com)

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## ❤️ Support

If this project helped you, feel free to ⭐ the repo or contribute.  
Spread kindness. Automate it — ethically.
