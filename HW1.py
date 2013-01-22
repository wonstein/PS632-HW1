def shout(txt):
  new_txt = txt.upper()
  new_txt = new_txt.replace(". ", "! ")
  if new_txt[len(new_txt) - 1] != ".":
    new_txt = new_txt + "!"
  new_txt = new_txt.replace("?", "!")
  return new_txt
  
def reverse(txt):
  if isinstance(txt, str) == False:
    return ""
      
  return txt[::-1]
  
def reversewords(txt):
  if isinstance(txt, str) == False:
    return ""
  
  new_text = ""
  reversed_sentences = []
    
  tmp = txt.replace("?", ".")
  tmp = tmp.replace("!", ".")
  sentences = tmp.split(". ")
  sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
  
  last_sentence = sentences[len(sentences) - 1]
  if last_sentence[len(last_sentence) - 1] == ".":
    sentences[len(sentences) - 1] = last_sentence[0:len(last_sentence)-1]
  
  for sentence in sentences:
    words = sentence.split()
    words.reverse()
    reversed_sentence = ""
    for word in words:
      reversed_sentence += word
      reversed_sentence += " "
    reversed_sentences.append(reversed_sentence[0:(len(reversed_sentence)-1)])
  
  for sentence in reversed_sentences:
    if len(sentence) > 0:
      new_text += sentence
      new_text += ". "
    
  return new_text
  
def reversewordletters(txt):
  if isinstance(txt, str) == False:
    return ""
  
  tmp_text = ""
  
  back_pointer = 0
  front_pointer = 0
  stop_chars = [" ", ".", "?", "!", ",", ":", ";"]
  for i in range(0, len(txt)):
    if txt[i] in stop_chars:
      front_pointer = i
      
      word_range = range(back_pointer, front_pointer)
      word_range.reverse()
      for j in word_range:
        tmp_text += txt[j]
      tmp_text += txt[i]
      
      back_pointer = i+1
      
  return tmp_text
  
def piglatin(txt):
  if isinstance(txt, str) == False:
    return ""
  
  words = txt.split()
  new_sentence = ''
  
  for word in words:
    pl_word = ''
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'o' or word[0] == 'u' or word[0] == 'i':
	  pl_word = word + 'way'
    elif not(word[0] == 'a' or word[0] == 'e' or word[0] == 'o' or word[0] == 'u' or word[0] == 'i'):
	  for letters in range(1, len(word)-1):
	    if word[letters] in ['a', 'e', 'i', 'o', 'u']:
		  if word[letters+1] in ['a', 'e', 'i', 'o', 'u']:
		    pl_word = word[letters:len(word)] + word[0:letters] + 'ay'
		    letters = len(word)
		  elif not(word[letters+1] in ['a', 'e', 'i', 'o', 'u']):
			pl_word = word[letters:len(word)] + word[0:letters] + 'ay'
            letters = len(word)
  
    new_sentence += pl_word + ' '
  
  return ''.join(new_sentence)
  
	