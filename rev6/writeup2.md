Credit: youtiaos

mini writeup for TEJ5M

considering that we have an unknown input which goes through 20 functions, and we are given the answer at the end of the 20 functions
we want to find the input that gives the answer after 20 functions. 

we can trivially solve this with angr by finding every intermediate solution to a single function starting from the last function right before the answer is checked and propagate upwards

*trying to angr 20 unconstrained functions at once will just lead to path explosion lol*

```py
# coding: utf-8
from pwn import p64, u64, log, context
import angr
import logging 

p = angr.Project("./isp")

# final answer
objective = 0x4ce876fceb
context.log_level = "error"
num_solved = 0
path = []

# plan: start from our final answer and climb up every function call
#       to find each intermediate answer between the final answer and our
#       input
#
# sample angr run path
"""
    START ----> mov rax, 001111100111100000001111000100011110100b
          ----> call f
    HOOK  ----> mov rax, 001111100111100000001111000100011110100b
    END   ----> call g
"""

while True:
    log.success(f"Equation {num_solved}")
    start_addr = 0x401122 - 0xf*num_solved
    state = p.factory.blank_state(addr=start_addr)

    # set num to a symbolic value
    x = state.solver.BVS('unk', 64)
    state.memory.store(0x402084, x)

    # hook an instruction to add our objective as a constraint on num after the function call
    hook_addr = 0x401122-0xf*num_solved+15
    p.hook(0x401122-0xf*num_solved+15, lambda x: x.add_constraints(x.regs.rax == objective))

    mgr = p.factory.simgr(state)
    if num_solved == 0:
        explore_addr = 0x401122-0xf*num_solved+23
    else:
        explore_addr = 0x401122-0xf*num_solved+25

    log.info(f"Explore from {hex(start_addr)} until @ {hex(explore_addr)}")
    log.info(f"Hook @ {hex(hook_addr)}")

    # explore until right before the next function call
    mgr.explore(find=explore_addr)
    if not mgr.found:
        log.warning("no answer!")
        objective = answers.pop()
        continue

    # if we have multiple answers, we want to keep it in case a previous answer
    # fails to work
    answers = [u64(p64(x)[::-1]) for x in mgr.found[0].solver.eval_upto(x, 10)]
    path.append(hex(objective))
    objective = answers.pop()

    assert (objective < int("1"*39, 2))
    log.info(f"Found intermediate answer at {hex(objective)}")
    num_solved += 1
    if num_solved == 20:
        log.success("SOLVED!")
        answers.append(objective)
        log.info("Answers: ")
        for answer in answers:
            log.info(bin(answer)[2:].zfill(39))
        break
```
