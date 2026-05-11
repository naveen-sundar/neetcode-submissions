class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [] # record is a stack
        for i in operations:
            if i not in ("+", "C", "D"):
                record.append(int(i))
            if i == "+":
                record.append(record[-1] + record[-2])
            if i == "D":
                record.append(2*record[-1])
            if i == "C":
                record.pop()
        return sum(record)