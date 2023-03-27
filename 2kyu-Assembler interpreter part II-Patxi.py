import os
import io
import contextlib
import ast
import operator as op


class Compiler(type):
    def __new__(cls, cls_name, superclasses, attribute_dict):
        return type.__new__(cls, cls_name, superclasses, attribute_dict)


def escape_text(text: str):
    for line in text.splitlines():
        r = line.split(';')[0].strip()
        if not r:
            continue
        yield r


class Register:
    def __init__(self, name, registers):
        self.name = name
        self.registers = registers

    def get_value(self):
        return self.registers.get(self.name)


class Constant:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Program:
    def parse_operation_line(self, line: str):
        s = line.partition(' ')
        yield getattr(self, s[0])

        tree = ast.parse(s[2].strip())
        for b in ast.walk(tree):
            if isinstance(b, ast.Continue):
                yield Register('continue', self.registers)
            if isinstance(b, ast.Constant):
                yield Constant(b.value)
            elif isinstance(b, ast.Name):
                yield Register(b.id, self.registers)
            elif isinstance(b, ast.Str):
                yield b.s

    def __init__(self, text):
        self.output = io.StringIO()
        self.registers = {}
        self.labels = {}
        self.instructions = []
        self.pointer = 0
        self.stack = []
        self.compare = 0

        for i, s in enumerate(escape_text(text)):
            if s.endswith(':'):
                self.labels[s.rstrip(':')] = i - len(self.labels) - 1
            else:
                self.instructions.append(tuple(self.parse_operation_line(s)))

    def run(self):
        try:
            while self.pointer != -1:
                instruction, *arguments = self.instructions[self.pointer]
                instruction(*arguments)
                self.pointer += 1
        except IndexError:
            return -1

        return self.output.getvalue()

    def mov(self, register, value):
        self.registers[register.name] = value.get_value()

    def add(self, register, value):
        self.registers[register.name] += value.get_value()

    def sub(self, register, value):
        self.registers[register.name] -= value.get_value()

    def inc(self, register):
        self.registers[register.name] += 1

    def dec(self, register):
        self.registers[register.name] -= 1

    def mul(self, register, value):
        self.registers[register.name] *= value.get_value()

    def div(self, register, value):
        self.registers[register.name] //= value.get_value()

    def call(self, label):
        self.stack.append(self.pointer)
        self.jmp(label)

    def ret(self):
        self.pointer = self.stack.pop()

    def jmp(self, label):
        self.pointer = self.labels[label.name]

    def cmp(self, left, right):
        self.compare = left.get_value() - right.get_value()

    def jne(self, label):
        if self.compare != 0:
            self.jmp(label)

    def je(self, label):
        if self.compare == 0:
            self.jmp(label)

    def jge(self, label):
        if self.compare >= 0:
            self.jmp(label)

    def jg(self, label):
        if self.compare > 0:
            self.jmp(label)

    def jle(self, label):
        if self.compare <= 0:
            self.jmp(label)

    def jl(self, label):
        if self.compare < 0:
            self.jmp(label)

    def msg(self, *args, **kwargs):
        with contextlib.redirect_stdout(self.output):
            for a in args:
                print(a.get_value(), **kwargs, end='')

    def end(self):
        self.pointer = -2


def assembler_interpreter(program):
    return Program(program).run()
