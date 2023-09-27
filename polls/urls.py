from django.urls import path
from .views import getallAuthor, getallbooks, getAuthorID, postAuthor, postBook, patchAuthor, patchBook, putAuthor, putBook, deleteAuthor, deleteBook

urlpatterns=[
    path('getallauthor/', getallAuthor.as_view()), #hamma authorlar ro'yhati
    path('getallbooks/', getallbooks.as_view()), #hamma kitoblar ro'yhati
    path('getAuthorID/<int:forid>', getAuthorID.as_view()), #Author ID sini kiritsa kitoblarini chiqarib beradi
    #pasdagi qismlar CRUD >>>
    path('postAuthor/', postAuthor.as_view()),
    path('postBook/', postBook.as_view()),
    path('patchAuthor/<int:forid>', patchAuthor.as_view()),
    path('patchBook/<int:forid>', patchBook.as_view()),
    path('putAuthor/<int:forid>', putAuthor.as_view()),
    path('putBook/<int:forid>', putBook.as_view()),
    path('deleteAuthor/<int:forid>', deleteAuthor.as_view()),
    path('deleteBook/<int:forid>', deleteBook.as_view())

    
]