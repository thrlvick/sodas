import os
import subprocess

subprocess.run("sudo rmmod psmouse && sudo modprobe psmouse", shell = True)

print("[+]succesfull.....")

input("Press Enter to continue.....")