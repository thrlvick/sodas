import os
import subprocess

subprocess.run("systemctl suspend -i", shell = True)

print("[+]shutting down.....")

input("Press Enter to continue.....")