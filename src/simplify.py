def simplify_path(path):
    """
    Simplify an absolute Unix-style path.

    :param path: string, e.g., "/a/./b/../../c/"
    :return: simplified canonical path, e.g., "/c"
    """
    stack = []
    parts = path.split("/")  # Split by /

    for part in parts:
        if part == "" or part == ".":
            # Ignore empty parts or current directory
            continue
        elif part == "..":
            # Go up one directory, if possible
            if stack:
                stack.pop()
        else:
            # Valid directory name, push onto stack
            stack.append(part)

    # Reconstruct the simplified path
    return "/" + "/".join(stack)
