class LLVMGenerator():

	header_text = ""
	main_text = ""
	buffer = ""
	main_reg = 1
	reg = 1
	br = 0

	brstack = list()
	
	def print(id):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = load i32, i32* %"+id+"\n"
		LLVMGenerator.reg += 1
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %"+str(LLVMGenerator.reg-1)+")\n"
		LLVMGenerator.reg += 1

	def read_int(id):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %"+id+")\n"
		LLVMGenerator.reg += 1

	def read_real(id):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = call double (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %"+id+")\n"
		LLVMGenerator.reg += 1

	def functionstart(id):
		LLVMGenerator.main_text += LLVMGenerator.buffer;
		LLVMGenerator.main_reg = LLVMGenerator.reg;
		LLVMGenerator.buffer = "define i32 @"+id+"() nounwind {\n";
		LLVMGenerator.reg = 1;

	def functionend():
		LLVMGenerator.buffer += "ret i32 %"+str(LLVMGenerator.reg-1)+"\n"; 
		LLVMGenerator.buffer += "}\n";
		LLVMGenerator.header_text += LLVMGenerator.buffer;
		LLVMGenerator.buffer = "";
		LLVMGenerator.reg = LLVMGenerator.main_reg;

	def call(id):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = call i32 @"+id+"()\n";
		LLVMGenerator.reg += 1;
		return LLVMGenerator.reg-1;

	def declare_int(id):
		LLVMGenerator.buffer += "%"+id+" = alloca i32\n"

	def declare_real(id):
		LLVMGenerator.buffer += "%"+id+" = alloca double\n";

	def assign_int(id, value):
		LLVMGenerator.buffer += "store i32 "+str(value)+", i32* %"+str(id)+"\n"

	def assign_real(id, value):
		LLVMGenerator.buffer += "store double "+str(value)+", double* %"+str(id)+"\n"

	def sitofp(id):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = sitofp i32 "+id+" to double\n";
		LLVMGenerator.reg += 1;

	def fptosi(id):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = fptosi double "+id+" to i32\n";
		LLVMGenerator.reg += 1;

	def loadint(id):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = load i32, i32* %"+id+"\n"
		LLVMGenerator.reg += 1

	def loadreal(id):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = load double, double* %"+id+"\n"
		LLVMGenerator.reg += 1

	def addint_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = add i32 "+str(LLVMGenerator.reg-2)+", "+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def addint_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = add i32 %"+str(LLVMGenerator.reg-1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1
	def addint_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = add i32 "+str(val1)+", %"+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def addint_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = add i32 "+str(val1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1

	def addreal_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = add double "+str(LLVMGenerator.reg-2)+", "+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def addreal_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = add double %"+str(LLVMGenerator.reg-1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1
	def addreal_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = add double "+str(val1)+", %"+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def addreal_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = add double "+str(val1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1

	def subint_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = sub i32 "+str(LLVMGenerator.reg-2)+", "+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def subint_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = sub i32 %"+str(LLVMGenerator.reg-1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1
	def subint_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = sub i32 "+str(val1)+", %"+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def subint_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = sub i32 "+str(val1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1

	def subreal_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = sub double "+str(LLVMGenerator.reg-2)+", "+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def subreal_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = sub double %"+str(LLVMGenerator.reg-1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1
	def subreal_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = sub double "+str(val1)+", %"+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def subreal_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = sub double "+str(val1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1

	def mulint_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = mul i32 "+str(LLVMGenerator.reg-2)+", "+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def mulint_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = mul i32 %"+str(LLVMGenerator.reg-1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1
	def mulint_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = mul i32 "+str(val1)+", %"+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def mulint_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = mul i32 "+str(val1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1

	def mulreal_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = mul double "+str(LLVMGenerator.reg-2)+", "+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def mulreal_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = mul double %"+str(LLVMGenerator.reg-1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1
	def mulreal_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = mul double "+str(val1)+", %"+str(LLVMGenerator.reg-1)+"\n"
		LLVMGenerator.reg += 1
	def mulreal_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = mul double "+str(val1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1

	def divint(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = div i32 "+str(val1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1

	def divreal(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = div double "+str(val1)+", "+str(val2)+"\n"
		LLVMGenerator.reg += 1

	def icmpint_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp eq i32 %"+str(LLVMGenerator.reg-1)+", %"+str(LLVMGenerator.reg-2)+"\n";
		LLVMGenerator.reg += 1
	def icmpint_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp eq i32 %"+str(LLVMGenerator.reg-1)+", "+val2+"\n";
		LLVMGenerator.reg += 1
	def icmpint_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp eq i32 "+val1+", %"+str(LLVMGenerator.reg-1)+"\n";
		LLVMGenerator.reg += 1
	def icmpint_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp eq i32 "+val1+", "+val2+"\n";
		LLVMGenerator.reg += 1

	def icmpreal_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp eq double %"+str(LLVMGenerator.reg-1)+", %"+str(LLVMGenerator.reg-2)+"\n";
		LLVMGenerator.reg += 1
	def icmpreal_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp eq double %"+str(LLVMGenerator.reg-1)+", "+val2+"\n";
		LLVMGenerator.reg += 1
	def icmpreal_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp eq double "+val1+", %"+str(LLVMGenerator.reg-1)+"\n";
		LLVMGenerator.reg += 1
	def icmpreal_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp eq double "+val1+", "+val2+"\n";
		LLVMGenerator.reg += 1

	def icmp_ne_int_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp ne i32 %"+str(LLVMGenerator.reg-1)+", %"+str(LLVMGenerator.reg-2)+"\n";
		LLVMGenerator.reg += 1
	def icmp_ne_int_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp ne i32 %"+str(LLVMGenerator.reg-1)+", "+val2+"\n";
		LLVMGenerator.reg += 1
	def icmp_ne_int_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp ne i32 "+val1+", %"+str(LLVMGenerator.reg-1)+"\n";
		LLVMGenerator.reg += 1
	def icmp_ne_int_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp ne i32 "+val1+", "+val2+"\n";
		LLVMGenerator.reg += 1

	def icmp_ne_real_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp ne double %"+str(LLVMGenerator.reg-1)+", %"+str(LLVMGenerator.reg-2)+"\n";
		LLVMGenerator.reg += 1
	def icmp_ne_real_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp ne double %"+str(LLVMGenerator.reg-1)+", "+val2+"\n";
		LLVMGenerator.reg += 1
	def icmp_ne_real_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp ne double "+val1+", %"+str(LLVMGenerator.reg-1)+"\n";
		LLVMGenerator.reg += 1
	def icmp_ne_real_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp ne double "+val1+", "+val2+"\n";
		LLVMGenerator.reg += 1

	def icmp_sgt_int_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp sgt i32 %"+str(LLVMGenerator.reg-1)+", %"+str(LLVMGenerator.reg-2)+"\n";
		LLVMGenerator.reg += 1
	def icmp_sgt_int_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp sgt i32 %"+str(LLVMGenerator.reg-1)+", "+val2+"\n";
		LLVMGenerator.reg += 1
	def icmp_sgt_int_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp sgt i32 "+val1+", %"+str(LLVMGenerator.reg-1)+"\n";
		LLVMGenerator.reg += 1
	def icmp_sgt_int_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp sgt i32 "+val1+", "+val2+"\n";
		LLVMGenerator.reg += 1

	def icmp_sgt_real_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp sgt double %"+str(LLVMGenerator.reg-1)+", %"+str(LLVMGenerator.reg-2)+"\n";
		LLVMGenerator.reg += 1
	def icmp_sgt_real_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp sgt double %"+str(LLVMGenerator.reg-1)+", "+val2+"\n";
		LLVMGenerator.reg += 1
	def icmp_sgt_real_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp sgt double "+val1+", %"+str(LLVMGenerator.reg-1)+"\n";
		LLVMGenerator.reg += 1
	def icmp_sgt_real_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp sgt double "+val1+", "+val2+"\n";
		LLVMGenerator.reg += 1

	def icmp_slt_int_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp slt i32 %"+str(LLVMGenerator.reg-1)+", %"+str(LLVMGenerator.reg-2)+"\n";
		LLVMGenerator.reg += 1
	def icmp_slt_int_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp slt i32 %"+str(LLVMGenerator.reg-1)+", "+val2+"\n";
		LLVMGenerator.reg += 1
	def icmp_slt_int_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp slt i32 "+val1+", %"+str(LLVMGenerator.reg-1)+"\n";
		LLVMGenerator.reg += 1
	def icmp_slt_int_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp slt i32 "+val1+", "+val2+"\n";
		LLVMGenerator.reg += 1

	def icmp_slt_real_11(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp slt double %"+str(LLVMGenerator.reg-1)+", %"+str(LLVMGenerator.reg-2)+"\n";
		LLVMGenerator.reg += 1
	def icmp_slt_real_10(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp slt double %"+str(LLVMGenerator.reg-1)+", "+val2+"\n";
		LLVMGenerator.reg += 1
	def icmp_slt_real_01(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp slt double "+val1+", %"+str(LLVMGenerator.reg-1)+"\n";
		LLVMGenerator.reg += 1
	def icmp_slt_real_00(val1, val2):
		LLVMGenerator.buffer += "%"+str(LLVMGenerator.reg)+" = icmp slt double "+val1+", "+val2+"\n";
		LLVMGenerator.reg += 1

	def blockwhilestart():
		LLVMGenerator.br += 1
		LLVMGenerator.buffer += "br label %header"+str(LLVMGenerator.br)+" \n"
		LLVMGenerator.buffer += "header"+str(LLVMGenerator.br)+": \n";
		LLVMGenerator.buffer += "br i"+str(LLVMGenerator.br)+" %"+str(LLVMGenerator.reg-1)+", label %true"+str(LLVMGenerator.br)+", label %false"+str(LLVMGenerator.br)+"\n";
		LLVMGenerator.buffer += "true"+str(LLVMGenerator.br)+":\n";
		LLVMGenerator.brstack.append(LLVMGenerator.br);

	def blockwhileend():
		b = LLVMGenerator.brstack.pop();
		LLVMGenerator.buffer += "br label %header"+str(b)+"\n";
		LLVMGenerator.buffer += "false"+str(b)+":\n";

	def blockifstart():
		LLVMGenerator.br += 1
		LLVMGenerator.buffer += "br i"+str(LLVMGenerator.br)+" %"+str(LLVMGenerator.reg-1)+", label %true"+str(LLVMGenerator.br)+", label %false"+str(LLVMGenerator.br)+"\n";
		LLVMGenerator.buffer += "true"+str(LLVMGenerator.br)+":\n";
		LLVMGenerator.brstack.append(LLVMGenerator.br);

	def blockifend():
		b = LLVMGenerator.brstack.pop();
		LLVMGenerator.buffer += "br label %end"+str(b)+"\n";
		LLVMGenerator.buffer += "false"+str(b)+":\n";
		LLVMGenerator.brstack.append(b);

	def ifend():
		b = LLVMGenerator.brstack.pop();
		LLVMGenerator.buffer += "br label %end"+str(b)+"\n";
		LLVMGenerator.buffer += "end"+str(b)+":\n";

	def generate():
		LLVMGenerator.main_text += LLVMGenerator.buffer
		text = ""
		#text += "declare i32 @printf(i8*, ...)\n"
		#text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
		#text += "@strp = constant [4 x i8] c\"%d\\0A\\00\"\n"
		#text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
		text += LLVMGenerator.header_text
		text += "define i32 @main() nounwind{\n";
		text += LLVMGenerator.main_text
		text += "ret i32 0 }\n"
		return text