import graphene 
from graphene_django import DjangoObjectType
from rest.models import Students,School
import json
# from django.core import serializers

class StudentsType(DjangoObjectType):
    class Meta:
        model=Students

class SchoolType(DjangoObjectType):
    class Meta:
        model=School

class Query(graphene.ObjectType):
    AllStudents=graphene.List(StudentsType,Sname=graphene.String())

    AllSchools=graphene.List(SchoolType)


    def resolve_AllSchools(root,info):
        return School.objects.all()

    def resolve_AllStudents(root,info,  Sname):
        print(Sname,"dggggggggdg")
        return Students.objects.all()


class CreateStudent(graphene.Mutation):
    class Arguments:
        sname=graphene.String()
        sage=graphene.Int()
        std=graphene.Int()
        school=graphene.String()
    
    ok=graphene.Boolean()
    data=graphene.Field(StudentsType)

    def mutate(self, info, sname,sage,std,school):
        scl=School.objects.get(name=school)
        v1=Students(name=sname,age=sage,standard=std,school=scl)
        v1.save() 
        data=v1
        ok=True
        return CreateStudent(ok=ok,data=data)



class Mutation(graphene.ObjectType):
    newStudent=CreateStudent.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)

