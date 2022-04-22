import argparse

# Create the parser
my_parser = argparse.ArgumentParser(description='List the arguments for py file')

phone_dict = {
    '0':' ',
    '1':' ',
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']
}

with open('dictionary.txt') as file:
    letter_list = file.read().split('\n')

def find_alp(number, result, string="",index = 0):
    if index == len(number):
        result.append(string.strip())
        return

    for i in phone_dict[number[index]]:
        find_alp(number,result,string+i,index+1)

def vanity_converter(number):
    number = ''.join(e for e in number if e.isdigit())
    if number:
        result = []
        find_alp(number,result)

        final = []
        for res in result:
            if res in letter_list:
                final.append(res)
        return final

    else:
        return 

# Add the arguments
my_parser.add_argument('--number', '-no',
                       required= True,
                       help='Enter your Phone Number')

if __name__ == "__main__":
    # Execute the parse_args() method
    args = my_parser.parse_args()
    print('Number is: ', args.number)
    result = vanity_converter(args.number)
    print('Result is: ', result)