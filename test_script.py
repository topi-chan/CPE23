from main import cpe23_to_dict

def run_tests():
    # Load test cases from separate file
    with open("test_cases.txt", "r") as file:
        test_cases = file.readlines()

    print("Running Test Cases:")
    for test in test_cases:
        test = test.strip()
        try:
            print(f"\nInput: {test}")
            print(cpe23_to_dict(test))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    run_tests()
