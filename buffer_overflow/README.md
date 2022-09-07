# Buffer Overflow

### Overview

One of the simplest "pwn" attacks is a buffer overflow. The idea is that a faulty program has allocated a buffer of a certain size, but allows you to write more than that size.

For example, `input_buffer` is only 16 bytes, but `gets` allows you to input as many characters as you want. So at some point you are writing over memory you are not supposed to, and we can use this to our advantage!

### The Stack

For many this may be the first time learning about the stack. Let's throw you right in, here is a diagram:

![Stack Diagram](https://eli.thegreenplace.net/images/2011/08/x64_frame_nonleaf.png)

Credit: https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64 (also a good read)

Okay wait up. There are others who can explain the stack way better than I, check out this video for a good explanation: https://youtu.be/jVzSBkbfdiw

Philosophical sidetrack - It is okay if things are confusing at this point, that is a lot of security. Just let it settle in and come back to it a little bit every day.

Let's extract out what is important. This is what is stored on a stack frame:

- Local variables
- Saved stack base from previous frame
- Return address

Local variables means that `input_buffer` is in the stack frame. Good to know, we also know that we can write past that due to the previous discussion about `gets`.

The return address is also on the stack. What does that mean? Well a function has to know where it was called from in order to return there. If I call `puts` from `main`, the computer needs to know that I need to resume execution in `main` after I finish `puts`. So it places the return address on the stack.

Right now a bell should be going off, look at the diagram again. The stack grows downwards (remember), so we can write past our buffer and overwrite the return address! We can tell the computer where to go next. This is the basic idea of a buffer overflow.

Notice how we attacked. We enumerated every resource that we controlled and figured out how they all interacted with the system. Keep this idea in mind.
