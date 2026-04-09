import os
import time

path_to_watch = "."
log_file = "logs/activity_log.txt"

before = dict([(f, None) for f in os.listdir(path_to_watch)])

print("Advanced Monitoring Started...")

while True:
    time.sleep(5)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])

    added = [f for f in after if f not in before]
    removed = [f for f in before if f not in after]

    with open(log_file, "a") as log:
        if added:
            log.write(f"Added: {', '.join(added)}\n")
            print("Added:", added)

        if removed:
            log.write(f"Removed: {', '.join(removed)}\n")
            print("Removed:", removed)

    before = after
