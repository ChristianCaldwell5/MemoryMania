# handles bad input for choice selection
def handle_invalid_option(option):
    try:
        int(option)
        print('Please select a valid option.')
    except ValueError:
        try:
            float(option)
            print('Please select a valid option.')
        except ValueError:
            print("Please enter a numeric value.")