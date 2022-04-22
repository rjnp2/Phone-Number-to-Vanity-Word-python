# Phone-Number-to-Vanity-Word-python (Assigment)

Most phone dialpads have letters written on them where the letter/number mapping is defined
according to the International Telecommunication Unions Standards. This allows businesses to
have a vanity phone number that is easy for their clients to remember such as:
1-800-PAINTER (1-800-724-6837)

(Instead of letters you dial the number that has the corresponding letter on it, so for
example:\
    Instead of A, B or C -> you would dial 2\
    Instead of G, H or I -> you would dial 4)

![image](https://user-images.githubusercontent.com/58425689/164577836-692b6396-1be7-4b3f-bd01-2cd9b68cfbdf.png)

Examples:
  - number 228 -> act bat cat
  - (762)-5387 -> pockets rockets sockets
  - letters ->
  - (2)-2-8 -> act bat cat

## Approach and Algorithm used
1. remove non-digit value from phone number and join all nmber
    ```python
      number = ''.join(e for e in number if e.isdigit())
     ```

2. convert number to set of alphabet
    ```python
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
    ```
3. use dynamic programing in recursive function
  Dynamic programming is nothing but recursion with memoization i.e. calculating and storing values that can be later accessed to solve subproblems that occur again, hence making your code faster and reducing the time complexity (computing CPU cycles are reduced).Aug 4, 2020
    ```python
        def find_alp(number, result, string="",index = 0):
          if index == len(number):
              result.append(string.strip())
              return

          for i in phone_dict[number[index]]:
              find_alp(number,result,string+i,index+1)
     ```

4. compare with dictionary file(dictionary.text file) if word exist in file or not

## Getting Started

### Developers Installation
    Instructions for clone in your development environment

    git clone https://github.com/rjnp2/Phone-Number-to-Vanity-Word-python.git
    cd Phone-Number-to-Vanity-Word-python/

## Usage

open terminal 

    python number_to_vanity.py --number 228
    Number is:  228
    Result is:  ['act', 'bat', 'cat']

    python number_to_vanity.py --number letter
    Number is:  letter
    Result is:  None

    python number_to_vanity.py --number '(228)'
    Number is:  (228)
    Result is:  ['act', 'bat', 'cat']

#### Last if you want to extend more, please add more data in dictionary.txt


