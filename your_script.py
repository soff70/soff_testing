import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            changed_files = file.readlines()
            print("Changed files:")
            for line in changed_files:
                print(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
