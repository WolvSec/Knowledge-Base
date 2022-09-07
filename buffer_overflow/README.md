# Buffer Overflow

### Overview

One of the simplest "pwn" attacks is a buffer overflow. The idea is that a faulty program has allocated a buffer of a certain size, but allows you to write more than that size.

For example, `input_buffer` is only 16 bytes, but `gets` allows you to input as many characters as you want. So at some point you are writing over memory you are not supposed to, and we can use this to our advantage!

### The Stack

For many this may be the first time learning about the stack. Here is a diagram:

![Stack Diagram](https://eli.thegreenplace.net/images/2011/08/x64_frame_nonleaf.png)

Note that this is from: https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64, you should check it out for a primer! But don't worry if some details go over your head.
