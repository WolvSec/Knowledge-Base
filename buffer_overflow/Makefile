CC=gcc
CFLAGS=-I. -fno-stack-protector -no-pie -Wno-stringop-overflow -Wno-nonnull

# Turns out modern compilers have a lot of default settings to prevent vulnerable code
# -fno-stack-protector: Disable stack canary: https://ctf101.org/binary-exploitation/stack-canaries/
# -no-pie: Disables ASLR essentially, loads executable to the same address every time
# -Wno-stringop-overflow: Disable complaining about fgets overflow
buffer_overflow: buffer_overflow.c
	$(CC) $(CFLAGS) -o buffer_overflow buffer_overflow.c

clean:
	$(RM) buffer_overflow
