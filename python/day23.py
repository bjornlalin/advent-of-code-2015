import sys

class Computer:

    def __init__(self, instrs):
        self.instrs = instrs
        self.reset()

    def reset(self):
        self.offset = 0
        self.regs = { 'a':0, 'b':0 }

    def hlf(self, reg):
        self.regs[reg] = self.regs[reg] / 2
        self.offset += 1

    def tpl(self, reg):
        self.regs[reg] = self.regs[reg] * 3
        self.offset += 1
    
    def inc(self, reg):
        self.regs[reg] = self.regs[reg] + 1
        self.offset += 1

    def jmp(self, offset):
        self.offset += offset

    def jie(self, reg, offset):
        if self.regs[reg] % 2 == 0:
            self.offset += offset
        else:
            self.offset += 1

    def jio(self, reg, offset):
        if self.regs[reg] == 1:
            self.offset += offset
        else:
            self.offset += 1

    def run(self):

        while self.offset < len(self.instrs):
            next = self.instrs[self.offset].strip('\n')

            _op = get_op(next)

            if _op == 'hlf':
                self.hlf(get_param(next, 0))
            if _op == 'tpl':
                self.tpl(get_param(next, 0))
            if _op == 'inc':
                self.inc(get_param(next, 0))
            if _op == 'jmp':
                self.jmp(int(get_param(next, 0).replace('+', '')))
            if _op == 'jie':
                self.jie(get_param(next, 0).replace('+', ''), int(get_param(next, 1).replace('+', '')))
            if _op == 'jio':
                self.jio(get_param(next, 0).replace('+', ''), int(get_param(next, 1).replace('+', '')))


def get_op(instr):
    return instr.split(' ')[0].strip()

def get_param(instr, index):
    return instr.split(' ')[index + 1].strip(',').strip(' ').strip('\n')

instrs = []
for line in sys.stdin:
    instrs.append(line)

computer = Computer(instrs)
computer.run()

print("Part 1: Register b contains {}".format(computer.regs['b']))

computer.reset()
computer.regs['a'] = 1
computer.run()

print("Part 2: Register b contains {}".format(computer.regs['b']))
