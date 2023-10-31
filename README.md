# CPE 2.3 Parser

This script provides functionality to parse CPE (Common Platform Enumeration) 2.3 formatted strings into a structured dictionary format. The conversion is based on the official CPE Naming specification provided by NIST.

## Installation

For running the program locally:

1. Create a virtual environment:
```bash
$ python3 -m venv venv
```

2. Activate the virtual environment:
- On macOS and Linux:
```bash
$ source venv/bin/activate
```
- On Windows:
```bash
$ .\venv\Scripts\activate
```

3. Install the required libraries:
```bash
$ pip install -r requirements.txt
```
(Note: As of now, no external libraries are required.)

## Usage

To use the parser, run:

```bash
$ python main.py cpe_string_here
```

For example:

```bash
$ python main.py cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*
```

The script will then output a dictionary representation of the provided CPE 2.3 formatted string.

## Testing

The provided test script can be run using:
```bash
$ python test_script.py
```

This will run multiple test cases on the main script using the CPE strings provided in the CPE 2.3 specification.

## References

The implementation and test cases are based on the CPE Naming specification documented by NIST.

- [CPE 2.3 Naming Specification (NISTIR 7695)](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7695.pdf)

## Note

If you're using `zsh` (like the default shell in macOS), you might encounter issues due to its interpretation of wildcards. You can either escape the `*` with `\*` or switch to `bash` for testing or add noglob param:
```bash
noglob python main.py cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*
```
