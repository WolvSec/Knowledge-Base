CC=gcc
CFLAGS=-I. -fno-stack-protector -no-pie -Wno-stringop-overflow -Wno-nonnull -static

# Statically linked to give more gadgets
buffer_overflow: rop.c
	$(CC) $(CFLAGS) -o rop rop.c

clean:
	$(RM) rop
