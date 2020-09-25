from django.shortcuts import render
from myapp.form import *
# Create your views here.
ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'fourty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

elevens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
           15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def homeform(request):

    if request.method == "POST":

        logs = Home_form(request.POST)
        # inputs = '513012'
        if logs.is_valid():
            inputs = logs.cleaned_data['inputs']
        out = convert(inputs)
        # else:
        # inputs = 82983
        # print(inputs)
        # else:
        #    c=0
    return render(request, "home.html", {'result': out})


def thousands(a, word):
    global ones
    global tens
    global elevens
    first_two_number = a[0:2]
    number = int(''.join(first_two_number))
    if str(first_two_number[0]) == '1' and int(''.join(first_two_number)) > 10:
        for key, value in elevens.items():
            if key == int(''.join(first_two_number)):
                word = value + word
        return word
    elif number < 10:
        if number == 0:
            second_word = ''
        else:
            for key, value in ones.items():
                if str(key) == str(first_two_number[1]):
                    second_word = value + word
        return second_word
    elif int(first_two_number[1]) == 0 and number != 0:
        for key, value in tens.items():
            if str(first_two_number[0]) in str(key):
                second_word = value + word
        return second_word
    else:
        for key, value in tens.items():
            if first_two_number[0] in str(key):
                second_word = value
        for key, value in ones.items():

            if int(first_two_number[1]) == key:

                once_value = value
        words = second_word + once_value + word

        return words
        return words


def hundred(a):
    hundred_value = a
    result_word_h = 'hundred'
    if int(''.join(hundred_value[1:])) == 0:
        hundred_word = hundred_value[0]
        for key, value in ones.items():
            if str(key) == hundred_word:
                hundred_words = value + result_word_h
                return hundred_words
    elif int(hundred_value[1]) == 0:
        # print(hundred_value[0])
        for key, value in ones.items():
            if str(key) == hundred_value[0]:
                hundred_place = value + result_word_h
            if str(key) == hundred_value[-1]:
                onesplace = 'and' + value
        hundred_words = hundred_place + onesplace
        return hundred_words
    elif int(hundred_value[-1]) == 0:
        for key, value in ones.items():
            if str(key) == hundred_value[0]:
                hundred_place = value + result_word_h
        for key, value in tens.items():
            # print(hundred_value)
            if hundred_value[1] in str(key):
                tens_place = 'and' + value
        hundred_words = hundred_place + tens_place
        return hundred_words
    elif int(''.join(hundred_value[1:])) < 20 and int(''.join(hundred_value[1:])) > 10:
        for key, value in ones.items():
            if str(key) == hundred_value[0]:
                hundred_place = value + result_word_h
        for key, value in elevens.items():
            if str(key) == ''.join(hundred_value[1:]):
                tens_place = 'and ' + value
        hundred_words = hundred_place + tens_place
        return hundred_words
    else:
        for key, value in ones.items():
            if str(key) == hundred_value[0]:
                hundred_place = value + result_word_h
            if str(key) == hundred_value[-1]:
                onesplace = value
        for key, value in tens.items():
            # print(key)
            if hundred_value[1] in str(key):
                tens_place = 'and' + value
        hundred_words = hundred_place + tens_place + onesplace
        return hundred_words


