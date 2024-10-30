from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

import sys
from LLVMGenerator import LLVMGenerator

functions = set()
variables = set()
local_variables = set()
stack = list()

function = ""
line = 1
global_flag = [True]

class VarType:
	ID = "ID"
	INT = "INT"
	REAL = "REAL"

class Value:
	def __init__(self, value, type, isId):
		self.value = value
		self.type = type
		self.isId = isId

# This class defines a complete listener for a parse tree produced by ExprParser.
class LLVMActions(ParseTreeListener):

	#def enterEveryRule(self, ctx:ExprParser.ProgContext):
	def enterEveryRule(self, ctx):
		pass

#Prog
	def enterProg(self, ctx:ExprParser.ProgContext):
		pass

	def exitProg(self, ctx:ExprParser.ProgContext):
		print(LLVMGenerator.generate())

#Block
	def enterBlock(self, ctx:ExprParser.BlockContext):
		pass

	def exitBlock(self, ctx:ExprParser.BlockContext):
		pass

#Stat
	def enterStat(self, ctx:ExprParser.StatContext):
		pass

	def exitStat(self, ctx:ExprParser.StatContext):
		pass

#Print
	def enterPrint(self, ctx:ExprParser.PrintContext):
		pass

	def exitPrint(self, ctx:ExprParser.PrintContext):
		print(ctx.expr().getText())
		ID = ctx.expr().getText()
		if(not(ID in variables)):
			LLVMGenerator.print(ID)
		else:
			print("line "+str(line)+", no variable found to print")
			sys.exit();

#Read
	def enterRead(self, ctx:ExprParser.ReadContext):
		pass

	def exitRead(self, ctx:ExprParser.ReadContext):
		ID = ctx.ID().getText()
		type = ctx.TYPE().getText()
		for i in variables:
			if(i.name == ID):
				ID = i
		if(not(ID in variables)):
			if(type == "int"):
				variables.add(Variable(ID, 0, "INT"))
				LLVMGenerator.declare_int(ID)
				LLVMGenerator.read_int(ID)
			else:
				variables.add(Variable(ID, 0, "REAL"))
				LLVMGenerator.declare_real(ID)
				LLVMGenerator.read_real(ID)
		else:
			if(type == "int"):
				LLVMGenerator.read_int(ID)
			else:
				LLVMGenerator.read_real(ID)

#Func
	def enterFunc(self, ctx:ExprParser.FuncContext):
		pass

	def exitFunc(self, ctx:ExprParser.FuncContext):
		type = ctx.TYPE().getText();
		if(type == "int"):
		#	LLVMGenerator.loadint(function);
			functions.add(Value(ctx.namefunc().getText(),VarType.INT, 0))
		else:
		#	LLVMGenerator.loadreal(function);
			functions.add(Value(ctx.namefunc().getText(),VarType.REAL, 0))
		LLVMGenerator.functionend();
		global local_variables
		local_variables = set()
		global_flag[0] = True

#Namefunc
	def enterNamefunc(self, ctx:ExprParser.NamefuncContext):
		pass

	def exitNamefunc(self, ctx:ExprParser.NamefuncContext):
		ID = ctx.ID().getText();
		functions.add(ID); 
		function = ID;
		LLVMGenerator.functionstart(ID);
		global_flag[0] = False

#Paramsfunc
	def enterParamsfunc(self, ctx:ExprParser.ParamsfuncContext):
		pass

	def exitParamsfunc(self, ctx:ExprParser.ParamsfuncContext):
		pass

#Paramfunc
	def enterParamfunc(self, ctx:ExprParser.ParamfuncContext):
		pass

	def exitParamfunc(self, ctx:ExprParser.ParamfuncContext):
		for i in variables:
			if(i.value == ctx.value().getText()):
				local_variables.add(i)
				if(i.type == "INT"):
					LLVMGenerator.declare_int(i.value)
					LLVMGenerator.loadint(i.value)
				elif(i.type == "REAL"):
					LLVMGenerator.declare_real(i.value)
					LLVMGenerator.loadreal(i.value)
				break;

