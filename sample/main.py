import pathlib

from jira_tool import process_excel_file

# Current directory
HERE = pathlib.Path(__file__).resolve().parent


def main():
    input_file = HERE.parent / "docs/red.xlsx"
    output_file = "sorted.xlsx"

    process_excel_file(input_file, output_file)


if __name__ == "__main__":
    main()
