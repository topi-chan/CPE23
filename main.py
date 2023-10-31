import sys


def process_quoted_chars(s: str) -> str:
    """
    Process the quoted special characters in the input string.

    For CPE 2.3, the special characters (`*`, `?`, `-`, and `\`) may be quoted using
    the `\` character (Section 6.2.3 of CPE 2.3 Specification). This function returns
    a string where these quoted characters are processed and unquoted.
    """
    out = []
    i = 0
    while i < len(s):
        if s[i] == "\\":
            if i + 1 < len(s) and s[i + 1] in "*?-\\":
                out.append(s[i + 1])
                i += 1
            else:
                out.append(s[i])
        else:
            out.append(s[i])
        i += 1
    return "".join(out)


def bind_value_for_fs(v: str) -> str:
    """
    Bind the logical value in the CPE 2.3 name to its corresponding value
    in the formatted string (FS) representation
    (Section 6.2.2 of CPE 2.3 Specification).

    For CPE 2.3, the logical value ANY binds to `*` in the FS, and NA binds
    to `-`. All other values are left unchanged, except that quoted special
    characters are processed and unquoted.
    """
    if v == "ANY":
        return "*"
    elif v == "NA":
        return "-"
    else:
        return process_quoted_chars(v)


def cpe23_to_dict(cpe23: str) -> dict:
    """
    Convert a CPE 2.3 formatted string to its dictionary representation
    (Section 6.2.2 of CPE 2.3 Specification).

    The formatted string must conform to the CPE 2.3 specification. This function
    returns a dictionary where the keys are CPE attributes and the values are
    derived from the input string. Raises a ValueError if the input string is not
    a valid CPE 2.3 formatted string.
    """
    # Ensure the CPE string starts with the required prefix (Section 6.2.2 of CPE 2.3 Specification)
    if not cpe23.startswith("cpe:2.3:"):
        raise ValueError("Niepoprawny ciąg CPE 2.3")

    # Split the CPE string into its components
    parts = cpe23[8:].split(":")
    # Ensure there are exactly 11 components, as specified (Section 6.2.2 of CPE 2.3 Specification)
    if len(parts) != 11:
        raise ValueError("Niepoprawny ciąg CPE 2.3")

    keys = [
        "part",
        "vendor",
        "product",
        "version",
        "update",
        "edition",
        "language",
        "sw_edition",
        "target_sw",
        "target_hw",
        "other",
    ]

    return {k: bind_value_for_fs(v) for k, v in zip(keys, parts)}


if __name__ == "__main__":
    # Ensure the user provides a CPE 2.3 string as an argument
    if len(sys.argv) < 2:
        print("Proszę podać ciąg CPE 2.3 jako argument.")
        sys.exit(1)

    cpe_string = sys.argv[1]

    # Convert the CPE string to dictionary form and print the result
    try:
        result = cpe23_to_dict(cpe_string)
        print(result)
    except Exception as e:
        print(f"Błąd: {e}")
