
# 2. Create a database (List of privileged users) print a specific
#   message with a personal greeting if the user is a privileged 
#  and just "Welcome otherwise"

programmer=input('Please enter Your name:')
privileged_programmers = ["Oleg", "Vytautas", "Mindaugas"]

if programmer in privileged_programmers:
    print(f"{programmer} You are best python programmer")
else:
    print("INTRUDER ALLERT. Silently calling police...")
