#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pygame


# In[4]:


pip install gtts


# In[9]:


# pip install gTTS
from pygame import mixer
from gtts import gTTS
def main():
  tts = gTTS(input('What would you like to say via speakers'))
  tts.save('python_8.mp3')
  mixer.init()
  mixer.music.load('python_8.mp3')
  mixer.music.play()

if __name__ == "__main__":
  main()


# In[ ]:




