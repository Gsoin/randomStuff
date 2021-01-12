from difflib import SequenceMatcher
text1 = "programming is like programs for programmers"
text2 = "program lik i am really programme"
m = SequenceMatcher(None, text1, text2)
print(m.ratio())
