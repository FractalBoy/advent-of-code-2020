#!/usr/bin/env python

from aoc_input import read_input_into_list

def main():
    passwords_and_policies = get_passwords_and_policies()

    valid = 0
    
    for password, policy in passwords_and_policies:
        if evaluate_password_with_policy(password, policy):
            valid += 1

    print()
    print(valid)

def evaluate_password_with_policy(password, policy):
    count = len([letter for letter in password if letter == policy['letter']])

    return count >= policy['range']['start'] and count <= policy['range']['end']

def get_passwords_and_policies():
    lines = read_input_into_list()

    for line in lines:
        parts = line.split()

        [range_start, range_end] = parts[0].split('-')
        letter = parts[1].replace(':', '')

        yield (
            parts[2],
            {
                'range': {
                    'start': int(range_start),
                    'end': int(range_end)
                },
                'letter': letter
            }
        )


if __name__ == '__main__':
    main()
