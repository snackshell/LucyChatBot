from bardapi import Bard

token = 'YAgJWHC1gFM8l0qRXzzBVkgXwLaukaAlUMQkivbjQUid9taadVsy4Q6PP-GnmRe6zaXPQg.'
bard = Bard(token=token)

def chat(text):
    """
    Take input text and return bard response.
    Args:
        text: Text which is send to bard AI.
    Return:
        A response from bard.
    """
    response = bard.get_answer(text)['content']
    
    return response