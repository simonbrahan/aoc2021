chunk_delimiter_matches = {'(': ')', '[': ']', '{': '}', '<': '>'}

def is_opening(char):
    return char in ['(', '[', '{', '<']


def closes_current_chunk(stack, char):
    return chunk_delimiter_matches[stack[-1]] == char


def get_first_error(line):
    stack = []
    for char in line:
        if is_opening(char):
            stack.append(char)
            continue

        if closes_current_chunk(stack, char):
            stack.pop()
        else:
            return char

    return None


def get_missing_chars(line):
    stack = []
    for char in line:
        if is_opening(char):
            stack.append(char)
            continue

        if closes_current_chunk(stack, char):
            stack.pop()

    return reversed([chunk_delimiter_matches[char] for char in stack])
