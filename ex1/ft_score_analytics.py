import sys


def score_catsing(score: str, score_valid: list[int]) -> None:
    try:
        score_valid.append(int(score))
    except ValueError:
        print(f"\033[31mInvalid parameter: '{score}'\033[0m")


def parsing_score(scores: list[str]) -> None:
    score_valid: list[int] = []
    for args in scores[1:]:
        score_catsing(args, score_valid)
    if len(score_valid) <= 0:
        print(
            "\033[31mNo scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ...\033[0m"
        )
        return
    print(f"\033[35mScores processed: {score_valid}\033[0m")
    print(f"Total players: {len(score_valid)}")
    print(f"Total score: {sum(score_valid)}")
    print(f"Average score: {float(sum(score_valid) / len(score_valid))}")
    print(f"\033[33mHigh score: {max(score_valid)}\033[0m")
    print(f"Low score: {min(score_valid)}")
    print(f"Range score: {max(score_valid) - min(score_valid)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    parsing_score(sys.argv)
