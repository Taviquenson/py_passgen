import argparse
import random
from definitions import CHARSETS

def get_parser():
    arg_parser = argparse.ArgumentParser(description="A program that generates passwords without ambiguous characters.",
                                         epilog="By default, a 12 characters long password with numbers, uppercase and lowercase letters is created."
                                         ) 
    # By default:
    # Include a dozen of upper, lower, digits, symbols
    arg_parser.add_argument('-l', '--lowercase', action='store_true', help='Use lowercase')
    arg_parser.add_argument('-u', '--uppercase', action='store_true', help='Use uppercase')
    arg_parser.add_argument('-d', '--digits', action='store_true', help='Use digits')
    arg_parser.add_argument('-s', '--symbols', action='store_true', help='Use symbols')
    arg_parser.add_argument('opt_pass_len', type=int, default=12, nargs='?', help='Optionally indicates password length')

    return arg_parser


def build_password(args):
    selected_sets = []
    guaranteed_chars = []

    # Add one character from each selected type
    for key in CHARSETS:
        if getattr(args, key):
            charset = CHARSETS[key]
            selected_sets.append(charset)
            guaranteed_chars.append(random.choice(charset))

    if not selected_sets:
        charset = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789!@#$%^&*'

    # Combine all selected character sets
    full_charset = ''.join(selected_sets)

    # How many more characters to generate?
    remaining_length = args.opt_pass_len - len(guaranteed_chars)
    if remaining_length < 0:
        raise ValueError(f"Password length too short to include one of each selected type ({len(guaranteed_chars)} required).")

    # Add random characters from full set
    if not selected_sets:
        return ''.join(random.choice(charset) for _ in range(args.opt_pass_len))
    else:
        password_chars = guaranteed_chars + [random.choice(full_charset) for _ in range(remaining_length)]

    # Shuffle to avoid placing guaranteed chars at the start
    random.shuffle(password_chars)

    return ''.join(password_chars)