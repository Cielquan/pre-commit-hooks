#!/usr/bin/env python3
"""Add a ruler comment to commit message."""
import pathlib
import sys

RULER_COMMENT = "#                20↑                 40↑                 60↑                 80↑                100↑                120↑"


def main() -> int:
    """Main."""
    commit_msg_file = pathlib.Path(sys.argv[1])

    commit_msg_lines = commit_msg_file.read_text("utf8").split("\n")
    print("### START\ncommit_msg_lines\n", commit_msg_lines, "\n### END")

    first_comment_line = len(commit_msg_lines)
    for idx, line in enumerate(commit_msg_lines):
        if line.lstrip(" ").startswith("#"):
            first_comment_line = idx
            break

    commit_msg_lines.insert(first_comment_line, RULER_COMMENT)
    print("### START\ncommit_msg_lines\n", commit_msg_lines, "\n### END")

    commit_msg_file.write_text("\n".join(commit_msg_lines), "utf8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
