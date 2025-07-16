#!/usr/bin/env python3      
      
import argparse      
import requests      
import random      
import time      
from pathlib import Path      
import sys      
from datetime import datetime, timedelta      
      
# ========== COMMON ARGUMENT MISTAKES ==========      
common_mistakes = {      
    "-message": "--message",      
    "-limit": "--limit",      
    "-username": "--username",      
    "--m-path": "-m-path",      
    "-message-path": "--message-path",      
    "-interval": "--interval",      
    "-dry-run": "--dry-run",      
    "-shuffle": "--shuffle"      
}      
      
# ========== OFFENSIVE WORD LIST ==========      
OFFENSIVE_WORDS = [
    "arse", "arsehole", "ass", "asshole", "asswipe", "baklola", "bakloli", "bakrichod", "bastard", "behenchara",
    "bellend", "bhenchod", "bhenchodi", "bhosda", "bhosdake", "bhosdika", "bhosdi", "bhosdiwala", "bhoska",
    "bhosadpappu", "bitch", "bollocks", "bugger", "chakka", "chhinar", "chhinal", "chhokri", "chhokru",
    "chodu", "choot", "chudal", "chuda", "chudail", "chudasi", "chut", "chutad", "chutappa", "chutkan",
    "chutkul", "chutmar", "chutmarani", "chutmarike", "chutni", "chutpana", "chutroo", "chutiya", "chutiyapa",
    "clunt", "cock", "coon", "crap", "cum", "dalla", "dick", "dickhead", "dickwad", "dipshit", "douche",
    "douchebag", "douchecanoe", "faggot", "fuck", "fucker", "fucktard", "fuckwit", "gandiya", "gand",
    "gandfat", "gandhasti", "gandmar", "gandmara", "gandora", "ganduk", "ganduwa", "gaandu", "gook", "hagni",
    "harami", "haramkhor", "hijra", "jackass", "jhaant", "jhaantoo", "jizz", "kameena", "kameeni", "kamina",
    "khotey", "khotta", "kike", "knob", "kotha", "kutti", "kutta", "lavda", "lavde", "madarchod", "madarsi",
    "motherfucker", "napunsak", "nigger", "paki", "phuddi", "prick", "pricktease", "pussy", "randbaaz",
    "randipana", "randwa", "randi", "retard", "sali", "schmuck", "scumbag", "shit", "shitbag", "shitface",
    "shithead", "shitty", "skank", "slag", "slut", "slutbag", "spic", "spick", "suar", "suar ka baccha",
    "tatti", "tossbag", "tosser", "tosspot", "tramp", "turd", "tattu", "twat", "wanker", "wankstain"
]
      
for arg in sys.argv:      
    if arg in common_mistakes:      
        correct = common_mistakes[arg]      
        sys.stderr.write(f"[ERROR] Did you mean {correct} instead of {arg} ?\n")      
        sys.exit(1)      
      
# ========== VERSION INFO ==========      
LEGAL_NOTICE = """      
nglstrike 1.2.0 - Anonymous Auto-Sender for NGL      
      
Author : Mallik Mohammed Musaddiq      
GitHub : https://github.com/mallikmusaddiq1/nglstrike      
Email  : mallikmusaddiq1@gmail.com      
      
─────────────────────────────────────────────────────────────      
LEGAL & ETHICAL NOTICE:      
This tool is intended strictly for educational and personal experimentation.      
      
It was created to promote thoughtful, uplifting, and respectful anonymous communication.      
Do NOT use this tool to spam, harass, or disturb anyone in any form.      
      
Misuse may violate NGL's Terms of Service and lead to penalties or bans.      
You alone are responsible for how you use this tool.      
      
Use it wisely — and help keep digital spaces kind, safe, and human.      
─────────────────────────────────────────────────────────────      
"""      
      
