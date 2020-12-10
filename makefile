antlr4=java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool

generate: c2llvm.g4
	$(antlr4) -Dlanguage=Python3 c2llvm.g4 -visitor

sync: c2llvmVisitor.py visitor.py
	./sync.sh visitor.py c2llvmVisitor.py
