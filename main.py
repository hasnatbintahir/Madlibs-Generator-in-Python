with open("story.txt", "r") as f:
    story = f.read()
    
target_starter = "<"
target_ender = ">"

words = set()
starting_idx = -1

for i, letter in enumerate(story):
    if letter == target_starter:
        starting_idx = i
        
    if letter == target_ender and starting_idx != -1:
        word = story[starting_idx:i+1]
        words.add(word)
        starting_idx = -1
        
        
answers = {}

for words_i in words:
    answer = input(f"Enter answer for {words_i[1:-1]}: ")
    answers[words_i] = answer
    
    
for key, value in answers.items():
    story = story.replace(key,value)
    
print("\n",story,"\n") 