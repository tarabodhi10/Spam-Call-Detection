import speech_recognition as sr

def converstation():
    textt=''
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
#         print("Time over, thanks")
#     print('sss',type(audio_text),audio_text)
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling  
    try:
        textt=r.recognize_google(audio_text)
      # using google speech recognition
        print("Text: ",textt)
    except:
        print("Sorry, I did not get that")

    ###############################
    # Load the pickled model
    import pickle
    #from sklearn.feature_extraction.text import TfidfVectorizer
    #  vectorizer = TfidfVectorizer()

    pickled_model = pickle.load(open('model_04_2022.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer_04_2022.pkl', 'rb'))

    transform_text = vectorizer.transform([textt])
    prediction = pickled_model.predict(transform_text)

    pred_value = prediction[0]
#     print(pred_value)

    #########################
#     if pred_value == 1:
#         print('Spam call')
#     else:
#         print('Normal')

    return pred_value


i = 20
while i != 0:
    
    if i % 2 == 0:
        print('-------------------THis is 3rd person speaking')
        value = converstation()
        if value == 1:
            print('     ')
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            print('$$$$          This is a spam call            $$$$')
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            print('     ')
            i=0
            break
    if i % 2 == 1:
        print('+++++++User speaking')
        value = converstation()
  
    i += 1
print('Code is over. Thank you')