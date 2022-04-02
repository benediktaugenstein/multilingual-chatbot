def helper2(x):
  x = x.upper() + 'lalala'
  return x

def new_input(input_initial, tokenizers, lengths_input, models, ohe, ohe2):
  from subs import sub
  from datetime import datetime, timezone, timedelta
  from tensorflow.keras.preprocessing.sequence import pad_sequences
  for key, value in contractions.items():
    search = key + ' '
    if search in input_initial:
      input_initial = input_initial.replace(key, value)
  input_prep = [input_initial]
  inp = tokenizers[0].texts_to_sequences(input_prep)
  inp = pad_sequences(inp, maxlen=lengths_input[0], padding='post', truncating='post')
  prediction = models[0].predict(inp)
  
  #print('Name', 'Time', 'Greeting')
  #print(prediction)
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
  if max_pred <= 0.33:
    output = 'Sorry, I did not understand that.'
  elif var == 'Greeting':
    output = 'Hello there'
  elif var == 'Name':
    output = 'My name is Ben, and yours?'
  elif var == 'Time':
    now = datetime.now().utcnow()+timedelta(hours=1)
    time = now.strftime("%H:%M")
    date = now.strftime("%Y-%m-%d")
    output = 'Currently, it is' + time + '\nThe date is: ' + date
  elif var =='Feeling':
    inp_feel = tokenizers[1].texts_to_sequences(input_prep)
    inp_feel = pad_sequences(inp_feel, maxlen=lengths_input[1], padding='post', truncating='post')
    prediction = models[1].predict(inp_feel)
    max_pred = max(prediction[0])
    for i, x in enumerate(prediction[0]):
      if x == max_pred:
        prediction[0][i] = 1
      else:
        prediction[0][i]=0
    prediction_inverse_transformed = ohe2.inverse_transform(prediction)
    var = prediction_inverse_transformed[0]
    if max_pred <= 0.3:
      output = 'Sorry, I did not understand that.'
    elif var == 'feel_HAL':
      output = 'Im good, how about you?'
    elif var == 'feel_person_good':
      output = 'I am happy that you are feeling well.'
    elif var == 'feel_person_bad':
      output = 'I am sorry to hear that.'
    elif var == 'feel_person_question':
      output = 'I do not know. How do you feel?'
  elif var == 'Existence':
    output = 'I am an artificial intelligence and my name is Ben. I do not have feelings. Basically, I am just statistics. My purpose is to talk to you. How may I help you?'
  
  #prediction = 'hello'
  ##var = prediction

  #var_string_prep = str(output) + '<br>' + str(initial_input) + '<br>'
  var_string_prep = output
  var_string = str(var_string_prep)
  return var_string
  
 
