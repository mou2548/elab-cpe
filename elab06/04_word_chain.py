def reset():
    global chain_count, longest_chain, streak
    longest_chain = max(streak, longest_chain)
    streak = 1
    chain_count += 1
    return

text = input("Text: ").split()
chain_count = 1
longest_chain = 1
streak = 1
    
for i in range(len(text) - 1):
    diff = 0
    if len(text[i]) != len(text[i+1]):
        reset()
        continue

    for c in range(len(text[i])):
        if text[i][c] != text[i+1][c]:
            diff += 1
    if diff > 2:
        reset()
        continue
    streak += 1

longest_chain = max(streak, longest_chain)
print(f"{chain_count} Chain(s). Maximum length is {longest_chain} word(s).")
            
        