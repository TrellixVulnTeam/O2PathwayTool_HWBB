from tkinter import *
from tkinter import ttk
from objects.app import app
from objects.project import Project
from objects.subject import Subject

class SubjectList(object):
    def __init__(self, sidePanel):
        self.container = LabelFrame(sidePanel, text="Subjects")
        self.container.pack(fill = BOTH, expand=TRUE)

        self.subjectList = Listbox(self.container, exportselection=FALSE)
        self.subjectList.pack(fill = BOTH, expand=TRUE)
        self.subjectList.bind( '<<ListboxSelect>>', lambda e: self.handleListboxSelect() )

        buttonContainer = ttk.Frame(self.container)
        buttonContainer.pack()
        ttk.Button(buttonContainer, text='Add', command=lambda: self.createSubject()).pack(side=LEFT)
        self.editButton = ttk.Button(buttonContainer, text='Edit', command=lambda: self.editSubject())
        self.editButton.pack(side=LEFT)
        ttk.Button(buttonContainer, text='Del', command=lambda: self.deleteSubject()).pack(side=LEFT)
        
        ttk.Button(self.container, text='Import...').pack()

    def editSubject(self):
        index = self.subjectList.curselection()[0]

        # Create edit popup
        editscreen = Toplevel(width=self.editButton.winfo_reqwidth()*3, height=self.editButton.winfo_reqheight()*3)
        editscreenX = self.editButton.winfo_rootx()-self.editButton.winfo_reqwidth() - 7
        ediscreenY = self.editButton.winfo_rooty()-(self.editButton.winfo_reqheight()*4.5)
        editscreen.geometry("+%d+%d" % ( editscreenX, ediscreenY ))
        editscreen.pack_propagate(False)
        
        ttk.Label(editscreen, text='Subject name').pack()
        nameEntry = ttk.Entry(editscreen)
        nameEntry.pack(expand=TRUE)
        ttk.Button(editscreen, text='Save', command=lambda: edit()).pack(side=BOTTOM,anchor='e')

        def edit():
            subject = app.getActiveSubject()
            subject.setId(nameEntry.get())
            self.refreshList()
            editscreen.destroy()

    def deleteSubject(self):
        index = self.subjectList.curselection()[0]
        project = app.getActiveProject()
        subjects = project.getSubjects()
        del subjects[index]
        app.setActiveSubject(None)
        self.refreshList()
        app.sidepanel_testList.refreshList()

    def createSubject(self):
        if app.getActiveProject() == None:
            # Create project and make it active
            project = Project()
            app.setActiveProject(project)
            app.addProject(project)

            # Create subject with index based on the size of project subject list
            index = self.subjectList.size()
            subject = Subject(index)

            # Append subject to list
            self.subjectList.insert('end', subject.id)
            self.subjectList.selection_clear(0, 'end')
            self.subjectList.selection_set('end')
            
            # Update app state
            app.setActiveSubject(subject)

            project.addSubject(subject)
            app.sidepanel_projectList.addToList(project.id)
        else:
            # Create subject with index based on the size of project subject list
            activeProject = app.getActiveProject()
            index = len(activeProject.getSubjects())
            subject = Subject(index)

            # Append subject to list
            self.subjectList.insert('end', subject.id)
            self.subjectList.selection_clear(0, 'end')
            self.subjectList.selection_set('end')

            # Update app state
            app.setActiveSubject(subject)
            app.setActiveTest(None)

            activeProject.addSubject(subject)
        
        # Refresh project details (=subject count)
        app.projectDetailModule.refreshDetails()
        app.sidepanel_testList.refreshList()

    def addToList(self, id):
        self.subjectList.insert('end', id)
        self.subjectList.selection_clear(0, 'end')
        self.subjectList.selection_set('end')

    def updateSelection(self):
        self.subjectList.selection_set('end')

    def refreshList(self):
        activeProject = app.getActiveProject()
        try:
            subjects = activeProject.getSubjects()
        except AttributeError:
            subjects = []
        #print(subjects)
        self.subjectList.delete(0, 'end')
        for s in subjects:
            self.subjectList.insert('end', s.id)

    def handleListboxSelect(self):
        # Set selected subject as active subject by index
        index = self.subjectList.curselection()[0]
        subject = app.getActiveProject().getSubjects()[index]
        
        # Refresh app state
        app.setActiveSubject(subject)
        app.setActiveTest(None)

        # Refresh views
        app.sidepanel_testList.refreshList()