# ========== LOAD MESSAGES ==========      
def load_messages_from_file(file_path):      
    path = Path(file_path)      
    if path.suffix.lower() != ".txt":      
        sys.stderr.write(f"[ERROR] Only .txt files are supported. You provided: {path.suffix}\n")      
        sys.exit(1)      
    if not path.exists():      
        sys.stderr.write(f"[ERROR] File not found: {file_path}\n")      
        sys.exit(1)      
    if not path.is_file():      
        sys.stderr.write(f"[ERROR] Path is not a file: {file_path}\n")      
        sys.exit(1)      
    try:      
        with open(path, "r", encoding="utf-8") as f:      
            messages = [line.strip() for line in f if line.strip()]      
        if not messages:      
            sys.stderr.write("[ERROR] Message file is empty.\n")      
            sys.exit(1)      
        return messages      
    except Exception as e:      
        sys.stderr.write(f"[ERROR] Failed to read messages from file: {e}\n")      
        sys.exit(1)      
      
def is_offensive(message):      
    lowered = message.lower()      
    return any(bad_word in lowered for bad_word in OFFENSIVE_WORDS)      
      
# ========== SEND MESSAGE ==========      
def send_message(username, message, dry_run=False, counter=None, device_id="termux-nglstrike"):      
    if dry_run:      
        prefix = f"[DRY-RUN] #{counter} → " if counter else "[DRY-RUN] → "      
        print(f"{prefix}{message}")      
        return True      
      
    url = "https://ngl.link/api/submit"      
    payload = {      
        "username": username,      
        "question": message,      
        "deviceId": device_id      
    }      
    headers = {      
        "Content-Type": "application/x-www-form-urlencoded"      
    }      
      
    try:      
        response = requests.post(url, data=payload, headers=headers)      
        if response.status_code == 200:      
            print(f"[SENT] {message}")      
            return True      
        elif response.status_code == 404:      
            sys.stderr.write(f"[ERROR] Username does not exist on NGL (404 Not Found): @{username}\n")      
            sys.exit(1)      
        else:      
            print(f"[FAILED] HTTP {response.status_code} → {message}")      
            return False      
    except Exception as e:      
        sys.stderr.write(f"[ERROR] Network error: {e}\n")      
        return False      
      
