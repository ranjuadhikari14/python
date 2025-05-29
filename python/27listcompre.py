fruits=['Apple','Banana','plum','kiwi','mango']
#filters the fruits having 5 letters using list comprehensive
fivelet_words=[ fruit for fruit in fruits if len(fruit) == 5]
print(f"five letter fruits are {fivelet_words}")