def convert(number):

    c = [digit for digit in str(number)]
    hundred_words = ''
    if len(c) > 7:
        answer = "max limit is upto 6 digits"
        return answer

    elif len(c) == 6:
        first_position = c[0]
        word = 'lakh'
        for key, value in ones.items():
            if str(key) == first_position:
                word = value + word
        thousand_position = c[1:3]
        word_t = 'thousand'
        result_word_t = thousands(thousand_position, word_t)
        word_h = 'hundred'
        result_word_h = 'hundred'
        hundred_value = c[-3:]
        number = ''.join(hundred_value)
        number = int(number)
        if len(str(number)) == 3:

            hundred_words = hundred(hundred_value)
        elif len(str(number)) == 2:
            if int(number) < 20 and int(number) > 10:

                for key, value in elevens.items():
                    if key == number:
                        hundred_words = value
            elif int(hundred_value[-1]) == 0:
                for key, value in tens.items():
                    if str(hundred_value[-1]) in str(key):
                        hundred_words = value
            else:
                for key, value in tens.items():
                    if hundred_value[0] in str(key):
                        tens_place = value
                for key, value in ones.items():
                    if hundred_value[1] == str(key):
                        onesplace = value
                hundred_words = tens_place + onesplace
        elif number >= 1:
            for key, value in ones.items():
                if hundred_value[-1] == str(key):
                    onesplace = value
            hundred_words = onesplace
        else:
            hundred_words = ' '

        if int(''.join(c[1:])) == 0:
            answer = word
        else:
            if not hundred_words:
                hundred_words = ' '
            answer = word + ' ' + result_word_t + ' ' + hundred_words
    if len(c) == 5:
        thousand_position = c[0:2]
        word = 'thousand'
        result_word_t = thousands(thousand_position, word)
        result_word_h = 'hundred'
        hundred_value = c[-3:]
        number = ''.join(hundred_value)
        number = int(number)
        if len(str(number)) == 3:

            hundred_words = hundred(hundred_value)
        elif len(str(number)) == 2:
            if int(number) < 20 and int(number) > 10:

                for key, value in elevens.items():
                    if key == number:
                        hundred_words = value
            elif int(hundred_value[-1]) == 0:
                for key, value in tens.items():
                    if str(hundred_value[-1]) in str(key):
                        hundred_words = value
            else:
                for key, value in tens.items():
                    if hundred_value[0] in str(key):
                        tens_place = value
                for key, value in ones.items():
                    if hundred_value[1] == str(key):
                        onesplace = value
                hundred_words = tens_place + onesplace
        elif number >= 1:
            for key, value in ones.items():
                if hundred_value[-1] == str(key):
                    onesplace = value
            hundred_words = onesplace
        else:
            hundred_words = ''
        if int(''.join(c[1:])) == 0:
            answer = result_word_t

        else:
            if not hundred_words:
                hundred_words = ''
            answer = result_word_t + ' ' + hundred_words
    if len(c) == 4:
        first_position = c[0]
        word = 'thousand'
        number = c[1:]

        for key, value in ones.items():
            if first_position == str(key):
                word = value + word
        result_word_h = 'hundred'
        hundred_value = c[-3:]
        if int(''.join(hundred_value[1:])) != 0:
            hundred_words = hundred(hundred_value)
        else:
            hundred_words = ''

        if int(''.join(c[1:])) == 0:
            answer = word

        else:

            answer = word + ' ' + hundred_words
    if len(c) == 3:
        result_word_h = 'hundred'
        hundred_value = c[-3:]
        hundred_words = hundred(hundred_value)

        if int(''.join(c[1:])) == 0:
            for key, value in ones.items():
                if str(key) == c[0]:

                    answer = value + result_word_h

        else:
            if not hundred_words:
                hundred_words = ''
            answer = hundred_words
    if len(c) == 2:
        first_position = c[0]
        if int(''.join(c)) < 20 and int(''.join(c)) > 10:

            for key, value in elevens.items():
                if str(key) == ''.join(c):
                    answer = value
        elif int(c[-1]) == 0:
            for key, value in tens.items():
                if first_position in str(key):
                    answer = value
        else:
            for key, value in tens.items():
                if first_position in str(key):
                    tens_place = value
            for key, value in ones.items():
                if c[1] == str(key):
                    onesplace = value
            answer = tens_place + onesplace
    if len(c) == 1:
        if int(c[0]) == 0:
            answer = 'zero'
        else:
            for key, value in ones.items():
                if str(key) == c[0]:
                    answer = value
    return(answer)
