################################################################################
#                                                                              #
#                               Helper Functions                               #
#                                                                              #
################################################################################

def nonEmpty(str):
    """Is the string empty?  Returns '' or a nonempty string.
    This works in a boolean context."""
    return ( str.strip() )

def isVar(str):
    """Is the string a legal variable name?"""
    # must contain only letters and digits, but the first
    # must be a letter.
    return ( str.isalnum() and str[0].isalpha() )
        
def isConst(str):
    """Is the string a legal integer constant?"""
    # isdigit requires at least one character
    return ( str.isdigit() 
             or ( str[1:] and str[0] == "-"  and str[1:].isdigit() ))

def isVarOrConst(str):
    """Is the string a legal variable name or constant?"""
    return ( isVar( str ) or isConst( str ))

def isLabel(str):
    """A legal label has same syntax as variable."""
    return isVar( str )

def isCommentLine(line):
    """A comment line is one that is empty or begins
    with (optionally) whitespace and a '#'."""
    line = line.strip()
    return not line or line[0] == "#"

################################################################################
#                                                                              #
#                            Low Instruction Objects                           #
#                                                                              #
################################################################################

import stack

"""This describes a simple stack-based assembly-like language called Low. 
   We begin with the following set of instructions.  TOS is top of stack.
   Args in brackets [] are optional. 

   -   DECL var [val]            -- declare a new variable, default to 0 for value
   -   OUT  var/int              -- output the value of var
   -   IN   var                  -- print a prompt and wait for input
   -   PUSH var/int              -- push value onto the stack
   -   POP  [var]                -- pop stack into variable var, or discard value
   -   TOP  var                  -- copy TOS into variable var, leave on stack
   -   DUP                       -- duplicate TOS and push
   -   DEC                       -- decrement the TOS value by 1
   -   INC                       -- increment the TOS value by 1
   -   ADD                       -- pop two values, add, push the result
   -   SUB                       -- pop two values, sub top from top2, push the result
   -   MUL                       -- pop two values, multiply, push the result
   -   MOD                       -- pop two values, compute s2 mod s1, push the result
   -   JMP  label                -- change pc to point to label
   -   CMP  var/int              -- compare TOS to var or value, set flags
   -   JEQ  label                -- jump to label if comparison = 0
   -   JNE  label                -- jump to label if comparison != 0
   -   JLT  label                -- jump to label is comparison < 0
   -   JGT  label                -- jump to label is comparison > 0
   -   JGE, label                -- jump to label if comparison >= 0
   -   JLE  label                -- jump to label if comparison <= 0
   -   CALL label                -- jump to label, save return address on callstack
   -   RET                       -- pop return address from callstack, jump
   -   HLT                       -- halt the machine

   To add a new Low instruction XYX:
   1.  Add a recognizer function legalXyz
   2.  Add a clause to the legalInstruction function
   3.  Add a semantic function xyzOp
   4.  Add a clause to the executeInstruction function
"""


