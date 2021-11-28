

class CleaningAssistant:
    def __init__(self):
        self.valid = ["text", "f0", "mel", "spk", "audio"]
        self.technique = {
            "text": ["token_truncation", "length_regularization"],
            "mel": ["check_extraction", "normalization", "length_regularization", "merge", "split|text"],
            "f0": ["check_extraction", "quantize", "normalization", "length_regularization", "merge", "split|text"],
            "spk": ["removal"],
            "audio": ["quantize"]
        }

        self.input_output_pair = {
            "text": ["f0", "mel"],
            "f0": ["f0|spk", "mel", "spk"],
            "mel": ["text", "f0", "mel|spk", "spk", "audio"],
            "spk": ["audio", "f0", "mel"],
            "audio": ["audio"]
        }

    def check_valid_input(self, input):
        if input not in self.valid:
            raise ValueError("Invalid input: " + str(input))

    def output_suggestion(self, input):
        self.check_valid_input(input)
        outputs = self.input_output_pair[input]
        results = []
        for o in outputs:
            cond = self.condition_parse(o)
            results.append((cond[0], cond[1]))
        return results

    def tech_suggestions(self, input, output):
        all = input.copy()
        all.extend(output)

        all_set = set(all)
        all_tech = []
        for keyword in all_set:
            self.check_valid_input(keyword)
            for spec in self.technique[keyword]:
                tech, cond = self.condition_parse(spec)
                if cond is None or cond not in all_set:
                    all_tech.append((keyword, tech))

        all_tech.sort()
        return all_tech

    def condition_parse(self, input):
        parse = input.split("|")
        output = parse[0]
        cond = None
        if len(output) > 1:
            cond = output
        return output, cond

# [0.1, 1, 0.5] quantize_bin = 3
# (2 (length), 3 (bin)) ,matrix
#            bin (0~1/3, 1/3~2/3, 2/3~1)
#            (k= 3)
# sequential [0           , 1 (1 > 2/3),   0]
#            [0,          , 0          ,   1]
#            [1(0.1 < 1/3), 0          ,   0] (n=3)

# audio -> Feature extraction mel
#  (text) -> (mel)


# n-length array, k bins
# n by k matrix (each bin has 1 / k length)

# if __name__ == "__main__":
#     a = CleaningAssistant()
#     print(a.tech_suggestions(["mel", "spk", "f0"], ["mel"]))
