from assignment1.censor_functions import censor_names, censor_dates;

def test_censor_names():
    # Input text containing names
    input_text = "Hello, my name is John and I work with Jane."
    
    # Expected output with names censored
    expected_output = "Hello, my name is ████ and I work with ████."
    
    # Apply censoring function
    output_text = censor_names(input_text)
    
    # Assert that names are censored
    assert output_text == expected_output, "Censoring names failed"

def test_censor_dates():
    # Input text containing dates
    input_text = "The meeting is scheduled for 12/25/2022 and the deadline is December 31, 2022."
    
    # Expected output with dates censored
    expected_output = "The meeting is scheduled for ██████████ and the deadline is █████████████████."
    
    # Apply censoring function
    output_text = censor_dates(input_text)
    
    # Assert that dates are censored
    assert output_text == expected_output, "Censoring dates failed"

