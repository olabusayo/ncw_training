import argparse


decoder = {str(i-96): chr(i) for i in range(ord('a'), ord('z')+1)}


def count_possible_decodings(input):
    final_decoded_hash = get_all_possible_decodings(input)
    return len(final_decoded_hash.keys())


def get_all_possible_decodings(enc):
    decoded = []
    final = {}
    for index in range(len(enc)):
        ind = index
        while True:
            st, ind = find_substr(enc, ind)
            decoded.append(st)
            if ind >= len(enc):
                final[f"{','.join(str(i) for i in decoded)}"] = 1
                decoded = [enc[i] for i in range(index+1)]
                break
    return final


def find_substr(substr, ind):
        if ind+1 < len(substr) and check_condition(substr[ind: ind+2]):
                return substr[ind: ind+2], ind+2
        else:
            return substr[ind], ind+1


def check_condition(substr):
    if substr:
        return 1 <= int(substr) <= 26


def decode(substr):
    if check_condition(substr) and substr in decoder:
        return decoder[f'{substr}']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="string to be decoded")
    args = parser.parse_args()

    dec = ""
    poss_dec_hash = get_all_possible_decodings(args.input)
    print(f"The string '{args.input}' has {str(len(poss_dec_hash.keys()))} possible decodings")

    for p_dec in poss_dec_hash:
        for num in p_dec.split(','):
            dec += decode(num)
        print(f"{p_dec} => {dec}")
        dec = ''


if __name__ == "__main__":
    main()
