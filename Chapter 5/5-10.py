current_users=['admin','jackie','jenny','tom','robert']
new_users=['jackie','tom','robert','jafferson']
for user in new_users:
    if user in current_users:
        print(f"{user} please enter a new username")
    else:
        print(f"your username {user} is available")
