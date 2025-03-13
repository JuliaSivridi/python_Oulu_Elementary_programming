def read_row(row, results):
    try:
        player1_name, player2_name, player1_score, player2_score = row.split(",")
        result = {
            "p1n": player1_name.strip(),
            "p1s": int(player1_score),
            "p2n": player2_name.strip(),
            "p2s": int(player2_score)
        }
        results.append(result)
    except ValueError:
        print(f"Unable to read row: {row}")

def show_results(filename):
    results = []
    try:
        with open(filename) as source:
            for row in source.readlines():
                read_row(row, results)
    except IOError:
        print("Unable to open the target file. Starting with an empty results.")
    for result in results:
        print(f"{result['p1n']} {result['p1s']} - {result['p2s']} {result['p2n']}")

show_results("hemulencup.csv")
