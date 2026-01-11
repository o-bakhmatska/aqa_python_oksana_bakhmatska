from datetime import datetime
from config import LOG_FILE, OUTPUT_LOG, KEY

def get_time_from_line(line):
    start_position = line.find("Timestamp ")
    if start_position == -1:
        return None
    time_str = line[start_position + 10 : start_position + 18]
    try:
        return datetime.strptime(time_str, "%H:%M:%S")
    except:
        return None

def analyze_heartbeat():
    filtered_log = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            if KEY in line:
                filtered_log.append(line.strip())
    timestamps = []
    for line in filtered_log:
        time = get_time_from_line(line)
        if time:
            timestamps.append((time, line))

    with open(OUTPUT_LOG, "w") as log:
        for i in range(len(timestamps) - 1):
            current_time, current_line = timestamps[i]
            next_time, next_line = timestamps[i + 1]

            delta = (current_time - next_time).total_seconds()

            if 31 < delta < 33:
                log.write(f"WARNING [{current_time.strftime('%H:%M:%S')}]: Heartbeat {delta:.1f} sec\n")
            elif delta >= 33:
                log.write(f"ERROR   [{current_time.strftime('%H:%M:%S')}]: Heartbeat {delta:.1f} sec\n")

    print("DONE. RESULT in hb_test.log")


if __name__ == "__main__":
    analyze_heartbeat()

