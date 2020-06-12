import PyPDF2
import re
from app import predict
import requests
import shutil
import glob
import sys
import os
import django
# from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from urllib import request
from zipfile import ZipFile

sys.path.append('/home/bidocean/Desktop/virtual_python/python_gnosis/gnosis_new/gnosis-library/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'GnosisLibrary.settings'
django.setup()
from LivingLibrary.models import Book, Author, Genre, Language
from LivingLibrary.forms import AuthorForm, GenreForm, LanguageForm,BookForm

mainfolder = ''

def pushothermodels(modelname ,modeldata):
	if modelname == 'language':
		langdict = {}
		langdict['name'] = modeldata
		form = LanguageForm(langdict)
		if form.is_valid():
			form.save()

	if modelname == 'genre':
		genredic = {}
		genredic['name'] = modeldata
		form = GenreForm(genredic)
		if form.is_valid():
			form.save()

	if modelname == 'authors':
		authorsdic = {}
		authors = modeldata
		for author in authors:
			authorsdic['name'] = author
			form = AuthorForm(authorsdic)
			if form.is_valid():
				form.save()

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
	# bookfiles['pdf'] = File(open(name,'rb'), os.path.basename(name))
	bookfiles['pdf'] = File(open(name,'rb'), bookdic['title']+os.path.splitext(name)[1])
	bookfiles['epub'] = File(open(name,'rb'), bookdic['title']+os.path.splitext(name)[1])

	testfile = request.URLopener()
	coverimagename = bookdetails['title']+'.jpg'
	testfile.retrieve(bookdetails['image'],coverimagename)
	bookfiles['cover'] = File(open(coverimagename,'rb'),coverimagename.replace('pdfbooks/',''))

	form = BookForm(bookdic,bookfiles)
	if form.is_valid():
		form.save()
	else:
		print(form.errors)
	os.remove(coverimagename)

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
	found = 2 #1->done 2->not done 3->duplicate
	pdfFileObj = open(name, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	done = False
	for x in range(0,10):
		try:
			page = pdfReader.getPage(x)
		except:
			break
		# print(page)
		try:
			x = re.findall(regex, page.extractText())
		except:
			break
		if x is not None:
			for isbn in x:
				api = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'
				isbn = isbn.replace('-','')
				isbnapi = api+isbn
				r = requests.get(isbnapi)
				data = r.json()
				if 'items' in data:
					ifisbnfound = Book.objects.filter(isbn=isbn)
					if ifisbnfound.count() == 1 :
						found = 3
					else:
						found = 1
						bookdetails = getisbndetails(isbn)
					done = True
					break
		if done:
			break
	if found == 1:
		pushtodatabase(bookdetails, name)
		newdir= name.replace(mainfolder,'')
		os.makedirs(os.path.dirname('done/'+newdir), exist_ok=True)
		shutil.move(name,'done/'+newdir)
		print('done')
	elif found == 2:
		newdir = name.replace(mainfolder,'')
		os.makedirs(os.path.dirname('notdone/'+newdir), exist_ok=True)
		shutil.move(name,'notdone/'+newdir)
		print('isbn not found')
	else:
		newdir = name.replace(mainfolder,'')
		os.makedirs(os.path.dirname('duplicate/'+newdir), exist_ok=True)
		shutil.move(name,'duplicate/'+newdir)
		print('its a duplicate')

def deletezippedfile():
	if os.path.exists('done/zipfiles'):
		shutil.rmtree('done/zipfiles')
	if os.path.exists('notdone/zipfiles'):
		shutil.rmtree('notdone/zipfiles')
	if os.path.exists('duplicate/zipfiles'):
		shutil.rmtree('duplicate/zipfiles')

def entrypoint(direc):
	booklist = glob.glob(direc+"*")
	for files in booklist:
		file_name, file_ext = os.path.splitext(files)
		if file_ext == '':
			dirname = os.path.basename(files)
			newdir = direc+dirname+'/'
			entrypoint(newdir)
			shutil.rmtree(newdir)
		elif file_ext == '.pdf':
			print(files)
			getbookdetails(files)
		elif file_ext == '.zip':
			if not os.path.exists('zipfiles'):
				os.mkdir('zipfiles')
			openedzippedfile = ZipFile(files)
			openedzippedfile.extractall('zipfiles')
			entrypoint('zipfiles/')
			deletezippedfile()
			shutil.rmtree('zipfiles')
			shutil.move(files,'done/'+os.path.basename(files))
		else:
			shutil.move(files,'filetypeunknown/'+os.path.basename(files))

mainfolder = 'pdfbooks/' 
if os.path.exists('done'):
	os.makedirs('done')
if os.path.exists('notdone'):
	os.makedirs('notdone')
if os.path.exists('duplicate'):
	os.makedirs('duplicate')
if os.path.exists('filetypeunknown'):
	os.makedirs('filetypeunknown')
entrypoint(mainfolder)