antlr4=java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool

generate: c2llvm.g4
	$(antlr4) -Dlanguage=Python3 c2llvm.g4 -visitor

tarball: 
	git archive --format=tar.gz -o c2llvm.tar.gz HEAD