#Callfunc
	def enterCallfunc(self, ctx:ExprParser.CallfuncContext):
		pass

	def exitCallfunc(self, ctx:ExprParser.CallfuncContext):
		reg = LLVMGenerator.call(ctx.ID().getText());
		if(not(stack == set())):
			stack.append(Value(reg, VarType.INT, 1))

#Blockfunc
	def enterBlockfunc(self, ctx:ExprParser.BlockfuncContext):
		pass

	def exitBlockfunc(self, ctx:ExprParser.BlockfuncContext):
		pass

#Blockwhile
	def enterBlockwhile(self, ctx:ExprParser.BlockwhileContext):
		LLVMGenerator.blockwhilestart()

	def exitBlockwhile(self, ctx:ExprParser.BlockwhileContext):
		LLVMGenerator.blockwhileend()

#Blockif
	def enterBlockif(self, ctx:ExprParser.BlockifContext):
		LLVMGenerator.blockifstart()

	def exitBlockif(self, ctx:ExprParser.BlockifContext):
		LLVMGenerator.blockifend()

#If
	def enterIf(self, ctx:ExprParser.IfContext):
		pass

	def exitIf(self, ctx:ExprParser.IfContext):
		LLVMGenerator.ifend()

#Cond
	def enterCond(self, ctx:ExprParser.CondContext):
		pass

	def exitCond(self, ctx:ExprParser.CondContext):
		v1 = stack.pop()
		v2 = stack.pop()
		if(global_flag[0] == True):
			set = variables
		else:
			set = local_variables
		if(v1.isId == 1):
			for i in set:
				if(i.value == v1.value):
					v1 = i
					if(v1.type == "INT"):
						LLVMGenerator.loadint(v1.value)
					elif(v1.type == "REAL"):
						LLVMGenerator.loadreal(v1.value)
		if(v2.isId == 1):
			for i in set:
				if(i.value == v2.value):
					v2 = i
					if(v2.type == "INT"):
						LLVMGenerator.loadint(v2.value)
					elif(v2.type == "REAL"):
						LLVMGenerator.loadreal(v2.value)
		if(v1.type == v2.type):
			cond = ctx.COND_OP().getText()
			if('==' == cond):
				if(v1.type == "INT"):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.icmpint_11(v1.value, v2.value);
						else:
							LLVMGenerator.icmpint_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.icmpint_01(v1.value, v2.value);
						else:
							LLVMGenerator.icmpint_00(v1.value, v2.value);
				elif(v1.type == "REAL"):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.icmpreal_11(v1.value, v2.value);
						else:
							LLVMGenerator.icmpreal_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.icmpreal_01(v1.value, v2.value);
						else:
							LLVMGenerator.icmpreal_00(v1.value, v2.value);
			elif('!=' == cond):
				if(v1.type == "INT"):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.icmp_ne_int_11(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_ne_int_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.icmp_ne_int_01(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_ne_int_00(v1.value, v2.value);
				elif(v1.type == "REAL"):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.icmp_ne_real_11(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_ne_real_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.icmp_ne_real_01(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_ne_real_00(v1.value, v2.value);
			elif('>' == cond):
				if(v1.type == "INT"):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.icmp_sgt_int_11(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_sgt_int_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.icmp_sgt_int_01(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_sgt_int_00(v1.value, v2.value);
				elif(v1.type == "REAL"):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.icmp_sgt_real_11(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_sgt_real_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.icmp_sgt_real_01(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_sgt_real_00(v1.value, v2.value);
			elif('<' == cond):
				if(v1.type == "INT"):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.icmp_slyt_int_11(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_slt_int_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.icmp_slt_int_01(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_slt_int_00(v1.value, v2.value);
				elif(v1.type == "REAL"):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.icmp_slt_real_11(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_slt_real_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.icmp_slt_real_01(v1.value, v2.value);
						else:
							LLVMGenerator.icmp_slt_real_00(v1.value, v2.value);
		else:
			print("line "+str(line)+", condition arguments type mismatch")
			sys.exit()	
				
#Assign
	def enterAssign(self, ctx:ExprParser.AssignContext):
		pass

	def exitAssign(self, ctx:ExprParser.AssignContext):
		ID = ctx.ID().getText(); # ID name in assign fe. x
		var1_exists = 0
		var2_exists = 0
		if(global_flag[0] == True):
			set = variables
		else:
			set = local_variables
		for i in set:
			if(i.value == ID):
				ID = i
				var1_exists = 1
				break;
		v = stack.pop()
		if(v.type == "ID"):
			for i in set:
				if(i.value == v.value):
					v = i
					var2_exists = 1
					break;
		else:
			var2_exists = 1
		if(var2_exists == 0):
			print("line "+str(line)+", missing variable")
			sys.exit()
		if(var1_exists == 0):
			set.add(Value(ID, v.type, 1));
			if(v.type == "INT"):
				LLVMGenerator.declare_int(ID);
				LLVMGenerator.assign_int(ID, v.value);
			elif(v.type == "REAL"):
				LLVMGenerator.declare_real(ID);
				LLVMGenerator.assign_real(ID, v.value);
		else:
			if(v.type == ID.type):
				if(v.type == "INT"):
					LLVMGenerator.assign_int(ID.value, v.value);
				if(v.type == "REAL"):
					LLVMGenerator.assign_real(ID.value, v.value);
			else:
				print("line "+str(line)+", = type mismatch")
				sys.exit()

#Expr
	def enterExpr(self, ctx:ExprParser.ExprContext):
		pass

	def exitExpr(self, ctx:ExprParser.ExprContext):
		pass

#Expr_follow
	def enterExpr_follow(self, ctx:ExprParser.Expr_followContext):
		pass

	def exitExpr_follow(self, ctx:ExprParser.Expr_followContext):
		pass

#Muldiv
	def enterMuldiv(self, ctx:ExprParser.MuldivContext):
		pass

	def exitMuldiv(self, ctx:ExprParser.MuldivContext):
		v1 = stack.pop()
		v2 = stack.pop()
		if(global_flag[0] == True):
			set = variables
		else:
			set = local_variables
		if(v1.isId == 1):
			for i in set:
				if(i.value == v1.value):
					v1 = i
					if(v2.type == "INT"):
						LLVMGenerator.loadint(v2.value)
					elif(v2.type == "REAL"):
						LLVMGenerator.loadreal(v2.value)
		if(v2.isId == 1):
			for i in set:
				if(i.value == v2.value):
					v2 = i
					if(v2.type == "INT"):
						LLVMGenerator.loadint(v2.value)
					elif(v2.type == "REAL"):
						LLVMGenerator.loadreal(v2.value)
		if(v1.type == v2.type):
			if(v1.type == "INT"):
				symbol = ctx.MULDIVSIGN().getText()
				if(symbol == '*'):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.mulint_11(v1.value, v2.value);
						else:
							LLVMGenerator.mulint_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.mulint_01(v1.value, v2.value);
						else:
							LLVMGenerator.mulint_00(v1.value, v2.value);
				stack.append(Value("%"+str(LLVMGenerator.reg-1), VarType.INT, 0)); 
			if(v1.type == "REAL"):
				symbol = ctx.MULDIVSIGN().getText()
				if(symbol == '*'):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.mulreal_11(v1.value, v2.value);
						else:
							LLVMGenerator.mulreal_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.mulreal_01(v1.value, v2.value);
						else:
							LLVMGenerator.mulreal_00(v1.value, v2.value);
				stack.append(Value("%"+str(LLVMGenerator.reg-1), VarType.REAL, 0)); 
		else:
			print("line "+str(line)+", "+ctx.MULDIVSIGN().getText()+" type mismatch")
			sys.exit()

#Addsub
	def enterAddsub(self, ctx:ExprParser.AddsubContext):
		pass

	def exitAddsub(self, ctx:ExprParser.AddsubContext):
		v1 = stack.pop()
		v2 = stack.pop()
		if(global_flag[0] == True):
			set = variables
		else:
			set = local_variables
		if(v1.isId == 1):
			for i in set:
				if(i.value == v1.value):
					v1 = i
					if(v2.type == "INT"):
						LLVMGenerator.loadint(v2.value)
					elif(v2.type == "REAL"):
						LLVMGenerator.loadreal(v2.value)
		if(v2.isId == 1):
			for i in set:
				if(i.value == v2.value):
					v2 = i
					if(v2.type == "INT"):
						LLVMGenerator.loadint(v2.value)
					elif(v2.type == "REAL"):
						LLVMGenerator.loadreal(v2.value)
		if(v1.type == v2.type):
			if(v1.type == "INT"):
				symbol = ctx.ADDSUBSIGN().getText()
				if(symbol == '+'):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.addint_11(v1.value, v2.value);
						else:
							LLVMGenerator.addint_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.addint_01(v1.value, v2.value);
						else:
							LLVMGenerator.addint_00(v1.value, v2.value);
				else:
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.subint_11(v1.value, v2.value);
						else:
							LLVMGenerator.subint_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.subint_01(v1.value, v2.value);
						else:
							LLVMGenerator.subint_00(v1.value, v2.value);
				stack.append(Value("%"+str(LLVMGenerator.reg-1), VarType.INT, 0));
			if(v1.type == "REAL"):
				symbol = ctx.ADDSUBSIGN().getText()
				if(symbol == '+'):
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.addreal_11(v1.value, v2.value);
						else:
							LLVMGenerator.addreal_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.addreal_01(v1.value, v2.value);
						else:
							LLVMGenerator.addreal_00(v1.value, v2.value);
				else:
					if(v1.isId == 1):
						if(v2.isId == 1):
							LLVMGenerator.subreal_11(v1.value, v2.value);
						else:
							LLVMGenerator.subreal_10(v1.value, v2.value);
					else:
						if(v2.isId == 1):
							LLVMGenerator.subreal_01(v1.value, v2.value);
						else:
							LLVMGenerator.subreal_00(v1.value, v2.value);
				stack.append(Value("%"+str(LLVMGenerator.reg-1), VarType.REAL, 0));
		else:
			print("line "+str(line)+", "+ctx.ADDSUBSIGN().getText()+" type mismatch")
			sys.exit()

#Id
	def enterId(self, ctx:ExprParser.IdContext):
		pass

	def exitId(self, ctx:ExprParser.IdContext):
		if(not(stack == set())):
			stack.append(Value(ctx.ID().getText(), VarType.ID, 1))

#Int
	def enterInt(self, ctx:ExprParser.IntContext):
		pass

	def exitInt(self, ctx:ExprParser.IntContext):
		stack.append(Value(ctx.INT().getText(), VarType.INT, 0))

#Real
	def enterReal(self, ctx:ExprParser.RealContext):
		pass

	def exitReal(self, ctx:ExprParser.RealContext):
		stack.append(Value(ctx.REAL().getText(), VarType.REAL, 0) );

#ToInt
	def enterToint(self, ctx:ExprParser.TointContext):
		pass

	def exitToint(self, ctx:ExprParser.TointContext):
		v = stack.pop();
		if(global_flag[0] == True):
			set = variables
		else:
			set = local_variables
		if(v.type == "ID"):
			for i in set:
				if(i.value == v.value):
					v = i
		LLVMGenerator.fptosi(v.value);
		stack.append(Value("%"+str(LLVMGenerator.reg-1), VarType.INT, 0))

#ToReal
	def enterToreal(self, ctx:ExprParser.TorealContext):
		pass

	def exitToreal(self, ctx:ExprParser.TorealContext):
		v = stack.pop();
		if(global_flag[0] == True):
			set = variables
		else:
			set = local_variables
		if(v.type == "ID"):
			for i in set:
				if(i.value == v.value):
					v = i
		LLVMGenerator.sitofp(v.value);
		stack.append(Value("%"+str(LLVMGenerator.reg-1), VarType.REAL, 0)); 
"""
#Value
	def enterValue(self, ctx:ExprParser.ValueContext):
		pass

	def exitValue(self, ctx:ExprParser.ValueContext):
		if(ctx.ID() != None):
			ID = ctx.ID().getText();
			if(not(ID in variables)):
				LLVMGenerator.load(ID);
				stack.append("%"+(LLVMGenerator.reg-1)); 
			else:
				error(ctx.getStart().getLine(), "unknown variable "+ID);
		if(ctx.INT() != None):
			stack.append(ctx.INT().getText())
"""

del ExprParser