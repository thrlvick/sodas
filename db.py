import os
import subprocess
import sqlite3

subprocess.run("fuser -k (#database_name.db )" shell = True)
subprocess.run("chmod 666 (#databse_name.db)" shell =True )

print("[*]working dependencies")
print("[+]successfull...")

input("Press any key to continue...")

