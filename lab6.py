def max_experience(levels: list[list[int]]) -> int:
    if not levels:
        return 0

    dp = levels[-1][:]
    for level in range(len(levels) - 2, -1, -1):
        current_level = []
        for i in range(len(levels[level])):
            max_exp = max(dp[i], dp[i + 1])
            current_level.append(levels[level][i] + max_exp)
        dp = current_level

    return dp[0]


def parse_input_file(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    L = int(lines[0])
    levels = [list(map(int, line.strip().split())) for line in lines[1:L + 1]]
    return levels


def write_output_file(file_path: str, result: int):
    with open(file_path, 'w') as f:
        f.write(f"{result}\n")


if __name__ == "__main__":
    input_levels = parse_input_file("input.txt")
    result = max_experience(input_levels)
    write_output_file("output.txt", result)
