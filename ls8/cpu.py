"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = {}
        self.registers = [0] * 8
        self.registers[SP] = 0xf4
        self.pc = 0
        self.running = True

        self.branchtable = {}

        # ALU OPERATIONS
        self.branchtable[ADD] = self.handle_op_ADD
        self.branchtable[SUB] = self.handle_op_SUB
        self.branchtable[MUL] = self.handle_op_MUL
        self.branchtable[DIV] = self.handle_op_DIV
        self.branchtable[MOD] = self.handle_op_MOD
        self.branchtable[INC] = self.handle_op_INC
        self.branchtable[DEC] = self.handle_op_DEC
        self.branchtable[CMP] = self.handle_op_CMP
        self.branchtable[AND] = self.handle_op_AND
        self.branchtable[NOT] = self.handle_op_NOT
        self.branchtable[OR] = self.handle_op_OR
        self.branchtable[XOR] = self.handle_op_XOR
        self.branchtable[SHL] = self.handle_op_SHL
        self.branchtable[SHR] = self.handle_op_SHR

        # PC MUTATORS
        self.branchtable[CALL] = self.handle_op_CALL
        self.branchtable[RET] = self.handle_op_RET
        self.branchtable[INT] = self.handle_op_INT
        self.branchtable[IRET] = self.handle_op_IRET
        self.branchtable[JMP] = self.handle_op_JMP
        self.branchtable[JEQ] = self.handle_op_JEQ
        self.branchtable[JNE] = self.handle_op_JNE
        self.branchtable[JGT] = self.handle_op_JGT
        self.branchtable[JLT] = self.handle_op_JLT
        self.branchtable[JLE] = self.handle_op_JLE
        self.branchtable[JGE] = self.handle_op_JGE

        # OTHER CODES
        self.branchtable[NOP] = self.handle_op_NOP
        self.branchtable[HLT] = self.handle_op_HLT
        self.branchtable[LDI] = self.handle_op_LDI
        self.branchtable[LD] = self.handle_op_LD
        self.branchtable[ST] = self.handle_op_ST
        self.branchtable[PUSH] = self.handle_op_PUSH
        self.branchtable[POP] = self.handle_op_POP
        self.branchtable[PRN] = self.handle_op_PRN
        self.branchtable[PRA] = self.handle_op_PRA

    def ram_read(self, mar):
        # is reading printing or returning?
        return self.ram[mar]

    def ram_write(self, mdr, val):
        self.ram[mdr] = val
        print(f"PC wrote {val} to ram at location {mdr}")

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        IR = self.ram[self.pc]
        # operand_a = self.ram_read(self.pc + 1) # lol, this is worst way to do it fix
        # operand_b = self.ram_read(self.pc + 2) # lol, this is worst way to do it fix  

        var = True

        while var:
            if IR == '00000001':
                var = False
            else:
                print(f'Unknown instruction: {IR}')
                sys.exit(1)

    
