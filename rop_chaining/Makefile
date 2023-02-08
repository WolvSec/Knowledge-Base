CC=gcc
CFLAGS=-I. -no-pie -Wno-stringop-overflow -Wno-nonnull -fno-stack-protector

rop_chaining: rop_chaining.c
	$(CC) $(CFLAGS) -o rop_chaining rop_chaining.c

clean:
	$(RM) rop_chaining
