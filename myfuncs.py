def helper2(x):
  x = x.upper() + 'lalala'
  return x

def new_input(input_initial):
  #input_initial = input('input here: ')
  #for word in inp.split():
    #if word.lower() in contractions:
      #inp = inp.replace(word, contractions[word.lower()])
  #for key, value in contractions.items():
    #search = key + ' '
    #if search in input_initial:
      #input_initial = input_initial.replace(key, value)
  #input_initial = [input_initial]
  #inp = tokenizers[0].texts_to_sequences(input_initial)
  #inp = pad_sequences(inp, maxlen=lengths_input[0], padding='post', truncating='post')
  prediction = models[0].predict(input_initial)
  #max_pred = max(prediction[0])
  #for i, x in enumerate(prediction[0]):
    #if x == max_pred:
      #print(x)
      #prediction[0][i] = 1
    #else:
      #prediction[0][i]=0

  #prediction_inverse_transformed = ohe.inverse_transform(prediction)
  #print('Predicted category is: ', prediction_inverse_transformed[0])
  #var = prediction_inverse_transformed[0]
  #prediction = 'hello'
  var_string = str(prediction)
  return var_string
  
 