class LowInstruction:
    """An instruction is just a list of fields:

         - a label, which may be empty
         - an opcode
         - up to two arguments

       All of these must be strings.
       """
    def __init__(self, opcode, label=None, arg1=None, arg2=None):
        """Create an Instruction object from a line in a file."""
        # Every instruction has an opcode
        self._opcode = opcode
        # There may or may not be arguments or a label
        self._label = label
        self._arg1 = arg1
        self._arg2 = arg2

    # Accessors for LowInstruction object fields

    def getLabel(self):
        return self._label

    def getOpcode(self):
        return self._opcode

    def getArg1(self):
        return self._arg1

    def getArg2(self):
        return self._arg2

    def __str__(self):
        """Print the instruction in a nice format."""
        if self._label:
            label = self._label + ":"
            outputstr = ("%-9s" % label) + self._opcode 
        else:
            outputstr = " "*9 + self._opcode 
        if self._arg1:
            outputstr = outputstr + " " + self._arg1 
        if self._arg2:
            outputstr = outputstr + " " + self._arg2
        return outputstr


    ## Parse an input line into an instruction object.

    # Notice that this is a class method, not an instance method.
    def parseLowInstruction(inputStr):
        """Takes a line from the input file and parses it into
        a LowInstruction object.  This currently does very little
        error checking. 
        """
        # print ("Parsing string: ", inputStr)
        fields = inputStr.split()
        
        # This shouldn't happen, but just to be safe, check for empty list
        if ( not fields ):
            print ("Instruction is empty")
            return
        if ( not fields[0].endswith(":") ):
            # If there is no label
            fields.insert(0, None)
        if ( len(fields) == 2 ):
            # If there are no args
            fields = fields + [None, None]
        elif ( len(fields) == 3 ):
            # If there's only one arg
            fields.append( None )
        label = ( fields[0][:-1] if fields[0] else None )
        opcode = fields[1]
        arg1 = fields[2]
        arg2 = fields[3]
        instructionObject = LowInstruction(opcode, label, arg1, arg2)
        return instructionObject

    def parseLowInstructionList (lst):
        """This creates a list of LowInstruction objects from a list
        of strings representing a Low program text.  It does little 
        error checking.  Comment lines (starting with whitespace and #
        are ignored. """
        print ("In parseLowInstructionList")
        prog = []
        for instr in lst:
            if isCommentLine( instr ):
                print ("Comment line found: ", instr)
                continue
            instObj = LowInstruction.parseLowInstruction( instr )
            prog.append( instObj )
        return prog


    # This series of methods recognize legal Low Instructions. 

    # Decl is the only operation (so far) that allows a second argument.

    def legalDecl( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "decl"
                 and isVar( arg1 )
                 and ( isConst( arg2 ) if arg2 else True ))

    def legalOut( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "out"
                 and isVarOrConst( arg1 )
                 and not arg2)

    def legalIn( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "in"
                 and isVar( arg1 )
                 and not arg2)

    def legalPush( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "push"
                 and isVarOrConst( arg1 )
                 and not arg2)

    def legalPop( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "pop"
                 and ( isVar( arg1 ) if arg1 else True)
                 and not arg2 )

    def legalTop( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "top"
                 and  isVar( arg1 )
                 and not arg2)

    def legalDup( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "dup" and not arg1 and not arg2 )

    def legalDec( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "dec" and not arg1 and not arg2 )

    def legalInc( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "inc" and not arg1 and not arg2 )

    def legalAdd( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "add" and not arg1 and not arg2 )

    def legalSub( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "sub" and not arg1 and not arg2 )

    def legalMul( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "mul" and not arg1 and not arg2 )

    def legalMod( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "mod" and not arg1 and not arg2 )

    def legalCmp( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "cmp"
                 and isVarOrConst( arg1 )
                 and not arg2 )

    def legalJmp( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "jmp"
                 and isLabel( arg1 )
                 and not arg2 )

    def legalJeq( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "jeq"
                 and isLabel( arg1 )
                 and not arg2 )

    def legalJne( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "jne"
                 and isLabel( arg1 )
                 and not arg2 )

    def legalJlt( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "jlt"
                 and isLabel( arg1 )
                 and not arg2 )

    def legalJgt( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "jgt"
                 and isLabel( arg1 )
                 and not arg2 )

    def legalJle( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "jle"
                 and isLabel( arg1 )
                 and not arg2 )

    def legalJge( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "jge"
                 and isLabel( arg1 )
                 and not arg2 )

    def legalCall( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "call"
                 and isLabel( arg1 )
                 and not arg2 )

    def legalRet( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "ret" and not arg1 and not arg2 )

    def legalHlt( self ):
        opcode = self.getOpcode()
        arg1 = self.getArg1()
        arg2 = self.getArg2()
        return ( opcode  == "hlt" and not arg1 and not arg2 )


    def legalInstruction( self ):
        # All instruction objects have four fields: 
        #   [ label, opcode, arg1, arg2 ]
        # but some of these could be None.

        # Check if the label is legal
        label = self.getLabel()
        if ( label and not isLabel( label )):
            print ("Bad instruction label: ", label)
            return            

        # Depending on the opcode, call the appropriate 
        # recognizer predicate.
        opcode = self.getOpcode()
        if ( opcode == "decl" ):
            return self.legalDecl( )
        elif ( opcode == "out"):
            return self.legalOut( )
        elif ( opcode == "in"):
            return self.legalIn( )
        elif ( opcode == "push"):
            return self.legalPush( )
        elif ( opcode == "pop"):
            return self.legalPop( )
        elif ( opcode == "top"):
            return self.legalTop( )
        elif ( opcode == "dup"):
            return self.legalDup( )
        elif ( opcode == "dec"):
            return self.legalDec( )
        elif ( opcode == "inc"):
            return self.legalInc( )
        elif ( opcode == "add"):
            return self.legalAdd( )
        elif ( opcode == "sub"):
            return self.legalSub( )
        elif ( opcode == "mul"):
            return self.legalMul( )
        elif ( opcode == "mod"):
            return self.legalMod( )
        elif ( opcode == "jmp"):
            return self.legalJmp( )
        elif ( opcode == "cmp"):
            return self.legalCmp( )
        elif ( opcode == "jeq"):
            return self.legalJeq( )
        elif ( opcode == "jne"):
            return self.legalJne( )
        elif ( opcode == "jlt"):
            return self.legalJlt( )
        elif ( opcode == "jgt"):
            return self.legalJgt( )
        elif ( opcode == "jge"):
            return self.legalJge( )
        elif ( opcode == "jle"):
            return self.legalJle( )
        elif ( opcode == "call"):
            return self.legalCall( )
        elif ( opcode == "ret"):
            return self.legalRet( )
        elif ( opcode == "hlt"):
            return self.legalHlt( )
        else:
            print ("Unrecognized operation: ", opcode)
            return False


