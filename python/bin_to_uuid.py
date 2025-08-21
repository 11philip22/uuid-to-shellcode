""""partially stolen from https://blog.sunggwanchoi.com/eng-uuid-shellcode-execution/"""
from sys import argv

from shellcode_to_uuid import convert_to_uuid


def main(file_path):
    with open(file_path, 'rb') as bin_file:
        byte_arr_file = bytearray(bin_file.read())
        uuids = convert_to_uuid(bytes(byte_arr_file))
        print(*uuids, sep=",\n")


if __name__ == "__main__":
    main(argv[1])
