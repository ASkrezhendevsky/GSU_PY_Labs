from heapq import heappush, heappop, heapify
from collections import defaultdict


class Encoder:
    def __init__(self, compression_coefficient):
        self.compression_coefficient = compression_coefficient

    def __set_compression_coefficient(self, compression_coefficient):
        self.compression_coefficient = compression_coefficient

    def get_compression_coefficient(self):
        return self.compression_coefficient

    def encode(self, message):
        return message

    def decode(self, message):
        return message


def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key

    return "key doesn't exist"


class HuffmanEncoder(Encoder):
    def __init__(self):
        self.char_dict = {}

    def encode(self, text):
        freq_lib = defaultdict(int)

        for ch in text:
            freq_lib[ch] += 1

        heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]
        heapify(heap)

        while len(heap) > 1:
            right = heappop(heap)
            left = heappop(heap)
            for pair in right[1:]:
                pair[1] = '0' + pair[1]  # add zero to all the right note
            for pair in left[1:]:
                pair[1] = '1' + pair[1]  # add one to all the left note
            heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])
            huffman_list = right[1:] + left[1:]
            huffman_dict = {a[0]: str(a[1]) for a in huffman_list}
        code = ""
        for char in text:
            code += huffman_dict[char]
        self.char_dict = huffman_dict
        return code

    def decode(self, code):
        items = list(self.char_dict.values())
        char_code = ""
        message = ""

        for ch in code:
            char_code += ch
            if char_code in items:
                message += get_key(char_code, self.char_dict)
                char_code = ""

        return message


class LZEncoder(Encoder):

    def encode(self, uncompressed):
        # Build the dictionary.
        dict_size = 256
        dictionary = dict((chr(i), chr(i)) for i in range(dict_size))
        # in Python 3: dictionary = {chr(i): chr(i) for i in range(dict_size)}

        w = ""
        result = []
        for c in uncompressed:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                # Add wc to the dictionary.
                dictionary[wc] = dict_size
                dict_size += 1
                w = c

        # Output the code for w.
        if w:
            result.append(dictionary[w])
        return result

    def decode(self, compressed):
        dict_size = 256
        dictionary = dict((chr(i), chr(i)) for i in range(dict_size))
        # in Python 3: dictionary = {chr(i): chr(i) for i in range(dict_size)}

        w = result = compressed.pop(0)
        for k in compressed:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[0]
            else:
                raise ValueError('Bad compressed k: %s' % k)
            result += entry

            # Add w+entry[0] to the dictionary.
            dictionary[dict_size] = w + entry[0]
            dict_size += 1

            w = entry
        return result


message = """Python is a widely used high-level programming language for
general-purpose programming, created by Guido van Rossum
and first released in 1991."""

h_encoder = HuffmanEncoder()
code = h_encoder.encode(message)
print("\nOriginal message : \n"+message)
print("\nEncoded message :")
print(code)
print("\nDecoded message : \n"+h_encoder.decode(code))

lze_encoder = LZEncoder(1)
code = lze_encoder.encode(message)
print("\nOriginal message : \n"+message)
print("\nEncoded message : ")
print(code)
print("\nDecoded message : \n"+lze_encoder.decode(code))