################################################################################
#                                                                              #
#                              Low Program Objects                             #
#                                                                              #
################################################################################

# from LowInstruction import *

class LowProgram:
    """A program object is simply a list of LowInstruction objects."""

    def __init__(self, code=[]):
        """A program is just a list of LowInstruction objects, but 
        is an empty list by default."""
        self._code = code

    def getCode(self):
        return self._code

    def getCodeLen(self):
        return len( self._code )

    def findLabel(self, label):
        """Return the program counter into the code that 
        corresponds to the instruction with the given label.
        We assume that the label is not multiply defined."""
        if (not label): return -1
        pos = 0
        code = self._code
        while pos < len(code):
            if ( code[pos].getLabel() == label ):
                return pos
            pos += 1
        return -1

    def getInstruction(self, index):
        """Return the instruction object at that index."""
        if ( index < 0 or index >= len(self._code) ):
            return None
        else:
            return self._code[index]

    def printProgram( self ):
        """Here program should be a list of instruction objects.
        Print it out in nice format."""
        instNum = 0
        for instructionObject in self._code:
            print (("%2d:  " % instNum), instructionObject)
            instNum += 1
        return

    def legalProgramAux( code, labelsFound ):
        for inst in code:
            label = LowInstruction.getLabel( inst )
            if ( label in labelsFound ):
                print ("Label multiply defined: ", label)
                return False
            b = inst.legalInstruction()
            if (not b):
                print ( "Illegal instruction found: ", inst )
                return False
        return True

    def legalProgram ( self ):
        print ("Checking legality of the code")
        progOK = LowProgram.legalProgramAux( self.getCode(), [] )
        return progOK


################################################################################
#                                                                              #
#                                Low Interpreter                               #
#                                                                              #
################################################################################

from stack import *

