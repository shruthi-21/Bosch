import sys
def main():
    # sys.argv[0] is the script name
    print("Script name:", sys.argv[0])

    # Check if any arguments are passed
    if len(sys.argv) > 1:
        print("Arguments passed:", sys.argv[1:])
    else:
        print("No arguments passed.")

if __name__ == "__main__":
    main()
