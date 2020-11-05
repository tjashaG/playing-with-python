from pathlib import Path

if __name__ == "__main__":
    p = Path(".", "data", "file.csv")
    lines = p.open(mode="r").readlines()

    for index, line in enumerate(lines):
        row = line.split(",")
        if line.lower().startswith("name"):
            continue
        else:
            print(f"{row[0]} is {row[1]} years old and a {row[2]}")
        