class LowInterpreter:
    """The interpreter operates on a state that consists of:
    - a dictionary of variables and their values
    - a run-time stack for execution
    - a call stack 
    - a program counter
    - a comparison flag (which can be pos, neg, or 0)

    The program for this first version is separate from the state.
    """

    def __init__(self):
        # variables is a dictionary mapping var names to integer values
        self._variables = {}
        # The stack should contain only integer values
        self._stack = Stack()
        self._callstack = Stack()
        self._pc = 0
        self._flag = 0

    def printState(self):
        print
        print ("  variables: ", self._variables)
        print ("  stack:     ", self._stack)
        print ("  callstack: ", self._callstack)
        print ("  pc:        ", self._pc)
        print ("  flag:      ", self._flag)
        print ()
    
    def getVariables(self):
        return self._variables

    def getStack(self):
        return self._stack

    def getCallstack(self):
        return self._callstack

    def getPc(self):
        return self._pc

    def getFlag(self):
        return self._flag

    def incPc(self):
        self._pc += 1

    def getValue(self, var):
        # Should I throw an error if the var is
        # not defined?
        return self._variables[var]

    def storeValue(self, var, val):
        self._variables[var] = val
    
    def setStack(self, newstack):
        self._stack = newstack

    def setPc(self, newpc):
        self._pc = newpc

    def setFlag(self, newflag):
        self._flag = newflag


    # The following functions define the semantics of the various Low
    # operations.

    def declOp (self, var, val=0):
        self.incPc()
        self.storeValue( var, int(val) if val else 0 )

    def inOp (self, var):
        """In reads in an integer constant from the command line."""
        self.incPc()
        while True:
            inp = input("Waiting for integer input: ")
            # This allows the same inputs as isConst, which should be
            # positive and negative integers.
            if (not isConst( inp )):
                print( " Bad input; try again.")
                continue
            # make sure to coerce the input string to an integer.
            val = int(inp)
            self.storeValue(var, val)
            return

    def outOp (self, arg):
        """Out can pring either a variable value or a constant to 
        standard output."""
        self.incPc()
        if ( isVar( arg )):
            val = self.getValue(arg)
        elif ( isConst( arg )):
            # arg is an integer constant (string)
            val = int(arg)
        else:
            print ("Bad argument to OUT instruction:", arg)
        print ("Value returned: ", val)

    def pushOp (self, arg):
        """Push pushes a value onto the runtime stack.  It takes
        either a variable name or an integer constant."""
        self.incPc()
        if ( isVar( arg )):
            val = self.getValue(arg)
        elif ( isConst( arg )):
            val = int(arg)
        else:
            print ("Bad argument to PUSH instruction:", arg)
        self._stack.push(val)
        
    def popOp (self, var):
        """Pop removes the top value from the runtime stack and
        returns it."""
        if ( var ):
            val = self._stack.pop()
            self.storeValue(var, val)
        else:
            self._stack.pop()
        self.incPc()

    def topOp (self, var):
        """Top returns the top value from the runtime stack but
        does not modify it."""
        self.incPc()
        val = self._stack.peek()
        self.storeValue(var, val)

    def dupOp (self):
        """Dup duplicates the top value on the stack and pushes
        the duplicate."""
        self.incPc()
        val = self._stack.peek()
        self._stack.push(val)

    def decOp (self):
        """Dec decrements the top value on the stack."""
        self.incPc()
        val = self._stack.pop()
        self._stack.push(val - 1)

    def incOp (self):
        """Inc increments the top value on the stack."""
        self.incPc()
        val = self._stack.pop()
        self._stack.push(val + 1)

    def addOp (self):
        """Add pops two values from the stack, adds them,
        and pushes the result."""
        self.incPc()
        val1 = self._stack.pop()
        val2 = self._stack.pop()
        self._stack.push(val2 + val1)

    def subOp (self):
        """Sub pops two values from the stack, subtracts them,
        and pushes the result."""
        self.incPc()
        val1 = self._stack.pop()
        val2 = self._stack.pop()
        self._stack.push(val2 - val1)

    def mulOp (self):
        """Mul pops two values from the stack, multiplies them,
        and pushes the result."""
        self.incPc()
        val1 = self._stack.pop()
        val2 = self._stack.pop()
        self._stack.push(val2 * val1)

    def modOp (self):
        """Mod pops two values from the stack, takes top2 \% top1,
        and pushes the result."""
        self.incPc()
        modulus = self._stack.pop()
        val = self._stack.pop()
        self._stack.push(val % modulus)

    def cmpOp (self, arg):
        """Cmp sets the flag according to the comparison of the 
        arg (either a variable or constant) with the top value on
        the stack."""
        self.incPc()
        if ( isVar( arg )):
            val = self.getValue(arg)
        elif ( isConst( arg )):
            val = int( arg )
        else:
            print ("Bad argument to CMP instruction: ", arg)
        tos = self._stack.peek()
        # I think this is right.
        res = tos - val
        self.setFlag(res)

    # For the jumps, I need to have the program so that
    # I can compute the jump target.

    def jmpOp (self, labelLoc):
        """Unconditional jump to label."""
        self.setPc(labelLoc)
    
    def jeqOp (self, labelLoc):
        """Jump to label if flag is zero."""
        if ( self.getFlag() == 0 ):
            self.setPc(labelLoc)
        else: 
            self.incPc()

    def jneOp (self, labelLoc):
        """Jump to label if flag is not zero."""
        if ( self.getFlag() != 0 ):
            self.setPc( labelLoc )
        else:
            self.incPc()

    def jltOp (self, labelLoc):
        """Jump to label if flag is lt zero."""
        if ( self.getFlag() < 0 ):
            self.setPc( labelLoc )
        else:
            self.incPc()

    def jgtOp (self, labelLoc):
        """Jump to label if flag is gt zero."""
        if ( self.getFlag() > 0 ):
            self.setPc( labelLoc )
        else:
            self.incPc()
        
    def jleOp (self, labelLoc):
        """Jump to label if flag is less than or equal to zero."""
        if ( self.getFlag() <= 0 ):
            self.setPc( labelLoc )
        else:
            self.incPc()

    def jgeOp (self, labelLoc):
        """Jump to label if flag is greater than or equal to zero."""
        if ( self.getFlag() >= 0 ):
            self.setPc( labelLoc )
        else:
            self.incPc()

    def callOp (self, labelLoc ):
        """Make a call to the subroutine at label. 
        A call is just a jump to a label, but also
        pushes the return address (current pc + 1) 
        onto the call stack.  Parameter passing is
        all handled by convention, but may be in 
        variables or on the runtime stack."""
        pc = self.getPc()
        pc += 1
        self.getCallstack().push(pc)
        self.setPc( labelLoc )

    def retOp (self):
        """Ret from a subroutine.  Restore pc
        from the callstack.  Parameter and value
        passing is by convention."""
        retPc = self.getCallstack().pop()
        self.setPc( retPc )

    def hltOp (self):
        """Halt the machine execution.  The interpreter
        stops the machine if the Pc  goes negative."""
        self.setPc( -1 )



    # >> Could I have implemented this with a jump table (see pp 238ff
    # instead of this big if?

    def executeInstruction(self, inst, prog):
        """Execute an instruction, in the form of
        an instruction object. The program is needed
        is needed to compute jump targets."""
        
        opcode = inst.getOpcode()
        arg1 = inst.getArg1()
        arg2 = inst.getArg2()

        if ( opcode == "decl" ):
            self.declOp(arg1, arg2)
        elif ( opcode == "out"):
            self.outOp(arg1)
        elif ( opcode == "in"):
            self.inOp(arg1)
        elif ( opcode == "push"):
            self.pushOp(arg1)
        elif ( opcode == "pop"):
            self.popOp(arg1)
        elif ( opcode == "top"):
            self.topOp(arg1)
        elif ( opcode == "dup"):
            self.dupOp()
        elif ( opcode == "dec"):
            self.decOp()
        elif ( opcode == "inc"):
            self.incOp()
        elif ( opcode == "add"):
            self.addOp()
        elif ( opcode == "sub"):
            self.subOp()
        elif ( opcode == "mul"):
            self.mulOp()
        elif ( opcode == "mod"):
            self.modOp()
        elif ( opcode == "jmp"):
            self.jmpOp(prog.findLabel(arg1))
        elif ( opcode == "cmp"):
            self.cmpOp(arg1)
        elif ( opcode == "jeq"):
            self.jeqOp(prog.findLabel(arg1))
        elif ( opcode == "jne"):
            self.jneOp(prog.findLabel(arg1))
        elif ( opcode == "jlt"):
            self.jltOp(prog.findLabel(arg1))
        elif ( opcode == "jgt"):
            self.jgtOp(prog.findLabel(arg1))
        elif ( opcode == "jge"):
            self.jgeOp(prog.findLabel(arg1))
        elif ( opcode == "call"):
            self.callOp(prog.findLabel(arg1))
        elif ( opcode == "ret"):
            self.retOp()
        elif ( opcode == "hlt"):
            self.hltOp()
        else:
            print ("Unrecognized operation: ", opcode)
            self.hltOp()


    def runI (self, clk, prog, label=None):
        """Run a program to completion, or for clk number of steps.  
        The label parameter tells where to begin execution, and defaults to 0."""
        print ("Initial state:")
        self.printState()
        # If a label is given, it tells where to
        # begin execution. 
        if label:
            labelLoc = prog.findLabel( label )
            if ( labelLoc == -1 ):
                print ("Start label ", label, " not found")
            self._pc = labelLoc
        else:
            self._pc = 0
        # stepCnt is used to label the steps in order.
        stepCnt = 1
        # Terminates when we time out or run off the 
        # end of the list
        while True:
            if ( clk <= 0 ):
                print ("Terminating: timed out")
                self.printState()
                return
            cl = prog.getCodeLen()
            pc = self._pc
            # If the pc ever gets outside the program,
            # break.  This will handle if we fall off the 
            # end of a straightline program.
            if ( pc < 0 or pc >= cl ):
                break
            inst = prog.getInstruction( pc )
            print (("Step %3d: %s" % (stepCnt, inst)))
            self.executeInstruction ( inst, prog )
            self.printState()
            clk -= 1
            stepCnt += 1
        # When execution terminates, print out the final
        # state.
        print( "Program terminated with the following values:")
        self.printState()


################################################################################
#                                                                              #
#                                   Test Code                                  #
#                                                                              #
################################################################################


def TestFileInput():
    # These create a list of lines (strings) from the file.
    fileName = "inputFile5.txt"
    print ("Reading instructions from ", fileName)
    assemblerFile = open(fileName, 'r')
    lines = assemblerFile.readlines()

    # parse and print the program
    instList = LowInstruction.parseLowInstructionList( lines )
    program = LowProgram(instList)

    # Check if program is legal
    if not program.legalProgram():
        program.printProgram()
        # Now execute the program
        state = LowInterpreter()
        state.runI(50, program, "main")

# Run the test program

TestFileInput()