# ========== MAIN ==========      
def main():      
    parser = argparse.ArgumentParser(      
        prog="nglstrike",      
        description="""      
nglstrike - Anonymous Auto-Sender for NGL      
Version: 1.1.0      
      
USAGE EXAMPLES:      
  nglstrike -u your_username -m "Stay strong!"      
  nglstrike -u your_username -m-path messages.txt --limit 10 -i 15      
      
MESSAGE MODES:      
  -m, --message         Send a single repeated message      
  -m-path, --message-path      
                        Load multiple messages from a .txt file      
                        (One per line. Empty lines ignored.)      
      
OPTIONS:      
  -u, --username        Required. Your NGL username (no link)      
  -i, --interval        Interval between messages in seconds [default: 60]      
  --limit               Stop after sending N messages      
  --dry-run             Preview messages without sending      
  --shuffle             Send each message once in random order (no repeats)      
  -v, --version         Show version and legal notice      
  -h, --help            Show this help message and exit      
      
EXAMPLE messages.txt:      
  You're doing great.      
  Someone out there believes in you.      
  Keep pushing. You're almost there.      
  The best is yet to come.      
      
NOTES:      
  - Only plain .txt files are supported for --message-path.      
  - --limit restricts total messages; --dry-run disables actual sending.      
  - With --shuffle, each message is sent only once until exhausted.      
      
─────────────────────────────────────────────────────────────      
Created by Mallik Mohammed Musaddiq      
GitHub: https://github.com/mallikmusaddiq1/nglstrike      
Email : mallikmusaddiq1@gmail.com      
─────────────────────────────────────────────────────────────      
""",      
        formatter_class=argparse.RawTextHelpFormatter      
    )      
      
    parser.add_argument("-u", "--username", required=True, help="Your NGL username (no URL)")      
    group = parser.add_mutually_exclusive_group(required=True)      
    group.add_argument("-m", "--message", help="Single message to send")      
    group.add_argument("-m-path", "--message-path", help="Path to .txt file containing messages (1 per line)")      
    parser.add_argument("-i", "--interval", default="60", help="Delay between messages in seconds (default: 60)")      
    parser.add_argument("--limit", type=int, help="Limit number of messages to send, then exit")      
    parser.add_argument("--dry-run", action="store_true", help="Print messages instead of sending")      
    parser.add_argument("--shuffle", action="store_true", help="Send each message once in shuffled order (no repeats)")      
    parser.add_argument("-v", "--version", action="version", version=LEGAL_NOTICE)      
      
    args = parser.parse_args()      
    try:      
        interval = int(args.interval)      
        if interval < 1:      
            raise ValueError      
    except ValueError:      
        sys.stderr.write("[ERROR] Use positive integers only: -i/--interval 5, 10, 60 etc.\n")      
        sys.exit(1)      
      
    if args.limit is not None and args.limit < 1:      
        sys.stderr.write("[ERROR] Limit must be at least 1.\n")      
        sys.exit(1)      
      
    if args.message:      
        messages = [args.message.strip()]      
        if args.shuffle:      
            print("[WARNING] --shuffle has no effect when using a single message. Ignoring it.")      
            args.shuffle = False      
    elif args.message_path:      
        messages = load_messages_from_file(args.message_path)      
        if args.shuffle:      
            random.shuffle(messages)      
    else:      
        sys.stderr.write("[ERROR] Either --message or --message-path must be provided.\n")      
        sys.exit(1)      
    if all(is_offensive(msg) for msg in messages):      
        sys.stderr.write("[ERROR] All messages are offensive. Exiting.\n")      
        sys.exit(1)      
      
    print(f"[INFO] Starting nglstrike on @{args.username} every {interval}s.")      
    print("[INFO] Press CTRL+C to exit.")      
    if args.dry_run:      
        print("[INFO] Dry-run mode: No messages will actually be sent.")      
    if args.shuffle:      
        print("[INFO] Shuffle mode enabled: Messages will not repeat.")      
      
    if args.dry_run and args.limit:      
        print(f"\n[DRY-RUN] Planned Message Order (Limit: {args.limit}):\n")      
        preview = messages[:args.limit] if args.shuffle else [random.choice(messages) for _ in range(args.limit)]      
        for i, msg in enumerate(preview, 1):      
            print(f"  #{i} → {msg}")      
        print(f"\n[DRY-RUN] {len(preview)} messages would be sent to @{args.username}, interval: {interval}s\n")      
        return      
    elif args.dry_run and args.message:      
        print(f"\n[DRY-RUN] Would repeatedly send:\n  → {messages[0]}\n")      
        return      
      
    count = 0      
    index = 0      
    sent = 0      
    skipped = 0      
    failed = 0      
    start_time = datetime.now()      
    print(f"[INFO] Started at: {start_time.strftime('%H:%M:%S')}")      
      
    try:      
        while True:      
            if args.shuffle:      
                if index >= len(messages):      
                    print("[INFO] All messages sent (shuffled list exhausted). Exiting.")      
                    break      
                message = messages[index]      
                index += 1      
            else:      
                message = random.choice(messages)      
      
            if is_offensive(message):      
                print(f"[SKIPPED] Offensive content detected → {message}")      
                skipped += 1      
            else:      
                result = send_message(args.username, message, dry_run=args.dry_run, counter=count + 1)      
                if result:      
                    sent += 1      
                else:      
                    failed += 1      
      
            count += 1  # ← Always increment once per loop      
      
            if args.limit and count >= args.limit:      
                print(f"[INFO] Limit of {args.limit} messages reached. Exiting.")      
                break      
      
            remaining = (args.limit - count) if args.limit else None      
            if remaining:      
                eta = datetime.now() + timedelta(seconds=interval * remaining)      
                print(f"[ETA] {remaining} remaining. Estimated finish: {eta.strftime('%H:%M:%S')}")      
      
            time.sleep(interval)      
      
    except KeyboardInterrupt:      
        print("\n[INFO] Interrupted. Exiting.")      
        sys.exit(0)      
      
    # ======= FINAL SUMMARY ========      
    end_time = datetime.now()      
    duration = end_time - start_time      
    print("\n[SUMMARY]")      
    print(f"  Sent     : {sent}")      
    print(f"  Failed   : {failed}")      
    print(f"  Skipped  : {skipped}")      
    print(f"  Duration : {str(duration).split('.')[0]}")      
    print(f"  Finished : {end_time.strftime('%H:%M:%S')}")      
      
if __name__ == "__main__":      
    main()