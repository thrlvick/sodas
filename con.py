import contextlib
print("[*]launching silent recnaisance scan...")
with contextlib .suppress(FileNotFoundError):
    with open("hidden_token.txt","r") as f:
        token = f.read()
        print("[*]Sript continued running smoothly in total silence, ")