
# Roman Numbers

**🎯 Write a function `roman2arabic()`, that translates a Roman into an Arabic number.**

## Tests

The following code helps you to check the results:

    def test_roman(self):
        assert roman2arabic("I") == 1
        assert roman2arabic("XI") == 11
        assert roman2arabic("IX") == 9
        assert roman2arabic("CLI") == 151
        assert roman2arabic("XCIII") == 93
        assert roman2arabic("CCXCIV") == 294
        assert roman2arabic("MCM") == 1900
        assert roman2arabic("MI") == 1001

## Hints

* You only have to consider numbers from 1-5000
* Which data structure is suitable for looking up the numerical values of Roman numerals?

## Extra Challenge

* Write a function that converts Arabic to Roman numerals.

*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
