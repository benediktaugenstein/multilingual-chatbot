#@title Contractions
def sub():
  contractions = {
  "ain't": "am not",
  "aren't": "are not",
  "can't": "cannot",
  "can't've": "cannot have",
  "'cause": "because",
  "could've": "could have",
  "couldn't": "could not",
  "couldn't've": "could not have",
  "didn't": "did not",
  "doesn't": "does not",
  "don't": "do not",
  "hadn't": "had not",
  "hadn't've": "had not have",
  "hasn't": "has not",
  "haven't": "have not",
  "he'd": "he had / he would",###########################
  "he'd've": "he would have",
  "he'll": "he will",
  "he'll've": "he will have",
  "he's": "he has / he is",##############
  "how'd": "how did",
  "how'd'y": "how do you",
  "how'll": "how will",
  "how's": "how has / how is",
  "i'd": "I had / I would",
  "i'd've": "I would have",
  "i'll": "I shall / I will",
  "i'll've": "I shall have / I will have",
  "i'm": "I am",
  "i've": "I have",
  "isn't": "is not",
  "it'd": "it had / it would",
  "it'd've": "it would have",
  "it'll": "it shall / it will",
  "it'll've": "it shall have / it will have",
  "it's": "it has / it is",
  "let's": "let us",
  "ma'am": "madam",
  "mayn't": "may not",
  "might've": "might have",
  "mightn't": "might not",
  "mightn't've": "might not have",
  "must've": "must have",
  "mustn't": "must not",
  "mustn't've": "must not have",
  "needn't": "need not",
  "needn't've": "need not have",
  "o'clock": "of the clock",
  "oughtn't": "ought not",
  "oughtn't've": "ought not have",
  "shan't": "shall not",
  "sha'n't": "shall not",
  "shan't've": "shall not have",
  "she'd": "she had / she would",
  "she'd've": "she would have",
  "she'll": "she shall / she will",
  "she'll've": "she shall have / she will have",
  "she's": "she has / she is",#######################
  "should've": "should have",
  "shouldn't": "should not",
  "shouldn't've": "should not have",
  "so've": "so have",
  "so's": "so is",
  "that'd": "that would / that had",
  "that'd've": "that would have",
  "that's": "that has / that is",
  "there'd": "there had / there would",
  "there'd've": "there would have",
  "there's": "there has / there is",
  "they'd": "they had / they would",
  "they'd've": "they would have",
  "they'll": "they shall / they will",
  "they'll've": "they shall have / they will have",
  "they're": "they are",
  "they've": "they have",
  "to've": "to have",
  "wasn't": "was not",
  "we'd": "we had / we would",
  "we'd've": "we would have",
  "we'll": "we will",
  "we'll've": "we will have",
  "we're": "we are",
  "we've": "we have",
  "weren't": "were not",
  "what'll": "what shall / what will",
  "what'll've": "what shall have / what will have",
  "what're": "what are",
  "what's": "what has / what is",
  "what've": "what have",
  "when's": "when has / when is",
  "when've": "when have",
  "where'd": "where did",
  "where's": "where has / where is",
  "where've": "where have",
  "who'll": "who shall / who will",
  "who'll've": "who shall have / who will have",
  "who's": "who has / who is",
  "who've": "who have",
  "why's": "why has / why is",
  "why've": "why have",
  "will've": "will have",
  "won't": "will not",
  "won't've": "will not have",
  "would've": "would have",
  "wouldn't": "would not",
  "wouldn't've": "would not have",
  "y'all": "you all",
  "y'all'd": "you all would",
  "y'all'd've": "you all would have",
  "y'all're": "you all are",
  "y'all've": "you all have",
  "you'd": "you had / you would",
  "you'd've": "you would have",
  "you'll": "you shall / you will",
  "you'll've": "you shall have / you will have",
  "you're": "you are",
  "you've": "you have",
  "aint": "am not / are not",
  "arent": "are not / am not",
  "cant": "cannot",
  "cantve": "cannot have",
  "cause": "because",
  "couldve": "could have",
  "couldnt": "could not",
  "couldntve": "could not have",
  "didnt": "did not",
  "doesnt": "does not",
  "dont": "do not",
  "hadnt": "had not",
  "hadntve": "had not have",
  "hasnt": "has not",
  "havent": "have not",
  "hed": "he had / he would",
  "hedve": "he would have",
  "hellve": "he shall have / he will have",
  "hes": "he has / he is",
  "howd": "how did",
  "howdy": "how do you",
  "howll": "how will",
  "hows": "how has / how is",
  "id": "I had / I would",
  "idve": "I would have",
  "ill": "I shall / I will",
  "illve": "I shall have / I will have",
  "im": "I am",
  "ive": "I have",
  "isnt": "is not",
  "itd": "it had / it would",
  "itdve": "it would have",
  "itll": "it shall / it will",
  "itllve": "it shall have / it will have",
  "its": "it has / it is",
  "lets": "let us",
  "maam": "madam",
  "maynt": "may not",
  "mightve": "might have",
  "mightnt": "might not",
  "mightntve": "might not have",
  "mustve": "must have",
  "mustnt": "must not",
  "mustntve": "must not have",
  "neednt": "need not",
  "needntve": "need not have",
  "oclock": "of the clock",
  "oughtnt": "ought not",
  "oughtntve": "ought not have",
  "shant": "shall not",
  "shant": "shall not",
  "shantve": "shall not have",
  "shed": "she had / she would",
  "shedve": "she would have",
  "shell": "she shall / she will",
  "shellve": "she shall have / she will have",
  "shes": "she has / she is",
  "shouldve": "should have",
  "shouldnt": "should not",
  "shouldntve": "should not have",
  "sove": "so have",
  "sos": "so as / so is",
  "thatd": "that would / that had",
  "thatdve": "that would have",
  "thats": "that has / that is",
  "thered": "there had / there would",
  "theredve": "there would have",
  "theres": "there has / there is",
  "theyd": "they had / they would",
  "theydve": "they would have",
  "theyll": "they shall / they will",
  "theyllve": "they shall have / they will have",
  "theyre": "they are",
  "theyve": "they have",
  "tove": "to have",
  "wasnt": "was not",
  "wed": "we had / we would",
  "wedve": "we would have",
  "well": "we will",
  "wellve": "we will have",
  "were": "we are",
  "weve": "we have",
  "werent": "were not",
  "whatll": "what shall / what will",
  "whatllve": "what shall have / what will have",
  "whatre": "what are",
  "whats": "what has / what is",
  "whatve": "what have",
  "whens": "when has / when is",
  "whenve": "when have",
  "whered": "where did",
  "wheres": "where has / where is",
  "whereve": "where have",
  "wholl": "who shall / who will",
  "whollve": "who shall have / who will have",
  "whos": "who has / who is",
  "whove": "who have",
  "whys": "why has / why is",
  "whyve": "why have",
  "willve": "will have",
  "wont": "will not",
  "wontve": "will not have",
  "wouldve": "would have",
  "wouldnt": "would not",
  "wouldntve": "would not have",
  "yall": "you all",
  "yalld": "you all would",
  "yalldve": "you all would have",
  "yallre": "you all are",
  "yallve": "you all have",
  "youd": "you had / you would",
  "youdve": "you would have",
  "youll": "you shall / you will",
  "youllve": "you shall have / you will have",
  "youre": "you are",
  "youve": "you have",
  "ain t": "am not / are not",
  "aren t": "are not / am not",
  "can t": "cannot",
  "can t ve": "cannot have",
  " cause": "because",
  "could ve": "could have",
  "couldn t": "could not",
  "couldn t ve": "could not have",
  "didn t": "did not",
  "doesn t": "does not",
  "don t": "do not",
  "hadn t": "had not",
  "hadn t ve": "had not have",
  "hasn t": "has not",
  "haven t": "have not",
  "he d": "he had / he would",
  "he d ve": "he would have",
  "he ll": "he shall / he will",
  "he ll ve": "he shall have / he will have",
  "he s": "he has / he is",
  "how d": "how did",
  "how d y": "how do you",
  "how ll": "how will",
  "how s": "how has / how is",
  "i d": "I had / I would",
  "i d ve": "I would have",
  "i ll": "I shall / I will",
  "i ll ve": "I shall have / I will have",
  "i m": "I am",
  "i ve": "I have",
  "isn t": "is not",
  "it d": "it had / it would",
  "it d ve": "it would have",
  "it ll": "it shall / it will",
  "it ll ve": "it shall have / it will have",
  "it s": "it has / it is",
  "let s": "let us",
  "ma am": "madam",
  "mayn t": "may not",
  "might ve": "might have",
  "mightn t": "might not",
  "mightn t ve": "might not have",
  "must ve": "must have",
  "mustn t": "must not",
  "mustn t ve": "must not have",
  "needn t": "need not",
  "needn t ve": "need not have",
  "o clock": "of the clock",
  "oughtn t": "ought not",
  "oughtn t ve": "ought not have",
  "shan t": "shall not",
  "sha n t": "shall not",
  "shan t ve": "shall not have",
  "she d": "she had / she would",
  "she d ve": "she would have",
  "she ll": "she shall / she will",
  "she ll ve": "she shall have / she will have",
  "she s": "she has / she is",
  "should ve": "should have",
  "shouldn t": "should not",
  "shouldn t ve": "should not have",
  "so ve": "so have",
  "so s": "so as / so is",
  "that d": "that would / that had",
  "that d ve": "that would have",
  "that s": "that has / that is",
  "there d": "there had / there would",
  "there d ve": "there would have",
  "there s": "there has / there is",
  "they d": "they had / they would",
  "they d ve": "they would have",
  "they ll": "they shall / they will",
  "they ll ve": "they shall have / they will have",
  "they re": "they are",
  "they ve": "they have",
  "to ve": "to have",
  "wasn t": "was not",
  "we d": "we had / we would",
  "we d ve": "we would have",
  "we ll": "we will",
  "we ll ve": "we will have",
  "we re": "we are",
  "we ve": "we have",
  "weren t": "were not",
  "what ll": "what shall / what will",
  "what ll ve": "what shall have / what will have",
  "what re": "what are",
  "what s": "what has / what is",
  "what ve": "what have",
  "when s": "when has / when is",
  "when ve": "when have",
  "where d": "where did",
  "where s": "where has / where is",
  "where ve": "where have",
  "who ll": "who shall / who will",
  "who ll ve": "who shall have / who will have",
  "who s": "who has / who is",
  "who ve": "who have",
  "why s": "why has / why is",
  "why ve": "why have",
  "will ve": "will have",
  "won t": "will not",
  "won t ve": "will not have",
  "would ve": "would have",
  "wouldn t": "would not",
  "wouldn t ve": "would not have",
  "y all": "you all",
  "y all d": "you all would",
  "y all d ve": "you all would have",
  "y all re": "you all are",
  "y all ve": "you all have",
  "you d": "you had / you would",
  "you d ve": "you would have",
  "you ll": "you shall / you will",
  "you ll ve": "you shall have / you will have",
  "you re": "you are",
  "you ve": "you have"
  }
  return contractions