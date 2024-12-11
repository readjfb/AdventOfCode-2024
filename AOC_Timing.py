import subprocess
import time
import pandas as pd


def measure_script_timing(script_path):
    sector_times_ms = []
    setup = None
    answer_1 = None
    answer_2 = None

    # Start timing
    start_time = time.perf_counter()

    # Run the script and capture its output in real-time
    process = subprocess.Popen(
        ["python", "-u", script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=False,
    )

    last_time = start_time
    for line in iter(process.stdout.readline, ""):
        current_time = time.perf_counter()
        elapsed_since_start = current_time - start_time
        elapsed_since_last = current_time - last_time
        # print(f"Elapsed time since start: {1000 * elapsed_since_start:.2f}ms")
        # print(f"Elapsed time since last output: {1000 * elapsed_since_last:.2f}ms")

        sector_times_ms.append(elapsed_since_last)
        if not setup:
            setup = line
        elif not answer_1:
            answer_1 = line
        elif not answer_2:
            answer_2 = line

        last_time = current_time

    process.stdout.close()
    process.wait()

    return *sector_times_ms, answer_1, answer_2


if __name__ == "__main__":
    days = range(1, 11 + 1)
    n_trials = 3

    data = []
    for d in days:
        for i in range(n_trials):
            data.append(
                list(measure_script_timing(f"AdventOfCode-2024/day{d}/day{d}.py")) + [d]
            )

    data_df = pd.DataFrame(data)

    data_df.columns = [
        "Startup",
        "Part 1",
        "Part 2",
        "Solution P1",
        "Solution P2",
        "Day",
    ]

    data_df["Solution P1"] = (
        data_df["Solution P1"].str.strip().apply(lambda x: x.split(" ")[-1])
    )
    data_df["Solution P2"] = (
        data_df["Solution P1"].str.strip().apply(lambda x: x.split(" ")[-1])
    )

    data_df["Solution P1"] = data_df["Solution P1"].astype(int)
    data_df["Solution P2"] = data_df["Solution P2"].astype(int)

    data_df[["Startup", "Part 1", "Part 2"]] *= 1000

    data_df["Total"] = data_df[["Startup", "Part 1", "Part 2"]].sum(axis=1)

    # print(data_df)
    print(data_df.groupby("Day").mean())
