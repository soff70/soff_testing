import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "processed_files.txt"

    try:
        with open(input_file, 'r') as file:
            changed_files = [line.strip() for line in file.readlines()]

        # Combine the contents of all files listed in changed_files.txt
        combined_contents = []
        for file_path in changed_files:
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    combined_contents.append(f"Contents of {file_path}:\n")
                    combined_contents.append(f.read())
                    combined_contents.append("\n")
            else:
                combined_contents.append(f"File not found: {file_path}\n")

        # Write the combined contents to processed_files.txt
        with open(output_file, 'w') as file:
            file.write("\n".join(combined_contents))

        print(f"Processed files written to {output_file}")
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        sys.exit(1)

if __name__ == "__main__":
    main()
