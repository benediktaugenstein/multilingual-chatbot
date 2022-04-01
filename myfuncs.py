model = keras.models.load_model('/model/general')
model2 = keras.models.load_model('/model/feeling')

link_general = '/data/general.csv'
link_feeling = '/data/feeling.csv'
models = [model, model2]
datasets = [link_general, link_feeling]
tokenizers = []
word_indices = []
sequences_array = []
lengths_input = []
labels_transformed_array = []

#@title For every model get data, transform data and save important variables
for i, model in enumerate(models):
  data = pd.read_csv(datasets[i])

  sentences = data['Sentence']
  labels = data['Result']

  #tokenizer = Tokenizer(num_words = 100)
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(sentences)
  word_index = tokenizer.word_index
  sequences = tokenizer.texts_to_sequences(sentences)

  tokenizers.append(tokenizer)
  word_indices.append(word_index)

  sequences = pad_sequences(sequences, padding='post', truncating='post')
  sequences_array.append(sequences)

  #word_count = len(word_index)
  len_input = len(sequences[0])
  lengths_input.append(len_input)
  if i == 0: # General
    ohe = LabelBinarizer()
    labels_transformed_general = ohe.fit_transform(labels)
  else: # Feeling
    ohe2 = LabelBinarizer()
    labels_transformed_feeling = ohe2.fit_transform(labels)
  #len_output = len(labels_transformed[0])

def helper2(x):
  x = x.upper() + 'lalala'
  return x

def new_input(input_initial):
    input_initial = input('input here: ')
  #for word in inp.split():
    #if word.lower() in contractions:
      #inp = inp.replace(word, contractions[word.lower()])
  #for key, value in contractions.items():
    #search = key + ' '
    #if search in input_initial:
      #input_initial = input_initial.replace(key, value)
  input_initial = [input_initial]
  inp = tokenizers[0].texts_to_sequences(input_initial)
  inp = pad_sequences(inp, maxlen=lengths_input[0], padding='post', truncating='post')
  prediction = models[0].predict(inp)
  max_pred = max(prediction[0])
  for i, x in enumerate(prediction[0]):
    if x == max_pred:
      #print(x)
      prediction[0][i] = 1
    else:
      prediction[0][i]=0

  prediction_inverse_transformed = ohe.inverse_transform(prediction)
  #print('Predicted category is: ', prediction_inverse_transformed[0])
  var = prediction_inverse_transformed[0]
  var_string = str(var)
  return var_string
  
 
