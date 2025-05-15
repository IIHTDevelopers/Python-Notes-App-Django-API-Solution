from notesapp.models import NotesModel
class NotesService:
    def search_by_id(id):
        qs=NotesModel.objects.all()
        qs=qs.filter(id=id)
        #print("1",qs,type(qs))
        return qs
    def search_by_author(name):
        qs=NotesModel.objects.all()
        qs=qs.filter(author=name)
        #print("2",qs,type(qs))
        return qs
    def search_by_status(status):
        qs=NotesModel.objects.all()
        qs=qs.filter(status=status)
        #print("3",qs,type(qs))
        return qs
