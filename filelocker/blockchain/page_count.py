# -*- coding: utf-8 -*-
"""page_count.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O6t_85cVNgLLYmIIPKzf_QdhBOccbeH4
"""

# Commented out IPython magic to ensure Python compatibility.
'''!apt-get install poppler-utils 
# %pip install pdf2image'''

from pdf2image import convert_from_path,convert_from_bytes

def check_page_count(pdf):
    #pages = convert_from_path(pdfs, 500)
    pages = convert_from_bytes(pdfs.read(), 500)
    l = len(pages)

    if l<6:
      return True
    else:
      return False