# Spoken To Written

This is a Python module which can that can convert a paragraph of spoken english to written english.

 For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.


## Installation:


  Please ensure that you have **updated pip3** to the latest version before installing spoken2written.
  
  You can install the module using Python Package Index using the below command.
   ```
   >>python3 setup.py install
   ```

## Usage:
   ```
    >>python3 convert.py
	>>
    Enter Your paragraph of spoken english:
    "My life is triple B. European authorities fined Google a record thousand dollars on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices. Furthermore , The T - Shirt size of C M is double X in 2019 and it costs six dollars."

    Converted Written English Paragraph:
    "My life is BBB. European authorities fined Google a record $1000 on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices. Furthermore , The T - Shirt size of CM is XX in 2019 and it costs six dollars."

## Future Scope:
* Added new rules like punctuation.
* New rules can be added in rules.py without having to re-test all the previous rule implementations.