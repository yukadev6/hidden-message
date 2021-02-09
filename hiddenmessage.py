from PIL import Image

words = Image.open('/Users/yuka/Desktop/Coding/Udemy/Complete-Python-3-Bootcamp-master/14-Working-with-Images/word_matrix.png')

words.size

reveal = Image.open('/Users/yuka/Desktop/Coding/Udemy/Complete-Python-3-Bootcamp-master/14-Working-with-Images/mask.png')

reveal.putalpha(90)

reveal.size

reveal = reveal.resize((1015,559))

words.paste(reveal,box=(0,0),mask=reveal)

