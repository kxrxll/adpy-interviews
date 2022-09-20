from stack import Stack

data = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{}",
    "{{[(])]}}",
    "[[{())}]"
]


def balance_check(string_to_check: str) -> str:
    stack = Stack()
    compliance_dict = {
        "{": 0,
        "}": 0,
        "(": 0,
        ")": 0,
        "[": 0,
        "]": 0
    }
    for char in string_to_check:
        stack.push(char)
    while not stack.isEmpty():
        compliance_dict[stack.pop()] += 1
    if compliance_dict['{'] == compliance_dict['}']\
            and compliance_dict['['] == compliance_dict[']']\
            and compliance_dict['('] == compliance_dict[')']:
        return 'Balanced!'
    else:
        return 'Not balanced!'


if __name__ == "__main__":
    for item in data:
        print(balance_check(item))
