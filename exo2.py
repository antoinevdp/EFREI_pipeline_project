import json, os

def load_sample(path):
    with open(path) as f:
        text = []
        for line in f:
            if line != '\n':
                line = line[:-1]
                text.append(line)
        return text


def generate_json(str_list):
    dico = {}
    total_sent = 0
    for i in str_list:
        l = i.split(' ')
        num = float(l[2][:-1])
        total_sent += num
        dico["name"] = l[0]
    dico["total_sent"] = total_sent
    return dico


def save_result(path, result):
    json.dump(result, open(path, "w+"))


if __name__ == "__main__":
    directory = 'source'
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        print(f)
        sample = load_sample(f)
        dico = generate_json(sample)
        string = (f"result_{file}.json")
        save_result(f'result/{string}', dico)