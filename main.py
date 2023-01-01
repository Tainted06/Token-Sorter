# Imports
import os, base64, datetime

def main():
    # Starting
    print("Starting...")
    start_time = datetime.datetime.utcnow()

    # Output folder
    name = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
    dirs = [f"output/{name}", f"output/{name}/sorted_by_month", f"output/{name}/sorted_by_year", f"output/{name}/sorted_by_relative_time_year", f"output/{name}/sorted_by_relative_time_month"]
    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)

    # Iterate through file
    with open("input.txt") as f:
        tokens = f.read().splitlines()

    for token in tokens:
        # Splitting token to remove email/pass
        full_token = token
        if ":" in token:
            token = token.split(":")[2]

        # Getting userid
        userid = base64.b64decode(token.split(".")[0] + "==").decode("utf-8")

        # Getting timestamp
        creationdate_unix = int(bin(int(userid))[:-22], 2) + 1420070400000

        # Get date
        year, month = datetime.datetime.fromtimestamp(creationdate_unix / 1000).strftime("%Y"), datetime.datetime.fromtimestamp(creationdate_unix / 1000).strftime("%m")
        difference = datetime.datetime.utcnow() - datetime.datetime.fromtimestamp(creationdate_unix / 1000)
        years, months = difference.days // 365, (difference.days % 365) // 30

        # Write token
        for dir in dirs:
            if "by_year" in dir:
                with open(f"{dir}/{year}.txt", "a") as f:
                    f.write(full_token + "\n")
            elif "by_month" in dir:
                with open(f"{dir}/{year}-{month}.txt", "a") as f:
                    f.write(full_token + "\n")
            elif "relative_time_year" in dir:
                with open(f"{dir}/{years} year(s).txt", "a") as f:
                    f.write(full_token + "\n")
            elif "relative_time_month" in dir:
                with open(f"{dir}/{years} year(s) {months%12} month(s).txt", "a") as f:
                    f.write(full_token + "\n")

    # Finishing
    print(f"Finished sorting {len(tokens)} tokens in {(datetime.datetime.utcnow() - start_time).total_seconds()} seconds!")

if __name__ == "__main__":
    os.system("cls")
    main()