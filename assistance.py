class CleaningAssistant:
    def __init__(self):
        self.valid = ["text", "f0", "mel", "spk", "audio"]
        self.technique = {
            "text": ["token_truncation", "length_regularization"],
            "mel": ["normalization", "length_regularization", "merge", "split|text"],
            "f0": ["quantize", "normalization", "length_regularization", "merge", "split|text"],
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
                    all_tech.append((spec, tech))

        all_tech.sort()
        return all_tech

    def condition_parse(self, input):
        parse = input.split("|")
        output = parse[0]
        cond = None
        if len(output) > 1:
            cond = output
        return output, cond
