file1_path = "works_with_csv/rmc.csv"
file2_path = "works_with_csv/r-m-c.csv"

def read_csv(filepath):
    rows = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            rows.append(line)
    return rows

def write_csv(filepath, rows):
    with open(filepath, "w") as f:
        for row in rows:
            f.write(row + "\n")

rows1 = read_csv(file1_path)
rows2 = read_csv(file2_path)
combined_rows = rows1 + rows2

unique_rows = list(dict.fromkeys(combined_rows))

output_file = "result_bakhmatska.csv"
write_csv(output_file, unique_rows)

