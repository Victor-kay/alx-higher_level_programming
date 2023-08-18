#!/usr/bin/python3

if __name__ == "__main__":
    import dis

    with open("hidden_4.pyc", "rb") as pyc_file:
        bytecode = pyc_file.read()

    code = compile(bytecode, "hidden_4.pyc", "exec")
    names = set()

    for instr in dis.get_instructions(code):
        if instr.opname == "LOAD_CONST":
            const = instr.arg
            if isinstance(const, str) and not const.startswith("__"):
                names.add(const)

    for name in sorted(names):
        print(name)
