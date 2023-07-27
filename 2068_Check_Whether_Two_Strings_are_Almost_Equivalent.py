class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        step = 0
        let_map = {}

        while step != len(word1):
            if word1[step] not in let_map:
                let_map[word1[step]] = {"w1": 1}
            else:
                if "w1" in let_map[word1[step]]:
                    let_map[word1[step]]["w1"] += 1
                else:
                    let_map[word1[step]].update({"w1": 1})

            if word2[step] not in let_map:
                let_map[word2[step]] = {"w2": 1}
            else:
                if "w2" in let_map[word2[step]]:
                    let_map[word2[step]]["w2"] += 1
                else:
                    let_map[word2[step]].update({"w2": 1})

            step += 1

        for _, req in let_map.items():
            if "w1" in req and "w2" not in req and req["w1"] > 3:
                return False
            if "w2" in req and "w1" not in req and req["w2"] > 3:
                return False
            if "w1" in req and "w2" in req and abs(req["w1"] - req["w2"]) > 3:
                return False

        return True


s = Solution()
print(s.checkAlmostEquivalent(word1="cccddabba", word2="babababab"))
