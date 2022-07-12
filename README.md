# multilingual-chatbot

The chatbot can be accessed here (booting of the app may take some time):
https://multilingual-chatbot.herokuapp.com/

Currently, it is able to understand and respond to very simple sentences in over 100 languages.

The chatbot is able to understand sentences in the following areas:

- Greetings (e.g. hello, hey, ...)
- Asking the chatbot how it feels (e.g. How are you?)
- Asking the chatbot for it's name (e.g. What is your name?)
- Asking the chatbot for the time or the date (e.g. What time is it? What is the current date?)
- Asking where the chatbot comes from / what it is (e.g. What are you?)

The chatbot has been developed using TensorFlow as well as Flask to create the Web App.
The TensorFlow-model has been trained with labelled data. For each label (e.g. Greeting), multiple sentences have been given as examples for the neural network to learn. The sentences have been transformed to numerical values using the Tokenizer provided by TensorFlow. These transformed sentences and the labels have been used for training. 
For each new user input, the chatbot-program then transforms the input into numerical values using the previously mentioned Tokenizer. The tokenized inputs can then be run through the neural network resulting in a prediction of a class/label. Based on the predicted class/label, the chatbot will give a previously specified response.

