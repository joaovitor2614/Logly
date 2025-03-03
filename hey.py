

def int_to_roman_numeral(num: int) -> str:
        roman_symbols_to_values_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        roman_numeral = ''
        stringfied_int = str(num)
        stringfied_int_len = len(stringfied_int)
        for index, stringfied_int_number in enumerate(stringfied_int):
            current_int_number_decimal_base_representation = str(10 ** (stringfied_int_len - index - 1))

            last_items_of_current_int_number_decimal_base_representation = len(current_int_number_decimal_base_representation) - 1
            last_items_of_current_int_number_decimal_base_representation = -last_items_of_current_int_number_decimal_base_representation
          
            stringfied_int_number_decimal_base = stringfied_int_number + current_int_number_decimal_base_representation[last_items_of_current_int_number_decimal_base_representation:]
        
            int_number_decimal_base = int(stringfied_int_number_decimal_base)
            int_number_decimal_base_copy = int(int_number_decimal_base)
            print('int_number_decimal_base_copy', int_number_decimal_base_copy)
            while int_number_decimal_base_copy > 0:

                for roman_symbol, roman_symbol_value in roman_symbols_to_values_mapping.items():
                    current_roman_numeral_symbol = None
                    if roman_symbol_value <= int_number_decimal_base_copy:
                        current_roman_numeral_symbol = roman_symbol
             
            roman_numeral += current_roman_numeral_symbol 
            int_number_decimal_base_copy -= roman_symbol_value
      
        return roman_numeral

int_to_roman_numeral(3749)