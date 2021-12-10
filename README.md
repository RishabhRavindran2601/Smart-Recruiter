# Smart-Recruiter
initial commit

The idea behind creating this project was to build a machine learning model that could interect with a candidate, the way a recruiter would. An interviewer looks for various criterias in a candidate, some of them include knowing in what mood is the candidate giving an interview, knowing the sentiment behind the answers that he/she gives (especially for personal questions), knowing how correct is a particular answer, etc.
This project is a chatbot that takes care of some of the basic requirements in judging a candidate.


DATASETS:

Made use of two different datasets:

RAVDESS. This dataset includes around 1500 audio file input from 24 different actors. 12 male and 12 female where these actors record short audios in 8 different emotions i.e 1 = neutral, 2 = calm, 3 = happy, 4 = sad, 5 = angry, 6 = fearful, 7 = disgust, 8 = surprised.
Each audio file is named in such a way that the 7th character is consistent with the different emotions that they represent.

Twitter_Tweets. This dataset includes around 30000 entries of tweets from twitter in 3 different sentiments i.e. positive, neutral and negative.

FEATURES OF THIS PROJECT:
1. Completely voice automated, just like an interview.
2. speech emotion recognizer to analyze the mood of a candidate.
3. sentiment analyzer to get insight on the sentiment behind a answer.
4. spacy pre-trained models to recognize name, place of stay and previously worked company of the candidate.
5. resume summarizer to extract kep parts of a resume.
6. github parser to list down the project that the candidate has worked on.
7. text similarity (or distance) calculation to check the degree of correctness of some technical answers.

NOTE: the questions in the code can be modified based on the requirements of the person using it.

CONCLUSION
Building the model was a challenging task as it involved lot of trail and error methods, tuning etc. The biggest challenge was to incorporate input and output speeches from candidate and recruiter respectively. The speech recognition model is very accurate and fine tuned to perfection.

NOTE: this code will not work on Google Colab, since google colab requires a different code to access your microphone using chrome.
