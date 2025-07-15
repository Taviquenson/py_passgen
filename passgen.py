from functions import get_parser, build_password

def main():
    # Parse command line arguments
    arg_parser = get_parser()
    args = arg_parser.parse_args()

    password = build_password(args)

    print(password)


if __name__ == "__main__":
    main() 
