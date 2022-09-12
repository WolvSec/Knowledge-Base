CC=gcc
CFLAGS=-I.

buffer_overflow: buffer_overflow.c
	$(CC) -o buffer_overflow buffer_overflow.c -fno-stack-protector -no-pie -Wno-stringop-overflow

clean:
	$(RM) buffer_overflow
