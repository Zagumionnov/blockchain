"""Simple blockchain training project"""
import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'


def get_files():
    """get names of block"""
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])


def get_hash(filename):
    """Hashing data func"""
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def write_block(name, amount, to_whom, prev_hash=""):
    """Block creation func"""

    files = get_files()

    prev_file = files[-1]
    filename = str(prev_file + 1)

    prev_hash = get_hash(str(prev_file))

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash_sum': prev_hash
            }

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def check_integrity():
    """Block integrity check"""

    files = get_files()

    results = []

    for file in files[1:]:
        cur_hash = json.load(open(blockchain_dir + str(file)))['hash_sum']
        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if cur_hash == actual_hash:
            res = "OK"
        else:
            res = "Corrupted"
        results.append({'block': prev_file, 'result': res})

    return results


def main():
    print(check_integrity())


if __name__ == '__main__':
    main()