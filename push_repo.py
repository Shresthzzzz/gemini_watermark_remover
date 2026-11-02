import subprocess
import sys

git = r"C:\Program Files\Git\cmd\git.exe"

commands = [
    [git, "init"],
    [git, "config", "user.name", "Shresth"],
    [git, "config", "user.email", "shresth@users.noreply.github.com"],
    [git, "add", "."],
    [git, "commit", "-m", "Initial commit: Gemini & Veo Image and Video Watermark Remover by Shresth"],
    [git, "branch", "-M", "main"],
    [git, "remote", "add", "origin", "https://github.com/Shresthzzzz/gemini_watermark_remover.git"],
]

for cmd in commands:
    print("Running:", " ".join(cmd))
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.stdout:
        print(res.stdout)
    if res.stderr:
        print(res.stderr)

print("Now attempting git push:")
push_res = subprocess.run([git, "push", "-u", "origin", "main"], capture_output=True, text=True)
print("Push stdout:", push_res.stdout)
print("Push stderr:", push_res.stderr)
