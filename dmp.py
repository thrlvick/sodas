import os
import subprocess

subprocess.run("systemctl poweroff -i", shell = True)

print("[+]shutting down.....")

input("Press Enter to continue.....")