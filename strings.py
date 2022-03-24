a = ""
length = 0


b = "it's ok"
length = 7


c = 'it\'s ok'
length = 7


d = """hey"""
length = 3


e = '\n'
length = 1



def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return len(zip_code) == 5 and zip_code.isdigit()
  
  
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    indices = []
    
    for i, doc in enumerate(doc_list):
        
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        
        if keyword.lower() in normalized:
            indices.append(i)
            
            
    
    return indices
  
  
  
  
  
  def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    new_dic = {}
    for keyword in keywords:
        new_dic[keyword] =  word_search(doc_list, keyword)
    return new_dic
  

