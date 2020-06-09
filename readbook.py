import PyPDF2
import re
from app import predict
import requests
import shutil
import glob
import sys
import os
import django
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from urllib import request

sys.path.append('/home/bidocean/Desktop/virtual_python/python_gnosis/gnosis_new/gnosis-library/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'GnosisLibrary.settings'
django.setup()
from LivingLibrary.models import Book, Author, Genre, Language
from LivingLibrary.forms import AuthorForm, GenreForm, LanguageForm,BookForm


def pushothermodels(modelname ,modeldata):
	if modelname == 'language':
		langdict = {}
		langdict['name'] = modeldata
		form = LanguageForm(langdict)
		if form.is_valid():
			form.save()
			print('language saved to db')

	if modelname == 'genre':
		genredic = {}
		genredic['name'] = modeldata
		form = GenreForm(genredic)
		if form.is_valid():
			form.save()
			print('language saved to db')

	if modelname == 'authors':
		authorsdic = {}
		authors = modeldata
		for author in authors:
			authorsdic['name'] = author
			form = AuthorForm(authorsdic)
			if form.is_valid():
				form.save()
				print('saved author')
				print(author)


def getisbndetails(isbn):
	api = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'
	isbnapi = api+isbn
	r = requests.get(isbnapi)
	data = r.json()
	bookdetails = {}
	bookdetails['title'] = data['items'][0]['volumeInfo']['title']
	bookdetails['authors'] = data['items'][0]['volumeInfo']['authors']
	bookdetails['pageCount'] = data['items'][0]['volumeInfo']['pageCount']
	bookdetails['genre'] = predict(data['items'][0]['volumeInfo']['title'])
	bookdetails['isbn'] = isbn
	bookdetails['image'] = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
	language = data['items'][0]['volumeInfo']['language']
	if language.lower() == 'en':
		bookdetails['language'] = 'English'
	else:
		bookdetails['language'] = language
	return bookdetails

def getbookdetails(name):
	regex=r'978[-0-9]{10,15}'
	found = False
	pdfFileObj = open(name, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	for x in range(0,10):
		page = pdfReader.getPage(x)
		x = re.search(regex, page.extractText())
		if x is not None:
			isbn = format(x.group(0)).replace('-','')
			found = True
			bookdetails = getisbndetails(isbn)
			break
	if found:
		# shutil.move(name,'done/'+name)
		pushtodatabase(bookdetails, name)
		return bookdetails
	else:
		# shutil.move(name,'notdone/'+name)
		print('not found')
		return 'not found'


def pushtodatabase(bookdetails, name):
	pushothermodels('language', bookdetails['language'])
	pushothermodels('genre', bookdetails['genre'])
	pushothermodels('authors', bookdetails['authors'])

	bookdic = {}
	bookdic['title'] = bookdetails['title']
	bookdic['pageCount'] = bookdetails['pageCount']
	bookdic['isbn'] = bookdetails['isbn']
	bookdic['pages'] = bookdetails['pageCount']

	languageids = Language.objects.filter(name=bookdetails['language']).values('id')[0]['id']
	bookdic['language'] = str(languageids)
	
	genreid = Genre.objects.filter(name=bookdetails['genre']).values('id')[0]['id']
	bookdic['genre'] = [str(genreid)]
	
	authorlist = []
	for author in bookdetails['authors']:
		authorid = Author.objects.filter(name=author.capitalize()).values('id')[0]['id']
		authorlist.append(str(authorid))
	bookdic['author'] = authorlist
	
	bookfiles = {}
	bookfiles['pdf'] = File(open(name,'rb'))
	# bookfiles['cover'] = File(open('AI.png','rb'))
	bookfiles['epub'] = File(open(name,'rb'))

	testfile = request.URLopener()
	coverimagename = bookdetails['title']+'.jpg'
	testfile.retrieve(bookdetails['image'],coverimagename)
	bookfiles['cover'] = File(open(coverimagename,'rb'))
	form = BookForm(bookdic,bookfiles)
	if form.is_valid():
		form.save()
	else:
		print(form.errors)
	os.remove(coverimagename)

booklist = glob.glob("*.pdf")
for book in booklist:
	print(book)
	getbookdetails(book)
