import sys


def process_quoted_chars(s: str) -> str:
    """
    Process the quoted special characters in the input string.
    Follows documentation: https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7695.pdf
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


def cpe23_to_dict(cpe_string: str) -> dict:
    """
    Convert a CPE 2.3 formatted string into a dictionary representation.
    The function follows the mapping given in section 6.2.2.3 of the official CPE Naming documentation.

    :param cpe_string: A CPE 2.3 formatted string.
    :return: Dictionary representation of the CPE string.
    """

    # Checking for proper CPE 2.3 URI format
    if not cpe_string.startswith("cpe:2.3:"):
        raise ValueError("Niepoprawny format CPE 2.3")

    # Extracting components of the CPE 2.3 URI
    parts = cpe_string[8:].split(":")

    # A CPE 2.3 URI should split into 11 components for validation, as per the standard.
    if len(parts) != 11:
        raise ValueError("Niepoprawny ciąg CPE 2.3")

    # Mapping parts of the CPE URI to their respective dictionary keys
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

    # Constructing the dictionary
    cpe_dict = dict(zip(keys, parts))

    # Translating values based on the standard.
    # In section 6.2.2.3 of the documentation, it specifies how certain characters
    # and patterns should be interpreted.
    for key, value in cpe_dict.items():
        cpe_dict[key] = value.replace("\\", "").replace("*", "ANY").replace("-", "NA")

    return cpe_dict


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
