# importing all required libraries
import imdb
import pyttsx3
import speech_recognition as sr
import datetime


# Function for speaking
def speak(text):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	rate = engine.getProperty('rate')

	engine.setProperty('rate', rate-20)

	engine.say(text)
	engine.runAndWait()


# calling the speak() function
speak("Say the movie name")


# Function to get input in the audio format
def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
		said = ""

	try:

		# will recognize the input
		said = r.recognize_google(audio)
		print(said)

	except:
		speak("Didn't get that")
	# will return the input in lowercase
	return said.lower()


# Function for searching movie
def search_movie():

	# gathering information from IMDb
	moviesdb = imdb.IMDb()

	# search for title
	text = get_audio()

	# passing input for searching movie
	movies = moviesdb.search_movie(text)

	speak("Searching for " + text)
	if len(movies) == 0:
		speak("No result found")
	else:

		speak("I found these:")

		for movie in movies:

			title = movie['title']
			year = movie['year']
			# speaking title with releasing year
			speak(f'{title}-{year}')

			info = movie.getID()
			movie = moviesdb.get_movie(info)

			title = movie['title']
			year = movie['year']
			rating = movie['rating']
			plot = movie['plot outline']

			# the below if-else is for past and future release
			if year < int(datetime.datetime.now().strftime("%Y")):
				speak(
					f'{title}was released in {year} has IMDB rating of {rating}.\
					The plot summary of movie is{plot}')
				print(
					f'{title}was released in {year} has IMDB rating of {rating}.\
					The plot summary of movie is{plot}')
				break

			else:
				speak(
					f'{title}will release in {year} has IMDB rating of {rating}.\
					The plot summary of movie is{plot}')
				print(
					f'{title}will release in {year} has IMDB rating of {rating}.\
					The plot summary of movie is{plot}')
				break


search_movie()
